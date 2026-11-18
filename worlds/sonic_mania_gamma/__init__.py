"""
Archipelago World definition for Sonic Mania Plus
"""
import logging
import typing

from BaseClasses import Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World

from .data import ItemNames, LocationNames
from .data.constants import GAME_NAME
from .items import (
    SonicManiaGammaItem,
    character_table,
    encore_character_table,
    event_table,
    item_groups,
    item_table,
    junk_table,
)
from .locations import SonicManiaGammaLocation, location_groups, location_table, setup_locations
from .options import MainLevelSelection, SonicManiaGammaOptions, sonic_mania_gamma_option_groups
from .regions import connect_regions, create_regions
from .rules import set_rules


class SonicManiaGammaWebWorld(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Sonic Mania Plus (CodenameGamma's version) with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["SilicDev"]
    )

    tutorials = [setup_en]

    option_groups = sonic_mania_gamma_option_groups

class SonicManiaGammaWorld(World):
    game = GAME_NAME
    web = SonicManiaGammaWebWorld()
    topology_present = True

    options_dataclass = SonicManiaGammaOptions
    options: SonicManiaGammaOptions

    item_name_to_id = {name: data.code for name, data in item_table.items() if data.code}
    location_name_to_id = location_table
    item_name_groups = item_groups
    location_name_groups = location_groups

    origin_region_name = LocationNames.origin_region
    logger: logging.Logger

    ut_can_gen_without_yaml = True

    def __init__(self, multiworld: MultiWorld, player: int) -> None:
        super().__init__(multiworld, player)
        self.logger = logging.getLogger(GAME_NAME)

    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data: dict[str, typing.Any] = re_gen_passthrough[self.game]
            self.options.main_level_selection.value = slot_data["main_level_selection"]
            self.options.special_stage_selection.value = slot_data["special_stage_selection"]
            self.options.bluespheres_in_logic.value = slot_data["bluespheres_in_logic"]
            pass # UT yamlless

    def create_regions(self) -> None:
        active_locations = setup_locations(self, self.player)
        create_regions(self, active_locations)
        connect_regions(self)

    def create_items(self) -> None:
        # starting inventory
        self.push_precollected(self.create_item(ItemNames.sonic))
        # place locked local items
        self.get_location(LocationNames.victory).place_locked_item(self.create_item(ItemNames.victory))

        # create items to place in the multiworld
        num_locations_to_fill = len(self.multiworld.get_unfilled_locations(self.player))
        itempool: list[Item] = []
        itempool.extend([self.create_item(char) for char in character_table if char != ItemNames.sonic])
        if self.options.main_level_selection.value >= MainLevelSelection.option_encore:
            itempool.extend([self.create_item(char) for char in encore_character_table if char != ItemNames.sonic])

        # create filler for remaining
        surplus_checks = num_locations_to_fill - len(itempool)
        itempool += [self.create_filler() for _ in range(surplus_checks)]
        self.multiworld.itempool += itempool

    def create_item(self, name: str) -> Item:
        data = None
        if name in event_table:
            data = event_table[name]
        else:
            data = item_table[name]
        classification = ItemClassification.filler
        if data.progression:
            classification = ItemClassification.progression
        elif data.trap:
            classification = ItemClassification.trap
        return SonicManiaGammaItem(name, classification, data.code, self.player)

    def set_rules(self) -> None:
        set_rules(self)

    def get_filler_item_name(self) -> str:
        junk_items = sorted(junk_table)
        return self.random.choice(junk_items)

    def fill_slot_data(self) -> dict[str, typing.Any]:
        slot_data = self.options.as_dict(
            "death_link",
            "main_level_selection",
            "special_stage_selection",
            "bluespheres_in_logic",
        )
        return slot_data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, typing.Any]) -> dict[str, typing.Any]:
        return slot_data
