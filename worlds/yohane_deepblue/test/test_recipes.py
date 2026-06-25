from unittest import TestCase

from ..data import ItemNames
from ..items import rare_material_table
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
