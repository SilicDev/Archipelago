import ctypes
import struct
import typing
from dataclasses import dataclass

from rule_builder.rules import CanReachRegion, Has, Rule, True_
from worlds.AutoWorld import World

from .data import DataMaps, ItemNames, LocationNames
from .items import (
    breakable_material_table,
    consumables_table,
    enemy_material_table,
    item_table,
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

@dataclass
class Recipe:
    ingredient1: Ingredient
    ingredient2: Ingredient
    ingredient3: Ingredient
    ingredient4: Ingredient
    access_rule: Rule|None = None

    def dump_bytes(self) -> bytearray:
        out: bytearray = bytearray([0]*12)
        struct.pack_into("<hb", out, 0, item_table[self.ingredient1.item_name].code, self.ingredient1.amount)
        struct.pack_into("<hb", out, 3, item_table[self.ingredient2.item_name].code, self.ingredient2.amount)
        if len(self.ingredient3.item_name) != 0:
            struct.pack_into("<hb", out, 6, item_table[self.ingredient3.item_name].code, self.ingredient3.amount)
        else:
            struct.pack_into("<hb", out, 6, 0, 0)
        if len(self.ingredient4.item_name) != 0:
            struct.pack_into("<hb", out, 9, item_table[self.ingredient4.item_name].code, self.ingredient4.amount)
        else:
            struct.pack_into("<hb", out, 9, 0, 0)
        return out

recipe_ingredients = sorted(stackables_set)
consumable_ingredients = list(consumables_table.keys())
consumable_ingredients.remove(ItemNames.musical_score)

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
            self._count_rare_materials(ingredient1, ingredient2, ingredient3, ingredient4)
            access_rule = self._get_ingredients_rule(ingredient1, ingredient2, ingredient3, ingredient4)
            self.recipes.append(Recipe(ingredient1, ingredient2, ingredient3, ingredient4, access_rule))
        pass

    def get_bytes(self) -> bytes:
        out: bytearray = bytearray(b"")
        for recipe in self.recipes:
            out.extend(recipe.dump_bytes())
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

    def _get_ingredient_rule(self, ingredient: Ingredient|None) -> Rule:
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
        return True_()

    def _get_ingredients_rule(self, *ingredients: Ingredient|None) -> Rule:
        rule = True_()
        for ingredient in ingredients:
            rule &= self._get_ingredient_rule(ingredient)
        return rule
