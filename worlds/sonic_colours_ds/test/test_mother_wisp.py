from ..data import ItemNames, LocationNames
from .bases import SonicColoursDSTestBase


class TestGoal(SonicColoursDSTestBase):
    options = {
        "goal": 1,
    }

    def test_goal_access(self) -> None:
        self.collect_by_name([
            ItemNames.white_wisp_unlock,
            ItemNames.red_wisp_unlock,
            ItemNames.orange_wisp_unlock,
            ItemNames.yellow_wisp_unlock,
            ItemNames.cyan_wisp_unlock,
            ItemNames.violet_wisp_unlock,
            ItemNames.terminal_velocity_unlock,
            ItemNames.green_emerald,
            ItemNames.yellow_emerald,
            ItemNames.white_emerald,
            ItemNames.red_emerald,
            ItemNames.purple_emerald,
            ItemNames.blue_emerald,
            ItemNames.cyan_emerald,
            ])
        self.assertTrue(self.can_reach_location(LocationNames.nega_wisp_armor))
