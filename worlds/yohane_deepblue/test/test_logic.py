from BaseClasses import CollectionState

from ..data import ItemNames, LocationNames
from .bases import YohaneDeepblueTestBase


class TestAccessibilityDefault(YohaneDeepblueTestBase):

    def test_beatable(self):
        progression_variant1 = [
            ItemNames.fallen_angels_soarshoes,
            ItemNames.gloves_of_might,
            ItemNames.sea_deitys_charm,
            ItemNames.kanan_unlock,
            ItemNames.riko_unlock,
            ItemNames.dia_unlock,
            ItemNames.hanamaru_unlock,
            ItemNames.ruby_unlock
        ]
        self.collect_by_name(progression_variant1)
        self.assertBeatable(True)
        self.multiworld.state = CollectionState(self.multiworld)
        for i in progression_variant1:
            try:
                self.collect_by_name([item for item in progression_variant1 if item != i])
                self.assertBeatable(False)
                self.multiworld.state = CollectionState(self.multiworld)
            except AssertionError as e:
                raise AssertionError(f"{e}, Item '{i}' not required to beat the game!") from e

        progression_variant2 = [
            ItemNames.fallen_angels_soarshoes,
            ItemNames.gloves_of_might,
            ItemNames.sea_deitys_charm,
            ItemNames.kanan_unlock,
            ItemNames.riko_unlock,
            ItemNames.hanamaru_unlock,
            ItemNames.ruby_unlock,
            ItemNames.ruby_upgrade
        ]
        self.collect_by_name(progression_variant2)
        self.assertBeatable(True)
        self.multiworld.state = CollectionState(self.multiworld)
        for i in progression_variant2:
            try:
                self.collect_by_name([item for item in progression_variant2 if item != i])
                self.assertBeatable(False)
                self.multiworld.state = CollectionState(self.multiworld)
            except AssertionError as e:
                raise AssertionError(f"{e}, Item '{i}' not required to beat the game!") from e

    def test_accessibility_grotto(self) -> None:
        self.assertTrue(self.can_reach_location(LocationNames.grotto_next_to_first_save_room_chest))

class TestChikaBlocksNotMoved(YohaneDeepblueTestBase):
    options = {
        "early_chika_blocks_moved": False
    }

    def test_accessibility_grotto(self) -> None:
        self.assertAccessDependency([LocationNames.grotto_next_to_first_save_room_chest],
                                    [
                                        [ItemNames.chika_unlock],
                                        [ItemNames.ruby_unlock, ItemNames.ruby_upgrade]
                                    ], True)

    def test_beatable(self):
        progression_variant1 = [
            ItemNames.fallen_angels_soarshoes,
            ItemNames.gloves_of_might,
            ItemNames.sea_deitys_charm,
            ItemNames.chika_unlock,
            ItemNames.kanan_unlock,
            ItemNames.riko_unlock,
            ItemNames.dia_unlock,
            ItemNames.hanamaru_unlock,
            ItemNames.ruby_unlock
        ]
        self.collect_by_name(progression_variant1)
        self.assertBeatable(True)
        self.multiworld.state = CollectionState(self.multiworld)
        for i in progression_variant1:
            try:
                self.collect_by_name([item for item in progression_variant1 if item != i])
                self.assertBeatable(False)
                self.multiworld.state = CollectionState(self.multiworld)
            except AssertionError as e:
                raise AssertionError(f"{e}, Item '{i}' not required to beat the game!") from e

        progression_variant2 = [
            ItemNames.fallen_angels_soarshoes,
            ItemNames.gloves_of_might,
            ItemNames.sea_deitys_charm,
            ItemNames.kanan_unlock,
            ItemNames.riko_unlock,
            ItemNames.hanamaru_unlock,
            ItemNames.ruby_unlock,
            ItemNames.ruby_upgrade
        ]
        self.collect_by_name(progression_variant2)
        self.assertBeatable(True)
        self.multiworld.state = CollectionState(self.multiworld)
        for i in progression_variant2:
            try:
                self.collect_by_name([item for item in progression_variant2 if item != i])
                self.assertBeatable(False)
                self.multiworld.state = CollectionState(self.multiworld)
            except AssertionError as e:
                raise AssertionError(f"{e}, Item '{i}' not required to beat the game!") from e
