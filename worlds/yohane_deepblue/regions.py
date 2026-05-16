from enum import IntEnum
import typing

from BaseClasses import CollectionState, Region, Entrance, EntranceType, ItemClassification
from rule_builder.rules import *
from worlds.AutoWorld import World
from Options import Toggle
from .locations import *
from .items import YohaneDeepblueItem
from .data import LocationNames, ItemNames, DataMaps
from .rules import *

def create_regions(world: World, active_locations: dict[str, int]) -> None:
    menu_region = create_region(world, world.origin_region_name, active_locations, menu_region_locations)

    sunken_temple_entrance_region = create_region(world, LocationNames.sunken_temple_entrance_region, active_locations, sunken_temple_entrance_region_locations)
    sunken_temple_random_region = create_region(world, LocationNames.sunken_temple_random_region, active_locations, sunken_temple_random_region_locations)
    sunken_temple_main_region = create_region(world, LocationNames.sunken_temple_main_region, active_locations, sunken_temple_main_region_locations)
    sunken_temple_post_boss_region = create_region(world, LocationNames.sunken_temple_post_boss_region, active_locations, sunken_temple_post_boss_region_locations)

    ruins_grotto_entrance_region = create_region(world, LocationNames.ruins_grotto_entrance_region, active_locations, ruins_grotto_entrance_region_locations)
    ruins_boss_1_region = create_region(world, LocationNames.ruins_boss_1_region, active_locations, ruins_boss_1_region_locations)
    ruins_boss_2_region = create_region(world, LocationNames.ruins_boss_2_region, active_locations, ruins_boss_2_region_locations)
    ruins_post_boss_2_region = create_region(world, LocationNames.ruins_post_boss_2_region, active_locations, ruins_post_boss_2_region_locations)
    ruins_boss_3_region = create_region(world, LocationNames.ruins_boss_3_region, active_locations, ruins_boss_3_region_locations)
    ruins_post_boss_3_region = create_region(world, LocationNames.ruins_post_boss_3_region, active_locations, ruins_post_boss_3_region_locations)
    ruins_left_of_sandpit_region = create_region(world, LocationNames.ruins_left_of_sandpit_region, active_locations, ruins_left_of_sandpit_region_locations)

    grotto_main_region = create_region(world, LocationNames.grotto_main_region, active_locations, grotto_main_region_locations)
    grotto_top_corridor_region = create_region(world, LocationNames.grotto_top_corridor_region, active_locations, grotto_top_corridor_region_locations)
    grotto_top_region = create_region(world, LocationNames.grotto_top_region, active_locations, grotto_top_region_locations)
    grotto_coral_hill_entrance_region = create_region(world, LocationNames.grotto_coral_hill_entrance_region, active_locations, grotto_coral_hill_entrance_region_locations)
    grotto_boss_region = create_region(world, LocationNames.grotto_boss_region, active_locations, grotto_boss_region_locations)

    coral_hill_left_entrance_region = create_region(world, LocationNames.coral_hill_left_entrance_region, active_locations, coral_hill_left_entrance_region_locations)
    coral_hill_left_save_region = create_region(world, LocationNames.coral_hill_left_save_region, active_locations, coral_hill_left_save_region_locations)
    coral_hill_top_left_region = create_region(world, LocationNames.coral_hill_top_left_region, active_locations, coral_hill_top_left_region_locations)
    coral_hill_bottom_left_region = create_region(world, LocationNames.coral_hill_bottom_left_region, active_locations, coral_hill_bottom_left_region_locations)
    coral_hill_left_climb_region = create_region(world, LocationNames.coral_hill_left_climb_region, active_locations, coral_hill_left_climb_region_locations)
    coral_hill_random_save_region = create_region(world, LocationNames.coral_hill_random_save_region, active_locations, coral_hill_random_save_region_locations)
    coral_hill_bottom_region = create_region(world, LocationNames.coral_hill_bottom_region, active_locations, coral_hill_bottom_region_locations)
    coral_hill_random_region = create_region(world, LocationNames.coral_hill_random_region, active_locations, coral_hill_random_region_locations)
    coral_hill_post_random_region = create_region(world, LocationNames.coral_hill_post_random_region, active_locations, coral_hill_post_random_region_locations)
    coral_hill_soarshoesnt_chest_region = create_region(world, LocationNames.coral_hill_soarshoesnt_chest_region, active_locations, coral_hill_soarshoesnt_chest_region_locations)
    coral_hill_center_save_region = create_region(world, LocationNames.coral_hill_center_save_region, active_locations, coral_hill_center_save_region_locations)
    coral_hill_teleporting_fish_chest_region = create_region(world, LocationNames.coral_hill_teleporting_fish_chest_region, active_locations, coral_hill_teleporting_fish_chest_region_locations)
    coral_hill_climb_bottom_region = create_region(world, LocationNames.coral_hill_climb_bottom_region, active_locations, coral_hill_climb_bottom_region_locations)
    coral_hill_teleporting_fish_room_region = create_region(world, LocationNames.coral_hill_teleporting_fish_room_region, active_locations, coral_hill_teleporting_fish_room_region_locations)
    coral_hill_climb_top_region = create_region(world, LocationNames.coral_hill_climb_top_region, active_locations, coral_hill_climb_top_region_locations)
    coral_hill_below_top_save_region = create_region(world, LocationNames.coral_hill_below_top_save_region, active_locations, coral_hill_below_top_save_region_locations)
    coral_hill_top_save_region = create_region(world, LocationNames.coral_hill_top_save_region, active_locations, coral_hill_top_save_region_locations)
    coral_hill_top_save_climb_region = create_region(world, LocationNames.coral_hill_top_save_climb_region, active_locations, coral_hill_top_save_climb_region_locations)
    coral_hill_left_wall_crab_region = create_region(world, LocationNames.coral_hill_left_wall_crab_region, active_locations, coral_hill_left_wall_crab_region_locations)
    coral_hill_wall_crab_chest_region = create_region(world, LocationNames.coral_hill_wall_crab_chest_region, active_locations, coral_hill_wall_crab_chest_region_locations)
    coral_hill_right_wall_crab_region = create_region(world, LocationNames.coral_hill_right_wall_crab_region, active_locations, coral_hill_right_wall_crab_region_locations)
    coral_hill_boss_region = create_region(world, LocationNames.coral_hill_boss_region, active_locations, coral_hill_boss_region_locations)
    coral_hill_spawner_trident_region = create_region(world, LocationNames.coral_hill_spawner_trident_region, active_locations, coral_hill_spawner_trident_region_locations)
    coral_hill_right_entrance_region = create_region(world, LocationNames.coral_hill_right_entrance_region, active_locations, coral_hill_right_entrance_region_locations)
    coral_hill_bottom_entrance_region = create_region(world, LocationNames.coral_hill_bottom_entrance_region, active_locations, coral_hill_bottom_entrance_region_locations)

    sea_of_trees_main_region = create_region(world, LocationNames.sea_of_trees_main_region, active_locations, sea_of_trees_main_region_locations)
    sea_of_trees_random_region = create_region(world, LocationNames.sea_of_trees_random_region, active_locations, sea_of_trees_random_region_locations)
    sea_of_trees_top_left_region = create_region(world, LocationNames.sea_of_trees_top_left_region, active_locations, sea_of_trees_top_left_region_locations)
    sea_of_trees_right_region = create_region(world, LocationNames.sea_of_trees_right_region, active_locations, sea_of_trees_right_region_locations)
    sea_of_trees_boss_region = create_region(world, LocationNames.sea_of_trees_boss_region, active_locations, sea_of_trees_boss_region_locations)
    sea_of_trees_post_boss_region = create_region(world, LocationNames.sea_of_trees_post_boss_region, active_locations, sea_of_trees_post_boss_region_locations)
    sea_of_trees_center_save_region = create_region(world, LocationNames.sea_of_trees_center_save_region, active_locations, sea_of_trees_center_save_region_locations)
    sea_of_trees_center_chika_region = create_region(world, LocationNames.sea_of_trees_center_chika_region, active_locations, sea_of_trees_center_chika_region_locations)

    crystalline_grotto_entrance_region = create_region(world, LocationNames.crystalline_grotto_entrance_region, active_locations, crystalline_grotto_entrance_region_locations)
    crystalline_grotto_left_save_region = create_region(world, LocationNames.crystalline_grotto_left_save_region, active_locations, crystalline_grotto_left_save_region_locations)
    crystalline_grotto_top_left_save_region = create_region(world, LocationNames.crystalline_grotto_top_left_save_region, active_locations, crystalline_grotto_top_left_save_region_locations)
    crystalline_grotto_top_region = create_region(world, LocationNames.crystalline_grotto_top_region, active_locations, crystalline_grotto_top_region_locations)
    crystalline_grotto_top_save_region = create_region(world, LocationNames.crystalline_grotto_top_save_region, active_locations, crystalline_grotto_top_save_region_locations)
    crystalline_grotto_random_region = create_region(world, LocationNames.crystalline_grotto_random_region, active_locations, crystalline_grotto_random_region_locations)
    crystalline_grotto_right_save_region = create_region(world, LocationNames.crystalline_grotto_right_save_region, active_locations, crystalline_grotto_right_save_region_locations)
    crystalline_grotto_bottom_region = create_region(world, LocationNames.crystalline_grotto_bottom_region, active_locations, crystalline_grotto_bottom_region_locations)
    crystalline_grotto_left_region = create_region(world, LocationNames.crystalline_grotto_left_region, active_locations, crystalline_grotto_left_region_locations)
    crystalline_grotto_center_region = create_region(world, LocationNames.crystalline_grotto_center_region, active_locations, crystalline_grotto_center_region_locations)
    crystalline_grotto_center_save_region = create_region(world, LocationNames.crystalline_grotto_center_save_region, active_locations, crystalline_grotto_center_save_region_locations)
    crystalline_grotto_left_center_save_region = create_region(world, LocationNames.crystalline_grotto_left_center_save_region, active_locations, crystalline_grotto_left_center_save_region_locations)
    crystalline_grotto_boss_region = create_region(world, LocationNames.crystalline_grotto_boss_region, active_locations, crystalline_grotto_boss_region_locations)
    crystalline_grotto_mari_chest_region = create_region(world, LocationNames.crystalline_grotto_mari_chest_region, active_locations, crystalline_grotto_mari_chest_region_locations)

    sunken_volcano_left_entrance_region = create_region(world, LocationNames.sunken_volcano_left_entrance_region, active_locations, sunken_volcano_left_entrance_region_locations)
    sunken_volcano_soarshoes_region = create_region(world, LocationNames.sunken_volcano_soarshoes_region, active_locations, sunken_volcano_soarshoes_region_locations)
    sunken_volcano_top_region = create_region(world, LocationNames.sunken_volcano_top_region, active_locations, sunken_volcano_top_region_locations)
    sunken_volcano_main_region = create_region(world, LocationNames.sunken_volcano_main_region, active_locations, sunken_volcano_main_region_locations)
    sunken_volcano_left_region = create_region(world, LocationNames.sunken_volcano_left_region, active_locations, sunken_volcano_left_region_locations)
    sunken_volcano_boss_region = create_region(world, LocationNames.sunken_volcano_boss_region, active_locations, sunken_volcano_boss_region_locations)
    sunken_volcano_path_to_tonosama_region = create_region(world, LocationNames.sunken_volcano_path_to_tonosama_region, active_locations, sunken_volcano_path_to_tonosama_region_locations)
    sunken_volcano_tonosama_region = create_region(world, LocationNames.sunken_volcano_tonosama_region, active_locations, sunken_volcano_tonosama_region_locations)

    shipwreck_left_region = create_region(world, LocationNames.shipwreck_left_region, active_locations, shipwreck_left_region_locations)
    shipwreck_left_mast_region = create_region(world, LocationNames.shipwreck_left_mast_region, active_locations, shipwreck_left_mast_region_locations)
    shipwreck_main_region = create_region(world, LocationNames.shipwreck_main_region, active_locations, shipwreck_main_region_locations)
    shipwreck_bottom_region = create_region(world, LocationNames.shipwreck_bottom_region, active_locations, shipwreck_bottom_region_locations)
    shipwreck_sealed_off_chest_region = create_region(world, LocationNames.shipwreck_sealed_off_chest_region, active_locations, shipwreck_sealed_off_chest_region_locations)
    shipwreck_postal_guild_bag_region = create_region(world, LocationNames.shipwreck_postal_guild_bag_region, active_locations, shipwreck_postal_guild_bag_region_locations)
    shipwreck_gloves_region = create_region(world, LocationNames.shipwreck_gloves_region, active_locations, shipwreck_gloves_region_locations)
    shipwreck_top_gloves_region = create_region(world, LocationNames.shipwreck_top_gloves_region, active_locations, shipwreck_top_gloves_region_locations)
    shipwreck_right_mast_region = create_region(world, LocationNames.shipwreck_right_mast_region, active_locations, shipwreck_right_mast_region_locations)
    shipwreck_top_entrance_region = create_region(world, LocationNames.shipwreck_top_entrance_region, active_locations, shipwreck_top_entrance_region_locations)
    shipwreck_boss_region = create_region(world, LocationNames.shipwreck_boss_region, active_locations, shipwreck_boss_region_locations)
    shipwreck_right_entrance_region = create_region(world, LocationNames.shipwreck_right_entrance_region, active_locations, shipwreck_right_entrance_region_locations)

    infernal_altar_region = create_region(world, LocationNames.infernal_altar_region, active_locations, infernal_altar_region_locations)
    aqours_memoria_region = create_region(world, LocationNames.aqours_memoria_region, active_locations, aqours_memoria_region_locations)

    if world.options.progressive_character_unlocks == Toggle.option_true:
        for item in DataMaps.character_item_to_progressive_map.keys():
            progressive = DataMaps.character_item_to_progressive_map[item]
            menu_region.add_event(item, item, Has(progressive[0], progressive[1]), YohaneDeepblueLocation, YohaneDeepblueItem, False)

    world.multiworld.regions += [
        menu_region,

        sunken_temple_entrance_region,
        sunken_temple_random_region,
        sunken_temple_main_region,
        sunken_temple_post_boss_region,

        ruins_grotto_entrance_region,
        ruins_boss_1_region,
        ruins_boss_2_region,
        ruins_post_boss_2_region,
        ruins_boss_3_region,
        ruins_post_boss_3_region,
        ruins_left_of_sandpit_region,

        grotto_main_region,
        grotto_top_corridor_region,
        grotto_top_region,
        grotto_coral_hill_entrance_region,
        grotto_boss_region,

        coral_hill_left_entrance_region,
        coral_hill_left_save_region,
        coral_hill_top_left_region,
        coral_hill_bottom_left_region,
        coral_hill_left_climb_region,
        coral_hill_random_save_region,
        coral_hill_bottom_region,
        coral_hill_random_region,
        coral_hill_post_random_region,
        coral_hill_soarshoesnt_chest_region,
        coral_hill_center_save_region,
        coral_hill_teleporting_fish_chest_region,
        coral_hill_climb_bottom_region,
        coral_hill_teleporting_fish_room_region,
        coral_hill_climb_top_region,
        coral_hill_below_top_save_region,
        coral_hill_top_save_region,
        coral_hill_top_save_climb_region,
        coral_hill_left_wall_crab_region,
        coral_hill_wall_crab_chest_region,
        coral_hill_right_wall_crab_region,
        coral_hill_boss_region,
        coral_hill_spawner_trident_region,
        coral_hill_right_entrance_region,
        coral_hill_bottom_entrance_region,

        sea_of_trees_main_region,
        sea_of_trees_random_region,
        sea_of_trees_top_left_region,
        sea_of_trees_right_region,
        sea_of_trees_boss_region,
        sea_of_trees_post_boss_region,
        sea_of_trees_center_save_region,
        sea_of_trees_center_chika_region,

        crystalline_grotto_entrance_region,
        crystalline_grotto_left_save_region,
        crystalline_grotto_top_left_save_region,
        crystalline_grotto_top_region,
        crystalline_grotto_top_save_region,
        crystalline_grotto_random_region,
        crystalline_grotto_right_save_region,
        crystalline_grotto_bottom_region,
        crystalline_grotto_left_region,
        crystalline_grotto_center_region,
        crystalline_grotto_center_save_region,
        crystalline_grotto_left_center_save_region,
        crystalline_grotto_mari_chest_region,
        crystalline_grotto_boss_region,

        sunken_volcano_left_entrance_region,
        sunken_volcano_soarshoes_region,
        sunken_volcano_top_region,
        sunken_volcano_main_region,
        sunken_volcano_left_region,
        sunken_volcano_boss_region,
        sunken_volcano_path_to_tonosama_region,
        sunken_volcano_tonosama_region,

        shipwreck_left_region,
        shipwreck_left_mast_region,
        shipwreck_main_region,
        shipwreck_bottom_region,
        shipwreck_sealed_off_chest_region,
        shipwreck_postal_guild_bag_region,
        shipwreck_gloves_region,
        shipwreck_top_gloves_region,
        shipwreck_right_mast_region,
        shipwreck_top_entrance_region,
        shipwreck_boss_region,
        shipwreck_right_entrance_region,

        infernal_altar_region,
        aqours_memoria_region,
    ]

def connect_regions(world: World) -> None:
    connect(world, world.origin_region_name, LocationNames.sunken_temple_entrance_region, None)
    connect(world, LocationNames.sunken_temple_entrance_region, LocationNames.sunken_temple_random_region, None, True)
    connect(world, LocationNames.sunken_temple_random_region, LocationNames.sunken_temple_entrance_region, gloves_rule, True)
    connect(world, LocationNames.sunken_temple_random_region, LocationNames.sunken_temple_main_region, None, True)
    connect(world, LocationNames.sunken_temple_main_region, LocationNames.sunken_temple_post_boss_region, 
            Filtered(chika_block_rule, options=chika_blocks_filter, filtered_resolution=True), True)
    connect(world, LocationNames.sunken_temple_main_region, LocationNames.infernal_altar_region, boss_token_rule)
    connect(world, LocationNames.sunken_temple_post_boss_region, LocationNames.grotto_main_region, None)
    
    connect(world, LocationNames.grotto_main_region, LocationNames.grotto_boss_region, sea_charm_rule, True)
    connect(world, LocationNames.grotto_main_region, LocationNames.grotto_top_corridor_region, None, True)
    connect(world, LocationNames.grotto_main_region, LocationNames.ruins_grotto_entrance_region, None)
    connect(world, LocationNames.grotto_top_corridor_region, LocationNames.grotto_main_region, chika_block_rule, True)
    connect(world, LocationNames.grotto_top_corridor_region, LocationNames.grotto_top_region, dia_rule | soarshoes_rule)
    connect(world, LocationNames.grotto_top_region, LocationNames.grotto_coral_hill_entrance_region, you_rule | gloves_rule)
    connect(world, LocationNames.grotto_coral_hill_entrance_region, LocationNames.coral_hill_left_entrance_region, None)
    connect(world, LocationNames.grotto_boss_region, LocationNames.shipwreck_left_region, None, True)

    connect(world, LocationNames.ruins_grotto_entrance_region, LocationNames.ruins_boss_1_region, None, True)
    connect(world, LocationNames.ruins_grotto_entrance_region, LocationNames.ruins_left_of_sandpit_region, soarshoes_rule | you_rule, True)
    connect(world, LocationNames.ruins_left_of_sandpit_region, LocationNames.ruins_grotto_entrance_region, you_rule, True)
    connect(world, LocationNames.ruins_boss_1_region, LocationNames.ruins_boss_2_region, None, True)
    connect(world, LocationNames.ruins_boss_2_region, LocationNames.ruins_left_of_sandpit_region, kanan_rule)
    connect(world, LocationNames.ruins_boss_2_region, LocationNames.ruins_post_boss_2_region, None, True)
    connect(world, LocationNames.ruins_post_boss_2_region, LocationNames.ruins_boss_2_region, None, True)
    connect(world, LocationNames.ruins_post_boss_2_region, LocationNames.ruins_boss_3_region, None, True)
    connect(world, LocationNames.ruins_post_boss_2_region, LocationNames.sunken_volcano_left_entrance_region, None, True)
    connect(world, LocationNames.ruins_boss_3_region, LocationNames.ruins_post_boss_3_region, kanan_rule)
    connect(world, LocationNames.ruins_post_boss_3_region, LocationNames.sunken_volcano_top_region, None)

    connect(world, LocationNames.shipwreck_left_region, LocationNames.shipwreck_left_mast_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.shipwreck_left_region, LocationNames.shipwreck_bottom_region, kanan_rule)
    connect(world, LocationNames.shipwreck_left_region, LocationNames.shipwreck_sealed_off_chest_region, you_skip_rule, True)
    connect(world, LocationNames.shipwreck_sealed_off_chest_region, LocationNames.shipwreck_left_region, None, True)
    connect(world, LocationNames.shipwreck_left_mast_region, LocationNames.shipwreck_left_region, None, True)
    connect(world, LocationNames.shipwreck_left_mast_region, LocationNames.shipwreck_main_region, None, True)
    connect(world, LocationNames.shipwreck_main_region, LocationNames.shipwreck_left_mast_region, gloves_rule, True)
    connect(world, LocationNames.shipwreck_bottom_region, LocationNames.shipwreck_postal_guild_bag_region, 
            (you_skip_rule & kanan_rule & gloves_rule & soarshoes_rule) | (chika_block_rule & upgraded_mari_rule), True)
    connect(world, LocationNames.shipwreck_postal_guild_bag_region, LocationNames.shipwreck_bottom_region, kanan_rule | upgraded_mari_rule, True)
    connect(world, LocationNames.shipwreck_bottom_region, LocationNames.shipwreck_sealed_off_chest_region, riko_rule)
    connect(world, LocationNames.shipwreck_bottom_region, LocationNames.shipwreck_main_region, chika_rule | soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.shipwreck_main_region, LocationNames.shipwreck_bottom_region, None, True)
    connect(world, LocationNames.shipwreck_main_region, LocationNames.shipwreck_gloves_region, None, True)
    connect(world, LocationNames.shipwreck_main_region, LocationNames.shipwreck_top_gloves_region, you_skip_rule & (soarshoes_rule | gloves_rule), True)
    connect(world, LocationNames.shipwreck_top_gloves_region, LocationNames.shipwreck_main_region, None, True)
    connect(world, LocationNames.shipwreck_top_gloves_region, LocationNames.shipwreck_gloves_region, None, True)
    connect(world, LocationNames.shipwreck_top_gloves_region, LocationNames.shipwreck_right_mast_region, gloves_rule, True)
    connect(world, LocationNames.shipwreck_right_mast_region, LocationNames.shipwreck_top_gloves_region, None, True)
    connect(world, LocationNames.shipwreck_right_mast_region, LocationNames.shipwreck_top_entrance_region, soarshoes_rule, True)
    connect(world, LocationNames.shipwreck_right_mast_region, LocationNames.shipwreck_boss_region, ignore_projectile_rule, True)
    connect(world, LocationNames.shipwreck_top_entrance_region, LocationNames.shipwreck_right_mast_region, None, True)
    connect(world, LocationNames.shipwreck_gloves_region, LocationNames.shipwreck_top_gloves_region, gloves_rule, True)
    connect(world, LocationNames.shipwreck_boss_region, LocationNames.shipwreck_right_entrance_region, (hanamaru_rule | you_rule), True)
    connect(world, LocationNames.shipwreck_boss_region, LocationNames.shipwreck_right_mast_region, gloves_rule, True)
    connect(world, LocationNames.shipwreck_right_entrance_region, LocationNames.sea_of_trees_main_region, None)

    connect(world, LocationNames.coral_hill_left_entrance_region, LocationNames.coral_hill_left_save_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_left_save_region, LocationNames.coral_hill_left_entrance_region, None, True)
    connect(world, LocationNames.coral_hill_left_save_region, LocationNames.coral_hill_top_left_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_top_left_region, LocationNames.coral_hill_left_save_region, None, True)
    connect(world, LocationNames.coral_hill_left_save_region, LocationNames.coral_hill_bottom_left_region, None, True)
    connect(world, LocationNames.coral_hill_bottom_left_region, LocationNames.coral_hill_left_save_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_top_left_region, LocationNames.coral_hill_bottom_left_region, None, True)
    connect(world, LocationNames.coral_hill_bottom_left_region, LocationNames.coral_hill_top_left_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_top_left_region, LocationNames.coral_hill_left_climb_region, None, True)
    connect(world, LocationNames.coral_hill_left_climb_region, LocationNames.coral_hill_top_left_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_top_left_region, LocationNames.coral_hill_teleporting_fish_chest_region, you_skip_rule & (soarshoes_rule | gloves_rule), True)
    connect(world, LocationNames.coral_hill_teleporting_fish_chest_region, LocationNames.coral_hill_top_left_region, None, True)
    connect(world, LocationNames.coral_hill_bottom_left_region, LocationNames.coral_hill_left_climb_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_left_climb_region, LocationNames.coral_hill_bottom_left_region, None, True)
    connect(world, LocationNames.coral_hill_bottom_left_region, LocationNames.coral_hill_bottom_region, None, True)
    connect(world, LocationNames.coral_hill_bottom_region, LocationNames.coral_hill_bottom_left_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_left_climb_region, LocationNames.coral_hill_random_save_region, you_skip_rule, True)
    connect(world, LocationNames.coral_hill_random_save_region, LocationNames.coral_hill_left_climb_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_random_save_region, LocationNames.coral_hill_bottom_region, None, True)
    connect(world, LocationNames.coral_hill_bottom_region, LocationNames.coral_hill_random_save_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_random_save_region, LocationNames.coral_hill_random_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_random_region, LocationNames.coral_hill_random_save_region, None, True)
    connect(world, LocationNames.coral_hill_random_region, LocationNames.coral_hill_post_random_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_post_random_region, LocationNames.coral_hill_soarshoesnt_chest_region, None, True)
    connect(world, LocationNames.coral_hill_random_save_region, LocationNames.coral_hill_soarshoesnt_chest_region, soarshoes_rule & gloves_rule, True)
    connect(world, LocationNames.coral_hill_soarshoesnt_chest_region, LocationNames.coral_hill_random_save_region, None, True)
    connect(world, LocationNames.coral_hill_post_random_region, LocationNames.coral_hill_center_save_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_center_save_region, LocationNames.coral_hill_post_random_region, None, True)
    connect(world, LocationNames.coral_hill_center_save_region, LocationNames.coral_hill_teleporting_fish_chest_region, None, True)
    connect(world, LocationNames.coral_hill_teleporting_fish_chest_region, LocationNames.coral_hill_center_save_region, you_rule, True)
    connect(world, LocationNames.coral_hill_center_save_region, LocationNames.coral_hill_teleporting_fish_room_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_teleporting_fish_room_region, LocationNames.coral_hill_center_save_region, None, True)
    connect(world, LocationNames.coral_hill_teleporting_fish_room_region, LocationNames.coral_hill_climb_top_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_climb_top_region, LocationNames.coral_hill_teleporting_fish_room_region, None, True)
    connect(world, LocationNames.coral_hill_climb_top_region, LocationNames.coral_hill_below_top_save_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_below_top_save_region, LocationNames.coral_hill_climb_top_region, None, True)
    connect(world, LocationNames.coral_hill_below_top_save_region, LocationNames.coral_hill_top_save_climb_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_top_save_climb_region, LocationNames.coral_hill_below_top_save_region, None, True)
    connect(world, LocationNames.coral_hill_climb_top_region, LocationNames.coral_hill_top_save_climb_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_top_save_climb_region, LocationNames.coral_hill_climb_top_region, None, True)
    connect(world, LocationNames.coral_hill_top_save_climb_region, LocationNames.coral_hill_top_save_region, soarshoes_rule, True)
    connect(world, LocationNames.coral_hill_top_save_region, LocationNames.coral_hill_top_save_climb_region, None, True)
    connect(world, LocationNames.coral_hill_top_save_region, LocationNames.coral_hill_left_wall_crab_region, soarshoes_rule, True)
    connect(world, LocationNames.coral_hill_left_wall_crab_region, LocationNames.coral_hill_top_save_region, None, True)
    connect(world, LocationNames.coral_hill_left_wall_crab_region, LocationNames.coral_hill_wall_crab_chest_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_wall_crab_chest_region, LocationNames.coral_hill_left_wall_crab_region, None, True)
    connect(world, LocationNames.coral_hill_right_wall_crab_region, LocationNames.coral_hill_wall_crab_chest_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_wall_crab_chest_region, LocationNames.coral_hill_right_wall_crab_region, None, True)
    connect(world, LocationNames.coral_hill_post_random_region, LocationNames.coral_hill_climb_bottom_region, soarshoes_rule, True)
    connect(world, LocationNames.coral_hill_climb_bottom_region, LocationNames.coral_hill_post_random_region, None, True)
    connect(world, LocationNames.coral_hill_climb_top_region, LocationNames.coral_hill_climb_bottom_region, upgraded_ruby_rule, True)
    connect(world, LocationNames.coral_hill_climb_bottom_region, LocationNames.coral_hill_climb_top_region, upgraded_ruby_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_top_save_climb_region, LocationNames.coral_hill_spawner_trident_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_spawner_trident_region, LocationNames.coral_hill_top_save_climb_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_spawner_trident_region, LocationNames.coral_hill_boss_region, gloves_rule, True)
    connect(world, LocationNames.coral_hill_boss_region, LocationNames.coral_hill_spawner_trident_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_boss_region, LocationNames.coral_hill_right_wall_crab_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.coral_hill_boss_region, LocationNames.coral_hill_bottom_entrance_region, upgraded_mari_rule | kanan_rule, True)
    connect(world, LocationNames.coral_hill_boss_region, LocationNames.coral_hill_right_entrance_region, ignore_projectile_rule, True)
    connect(world, LocationNames.coral_hill_right_entrance_region, LocationNames.coral_hill_boss_region, None, True)
    connect(world, LocationNames.coral_hill_bottom_entrance_region, LocationNames.shipwreck_boss_region, None)
    connect(world, LocationNames.coral_hill_right_entrance_region, LocationNames.crystalline_grotto_entrance_region, None)

    connect(world, LocationNames.sea_of_trees_main_region, LocationNames.sea_of_trees_random_region, (soarshoes_rule | gloves_rule) & upgraded_kanan_rule, True)
    connect(world, LocationNames.sea_of_trees_random_region, LocationNames.sea_of_trees_main_region, kanan_rule, True)
    connect(world, LocationNames.sea_of_trees_main_region, LocationNames.sea_of_trees_center_save_region, chika_block_rule | soarshoes_rule, True)
    connect(world, LocationNames.sea_of_trees_main_region, LocationNames.sea_of_trees_center_chika_region, riko_rule)
    connect(world, LocationNames.sea_of_trees_center_save_region, LocationNames.sea_of_trees_main_region, None, True)
    connect(world, LocationNames.sea_of_trees_center_save_region, LocationNames.sea_of_trees_center_chika_region, upgraded_kanan_rule, True)
    connect(world, LocationNames.sea_of_trees_center_chika_region, LocationNames.sea_of_trees_center_save_region, kanan_rule, True)
    connect(world, LocationNames.sea_of_trees_center_chika_region, LocationNames.sea_of_trees_random_region, kanan_rule | chika_rule, True)
    connect(world, LocationNames.sea_of_trees_random_region, LocationNames.sea_of_trees_right_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.sea_of_trees_right_region, LocationNames.sea_of_trees_boss_region, None, True)
    connect(world, LocationNames.sea_of_trees_right_region, LocationNames.sea_of_trees_top_left_region, soarshoes_rule)
    connect(world, LocationNames.sea_of_trees_random_region, LocationNames.sea_of_trees_top_left_region, soarshoes_rule & gloves_rule & you_skip_rule, True)
    connect(world, LocationNames.sea_of_trees_top_left_region, LocationNames.sea_of_trees_random_region, gloves_rule | you_skip_rule, True)
    connect(world, LocationNames.sea_of_trees_boss_region, LocationNames.sea_of_trees_right_region, you_rule, True)
    connect(world, LocationNames.sea_of_trees_boss_region, LocationNames.sea_of_trees_post_boss_region, None, True)

    connect(world, LocationNames.crystalline_grotto_entrance_region, LocationNames.crystalline_grotto_left_save_region, soarshoes_rule | gloves_rule)
    connect(world, LocationNames.crystalline_grotto_entrance_region, LocationNames.crystalline_grotto_left_region, hanamaru_rule | soarshoes_rule | gloves_rule) # you_rule on hard
    connect(world, LocationNames.crystalline_grotto_left_save_region, LocationNames.crystalline_grotto_top_left_save_region, gloves_rule, True)
    connect(world, LocationNames.crystalline_grotto_top_left_save_region, LocationNames.crystalline_grotto_left_save_region, None, True)
    connect(world, LocationNames.crystalline_grotto_top_left_save_region, LocationNames.crystalline_grotto_top_region, soarshoes_rule | gloves_rule)
    connect(world, LocationNames.crystalline_grotto_top_region, LocationNames.crystalline_grotto_left_region, kanan_rule, True)
    connect(world, LocationNames.crystalline_grotto_top_region, LocationNames.crystalline_grotto_center_region, you_rule & riko_rule, True)
    connect(world, LocationNames.crystalline_grotto_left_region, LocationNames.crystalline_grotto_top_region, upgraded_kanan_rule, True)
    connect(world, LocationNames.crystalline_grotto_left_region, LocationNames.crystalline_grotto_center_region, chika_block_rule & CanReachRegion(LocationNames.crystalline_grotto_center_save_region), True)
    connect(world, LocationNames.crystalline_grotto_center_region, LocationNames.crystalline_grotto_left_region, upgraded_ruby_rule & CanReachRegion(LocationNames.crystalline_grotto_center_save_region), True)
    connect(world, LocationNames.crystalline_grotto_left_region, LocationNames.crystalline_grotto_center_save_region, upgraded_ruby_rule, True)
    connect(world, LocationNames.crystalline_grotto_left_region, LocationNames.crystalline_grotto_left_center_save_region, None)
    connect(world, LocationNames.crystalline_grotto_left_center_save_region, LocationNames.crystalline_grotto_center_save_region, None, True)
    connect(world, LocationNames.crystalline_grotto_center_save_region, LocationNames.crystalline_grotto_left_center_save_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.crystalline_grotto_center_save_region, LocationNames.crystalline_grotto_center_region, None, True)
    connect(world, LocationNames.crystalline_grotto_center_region, LocationNames.crystalline_grotto_top_save_region, gloves_rule, True)
    connect(world, LocationNames.crystalline_grotto_center_region, LocationNames.crystalline_grotto_top_region, riko_rule, True)
    connect(world, LocationNames.crystalline_grotto_center_region, LocationNames.crystalline_grotto_bottom_region, upgraded_ruby_rule, True)
    connect(world, LocationNames.crystalline_grotto_center_region, LocationNames.crystalline_grotto_mari_chest_region, None, True)
    connect(world, LocationNames.crystalline_grotto_mari_chest_region, LocationNames.crystalline_grotto_center_region, gloves_rule, True)
    connect(world, LocationNames.crystalline_grotto_mari_chest_region, LocationNames.crystalline_grotto_center_save_region, mari_rule & sea_charm_rule, True)
    connect(world, LocationNames.crystalline_grotto_top_save_region, LocationNames.crystalline_grotto_center_region, None, True)
    connect(world, LocationNames.crystalline_grotto_top_save_region, LocationNames.crystalline_grotto_random_region, gloves_rule, True)
    connect(world, LocationNames.crystalline_grotto_random_region, LocationNames.crystalline_grotto_top_save_region, None, True)
    connect(world, LocationNames.crystalline_grotto_random_region, LocationNames.crystalline_grotto_right_save_region, dia_rule & kanan_rule & sea_charm_rule, True)
    connect(world, LocationNames.crystalline_grotto_right_save_region, LocationNames.crystalline_grotto_center_region, chika_block_rule, True)
    connect(world, LocationNames.crystalline_grotto_right_save_region, LocationNames.crystalline_grotto_bottom_region, None, True)
    connect(world, LocationNames.crystalline_grotto_bottom_region, LocationNames.crystalline_grotto_center_region, chika_block_rule, True)
    connect(world, LocationNames.crystalline_grotto_bottom_region, LocationNames.crystalline_grotto_boss_region, dia_rule | (gloves_rule & soarshoes_rule), True)
    connect(world, LocationNames.crystalline_grotto_boss_region, LocationNames.crystalline_grotto_left_region, mari_rule, True)

    connect(world, LocationNames.sunken_volcano_top_region, LocationNames.sunken_volcano_main_region, None, True)
    connect(world, LocationNames.sunken_volcano_top_region, LocationNames.sunken_volcano_boss_region, soarshoes_rule | (you_rule & gloves_rule), True)
    connect(world, LocationNames.sunken_volcano_main_region, LocationNames.sunken_volcano_top_region, soarshoes_rule | gloves_rule, True)
    connect(world, LocationNames.sunken_volcano_main_region, LocationNames.sunken_volcano_boss_region, you_rule, True)
    connect(world, LocationNames.sunken_volcano_main_region, LocationNames.sunken_volcano_path_to_tonosama_region, hanamaru_rule | you_rule, True)
    connect(world, LocationNames.sunken_volcano_main_region, LocationNames.sunken_volcano_left_region, None, True)
    connect(world, LocationNames.sunken_volcano_path_to_tonosama_region, LocationNames.sunken_volcano_tonosama_region, riko_rule)
    connect(world, LocationNames.sunken_volcano_path_to_tonosama_region, LocationNames.sunken_volcano_main_region, None, True)
    connect(world, LocationNames.sunken_volcano_tonosama_region, LocationNames.sunken_volcano_left_region, mari_rule | dia_rule | big_weapon_rule | upgraded_hanamaru_rule)
    connect(world, LocationNames.sunken_volcano_left_entrance_region, LocationNames.sunken_volcano_soarshoes_region, (soarshoes_rule & gloves_rule) | (you_rule & (soarshoes_rule | gloves_rule)), True)
    connect(world, LocationNames.sunken_volcano_soarshoes_region, LocationNames.sunken_volcano_left_entrance_region, None, True)
    connect(world, LocationNames.sunken_volcano_soarshoes_region, LocationNames.sunken_volcano_left_region, you_rule, True)
    connect(world, LocationNames.sunken_volcano_left_region, LocationNames.sunken_volcano_soarshoes_region, None, True)
    connect(world, LocationNames.sunken_volcano_boss_region, LocationNames.sunken_volcano_top_region, None, True)
    connect(world, LocationNames.sunken_volcano_boss_region, LocationNames.sunken_volcano_main_region, None, True)

    connect(world, LocationNames.infernal_altar_region, LocationNames.aqours_memoria_region, CanReachLocation(LocationNames.infernal_altar_boss_defeated))
    pass

def create_region(world: World, name: str, active_locations: dict[str, int], location_set: set[str]) -> Region:
    region = Region(name, world.player, world.multiworld)
    for location in location_set:
        code = active_locations.get(location, 0)
        if location in active_locations.keys():
            region.locations.append(YohaneDeepblueLocation(world.player, location, code, region))
    return region

def connect(world: World, source: str, destination: str, rule: typing.Optional[Rule | typing.Callable[[CollectionState],bool]], one_way: bool = False, randomization_group: int = 0) -> None:
    source_region = world.multiworld.get_region(source, world.player)
    dest_region = world.multiworld.get_region(destination, world.player)

    entrance_name = source
    randomization_type = EntranceType.ONE_WAY
    if one_way:
        entrance_name += " -> "
    else:
        randomization_type = EntranceType.TWO_WAY
        entrance_name += " <-> "
    entrance_name += destination 
    entrance = Entrance(world.player, entrance_name, source_region, randomization_group, randomization_type)

    if rule is not None:
        world.set_rule(entrance, rule)
    
    source_region.exits.append(entrance)
    entrance.connect(dest_region)