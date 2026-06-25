from unittest import TestCase

from ..data import ItemNames
from ..items import rare_material_table
from ..recipe import RecipeList


class TestRecipeVanilla(TestCase):

    def test_materials_vanilla(self) -> None:
        recipe_list: RecipeList = RecipeList()
        recipe_list.generate_default()
        #for key in recipe_list.rare_materials:
        self.assertDictEqual(recipe_list.rare_materials, {key: rare_material_table[key].quantity for key in recipe_list.rare_materials})
        self.assertDictEqual(recipe_list.accessories, {
            ItemNames.silk_cape: 1,
            ItemNames.fortune_tellers_veil: 1,
            ItemNames.fallen_angels_cloak_bad: 1,
            ItemNames.gold_threaded_cape: 2,
            ItemNames.bunny_earring: 1,
            ItemNames.clover_earring: 1,
            ItemNames.tattered_cloth: 2,
        })
