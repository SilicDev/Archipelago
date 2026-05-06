"""
Archipelago World definition for Sonic Colours (DS)
"""
import os
import typing
import pkgutil

from BaseClasses import Item, ItemClassification, Region, Tutorial
import settings
from worlds.AutoWorld import WebWorld, World

from .client import SonicColoursDSClient
from .items import SonicColoursDSItem, item_groups, planet_access_table, wisp_unlocks_table, emeralds_table, item_table, event_table, junk_table
from .locations import SonicColoursDSLocation, location_groups, location_table, setup_locations
from .regions import create_regions, connect_regions
from .rules import set_rules
from .options import SonicColoursDSOptions, Goal, scds_option_groups
from .data import ItemNames, LocationNames
from .rom import SonicColoursDSProcedurePatch, write_tokens


class SonicColoursDSWebWorld(WebWorld):
    """
    Webhost info for Sonic Colours
    """
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Sonic Colours (DS) with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["SilicDev"]
    )

    tutorials = [setup_en]

    option_groups = scds_option_groups


class SonicColoursDSSettings(settings.Group):
    class SonicColoursDSRomFile(settings.UserFilePath):
        """File name of your European Sonic Colours DS ROM"""
        description = "Sonic Colours DS ROM File"
        copy_to = "Sonic Colours (Europe) (En,Ja,Fr,De,Es,It).nds"
        md5s = [SonicColoursDSProcedurePatch.hash]

    rom_file: SonicColoursDSRomFile = SonicColoursDSRomFile(SonicColoursDSRomFile.copy_to)


class SonicColoursDSWorld(World):
    game = "Sonic Colours (DS)"
    web = SonicColoursDSWebWorld()
    topology_present = True

    settings_key = "sonic_colours_ds_settings"
    settings: typing.ClassVar[SonicColoursDSSettings]

    options_dataclass = SonicColoursDSOptions
    options: SonicColoursDSOptions

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table
    item_name_groups = item_groups
    location_name_groups = location_groups

    required_client_version = (0, 6, 6)

    starting_planet_access: list[str] = [ItemNames.tropical_resort_unlock] # Todo: convert to option

    def create_regions(self) -> None:
        active_locations = setup_locations(self, self.player)
        create_regions(self, active_locations)
        connect_regions(self)

    def create_items(self) -> None:
        for planet_access in self.starting_planet_access:
            self.multiworld.push_precollected(self.create_item(planet_access))
        if self.options.goal.value == Goal.option_wisp_armor:
            self.multiworld.get_location(LocationNames.nega_wisp_armor, self.player).place_locked_item(self.create_item(ItemNames.park_keys))
        elif self.options.goal.value == Goal.option_mother_wisp:
            self.multiworld.get_location(LocationNames.nega_mother_wisp, self.player).place_locked_item(self.create_item(ItemNames.mother_wisp))

        num_locations_to_fill = len(self.multiworld.get_unfilled_locations(self.player))
        itempool: list[Item] = []

        for item in wisp_unlocks_table.keys():
            itempool.append(self.create_item(item))
        for item in planet_access_table.keys():
            if not item in self.starting_planet_access:
                itempool.append(self.create_item(item))
        if self.options.goal.value == Goal.option_mother_wisp:
            for item in emeralds_table.keys():
                itempool.append(self.create_item(item))
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
        item = SonicColoursDSItem(name, classification, data.code, self.player)
        return item

    def set_rules(self) -> None:
        set_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemNames.park_keys if self.options.goal.value == Goal.option_wisp_armor else ItemNames.mother_wisp, self.player)  

    def get_filler_item_name(self) -> str:
        junk_keys = list(junk_table.keys())
        return self.multiworld.random.choice(junk_keys)
    
    def generate_output(self, output_directory: str) -> None:
        patch = SonicColoursDSProcedurePatch(player=self.player, player_name=self.player_name)
        patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, "data/base_patch.bsdiff4"))
        write_tokens(self, patch)
        # Write Output
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
    
    def fill_slot_data(self) -> dict[str, typing.Any]:
        slot_data = self.options.as_dict(
            "goal",
            "rankrequirement",
            "redringsanity",
        )
        return slot_data