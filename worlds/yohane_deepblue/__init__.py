"""
Archipelago World definition for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
"""
import typing

from BaseClasses import Item, ItemClassification, Tutorial
from Options import Toggle
from rule_builder.cached_world import CachedRuleBuilderWorld
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, Type, components, launch

from .items import (YohaneDeepblueItem, item_groups, item_table, junk_table, event_table, unique_accessories_table, character_unlock_table, 
                    character_upgrade_table, rare_material_table, consumables_table, progressive_character_table)
from .locations import YohaneDeepblueLocation, location_groups, location_table, setup_locations
from .regions import create_regions, connect_regions
from .rules import set_rules
from .options import YohaneDeepblueOptions, yohane_deepblue_option_groups
from .data import ItemNames, LocationNames

def run_client(*args: str) -> None:
    from .client import launch_client
    launch(launch_client, name="YOHANE THE PARHELION -BLAZE in the DEEPBLUE- Client", args=args)

components.append(
    Component(
        "YOHANE THE PARHELION -BLAZE in the DEEPBLUE- Client",
        func=run_client,
        game_name="YOHANE THE PARHELION -BLAZE in the DEEPBLUE-",
        component_type=Type.CLIENT,
        supports_uri=True,
        description="Yohane BiD Client",
    )
)

class YohaneDeepblueWebWorld(WebWorld):
    """
    Webhost info for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
    """
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing YOHANE THE PARHELION -BLAZE in the DEEPBLUE- with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["SilicDev"]
    )

    tutorials = [setup_en]

    option_groups = yohane_deepblue_option_groups

class YohaneDeepblueWorld(CachedRuleBuilderWorld):
    game = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"
    web = YohaneDeepblueWebWorld()
    topology_present = True

    options_dataclass = YohaneDeepblueOptions
    options: YohaneDeepblueOptions

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table
    item_name_groups = item_groups
    location_name_groups = location_groups

    origin_region_name = LocationNames.origin_region

    required_client_version = (0, 6, 7)

    def create_regions(self) -> None:
        active_locations = setup_locations(self, self.player)
        create_regions(self, active_locations)
        connect_regions(self)

    def create_items(self) -> None:
        self.multiworld.push_precollected(self.create_item(ItemNames.katar))
        self.multiworld.push_precollected(self.create_item(ItemNames.lailaps_unlock))
        self.multiworld.get_location(LocationNames.sunken_temple_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.ruins_boss_defeated_3, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.grotto_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.coral_hill_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.sea_of_trees_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.crystalline_grotto_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.sunken_volcano_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.shipwreck_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.boss_token))
        self.multiworld.get_location(LocationNames.aquors_memoria_boss_defeated, self.player).place_locked_item(self.create_item(ItemNames.victory))
        num_locations_to_fill = len(self.multiworld.get_unfilled_locations(self.player))
        itempool: list[Item] = []
        for item in unique_accessories_table.keys():
            for _ in range(unique_accessories_table[item].quantity):
                itempool.append(self.create_item(item))
        for item in rare_material_table.keys():
            for _ in range(rare_material_table[item].quantity):
                itempool.append(self.create_item(item))
        if self.options.progressive_character_unlocks == Toggle.option_true:
            for item in progressive_character_table.keys():
                itempool.append(self.create_item(item))
                itempool.append(self.create_item(item))
        else:
            for item in character_unlock_table.keys():
                if item != ItemNames.lailaps_unlock:
                    itempool.append(self.create_item(item))
            for item in character_upgrade_table.keys():
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
        elif data.trap:
            classification = ItemClassification.trap
        elif name in rare_material_table.keys():
            classification = ItemClassification.useful
        item = YohaneDeepblueItem(name, classification, data.code, self.player)
        return item

    def set_rules(self) -> None:
        set_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemNames.victory, self.player)
    
    def get_filler_item_name(self) -> str:
        junk_items = sorted(junk_table)
        return self.multiworld.random.choice(junk_items)
    
    def fill_slot_data(self) -> dict[str, typing.Any]:
        slot_data = self.options.as_dict(
            "death_link",
            "death_link_group",
            "damage_link",
            "damage_link_group",
            "early_chika_blocks_moved",
            "enable_you_skips",
            "progressive_character_unlocks",
            "upgrade_hints",
        )
        upgrades = []
        for item in character_upgrade_table.keys():
            location = self.multiworld.find_item(item, self.player)
            upgrades.append((location.player, location.address))
        slot_data["upgrades"] = upgrades
        return slot_data