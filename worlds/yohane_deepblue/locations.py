from BaseClasses import Location
from Options import Toggle
from worlds.AutoWorld import World

from .data import LocationNames
from .data.constants import GAME_NAME


class YohaneDeepblueLocation(Location):
    game: str = GAME_NAME

character_rescue_locations = {
    LocationNames.chika_rescue: 1,
    LocationNames.kanan_rescue: 2,
    LocationNames.dia_rescue: 3,
    LocationNames.ruby_rescue: 4,
    LocationNames.you_rescue: 5,
    LocationNames.mari_rescue: 6,
    LocationNames.riko_rescue: 7,
    LocationNames.hanamaru_rescue: 8,
}

character_upgrade_locations = {
    LocationNames.chika_upgrade_quest: 20,
    LocationNames.riko_upgrade_quest: 21,
    LocationNames.kanan_upgrade_quest: 22,
    LocationNames.hanamaru_upgrade_quest: 23,
    LocationNames.ruby_upgrade_quest: 24,
    LocationNames.you_upgrade_quest: 25,
    LocationNames.dia_upgrade_quest: 26,
    LocationNames.mari_upgrade_quest: 27,
}

boss_fight_locations = {
    LocationNames.sunken_temple_boss_defeated: 40,
    LocationNames.ruins_boss_defeated_1: 41,
    LocationNames.ruins_boss_defeated_2: 42,
    LocationNames.ruins_boss_defeated_3: 43,
    LocationNames.grotto_boss_defeated: 44,
    LocationNames.coral_hill_boss_defeated: 45,
    LocationNames.sea_of_trees_boss_defeated: 46,
    LocationNames.crystalline_grotto_boss_defeated: 47,
    LocationNames.sunken_volcano_boss_defeated: 48,
    LocationNames.shipwreck_boss_defeated: 49,
    LocationNames.infernal_altar_boss_defeated: 50,

    LocationNames.aquors_memoria_boss_defeated: None
}

boss_refight_locations = {
    LocationNames.sunken_temple_boss_refight: 60,
    LocationNames.ruins_boss_refight: 61,
    LocationNames.grotto_boss_refight: 62,
    LocationNames.coral_hill_boss_refight: 63,
    LocationNames.sea_of_trees_boss_refight: 64,
    LocationNames.crystalline_grotto_boss_refight: 65,
    LocationNames.sunken_volcano_boss_refight: 66,
    LocationNames.shipwreck_boss_refight: 67,
    LocationNames.infernal_altar_boss_refight: 68,
}

chest_locations = {
    LocationNames.cast_tutorial_left_chest: 80,
    LocationNames.case_tutorial_right_chest: 81,
    LocationNames.fishy_archery_chest: 82,
    LocationNames.pathway_to_infernal_altar_chest: 83,
    LocationNames.katys_mask_room_chest: 84,
    LocationNames.chika_testing_grounds_chest: 85,

    LocationNames.grotto_next_to_first_save_room_chest: 86,
    LocationNames.first_waterfall_room_chest: 87,
    LocationNames.first_lake_room_chest: 88,
    LocationNames.second_lake_room_chest: 89,
    LocationNames.spellbook_room_chest: 90,
    LocationNames.long_waterfall_room_chest: 91,
    LocationNames.isolated_climb_room_chest: 92,
    LocationNames.small_cave_climb_room_chest: 93,

    LocationNames.sandy_trap_room_chest: 94,
    LocationNames.vertical_poison_room_chest: 95,
    LocationNames.rolling_rocks_room_chest: 96,
    LocationNames.laptop_room_chest: 97,
    LocationNames.hall_of_shame_chest: 98,

    LocationNames.sunken_volcano_next_to_first_save_room_chest: 99,
    LocationNames.hotspring_room_chest: 100,
    LocationNames.soarshoes_room_chest: 101,
    LocationNames.soarshoes_obligatory_issue_room_chest: 102,
    LocationNames.tonosamas_parts_room_chest: 103,

    LocationNames.really_sealed_off_chest_room_chest: 104,
    LocationNames.spikey_ball_fish_room_chest: 105,
    LocationNames.final_guard_room_chest: 106,
    LocationNames.gloves_of_might_room_chest: 107,
    LocationNames.postal_guild_bag_room: 108,

    LocationNames.soarshoesnt_chest_room_chest: 109,
    LocationNames.annoying_teleporting_fish_room_chest: 110,
    LocationNames.wallcrab_chest_room_chest: 111,
    LocationNames.dumb_block_room_chest: 112,
    LocationNames.lost_monstie_room_chest: 113,

    LocationNames.one_way_slide_room_chest: 114,
    LocationNames.giant_sliding_crystals_room_chest: 115,
    LocationNames.isolated_chest_room_chest: 116,
    LocationNames.looong_slide_room_chest: 117,
    LocationNames.mari_issue_room_chest: 118,

    LocationNames.giant_poison_enemy_crab_room_chest: 119,
    LocationNames.scarlet_delta_suit_room_chest: 120,
    LocationNames.golden_snail_room_chest: 121,
    LocationNames.slope_room_chest: 122,
    LocationNames.you_testing_grounds_chest: 123,

    LocationNames.purple_goo_room_chest: 124,
    LocationNames.dark_room_chest: 125,
}


crafting_locations = {
    LocationNames.recipe_01: 701,
    LocationNames.recipe_02: 702,
    LocationNames.recipe_03: 703,
    LocationNames.recipe_04: 704,
    LocationNames.recipe_05: 705,
    LocationNames.recipe_06: 706,
    LocationNames.recipe_07: 707,
    LocationNames.recipe_08: 708,
    LocationNames.recipe_09: 709,
    LocationNames.recipe_10: 710,
    LocationNames.recipe_11: 711,
    LocationNames.recipe_12: 712,
    LocationNames.recipe_13: 713,
    LocationNames.recipe_14: 714,
    LocationNames.recipe_15: 715,
    LocationNames.recipe_16: 716,
    LocationNames.recipe_17: 717,
    LocationNames.recipe_18: 718,
    LocationNames.recipe_19: 719,
    LocationNames.recipe_20: 720,
    LocationNames.recipe_21: 721,
    LocationNames.recipe_22: 722,
    LocationNames.recipe_23: 723,
    LocationNames.recipe_24: 724,
    LocationNames.recipe_25: 725,
    LocationNames.recipe_26: 726,
    LocationNames.recipe_27: 727,
    LocationNames.recipe_28: 728,
    LocationNames.recipe_29: 729,
    LocationNames.recipe_30: 730,
    LocationNames.recipe_31: 731,
    LocationNames.recipe_32: 732,
    LocationNames.recipe_33: 733,
    LocationNames.recipe_34: 734,
    LocationNames.recipe_35: 735,
    LocationNames.recipe_36: 736,
    LocationNames.recipe_37: 737,
    LocationNames.recipe_38: 738,
    LocationNames.recipe_39: 739,
    LocationNames.recipe_40: 740,
    LocationNames.recipe_41: 741,
    LocationNames.recipe_42: 742,
    LocationNames.recipe_43: 743,
    LocationNames.recipe_44: 744,
    LocationNames.recipe_45: 745,
    LocationNames.recipe_46: 746,
    LocationNames.recipe_47: 747,
    LocationNames.recipe_48: 748,
    LocationNames.recipe_49: 749,
    LocationNames.recipe_50: 750,
    LocationNames.recipe_51: 751,
    LocationNames.recipe_52: 752,
    LocationNames.recipe_53: 753,
    LocationNames.recipe_54: 754,
    LocationNames.recipe_55: 755,
    LocationNames.recipe_56: 756,
    LocationNames.recipe_57: 757,
    LocationNames.recipe_58: 758,
    LocationNames.recipe_59: 759,
    LocationNames.recipe_60: 760,
    LocationNames.recipe_61: 761,
    LocationNames.recipe_62: 762,
    LocationNames.recipe_63: 763,
    LocationNames.recipe_64: 764,
    LocationNames.recipe_65: 765,
    LocationNames.recipe_66: 766,
    LocationNames.recipe_67: 767,
    LocationNames.recipe_68: 768,
    LocationNames.recipe_69: 769,
    LocationNames.recipe_70: 770,
    LocationNames.recipe_71: 771,
    LocationNames.recipe_72: 772,
    LocationNames.recipe_73: 773,
    LocationNames.recipe_74: 774,
    LocationNames.recipe_75: 775,
    LocationNames.recipe_76: 776,
    LocationNames.recipe_77: 777,
    LocationNames.recipe_78: 778,
    LocationNames.recipe_79: 779,
    LocationNames.recipe_80: 780,
    LocationNames.recipe_81: 781,
    LocationNames.recipe_82: 782,
    LocationNames.recipe_83: 783,
    LocationNames.recipe_84: 784,
    LocationNames.recipe_85: 785,
    LocationNames.recipe_86: 786,
    LocationNames.recipe_87: 787,
    LocationNames.recipe_88: 788,
    LocationNames.recipe_89: 789,
    LocationNames.recipe_90: 790,
    LocationNames.recipe_91: 791,
    LocationNames.recipe_92: 792,
    LocationNames.recipe_93: 793,
}


menu_region_locations = {
    LocationNames.chika_upgrade_quest,
    LocationNames.riko_upgrade_quest,
    LocationNames.kanan_upgrade_quest,
    LocationNames.hanamaru_upgrade_quest,
    LocationNames.ruby_upgrade_quest,
    LocationNames.you_upgrade_quest,
    LocationNames.dia_upgrade_quest,
    LocationNames.mari_upgrade_quest,
    *crafting_locations
}


sunken_temple_entrance_region_locations = {
    LocationNames.cast_tutorial_left_chest,
    LocationNames.case_tutorial_right_chest,
    LocationNames.fishy_archery_chest,
}

sunken_temple_random_region_locations = set()

sunken_temple_main_region_locations = {
    LocationNames.sunken_temple_boss_defeated,

    LocationNames.pathway_to_infernal_altar_chest,
    LocationNames.katys_mask_room_chest,

    LocationNames.chika_rescue,
}

sunken_temple_post_boss_region_locations = {
    LocationNames.chika_testing_grounds_chest,
}


ruins_grotto_entrance_region_locations = set()

ruins_boss_1_region_locations = {
    LocationNames.ruins_boss_defeated_1,
}

ruins_boss_2_region_locations = {
    LocationNames.ruins_boss_defeated_2,

    LocationNames.vertical_poison_room_chest,
    LocationNames.laptop_room_chest,
}

ruins_post_boss_2_region_locations = {
    LocationNames.rolling_rocks_room_chest,
}

ruins_boss_3_region_locations = {
    LocationNames.ruins_boss_defeated_3,

    LocationNames.kanan_rescue,
}

ruins_post_boss_3_region_locations = set()

ruins_left_of_sandpit_region_locations = {
    LocationNames.sandy_trap_room_chest,
    LocationNames.hall_of_shame_chest,
}


grotto_main_region_locations = {
    LocationNames.grotto_next_to_first_save_room_chest,
    LocationNames.first_waterfall_room_chest,
    LocationNames.first_lake_room_chest,
    LocationNames.second_lake_room_chest,
    LocationNames.spellbook_room_chest,
    LocationNames.long_waterfall_room_chest,
}

grotto_top_corridor_region_locations = set()

grotto_top_region_locations = set()

grotto_coral_hill_entrance_region_locations = set()

grotto_boss_region_locations = {
    LocationNames.grotto_boss_defeated,

    LocationNames.isolated_climb_room_chest,
    LocationNames.small_cave_climb_room_chest,

    LocationNames.dia_rescue,
}


coral_hill_left_entrance_region_locations = set()

coral_hill_left_save_region_locations = set()

coral_hill_top_left_region_locations = set()

coral_hill_bottom_left_region_locations = set()

coral_hill_left_climb_region_locations = set()

coral_hill_random_save_region_locations = set()

coral_hill_bottom_region_locations = {
    LocationNames.lost_monstie_room_chest,
}

coral_hill_random_region_locations = set()

coral_hill_post_random_region_locations = set()

coral_hill_soarshoesnt_chest_region_locations = {
    LocationNames.soarshoesnt_chest_room_chest,
}

coral_hill_center_save_region_locations = set()

coral_hill_teleporting_fish_chest_region_locations = {
    LocationNames.annoying_teleporting_fish_room_chest,
}

coral_hill_climb_bottom_region_locations = {
    LocationNames.dumb_block_room_chest,
}

coral_hill_teleporting_fish_room_region_locations = set()

coral_hill_climb_top_region_locations = set()

coral_hill_below_top_save_region_locations = set()

coral_hill_top_save_region_locations = set()

coral_hill_top_save_climb_region_locations = set()

coral_hill_left_wall_crab_region_locations = set()

coral_hill_wall_crab_chest_region_locations = {
    LocationNames.wallcrab_chest_room_chest,
}

coral_hill_right_wall_crab_region_locations = set()

coral_hill_boss_region_locations = {
    LocationNames.coral_hill_boss_defeated,

    LocationNames.ruby_rescue,
}

coral_hill_spawner_trident_region_locations = set()

coral_hill_right_entrance_region_locations = set()

coral_hill_bottom_entrance_region_locations = set()


sea_of_trees_main_region_locations = {
    LocationNames.giant_poison_enemy_crab_room_chest,
    LocationNames.scarlet_delta_suit_room_chest,
}

sea_of_trees_random_region_locations = set()

sea_of_trees_top_left_region_locations = set()

sea_of_trees_right_region_locations = {
    LocationNames.golden_snail_room_chest,
    LocationNames.slope_room_chest,
}

sea_of_trees_boss_region_locations = {
    LocationNames.sea_of_trees_boss_defeated,

    LocationNames.you_rescue,
}

sea_of_trees_post_boss_region_locations = {
    LocationNames.you_testing_grounds_chest,
}

sea_of_trees_center_save_region_locations = set()

sea_of_trees_center_chika_region_locations = set()

sea_of_trees_long_slide_region_locations = set()


crystalline_grotto_entrance_region_locations = {
    LocationNames.one_way_slide_room_chest,
}

crystalline_grotto_left_save_region_locations = set()

crystalline_grotto_top_left_save_region_locations = set()

crystalline_grotto_top_region_locations = {
    LocationNames.giant_sliding_crystals_room_chest,
}

crystalline_grotto_top_save_region_locations = set()

crystalline_grotto_random_region_locations = set()

crystalline_grotto_right_save_region_locations = {
    LocationNames.isolated_chest_room_chest,
}

crystalline_grotto_bottom_region_locations = {
    LocationNames.looong_slide_room_chest,
}

crystalline_grotto_post_boss_region_locations = set()

crystalline_grotto_center_region_locations = set()

crystalline_grotto_center_save_region_locations = set()

crystalline_grotto_left_center_save_region_locations = set()

crystalline_grotto_mari_chest_region_locations = {
    LocationNames.mari_issue_room_chest,
}

crystalline_grotto_boss_region_locations = {
    LocationNames.crystalline_grotto_boss_defeated,

    LocationNames.mari_rescue,
}


sunken_volcano_left_entrance_region_locations = set()

sunken_volcano_soarshoes_region_locations = {
    LocationNames.soarshoes_room_chest
}

sunken_volcano_top_region_locations = {
    LocationNames.sunken_volcano_next_to_first_save_room_chest,
}

sunken_volcano_main_region_locations = {
    LocationNames.hotspring_room_chest,
}

sunken_volcano_left_region_locations = set()

sunken_volcano_path_to_tonosama_region_locations = set()

sunken_volcano_tonosama_region_locations = {
    LocationNames.tonosamas_parts_room_chest,
}

sunken_volcano_boss_region_locations = {
    LocationNames.sunken_volcano_boss_defeated,

    LocationNames.soarshoes_obligatory_issue_room_chest,

    LocationNames.riko_rescue,
}


shipwreck_left_region_locations = set()

shipwreck_left_mast_region_locations = {
    LocationNames.spikey_ball_fish_room_chest,
}

shipwreck_main_region_locations = {
    LocationNames.final_guard_room_chest,
}

shipwreck_bottom_region_locations = set()

shipwreck_sealed_off_chest_region_locations = {
    LocationNames.really_sealed_off_chest_room_chest,
}

shipwreck_postal_guild_bag_region_locations = {
    LocationNames.postal_guild_bag_room,
}

shipwreck_post_postal_guild_bag_region_locations = set()

shipwreck_gloves_region_locations = {
    LocationNames.gloves_of_might_room_chest,
}

shipwreck_top_gloves_region_locations = set()

shipwreck_right_mast_region_locations = set()

shipwreck_top_entrance_region_locations = set()

shipwreck_boss_region_locations = {
    LocationNames.shipwreck_boss_defeated,

    LocationNames.hanamaru_rescue,
}

shipwreck_right_entrance_region_locations = set()


infernal_altar_region_locations = {
    LocationNames.infernal_altar_boss_defeated,

    LocationNames.purple_goo_room_chest,
    LocationNames.dark_room_chest,
}

aqours_memoria_region_locations = {
    LocationNames.aquors_memoria_boss_defeated,

    LocationNames.sunken_temple_boss_refight,
    LocationNames.ruins_boss_refight,
    LocationNames.grotto_boss_refight,
    LocationNames.coral_hill_boss_refight,
    LocationNames.sea_of_trees_boss_refight,
    LocationNames.crystalline_grotto_boss_refight,
    LocationNames.sunken_volcano_boss_refight,
    LocationNames.shipwreck_boss_refight,
    LocationNames.infernal_altar_boss_refight,
}

location_table: dict[str, int | None] = {
    **character_rescue_locations,
    **character_upgrade_locations,
    **boss_fight_locations,
    **boss_refight_locations,
    **chest_locations,
    **crafting_locations
}

def setup_locations(world: World, player: int) -> dict[str, int | None]:
    is_ut = getattr(world.multiworld, "generation_is_fake", False)
    if is_ut:
        return location_table
    locations: dict[str, int | None] = {}
    locations.update({**character_rescue_locations})
    locations.update({**character_upgrade_locations})
    locations.update({**boss_fight_locations})
    locations.update({**boss_refight_locations})
    locations.update({**chest_locations})
    if world.options.craftsanity == Toggle.option_true:
        locations.update({**crafting_locations})
    return locations

lookup_id_to_name: dict[int, str] = {idx: name for name, idx in location_table.items() if idx is not None}

location_groups: dict[str, set[str]] = {
    "Bosses": set({boss for boss in (boss_fight_locations.keys() | boss_refight_locations.keys())
                   if location_table[boss] is not None}),
    "Chests": set(chest_locations.keys()),
    "Rescues": set(character_rescue_locations.keys()),
    "Upgrade Quests": set(character_upgrade_locations.keys()),
    "Sunken Temple": (sunken_temple_entrance_region_locations | sunken_temple_random_region_locations |
                      sunken_temple_main_region_locations | sunken_temple_post_boss_region_locations),
    "Grotto": (grotto_main_region_locations | grotto_boss_region_locations | grotto_top_corridor_region_locations |
               grotto_top_region_locations | grotto_coral_hill_entrance_region_locations),
    "Ruins": (ruins_grotto_entrance_region_locations | ruins_boss_1_region_locations | ruins_boss_2_region_locations |
              ruins_post_boss_2_region_locations | ruins_boss_3_region_locations | ruins_post_boss_3_region_locations |
              ruins_left_of_sandpit_region_locations),
    "Sunken Volcano": (sunken_volcano_left_region_locations | sunken_volcano_main_region_locations |
                       sunken_volcano_boss_region_locations),
    "Coral Hill": (coral_hill_left_entrance_region_locations | coral_hill_left_save_region_locations |
                   coral_hill_top_left_region_locations | coral_hill_bottom_left_region_locations |
                   coral_hill_left_climb_region_locations | coral_hill_random_save_region_locations |
                   coral_hill_bottom_region_locations | coral_hill_random_region_locations |
                   coral_hill_post_random_region_locations | coral_hill_soarshoesnt_chest_region_locations |
                   coral_hill_center_save_region_locations | coral_hill_teleporting_fish_chest_region_locations |
                   coral_hill_climb_bottom_region_locations | coral_hill_teleporting_fish_room_region_locations |
                   coral_hill_climb_top_region_locations | coral_hill_below_top_save_region_locations |
                   coral_hill_top_save_region_locations | coral_hill_top_save_climb_region_locations |
                   coral_hill_left_wall_crab_region_locations | coral_hill_wall_crab_chest_region_locations |
                   coral_hill_right_wall_crab_region_locations | coral_hill_boss_region_locations |
                   coral_hill_spawner_trident_region_locations | coral_hill_right_entrance_region_locations |
                   coral_hill_bottom_entrance_region_locations),
    "Crystalline Grotto": (crystalline_grotto_entrance_region_locations |
                           crystalline_grotto_left_save_region_locations |
                           crystalline_grotto_top_left_save_region_locations |
                           crystalline_grotto_top_region_locations | crystalline_grotto_top_save_region_locations |
                           crystalline_grotto_random_region_locations | crystalline_grotto_right_save_region_locations |
                           crystalline_grotto_bottom_region_locations | crystalline_grotto_post_boss_region_locations |
                           crystalline_grotto_center_region_locations |
                           crystalline_grotto_center_save_region_locations |
                           crystalline_grotto_left_center_save_region_locations |
                           crystalline_grotto_mari_chest_region_locations | crystalline_grotto_boss_region_locations),
    "Shipwreck": (shipwreck_left_region_locations | shipwreck_left_mast_region_locations |
                  shipwreck_main_region_locations | shipwreck_bottom_region_locations |
                  shipwreck_sealed_off_chest_region_locations | shipwreck_postal_guild_bag_region_locations |
                  shipwreck_post_postal_guild_bag_region_locations | shipwreck_gloves_region_locations |
                  shipwreck_top_gloves_region_locations | shipwreck_right_mast_region_locations |
                  shipwreck_top_entrance_region_locations | shipwreck_boss_region_locations |
                  shipwreck_right_entrance_region_locations),
    "Sea of Trees": (sea_of_trees_main_region_locations | sea_of_trees_random_region_locations |
                     sea_of_trees_right_region_locations | sea_of_trees_top_left_region_locations |
                     sea_of_trees_boss_region_locations | sea_of_trees_post_boss_region_locations |
                     sea_of_trees_center_save_region_locations | sea_of_trees_center_chika_region_locations |
                     sea_of_trees_long_slide_region_locations),
    "Infernal Altar": infernal_altar_region_locations,
    "Aqours Memoria": {boss for boss in aqours_memoria_region_locations if location_table[boss] is not None},
    "Crafting Recipe": set(crafting_locations.keys())
}

region_groups = {
    "Sunken Temple": {LocationNames.sunken_temple_entrance_region, LocationNames.sunken_temple_random_region,
                      LocationNames.sunken_temple_main_region, LocationNames.sunken_temple_post_boss_region},
    "Grotto": {LocationNames.grotto_main_region, LocationNames.grotto_boss_region,
               LocationNames.grotto_top_corridor_region, LocationNames.grotto_top_region,
               LocationNames.grotto_coral_hill_entrance_region},
    "Ruins": {LocationNames.ruins_grotto_entrance_region, LocationNames.ruins_boss_1_region,
              LocationNames.ruins_boss_2_region, LocationNames.ruins_post_boss_2_region,
              LocationNames.ruins_boss_3_region, LocationNames.ruins_post_boss_3_region,
              LocationNames.ruins_left_of_sandpit_region},
    "Sunken Volcano": {LocationNames.sunken_volcano_left_region, LocationNames.sunken_volcano_main_region,
                       LocationNames.sunken_volcano_boss_region},
    "Coral Hill": {LocationNames.coral_hill_left_entrance_region, LocationNames.coral_hill_left_save_region,
                   LocationNames.coral_hill_top_left_region, LocationNames.coral_hill_bottom_left_region,
                   LocationNames.coral_hill_left_climb_region, LocationNames.coral_hill_random_save_region,
                   LocationNames.coral_hill_bottom_region, LocationNames.coral_hill_random_region,
                   LocationNames.coral_hill_post_random_region, LocationNames.coral_hill_soarshoesnt_chest_region,
                   LocationNames.coral_hill_center_save_region, LocationNames.coral_hill_teleporting_fish_chest_region,
                   LocationNames.coral_hill_climb_bottom_region, LocationNames.coral_hill_teleporting_fish_room_region,
                   LocationNames.coral_hill_climb_top_region, LocationNames.coral_hill_below_top_save_region,
                   LocationNames.coral_hill_top_save_region, LocationNames.coral_hill_top_save_climb_region,
                   LocationNames.coral_hill_left_wall_crab_region, LocationNames.coral_hill_wall_crab_chest_region,
                   LocationNames.coral_hill_right_wall_crab_region, LocationNames.coral_hill_boss_region,
                   LocationNames.coral_hill_spawner_trident_region, LocationNames.coral_hill_right_entrance_region,
                   LocationNames.coral_hill_bottom_entrance_region},
    "Crystalline Grotto": {LocationNames.crystalline_grotto_entrance_region,
                           LocationNames.crystalline_grotto_left_save_region,
                           LocationNames.crystalline_grotto_top_left_save_region,
                           LocationNames.crystalline_grotto_top_region,
                           LocationNames.crystalline_grotto_top_save_region,
                           LocationNames.crystalline_grotto_random_region,
                           LocationNames.crystalline_grotto_right_save_region,
                           LocationNames.crystalline_grotto_bottom_region,
                           LocationNames.crystalline_grotto_post_boss_region,
                           LocationNames.crystalline_grotto_center_region,
                           LocationNames.crystalline_grotto_center_save_region,
                           LocationNames.crystalline_grotto_left_center_save_region,
                           LocationNames.crystalline_grotto_mari_chest_region,
                           LocationNames.crystalline_grotto_boss_region},
    "Shipwreck": {LocationNames.shipwreck_left_region, LocationNames.shipwreck_left_mast_region,
                  LocationNames.shipwreck_main_region, LocationNames.shipwreck_bottom_region,
                  LocationNames.shipwreck_sealed_off_chest_region, LocationNames.shipwreck_postal_guild_bag_region,
                  LocationNames.shipwreck_post_postal_guild_bag_region, LocationNames.shipwreck_gloves_region,
                  LocationNames.shipwreck_top_gloves_region, LocationNames.shipwreck_right_mast_region,
                  LocationNames.shipwreck_top_entrance_region, LocationNames.shipwreck_boss_region,
                  LocationNames.shipwreck_right_entrance_region},
    "Sea of Trees": {LocationNames.sea_of_trees_main_region, LocationNames.sea_of_trees_random_region,
                     LocationNames.sea_of_trees_right_region, LocationNames.sea_of_trees_top_left_region,
                     LocationNames.sea_of_trees_boss_region, LocationNames.sea_of_trees_post_boss_region,
                     LocationNames.sea_of_trees_center_save_region, LocationNames.sea_of_trees_center_chika_region,
                     LocationNames.sea_of_trees_long_slide_region},
    "Infernal Altar": {LocationNames.infernal_altar_region},
    "Aqours Memoria": {LocationNames.aqours_memoria_region},
}
