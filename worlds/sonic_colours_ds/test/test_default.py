from ..data import ItemNames, LocationNames
from .bases import SonicColoursDSTestBase


class TestBasic(SonicColoursDSTestBase):
    def test_special_stage_access(self) -> None:
        self.assertTrue(self.can_reach_location(LocationNames.special_stage_1))
        self.collect_by_name([ItemNames.sweet_mountain_unlock, ItemNames.red_wisp_unlock])
        self.assertTrue(self.can_reach_location(LocationNames.special_stage_2))
        self.remove_by_name([ItemNames.sweet_mountain_unlock, ItemNames.red_wisp_unlock])
        self.collect_by_name([ItemNames.starlight_carnival_unlock, ItemNames.orange_wisp_unlock])
        self.assertTrue(self.can_reach_location(LocationNames.special_stage_3))
        self.remove_by_name([ItemNames.starlight_carnival_unlock, ItemNames.orange_wisp_unlock])
        self.collect_by_name([ItemNames.planet_wisp_unlock, ItemNames.yellow_wisp_unlock])
        self.assertTrue(self.can_reach_location(LocationNames.special_stage_4))
        self.remove_by_name([ItemNames.planet_wisp_unlock, ItemNames.yellow_wisp_unlock])
        self.collect_by_name([ItemNames.aquarium_park_unlock])
        self.assertTrue(self.can_reach_location(LocationNames.special_stage_5))
        self.remove_by_name([ItemNames.aquarium_park_unlock])
        self.collect_by_name([ItemNames.asteroid_coaster_unlock, ItemNames.white_wisp_unlock, ItemNames.violet_wisp_unlock])
        self.assertTrue(self.can_reach_location(LocationNames.special_stage_6))
        self.remove_by_name([ItemNames.asteroid_coaster_unlock, ItemNames.white_wisp_unlock, ItemNames.violet_wisp_unlock])
        self.assertTrue(self.can_reach_location(LocationNames.special_stage_7))


    def test_planets_blocked(self) -> None: #TODO: read starting items
        self.assertTrue(self.can_reach_region(LocationNames.tropical_resort_region))
        self.assertFalse(self.can_reach_region(LocationNames.sweet_mountain_region))
        self.assertFalse(self.can_reach_region(LocationNames.starlight_carnival_region))
        self.assertFalse(self.can_reach_region(LocationNames.planet_wisp_region))
        self.assertFalse(self.can_reach_region(LocationNames.aquarium_park_region))
        self.assertFalse(self.can_reach_region(LocationNames.asteroid_coaster_region))
        self.assertFalse(self.can_reach_region(LocationNames.terminal_velocity_region))


class TestGoal(SonicColoursDSTestBase):
    def test_goal_access(self) -> None:
        self.collect_by_name([
            ItemNames.white_wisp_unlock,
            ItemNames.red_wisp_unlock,
            ItemNames.orange_wisp_unlock,
            ItemNames.yellow_wisp_unlock,
            ItemNames.cyan_wisp_unlock,
            ItemNames.violet_wisp_unlock,
            ItemNames.terminal_velocity_unlock,
            ])
        self.assertTrue(self.can_reach_location(LocationNames.nega_wisp_armor))
