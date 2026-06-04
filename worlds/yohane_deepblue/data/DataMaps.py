import typing

from . import ItemNames, LocationNames

# TODO: Some of these tables can probably be combined

class ChestData(typing.NamedTuple):
    offset: int
    mask: int
    vanilla_item: str

chest_data_map = {
    LocationNames.cast_tutorial_left_chest: ChestData(0x5129F, 0x20, ItemNames.sea_tamahagane),
    LocationNames.case_tutorial_right_chest: ChestData(0x5129F, 0x40, ItemNames.violet_shell),
    LocationNames.fishy_archery_chest: ChestData(0x512EC, 0x02, ItemNames.enchanted_optical_lens),
    LocationNames.pathway_to_infernal_altar_chest: ChestData(0x512EC, 0x04, ItemNames.sharp_arrowhead),
    LocationNames.katys_mask_room_chest: ChestData(0x5129F, 0x80, ItemNames.chika_upgrade),
    LocationNames.chika_testing_grounds_chest: ChestData(0x512EC, 0x01, ItemNames.extra_accessory_slot),

    LocationNames.grotto_next_to_first_save_room_chest: ChestData(0x512F4, 0x80, ItemNames.broken_lance),
    LocationNames.first_waterfall_room_chest: ChestData(0x512F4, 0x02, ItemNames.fragmented_shell),
    LocationNames.first_lake_room_chest: ChestData(0x512F4, 0x40, ItemNames.sardine_oil),
    LocationNames.second_lake_room_chest: ChestData(0x512F5, 0x01, ItemNames.canola_bouquet),
    LocationNames.spellbook_room_chest: ChestData(0x512F4, 0x01, ItemNames.riko_upgrade),
    LocationNames.long_waterfall_room_chest: ChestData(0x512A7, 0x80, ItemNames.sea_tamahagane),
    LocationNames.isolated_climb_room_chest: ChestData(0x512A7, 0x40, ItemNames.huge_conch),
    LocationNames.small_cave_climb_room_chest: ChestData(0x512A7, 0x20, ItemNames.tidelight),

    LocationNames.sandy_trap_room_chest: ChestData(0x512A3, 0x80, ItemNames.sea_deitys_charm),
    LocationNames.vertical_poison_room_chest: ChestData(0x512F0, 0x02, ItemNames.slender_tentacle),
    LocationNames.rolling_rocks_room_chest: ChestData(0x512F0, 0x01, ItemNames.splendid_shield),
    LocationNames.laptop_room_chest: ChestData(0x512A3, 0x20, ItemNames.hanamaru_upgrade),
    LocationNames.hall_of_shame_chest: ChestData(0x512A3, 0x40, ItemNames.ichimonji_scabbard),

    LocationNames.sunken_volcano_next_to_first_save_room_chest: ChestData(0x51305, 0x20, ItemNames.miniature_train),
    LocationNames.hotspring_room_chest: ChestData(0x51305, 0x40, ItemNames.sea_silk),
    LocationNames.soarshoes_room_chest: ChestData(0x51305, 0x04, ItemNames.fallen_angels_soarshoes),
    LocationNames.soarshoes_obligatory_issue_room_chest: ChestData(0x51305, 0x10, ItemNames.chilled_enzyme),
    LocationNames.tonosamas_parts_room_chest: ChestData(0x51305, 0x08, ItemNames.kanan_upgrade),

    LocationNames.really_sealed_off_chest_room_chest: ChestData(0x51308, 0x08, ItemNames.hole_filled_cube),
    LocationNames.spikey_ball_fish_room_chest: ChestData(0x51308, 0x10, ItemNames.extra_accessory_slot),
    LocationNames.final_guard_room_chest: ChestData(0x51308, 0x01, ItemNames.torn_collar),
    LocationNames.gloves_of_might_room_chest: ChestData(0x512BB, 0x80, ItemNames.gloves_of_might),
    LocationNames.postal_guild_bag_room: ChestData(0x512BB, 0x40, ItemNames.you_upgrade),

    LocationNames.soarshoesnt_chest_room_chest: ChestData(0x512AB, 0x80, ItemNames.magicolight),
    LocationNames.annoying_teleporting_fish_room_chest: ChestData(0x512F8, 0x10, ItemNames.lady_of_the_lakes_bromide),
    LocationNames.wallcrab_chest_room_chest: ChestData(0x512F8, 0x08, ItemNames.sardine_oil),
    LocationNames.dumb_block_room_chest: ChestData(0x512F8, 0x01, ItemNames.charge_stone),
    LocationNames.lost_monstie_room_chest: ChestData(0x512AB, 0x20, ItemNames.mari_upgrade),

    LocationNames.one_way_slide_room_chest: ChestData(0x512B3, 0x20, ItemNames.poison_pouch),
    LocationNames.giant_sliding_crystals_room_chest: ChestData(0x512B3, 0x40, ItemNames.ripple_shell),
    LocationNames.isolated_chest_room_chest: ChestData(0x51300, 0x01, ItemNames.draconic_crest),
    LocationNames.looong_slide_room_chest: ChestData(0x51300, 0x02, ItemNames.ruby_upgrade),
    LocationNames.mari_issue_room_chest: ChestData(0x512B3, 0x80, ItemNames.deepsea_magicite),

    LocationNames.giant_poison_enemy_crab_room_chest: ChestData(0x512AF, 0x40, ItemNames.princesss_diary),
    LocationNames.scarlet_delta_suit_room_chest: ChestData(0x512AF, 0x80, ItemNames.dia_upgrade),
    LocationNames.golden_snail_room_chest: ChestData(0x512FC, 0x04, ItemNames.shark_rib),
    LocationNames.slope_room_chest: ChestData(0x512FC, 0x01, ItemNames.sturdy_tuft),
    LocationNames.you_testing_grounds_chest: ChestData(0x512FC, 0x08, ItemNames.bright_red_cloth),

    LocationNames.purple_goo_room_chest: ChestData(0x512BF, 0x40, ItemNames.lady_of_the_lakes_fin),
    LocationNames.dark_room_chest: ChestData(0x512BF, 0x20, ItemNames.numazu_star),
}

important_item_chests = {
    LocationNames.sandy_trap_room_chest,
    LocationNames.soarshoes_room_chest,
    LocationNames.gloves_of_might_room_chest
}

character_rescue_flag_map = {
    LocationNames.chika_rescue: 0x80,
    LocationNames.kanan_rescue: 0x0100,
    LocationNames.dia_rescue: 0x0200,
    LocationNames.ruby_rescue: 0x0400,
    LocationNames.you_rescue: 0x0800,
    LocationNames.mari_rescue: 0x1000,
    LocationNames.riko_rescue: 0x2000,
    LocationNames.hanamaru_rescue: 0x4000,
}

character_quest_flag_map = {
    LocationNames.katys_mask_room_chest: 0x80,
    LocationNames.spellbook_room_chest: 0x0400,
    LocationNames.tonosamas_parts_room_chest: 0x2000,
    LocationNames.laptop_room_chest: 0x010000,
    LocationNames.looong_slide_room_chest: 0x080000,
    LocationNames.postal_guild_bag_room: 0x400000,
    LocationNames.scarlet_delta_suit_room_chest: 0x02000000,
    LocationNames.lost_monstie_room_chest: 0x10000000,
}

boss_defeated_flag_map = {
    LocationNames.sunken_temple_boss_defeated: 0x20,
    LocationNames.ruins_boss_defeated_1: 0x40,
    LocationNames.ruins_boss_defeated_2: 0x80,
    LocationNames.ruins_boss_defeated_3: 0x0100,
    LocationNames.grotto_boss_defeated: 0x0200,
    LocationNames.coral_hill_boss_defeated: 0x0400,
    LocationNames.sea_of_trees_boss_defeated: 0x0800,
    LocationNames.crystalline_grotto_boss_defeated: 0x1000,
    LocationNames.sunken_volcano_boss_defeated: 0x2000,
    LocationNames.shipwreck_boss_defeated: 0x4000,
    LocationNames.infernal_altar_boss_defeated: 0x8000,

    LocationNames.sunken_temple_boss_refight: 0x010000,
    LocationNames.ruins_boss_refight: 0x020000,
    LocationNames.grotto_boss_refight: 0x040000,
    LocationNames.coral_hill_boss_refight: 0x080000,
    LocationNames.sea_of_trees_boss_refight: 0x100000,
    LocationNames.crystalline_grotto_boss_refight: 0x200000,
    LocationNames.sunken_volcano_boss_refight: 0x400000,
    LocationNames.shipwreck_boss_refight: 0x800000,
    LocationNames.infernal_altar_boss_refight: 0x01000000,
}

character_item_flags_map = {
    ItemNames.lailaps_unlock: 0x20,
    #ItemNames.lailaps_upgrade: 0x40,
    ItemNames.chika_unlock: 0x80,
    #ItemNames.chika_upgrade: 0x0100,
    ItemNames.riko_unlock: 0x0200,
    #ItemNames.riko_upgrade: 0x0400,
    ItemNames.kanan_unlock: 0x0800,
    #ItemNames.kanan_upgrade: 0x1000,
    ItemNames.dia_unlock: 0x2000,
    #ItemNames.dia_upgrade: 0x4000,
    ItemNames.you_unlock: 0x8000,
    #ItemNames.you_upgrade: 0x010000,
    ItemNames.mari_unlock: 0x020000,
    #ItemNames.mari_upgrade: 0x040000,
    ItemNames.hanamaru_unlock: 0x080000,
    #ItemNames.hanamaru_upgrade: 0x100000,
    ItemNames.ruby_unlock: 0x200000,
    #ItemNames.ruby_upgrade: 0x400000,
}

character_to_upgrade_map: dict[str, str | None] = {
    ItemNames.lailaps_unlock: None,
    ItemNames.chika_unlock: ItemNames.chika_upgrade,
    ItemNames.riko_unlock: ItemNames.riko_upgrade,
    ItemNames.kanan_unlock: ItemNames.kanan_upgrade,
    ItemNames.dia_unlock: ItemNames.dia_upgrade,
    ItemNames.you_unlock: ItemNames.you_upgrade,
    ItemNames.mari_unlock: ItemNames.mari_upgrade,
    ItemNames.hanamaru_unlock: ItemNames.hanamaru_upgrade,
    ItemNames.ruby_unlock: ItemNames.ruby_upgrade,
}

upgrade_to_character_map = {upgrade: character for character, upgrade in character_to_upgrade_map.items()
                            if upgrade is not None}

upgrade_item_to_quest_location_map = {
    ItemNames.chika_upgrade: LocationNames.chika_upgrade_quest,
    ItemNames.riko_upgrade: LocationNames.riko_upgrade_quest,
    ItemNames.kanan_upgrade: LocationNames.kanan_upgrade_quest,
    ItemNames.dia_upgrade: LocationNames.dia_upgrade_quest,
    ItemNames.you_upgrade: LocationNames.you_upgrade_quest,
    ItemNames.mari_upgrade: LocationNames.mari_upgrade_quest,
    ItemNames.hanamaru_upgrade: LocationNames.hanamaru_upgrade_quest,
    ItemNames.ruby_upgrade: LocationNames.ruby_upgrade_quest,
}

character_item_to_progressive_map = {
    ItemNames.chika_unlock: (ItemNames.progressive_chika_unlock, 1),
    ItemNames.chika_upgrade: (ItemNames.progressive_chika_unlock, 2),
    ItemNames.riko_unlock: (ItemNames.progressive_riko_unlock, 1),
    ItemNames.riko_upgrade: (ItemNames.progressive_riko_unlock, 2),
    ItemNames.kanan_unlock: (ItemNames.progressive_kanan_unlock, 1),
    ItemNames.kanan_upgrade: (ItemNames.progressive_kanan_unlock, 2),
    ItemNames.hanamaru_unlock: (ItemNames.progressive_hanamaru_unlock, 1),
    ItemNames.hanamaru_upgrade: (ItemNames.progressive_hanamaru_unlock, 2),
    ItemNames.ruby_unlock: (ItemNames.progressive_ruby_unlock, 1),
    ItemNames.ruby_upgrade: (ItemNames.progressive_ruby_unlock, 2),
    ItemNames.you_unlock: (ItemNames.progressive_you_unlock, 1),
    ItemNames.you_upgrade: (ItemNames.progressive_you_unlock, 2),
    ItemNames.dia_unlock: (ItemNames.progressive_dia_unlock, 1),
    ItemNames.dia_upgrade: (ItemNames.progressive_dia_unlock, 2),
    ItemNames.mari_unlock: (ItemNames.progressive_mari_unlock, 1),
    ItemNames.mari_upgrade: (ItemNames.progressive_mari_unlock, 2),
}

progressive_to_character_item_map = {
    ItemNames.progressive_chika_unlock: (ItemNames.chika_unlock, ItemNames.chika_upgrade),
    ItemNames.progressive_riko_unlock: (ItemNames.riko_unlock, ItemNames.riko_upgrade),
    ItemNames.progressive_kanan_unlock: (ItemNames.kanan_unlock, ItemNames.kanan_upgrade),
    ItemNames.progressive_hanamaru_unlock: (ItemNames.hanamaru_unlock, ItemNames.hanamaru_upgrade),
    ItemNames.progressive_ruby_unlock: (ItemNames.ruby_unlock, ItemNames.ruby_upgrade),
    ItemNames.progressive_you_unlock: (ItemNames.you_unlock, ItemNames.you_upgrade),
    ItemNames.progressive_dia_unlock: (ItemNames.dia_unlock, ItemNames.dia_upgrade),
    ItemNames.progressive_mari_unlock: (ItemNames.mari_unlock, ItemNames.mari_upgrade),
}

character_item_to_quest_map = {
    ItemNames.chika_unlock: 0x80,
    ItemNames.riko_unlock: 0x0400,
    ItemNames.kanan_unlock: 0x2000,
    ItemNames.hanamaru_unlock: 0x010000,
    ItemNames.ruby_unlock: 0x080000,
    ItemNames.you_unlock: 0x400000,
    ItemNames.dia_unlock: 0x02000000,
    ItemNames.mari_unlock: 0x10000000,
}

character_upgrade_to_area_room = {
    #ItemNames.lailaps_upgrade: (0, [], ""),
    ItemNames.chika_upgrade: (1, [12, 11], LocationNames.katys_mask_room_chest),
    ItemNames.riko_upgrade: (3, [28, 25, 27], LocationNames.spellbook_room_chest),
    ItemNames.kanan_upgrade: (7, [55, 54, 56], LocationNames.tonosamas_parts_room_chest),
    ItemNames.dia_upgrade: (5, [23, 22], LocationNames.scarlet_delta_suit_room_chest),
    ItemNames.you_upgrade: (8, [17, 16, 18], LocationNames.postal_guild_bag_room),
    ItemNames.mari_upgrade: (4, [9, 8, 10], LocationNames.lost_monstie_room_chest),
    ItemNames.hanamaru_upgrade: (2, [19, 24], LocationNames.laptop_room_chest),
    ItemNames.ruby_upgrade: (6, [41, 40, 42], LocationNames.looong_slide_room_chest),
}
