import ctypes
import os
import pkgutil
import struct
import typing
from dataclasses import dataclass
from functools import cmp_to_key
from random import Random

from Options import Toggle
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachRegion, Has, Or, Rule, True_

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
from .options import Recipesanity
from .rules import Macro, region_group_rules, upgraded_mari_rule

recipe_ingredients = sorted(stackables_set)
consumable_ingredients = list(consumables_table.keys())
consumable_ingredients.remove(ItemNames.musical_score)

ingredient_rules: dict[str, Macro] = {
}

def setup_ingredient_rules() -> None:
    for item in item_table:
        if item in DataMaps.crafting_item_regions:
            rules = []
            for r in DataMaps.crafting_item_regions[item]:
                rule: Rule = True_()
                if r.is_group:
                    rule = region_group_rules[r.region]
                else:
                    rule = CanReachRegion(r.region)
                if len(r.weakness) != 0:
                    rule &= Has(DataMaps.element_to_character_map[r.weakness])
                rules.append(rule)
            rule = Or(*rules)
            if item == ItemNames.ninja_shuriken:
                rule &= upgraded_mari_rule
            ingredient_rules[item] = Macro(rule, f"Ingredient '{item}'")
        elif item in consumable_ingredients:
            rule = CanReachRegion(LocationNames.origin_region)
            if item in [ItemNames.shinestew, ItemNames.fallen_angels_tears]:
                rule &= Has(ItemNames.mari_unlock)
            ingredient_rules[item] = Macro(rule, f"Ingredient '{item}'")
        elif item in recipe_ingredients:
            ingredient_rules[item] = Macro(True_(), f"Ingredient '{item}'")
setup_ingredient_rules()

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

    @classmethod
    def unpack(cls, data: int) -> typing.Self:
        id = data & 0x03FF
        amount = (data & 0xFC00) >> 10
        if id != 0:
            return cls(lookup_id_to_name[id], amount)
        return cls("", 0)


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

    def get_ingredients(self) -> list[Ingredient]:
        return [self.ingredient1, self.ingredient2, self.ingredient3, self.ingredient4]

    @classmethod
    def unpack(cls, data: bytearray) -> typing.Self:
        return cls(
            Ingredient.unpack(struct.unpack_from("<h", data, 0)[0]),
            Ingredient.unpack(struct.unpack_from("<h", data, 2)[0]),
            Ingredient.unpack(struct.unpack_from("<h", data, 4)[0]),
            Ingredient.unpack(struct.unpack_from("<h", data, 6)[0]))


vanilla_recipes = {}
def setup_vanilla_recipes() -> None:
    recipe_data = pkgutil.get_data(__name__, "data/recipe_dump.txt")
    if recipe_data is None:
        raise FileNotFoundError("Couldn't find 'data/recipe_dump.txt'")
    text = recipe_data.decode("utf-8")
    recipes = text.splitlines()
    for r in recipes:
        parts = r.split(";")
        if len(parts) == 5:
            key = lookup_id_to_name[int(parts[0])]
            ingredients: list[Ingredient] = []
            for i in range(1, len(parts)):
                ingredient_parts = parts[i].split(":")
                id = int(ingredient_parts[0])
                if id != 0:
                    ingredients.append(Ingredient(lookup_id_to_name[id], int(ingredient_parts[1])))
            vanilla_recipes[key] = ingredients
setup_vanilla_recipes()


@cmp_to_key
def _sort_ingredients(a: Ingredient, b: Ingredient) -> int:
    if len(a.item_name) == 0:
        return 1
    if len(b.item_name) == 0:
        return -1
    return item_table[a.item_name].code - item_table[b.item_name].code

class RecipeList:
    def __init__(self) -> None:
        self.recipes: list[Recipe] = []
        self.rare_materials: dict[str, int] = {}
        self.accessories: dict[str, int] = {} # vanilla only

    def generate(self, random: Random, max_consumable: int, max_enemy: int, max_breakable: int) -> None:
        for _ in range(93):
            ingredient1 = self._select_breakable_ingredient(random, max_enemy, max_breakable)
            ingredient2 = self._select_ingredient(random, max_consumable, max_enemy, max_breakable)
            while ingredient2.item_name == ingredient1.item_name:
                ingredient2 = self._select_ingredient(random, max_consumable, max_enemy, max_breakable)
            ingredient3 = Ingredient("", 0)
            ingredient4 = Ingredient("", 0)
            rand = random.random()
            if rand < 0.5:
                ingredient3 = self._select_ingredient(random, max_consumable, max_enemy, max_breakable)
                while ingredient3.item_name in [ingredient1.item_name, ingredient2.item_name]:
                    ingredient3 = self._select_ingredient(random, max_consumable, max_enemy, max_breakable)
            if rand < 0.25:
                ingredient4 = self._select_ingredient(random, max_consumable, max_enemy, max_breakable)
                while ingredient4.item_name in [ingredient1.item_name, ingredient2.item_name, ingredient3.item_name]:
                    ingredient4 = self._select_ingredient(random, max_consumable, max_enemy, max_breakable)
            ingredients = sorted([ingredient1, ingredient2, ingredient3, ingredient4], key=_sort_ingredients)
            self._count_materials(*ingredients)
            access_rule = self._get_ingredients_rule(*ingredients)
            self.recipes.append(Recipe(*ingredients, access_rule=access_rule))
        pass

    def generate_default(self) -> None:
        for i in range(93):
            recipes = list(vanilla_recipes.values())
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
                self._count_materials(ingredient1, ingredient2, ingredient3, ingredient4)
                access_rule = self._get_ingredients_rule(ingredient1, ingredient2, ingredient3, ingredient4)
                self.recipes.append(Recipe(ingredient1, ingredient2, ingredient3, ingredient4, access_rule))
            pass
        pass

    def get_bytes(self) -> bytes:
        out: bytearray = bytearray(b"")
        for recipe in self.recipes:
            out.extend(recipe.pack())
        return bytes(out)

    def from_bytes(self, data: bytearray):
        for _ in range(93):
            recipe = Recipe.unpack(data)
            access_rule = self._get_ingredients_rule(*recipe.get_ingredients())
            recipe.access_rule = access_rule
            self.recipes.append(recipe)
            data = data[8:]
        pass

    def _select_breakable_ingredient(self, random: Random, max_enemy: int, max_breakable: int) -> Ingredient:
        rand = random.random()
        if rand < 0.5:
            item = random.choice(list(enemy_material_table.keys()))
            count = self._random_amount(random, 1, max_enemy)
            return Ingredient(item, count)
        item = random.choice(list(breakable_material_table.keys()))
        count = self._random_amount(random, 1, max_breakable, 5)
        return Ingredient(item, count)

    def _select_ingredient(self, random: Random, max_consumable: int, max_enemy: int, max_breakable: int) -> Ingredient:
        rand = random.random()
        if rand < 0.05:
            item = random.choice(list(rare_material_table.keys()))
            count = self._random_amount(random, 1, 3)
            return Ingredient(item, count)
        if rand < 0.2:
            item = random.choice(consumable_ingredients)
            count = self._random_amount(random, 1, max_consumable)
            return Ingredient(item, count)
        return self._select_breakable_ingredient(random, max_enemy, max_breakable)

    def _random_amount(self, random: Random, min: int, max: int, p: int = 2) -> int:
        return round(min + (max - min) * pow(random.random(), p))

    def _count_materials(self, *ingredients: Ingredient|None) -> None:
        for ingredient in ingredients:
            if ingredient is not None:
                if ingredient.item_name in rare_material_table:
                    item = ingredient.item_name
                    if item not in self.rare_materials:
                        self.rare_materials[item] = ingredient.amount
                    else:
                        self.rare_materials[item] += ingredient.amount
                if ingredient.item_name in accessories_table:
                    item = ingredient.item_name
                    if item not in self.accessories:
                        self.accessories[item] = ingredient.amount
                    else:
                        self.accessories[item] += ingredient.amount

    def _get_ingredient_rule(self, ingredient: Ingredient|None) -> Rule:
        if ingredient is None:
            return True_() # empty ingredient -> Optimize away
        if ingredient.item_name == "":
            return True_()

        # can't macro these
        if ingredient.item_name in rare_material_table:
            return Has(ingredient.item_name, ingredient.amount) | CanReachRegion(LocationNames.infernal_altar_region)
        if ingredient.item_name in accessories_table:
            return (Has(ingredient.item_name, ingredient.amount,
                        options=[OptionFilter(Recipesanity, Toggle.option_false)], filtered_resolution=True) &
                        Macro(True_(), options=[OptionFilter(Recipesanity, Toggle.option_true)],
                              filtered_resolution=True, name="Ingredient '{ingredient.item_name}'"))
        if ingredient.item_name in ingredient_rules:
            return ingredient_rules[ingredient.item_name]
        return True_()

    def _get_ingredients_rule(self, *ingredients: Ingredient|None) -> Rule:
        rule = True_()
        for ingredient in ingredients:
            rule &= self._get_ingredient_rule(ingredient)
        return rule
