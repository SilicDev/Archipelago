import ctypes
import struct
import typing
from dataclasses import dataclass
from functools import cmp_to_key

from Options import Toggle
from rule_builder.rules import CanReachRegion, Has, Rule, True_
from worlds.AutoWorld import World

from .data import DataMaps, ItemNames, LocationNames
from .items import (
    accessories_table,
    breakable_material_table,
    consumables_table,
    enemy_material_table,
    item_table,
    lookup_id_to_name,
    rare_material_table,
    stackables_set,
)
from .locations import region_groups


class RecipeStruct(ctypes.Structure):
    _fields_ = [
        ("reserved1_08", ctypes.c_uint),
        ("reserved2_01", ctypes.c_uint),
        ("result_id", ctypes.c_uint),
        ("result_count", ctypes.c_int),
        ("ingredient1_id", ctypes.c_uint),
        ("ingredient1_count", ctypes.c_int),
        ("ingredient2_id", ctypes.c_uint),
        ("ingredient2_count", ctypes.c_int),
        ("ingredient3_id", ctypes.c_uint),
        ("ingredient3_count", ctypes.c_int),
        ("ingredient4_id", ctypes.c_uint),
        ("ingredient4_count", ctypes.c_int),
    ]

class Ingredient(typing.NamedTuple):
    item_name: str
    amount: int

    def pack(self) -> int:
        if self.item_name in item_table:
            return (item_table[self.item_name].code & 0x03FF) | ((self.amount & 0x3F) << 10)
        return 0

@dataclass
class Recipe:
    ingredient1: Ingredient
    ingredient2: Ingredient
    ingredient3: Ingredient
    ingredient4: Ingredient
    access_rule: Rule|None = None

    def pack(self) -> bytearray:
        out: bytearray = bytearray([0]*8)
        struct.pack_into("<h", out, 0, self.ingredient1.pack())
        struct.pack_into("<h", out, 2, self.ingredient2.pack())
        struct.pack_into("<h", out, 4, self.ingredient3.pack())
        struct.pack_into("<h", out, 6, self.ingredient4.pack())
        return out

recipe_ingredients = sorted(stackables_set)
consumable_ingredients = list(consumables_table.keys())
consumable_ingredients.remove(ItemNames.musical_score)


vanilla_recipes = {}
with open("./worlds/yohane_deepblue/data/recipe_dump.bin", "r") as f:
    text = f.read()
    recipes = text.split("\n\n")
    for r in recipes:
        parts = r.split("\n")
        if len(parts) == 5:
            key = lookup_id_to_name[int(parts[0])]
            ingredients: list[Ingredient] = []
            for i in range(1, len(parts)):
                ingredient_parts = parts[i].split("\t")
                id = int(ingredient_parts[0])
                if id != 0:
                    ingredients.append(Ingredient(lookup_id_to_name[id], int(ingredient_parts[1])))
            vanilla_recipes[key] = ingredients


@cmp_to_key
def _sort_ingredients(a: Ingredient, b: Ingredient) -> int:
    if len(a.item_name) == 0:
        return -1
    if len(b.item_name) == 0:
        return 1
    return item_table[a.item_name].code - item_table[b.item_name].code

class RecipeList:
    def __init__(self) -> None:
        self.recipes: list[Recipe] = []
        self.rare_materials: dict[str, int] = {}

    def generate(self, world: World) -> None:
        for _ in range(93):
            ingredient1 = self._select_ingredient(world)
            ingredient2 = self._select_ingredient(world)
            while ingredient2.item_name == ingredient1.item_name:
                ingredient2 = self._select_ingredient(world)
            ingredient3 = Ingredient("", 0)
            ingredient4 = Ingredient("", 0)
            rand = world.random.random()
            if rand < 0.5:
                ingredient3 = self._select_ingredient(world)
                while ingredient3.item_name in [ingredient1.item_name, ingredient2.item_name]:
                    ingredient3 = self._select_ingredient(world)
            if rand < 0.25:
                ingredient4 = self._select_ingredient(world)
                while ingredient4.item_name in [ingredient1.item_name, ingredient2.item_name, ingredient3.item_name]:
                    ingredient4 = self._select_ingredient(world)
            ingredients = sorted([ingredient1, ingredient2, ingredient3, ingredient4], key=_sort_ingredients)
            self._count_rare_materials(*ingredients)
            access_rule = self._get_ingredients_rule(world, *ingredients)
            self.recipes.append(Recipe(*ingredients, access_rule=access_rule))
        pass

    def generate_default(self, world: World) -> None:
        for i in range(93):
            recipes = list(vanilla_recipes)
            if i < len(recipes):
                vanilla_recipe = recipes[i]
                ingredient1 = vanilla_recipe[0]
                ingredient2 = Ingredient("", 0)
                ingredient3 = Ingredient("", 0)
                ingredient4 = Ingredient("", 0)
                if len(vanilla_recipe) > 1:
                    ingredient2 = vanilla_recipe[1]
                if len(vanilla_recipe) > 2:
                    ingredient3 = vanilla_recipe[2]
                if len(vanilla_recipe) > 3:
                    ingredient4 = vanilla_recipe[3]
                self._count_rare_materials(ingredient1, ingredient2, ingredient3, ingredient4)
                access_rule = self._get_ingredients_rule(world, ingredient1, ingredient2, ingredient3, ingredient4)
                self.recipes.append(Recipe(ingredient1, ingredient2, ingredient3, ingredient4, access_rule))
            pass
        pass

    def get_bytes(self) -> bytes:
        out: bytearray = bytearray(b"")
        for recipe in self.recipes:
            out.extend(recipe.pack())
        return bytes(out)

    def _select_ingredient(self, world: World) -> Ingredient:
        rand = world.random.random()
        if rand < 0.05:
            item = world.random.choice(list(rare_material_table.keys()))
            count = self._random_amount(world, 1, 3)
            return Ingredient(item, count)
        if rand < 0.2:
            item = world.random.choice(consumable_ingredients)
            count = self._random_amount(world, 1, world.options.max_consumable_ingredient_count.value)
            return Ingredient(item, count)
        if rand < 0.6:
            item = world.random.choice(list(enemy_material_table.keys()))
            count = self._random_amount(world, 1, world.options.max_enemy_ingredient_count.value)
            return Ingredient(item, count)
        item = world.random.choice(list(breakable_material_table.keys()))
        count = self._random_amount(world, 1, world.options.max_breakable_ingredient_count.value, 5)
        return Ingredient(item, count)

    def _random_amount(self, world: World, min: int, max: int, p: int = 2) -> int:
        return round(min + (max - min) * pow(world.random.random(), p))

    def _count_rare_materials(self, *ingredients: Ingredient|None) -> Rule:
        rule = True_()
        for ingredient in ingredients:
            if ingredient is not None and ingredient.item_name in rare_material_table:
                item = ingredient.item_name
                if item not in self.rare_materials:
                    self.rare_materials[item] = ingredient.amount
                else:
                    self.rare_materials[item] += ingredient.amount
        return rule

    def _get_ingredient_rule(self, world: World, ingredient: Ingredient|None) -> Rule:
        if ingredient is None:
            return True_()
        if ingredient.item_name in rare_material_table:
            return Has(ingredient.item_name, ingredient.amount) | CanReachRegion(LocationNames.infernal_altar_region)
        if ingredient.item_name in [ItemNames.shinestew, ItemNames.fallen_angels_tears]:
            return Has(ItemNames.mari_unlock)
        if ingredient.item_name in DataMaps.crafting_item_regions:
            rule = True_()
            for r in DataMaps.crafting_item_regions[ingredient.item_name]:
                if r.is_group:
                    for region in region_groups[r.region]:
                        rule |= CanReachRegion(region)
                else:
                    rule |= CanReachRegion(r.region)
                if len(r.weakness) != 0:
                    rule &= Has(DataMaps.element_to_character_map[r.weakness])
            return rule
        if ingredient.item_name in accessories_table:
            if world.options.recipesanity == Toggle.option_false:
                return self._get_ingredients_rule(world, *DataMaps.vanilla_crafting_recipes[ingredient.item_name])
            # pray
        return True_()

    def _get_ingredients_rule(self, world: World, *ingredients: Ingredient|None) -> Rule:
        rule = True_()
        for ingredient in ingredients:
            rule &= self._get_ingredient_rule(world, ingredient)
        return rule
