from random import Random
from typing import ClassVar
from unittest import TestCase

from test.param import classvar_matrix

from ..data import ItemNames
from ..items import rare_material_table, consumables_table, breakable_material_table, enemy_material_table, stackables_set
from ..recipe import RecipeList

craft_accessories = {
    ItemNames.silk_cape: 1,
    ItemNames.fortune_tellers_veil: 1,
    ItemNames.fallen_angels_cloak_bad: 1,
    ItemNames.gold_threaded_cape: 2,
    ItemNames.bunny_earring: 1,
    ItemNames.clover_earring: 1,
    ItemNames.tattered_cloth: 2,
}

class TestRecipeVanilla(TestCase):

    def test_materials_vanilla(self) -> None:
        recipe_list: RecipeList = RecipeList()
        recipe_list.generate_default()
        #for key in recipe_list.rare_materials:
        rare_materials = {key: rare_material_table[key].quantity for key in rare_material_table}
        self.assertEqual(len(recipe_list.rare_materials), len(rare_materials))
        self.assertDictEqual({key: recipe_list.rare_materials[key] for key in rare_materials}, rare_materials)
        self.assertEqual(len(recipe_list.accessories), len(craft_accessories))
        self.assertDictEqual({key: recipe_list.accessories[key] for key in craft_accessories}, craft_accessories)

@classvar_matrix(max_consumable=[3,5,15], max_breakable=[3,5,10,15], max_enemy=[3,5,15])
class TestRecipeRecipeSanity(TestCase):
    max_consumable: ClassVar[int]
    max_enemy: ClassVar[int]
    max_breakable: ClassVar[int]

    def test_materials_recipesanity(self) -> None:
        recipe_list: RecipeList = RecipeList()
        recipe_list.generate(Random(), self.max_consumable, self.max_enemy, self.max_breakable)
        self.assertEqual(len(recipe_list.recipes), 93)
        for recipe in recipe_list.recipes:
            empty_ingredients = 0
            ingredient_names = set()
            for ingredient in recipe.get_ingredients():
                item_name = ingredient.item_name
                if item_name != "":
                    self.assertIn(item_name, stackables_set,
                                  f"Unknown crafting material {item_name}")
                    self.assertEqual(empty_ingredients, 0,
                                     f"Expected no more ingredients after `NONE`, but got {ingredient}")
                    self.assertNotIn(item_name, ingredient_names,
                                     f"Duplicate ingredient '{item_name}' detected")
                    if item_name in rare_material_table:
                        self.assertLessEqual(ingredient.amount, 3)
                    if item_name in consumables_table:
                        self.assertLessEqual(ingredient.amount, self.max_consumable)
                    if item_name in enemy_material_table:
                        self.assertLessEqual(ingredient.amount, self.max_enemy)
                    if item_name in breakable_material_table:
                        self.assertLessEqual(ingredient.amount, self.max_breakable)
                    ingredient_names.add(ingredient.item_name)
                else:
                    self.assertEqual(ingredient.amount, 0,
                                     f"Empty ingredient should have count 0, was '{ingredient.amount}'")
                    empty_ingredients += 1
            self.assertLessEqual(empty_ingredients, 2,
                                 f"Expected at most 2 empty ingredients, got '{empty_ingredients}'")
        pass
