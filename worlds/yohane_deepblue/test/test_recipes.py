from ..items import rare_material_table
from ..recipe import RecipeList
from .bases import YohaneDeepblueTestBase


class TestRecipeVanilla(YohaneDeepblueTestBase):

    @property
    def run_default_tests(self) -> bool:
        return False

    def test_rare_materials_vanilla(self) -> None:
        recipe_list: RecipeList = RecipeList()
        recipe_list.generate_default(self.world)
        #for key in recipe_list.rare_materials:
        self.assertDictEqual(recipe_list.rare_materials, {key: rare_material_table[key].quantity for key in recipe_list.rare_materials})
                            #f"Recipe list '{key}' count was {recipe_list.rare_materials[key]}, should be {rare_material_table[key].quantity}!")
