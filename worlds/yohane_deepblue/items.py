import typing

from BaseClasses import Item

from .data import ItemNames


class ItemData(typing.NamedTuple):
    code: int | None
    progression: bool
    trap: bool = False
    quantity: int = 1

class YohaneDeepblueItem(Item):
    game: str = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"


character_upgrade_table: dict[str, ItemData] = {
    #ItemNames.lailaps_upgrade: ItemData(0, True), # Unused
    ItemNames.chika_upgrade: ItemData(1, True),
    ItemNames.riko_upgrade: ItemData(2, True),
    ItemNames.kanan_upgrade: ItemData(3, True),
    ItemNames.hanamaru_upgrade: ItemData(4, True),
    ItemNames.ruby_upgrade: ItemData(5, True),
    ItemNames.you_upgrade: ItemData(6, True),
    ItemNames.dia_upgrade: ItemData(7, True),
    ItemNames.mari_upgrade: ItemData(8, True),
}

unique_accessories_table: dict[str, ItemData] = {
    ItemNames.extra_accessory_slot: ItemData(9, True, False, 2), # also 10
    ItemNames.fallen_angels_soarshoes: ItemData(11, True),
    ItemNames.gloves_of_might: ItemData(12, True),
    ItemNames.sea_deitys_charm: ItemData(13, True),
}

breakable_material_table: dict[str, ItemData] = {
    ItemNames.deepsea_cotton: ItemData(201, False),
    ItemNames.seaworms_cocoon: ItemData(202, False),
    ItemNames.sea_silk: ItemData(203, False),
    ItemNames.strange_metal: ItemData(204, False),
    ItemNames.antique_bronze_coin: ItemData(205, False),
    ItemNames.ancient_silver_coin: ItemData(206, False),
    ItemNames.lustrous_gold_coin: ItemData(207, False),
    ItemNames.platinum_idol: ItemData(208, False),
    ItemNames.orichalcum: ItemData(209, False),
    ItemNames.soul_crystal: ItemData(210, False),
    ItemNames.coral_ruby: ItemData(211, False),
    ItemNames.deepsea_diamond: ItemData(212, False),
    ItemNames.sirens_tear: ItemData(213, False),
    ItemNames.springy_shrub: ItemData(214, False),
    ItemNames.sharp_arrowhead: ItemData(215, False),
    ItemNames.broken_knife: ItemData(216, False),
    ItemNames.sea_tamahagane: ItemData(217, False),
    ItemNames.tidelight: ItemData(218, False),
    ItemNames.magicolight: ItemData(219, False),
    ItemNames.dissolvent: ItemData(220, False),
    ItemNames.sunstone: ItemData(221, False),
    ItemNames.charge_stone: ItemData(222, False),
    ItemNames.magic_mirror: ItemData(223, False),
    ItemNames.multicolered_seaweed: ItemData(224, False),
    ItemNames.umbra_rag: ItemData(225, False),
}

enemy_material_table: dict[str, ItemData] = {
    ItemNames.violet_shell: ItemData(227, False),
    ItemNames.viridian_claw: ItemData(228, False),
    ItemNames.emperors_crown: ItemData(229, False),
    #ItemNames.compound_lens: ItemData(230, False),
    ItemNames.squishy_hide: ItemData(231, False),
    ItemNames.freaky_tentacle: ItemData(232, False),
    #ItemNames.supreme_squid_ink: ItemData(233, False),
    ItemNames.sharp_tooth: ItemData(234, False),
    ItemNames.shiny_tail: ItemData(235, False),
    ItemNames.prismatic_organ: ItemData(236, False),
    #ItemNames.dried_jellyfish: ItemData(237, False),
    ItemNames.mysterious_component: ItemData(238, False),
    ItemNames.paralytic_slime: ItemData(239, False),
    #ItemNames.demecore: ItemData(240, False),
    ItemNames.golden_eye: ItemData(241, False),
    #ItemNames.proof_of_officership: ItemData(242, False),
    ItemNames.archs_timber: ItemData(243, False),
    ItemNames.scaled_quiver: ItemData(244, False),
    ItemNames.broken_lance: ItemData(245, False),
    ItemNames.fishing_harpoon: ItemData(246, False),
    ItemNames.greataxe_fragment: ItemData(247, False),
    ItemNames.spikey_orb: ItemData(248, False),
    ItemNames.pirates_symbol: ItemData(249, False),
    ItemNames.aiming_lens: ItemData(250, False),
    ItemNames.high_spec_lens: ItemData(251, False),
    #ItemNames.octobomb: ItemData(252, False),
    ItemNames.huge_pinchers: ItemData(253, False),
    ItemNames.sturdy_tuft: ItemData(254, False),
    #ItemNames.solid_eyeball: ItemData(255, False),
    ItemNames.frozen_meat: ItemData(256, False),
    ItemNames.poison_pouch: ItemData(257, False),
    #ItemNames.sea_cucumber_mucus: ItemData(258, False),
    ItemNames.fragmented_shell: ItemData(259, False),
    ItemNames.chilled_enzyme: ItemData(260, False),
    #ItemNames.hairy_tentacle: ItemData(261, False),
    ItemNames.tender_meat: ItemData(262, False),
    ItemNames.explosive_material: ItemData(263, False),
    #ItemNames.turtle_claw: ItemData(264, False),
    ItemNames.natural_sea_radish: ItemData(265, False),
    ItemNames.phony_eggshell: ItemData(266, False),
    ItemNames.crimson_eye: ItemData(267, False),
    #ItemNames.agapeweed: ItemData(268, False),
    ItemNames.sturdy_string: ItemData(269, False),
    ItemNames.splendid_shield: ItemData(271, False),
    ItemNames.slick_armor: ItemData(272, False),
    #ItemNames.standard_helmet: ItemData(273, False),
    ItemNames.sharp_splinter: ItemData(274, False),
    ItemNames.orange_crab_meat: ItemData(275, False),
    #ItemNames.spikey_carapace: ItemData(276, False),
    ItemNames.elongated_horn: ItemData(277, False),
    ItemNames.rugged_shrimp_leg: ItemData(278, False),
    #ItemNames.giant_shrimp_husk: ItemData(279, False),
    ItemNames.sardine_oil: ItemData(280, False),
    ItemNames.sardine_core: ItemData(281, False),
    #ItemNames.stray_sardine_scale: ItemData(282, False),
    ItemNames.teal_fish_skin: ItemData(283, False),
    ItemNames.orange_scale: ItemData(285, False),
    ItemNames.ninja_shuriken: ItemData(286, False),
    #ItemNames.secret_sauce: ItemData(287, False),
    ItemNames.rainbow_horn: ItemData(288, False),
    #ItemNames.feeble_leg: ItemData(289, False),
    ItemNames.dirt_ball: ItemData(290, False),
    ItemNames.poison_ball: ItemData(291, False),
    ItemNames.ice_ball: ItemData(292, False),
    ItemNames.venom_ball: ItemData(293, False),
    #ItemNames.pufferfish_stomach: ItemData(294, False),
    ItemNames.slender_tentacle: ItemData(295, False),
    ItemNames.stiff_tentacle: ItemData(296, False),
    ItemNames.tingly_tentacle: ItemData(297, False),
    ItemNames.toasty_tentacle: ItemData(298, False),
    #ItemNames.octospider_thread: ItemData(299, False),
    ItemNames.poison_drop: ItemData(300, False),
    ItemNames.frozen_drop: ItemData(301, False),
    ItemNames.majestic_drop: ItemData(302, False),
    #ItemNames.moist_algae: ItemData(303, False),
    ItemNames.deepsea_magicite: ItemData(304, False),
    ItemNames.abyssal_jewel: ItemData(305, False),
    ItemNames.demonic_sculpture: ItemData(306, False),
    ItemNames.magic_medal: ItemData(307, False),
    #ItemNames.phony_lock: ItemData(308, False),
    ItemNames.turtle_shell: ItemData(309, False),
    ItemNames.ignis_crystal: ItemData(310, False),
    ItemNames.teleportation_paradigm: ItemData(312, False),
    #ItemNames.fishknight_helm: ItemData(313, False),
    ItemNames.draconic_crest: ItemData(314, False),
    #ItemNames.draconic_scale: ItemData(315, False),
    ItemNames.floatation_sack: ItemData(316, False),
    ItemNames.flamme_essence: ItemData(317, False),
    ItemNames.fulgur_essence: ItemData(318, False),
    #ItemNames.jellybooster: ItemData(319, False),
}

rare_material_table: dict[str, ItemData] = {
    ItemNames.whale_harp: ItemData(226, False, False, 2),
    ItemNames.shark_rib: ItemData(270, False),
    ItemNames.ichimonji_scabbard: ItemData(284, False),
    ItemNames.ripple_shell: ItemData(311, False),
    ItemNames.world_pinetree_lumber: ItemData(320, False),
    ItemNames.phantom_jewel: ItemData(321, False),
    ItemNames.rusty_rod: ItemData(322, False),
    ItemNames.lunar_grindstone: ItemData(323, False),
    ItemNames.twinkling_stardust: ItemData(324, False, False, 3),
    ItemNames.lucent_matter: ItemData(325, False, False, 3),
    ItemNames.princesss_diary: ItemData(326, False),
    ItemNames.numazu_star: ItemData(327, False, False, 3),
    ItemNames.torn_collar: ItemData(328, False),
    ItemNames.enchanted_optical_lens: ItemData(329, False),
    ItemNames.lady_of_the_lakes_fin: ItemData(330, False),
    ItemNames.lady_of_the_lakes_bromide: ItemData(331, False),
    ItemNames.bright_red_cloth: ItemData(332, False),
    ItemNames.hole_filled_cube: ItemData(333, False),
    ItemNames.canola_bouquet: ItemData(334, False),
    ItemNames.miniature_train: ItemData(335, False),
    ItemNames.huge_conch: ItemData(336, False),
}

consumables_table: dict[str, ItemData] = {
    ItemNames.health_potion: ItemData(401, False),
    ItemNames.quality_health_potion: ItemData(402, False),
    ItemNames.shinestew: ItemData(403, False),
    ItemNames.darkness_potion: ItemData(404, False),
    ItemNames.refined_darkness_potion: ItemData(405, False),
    ItemNames.fallen_angels_tears: ItemData(406, False),
    ItemNames.antidote: ItemData(407, False),
    ItemNames.ultimate_antidote: ItemData(408, False),
    ItemNames.disposable_heater: ItemData(409, False),
    ItemNames.normie_perfume: ItemData(410, False),
    ItemNames.remedy: ItemData(411, False),
    ItemNames.offense_talisman: ItemData(412, False),
    ItemNames.ex_offense_talisman: ItemData(413, False),
    ItemNames.prime_offense_talisman: ItemData(414, False),
    ItemNames.defense_talisman: ItemData(415, False),
    ItemNames.ex_defense_talisman: ItemData(416, False),
    ItemNames.prime_defense_talisman: ItemData(417, False),
    ItemNames.exorcism_talisman: ItemData(418, False),
    ItemNames.musical_score: ItemData(419, False),
}

weapons_table: dict[str, ItemData] = {
    ItemNames.crossbow: ItemData(601, False),
    ItemNames.burstbow: ItemData(602, False),
    ItemNames.mistilteinn: ItemData(603, True),
    ItemNames.tribow: ItemData(604, False),
    ItemNames.tres_perfora: ItemData(605, False),
    ItemNames.autobow: ItemData(606, False),
    ItemNames.ballista: ItemData(607, False),
    ItemNames.dagger: ItemData(608, False),
    ItemNames.stilletto: ItemData(609, False),
    ItemNames.carnwennan: ItemData(610, True),
    ItemNames.tri_knife: ItemData(611, False),
    ItemNames.spread_toss: ItemData(612, True),
    ItemNames.battle_axe: ItemData(613, False),
    ItemNames.great_axe: ItemData(614, False),
    ItemNames.buster_sword: ItemData(615, False),
    ItemNames.the_iron_bludgeoner: ItemData(616, False),
    ItemNames.akatsuki_no_tachi: ItemData(617, False),
    ItemNames.katar: ItemData(618, False),
    ItemNames.broadsword: ItemData(619, False),
    ItemNames.the_slicer: ItemData(620, False),
    ItemNames.balmung: ItemData(621, False),
    ItemNames.katana: ItemData(622, False),
    ItemNames.gekisei: ItemData(623, False),
    ItemNames.threaded_blade: ItemData(624, True),
    ItemNames.shamrock: ItemData(625, True),
    ItemNames.demon_slayer: ItemData(626, True),
    ItemNames.claiomh_solais: ItemData(627, True),
}

accessories_table: dict[str, ItemData] = {
    ItemNames.fortune_tellers_veil: ItemData(801, False),
    ItemNames.cotton_cape: ItemData(802, False),
    ItemNames.diving_suit: ItemData(803, False),
    ItemNames.crimson_cape: ItemData(804, False),
    ItemNames.chainmail_cape: ItemData(805, False),
    ItemNames.chemical_cape: ItemData(806, False),
    ItemNames.chainlink_cloak: ItemData(807, False),
    ItemNames.warriors_cloak: ItemData(808, False),
    ItemNames.silk_cape: ItemData(809, False),
    ItemNames.magical_cape: ItemData(810, False),
    ItemNames.fluffy_coat: ItemData(811, False),
    ItemNames.fireproof_cloak: ItemData(812, False),
    ItemNames.gold_threaded_cape: ItemData(813, False),
    ItemNames.platinum_cloak: ItemData(814, False),
    ItemNames.seaborne_cape: ItemData(815, False),
    ItemNames.bolteaters_garment: ItemData(816, False),
    ItemNames.solar_cloak: ItemData(817, False),
    ItemNames.luminous_cape: ItemData(818, False),
    ItemNames.princesss_cape: ItemData(819, False),
    ItemNames.dusk_garment: ItemData(820, False),
    ItemNames.fallen_angels_cloak_bad: ItemData(821, False),
    ItemNames.fallen_angels_cloak: ItemData(822, False),
    ItemNames.ring: ItemData(823, False),
    ItemNames.bronze_ring: ItemData(824, False),
    ItemNames.silver_ring: ItemData(825, False),
    ItemNames.gold_ring: ItemData(826, False),
    ItemNames.platinum_ring: ItemData(827, False),
    ItemNames.orichalcum_ring: ItemData(828, False),
    ItemNames.crystal_ring: ItemData(829, False),
    ItemNames.ruby_ring: ItemData(830, False),
    ItemNames.diamond_ring: ItemData(831, False),
    ItemNames.alexandrite_ring: ItemData(832, False),
    ItemNames.karkinos_pincer: ItemData(833, False),
    ItemNames.lovecadite: ItemData(834, False),
    ItemNames.medallion_of_numazu: ItemData(835, False),
    ItemNames.lady_of_the_lakes_charm: ItemData(836, False),
    ItemNames.lailaps_collar: ItemData(837, False),
    ItemNames.memorial_locket: ItemData(838, False),
    ItemNames.earring: ItemData(839, False),
    ItemNames.bunny_earring: ItemData(840, False),
    ItemNames.clover_earring: ItemData(841, False),
    ItemNames.beckoning_cat_earring: ItemData(842, False),
    ItemNames.holly_earring: ItemData(843, False),
    ItemNames.bell_earring: ItemData(844, False),
    ItemNames.tattered_cloth: ItemData(845, False),
    ItemNames.crabmet: ItemData(846, False),
    ItemNames.serpent_bracelet: ItemData(847, False),
    ItemNames.holy_circlet: ItemData(848, False),
    ItemNames.static_necklace: ItemData(849, False),
    ItemNames.warlords_bandage: ItemData(850, False),
    ItemNames.phantom_robe: ItemData(851, False),
    ItemNames.magic_mirror_pendant: ItemData(852, False),
    ItemNames.aegis_earring: ItemData(853, False),
    ItemNames.tranquil_foliate: ItemData(854, False),
    ItemNames.hot_blooded_bell: ItemData(855, False),
    ItemNames.motivational_headband: ItemData(856, False),
    ItemNames.analytics_spectacles: ItemData(857, False),
    ItemNames.shades_gauntlet: ItemData(858, False),
    ItemNames.victory_medal: ItemData(859, False),
    ItemNames.lady_of_the_lakes_locket: ItemData(860, False),
    ItemNames.kinek_cube: ItemData(861, False),
    ItemNames.canola_wreath: ItemData(862, False),
    ItemNames.locomotive_pendant: ItemData(863, False),
    ItemNames.fabled_conch: ItemData(864, False),
    ItemNames.goddesss_bracelet: ItemData(865, False),
    ItemNames.sphene_earring: ItemData(866, False),
}

character_unlock_table: dict[str, ItemData] = { # No actual items exist for these
    ItemNames.lailaps_unlock: ItemData(1000, True),
    ItemNames.chika_unlock: ItemData(1001, True),
    ItemNames.riko_unlock: ItemData(1002, True),
    ItemNames.kanan_unlock: ItemData(1003, True),
    ItemNames.dia_unlock: ItemData(1004, True),
    ItemNames.you_unlock: ItemData(1005, True),
    ItemNames.mari_unlock: ItemData(1006, True),
    ItemNames.hanamaru_unlock: ItemData(1007, True),
    ItemNames.ruby_unlock: ItemData(1008, True),
}

token_items = {
    ItemNames.boss_token: ItemData(2000, True),
}

progressive_character_table: dict[str, ItemData] = {
    #ItemNames.lailaps_upgrade: ItemData(0, True), # Unused
    ItemNames.progressive_chika_unlock: ItemData(2101, True),
    ItemNames.progressive_riko_unlock: ItemData(2102, True),
    ItemNames.progressive_kanan_unlock: ItemData(2103, True),
    ItemNames.progressive_hanamaru_unlock: ItemData(2104, True),
    ItemNames.progressive_ruby_unlock: ItemData(2105, True),
    ItemNames.progressive_you_unlock: ItemData(2106, True),
    ItemNames.progressive_dia_unlock: ItemData(2107, True),
    ItemNames.progressive_mari_unlock: ItemData(2108, True),
}

bundle_items = {
    ItemNames.small_yen: ItemData(3000, False),
    ItemNames.medium_yen: ItemData(3001, False),
    ItemNames.big_yen: ItemData(3002, False),
}

junk_table: set[str] = {
    *consumables_table.keys(),
    *bundle_items.keys(),
}

event_table: dict[str, ItemData] = {
    ItemNames.victory: ItemData(None, True),
}

stackables_set = {
    *breakable_material_table.keys(),
    *enemy_material_table.keys(),
    *rare_material_table.keys(),
    *consumables_table.keys(),
    *accessories_table.keys(),
}

equips_set = {
    *weapons_table.keys(),
    *accessories_table.keys(),
}

yen_set = {
    ItemNames.small_yen,
    ItemNames.medium_yen,
    ItemNames.big_yen,
}

crafting_accessories_set = {
    ItemNames.silk_cape,
    ItemNames.gold_threaded_cape,
    ItemNames.fortune_tellers_veil,
    ItemNames.fallen_angels_cloak_bad,
    ItemNames.tattered_cloth,
}

valid_crafting_results = {
    **unique_accessories_table,
    **character_upgrade_table,
    **breakable_material_table,
    **enemy_material_table,
    **rare_material_table,
    **consumables_table,
    **weapons_table,
    **accessories_table,
}

item_table: dict[str, ItemData] = {
    **unique_accessories_table,
    **character_unlock_table,
    **character_upgrade_table,
    **progressive_character_table,
    **breakable_material_table,
    **enemy_material_table,
    **rare_material_table,
    **consumables_table,
    **weapons_table,
    **accessories_table,
    **bundle_items,
    **token_items
}

lookup_id_to_name: dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}

item_groups: dict[str, set[str]] = {
    "Movement": set(unique_accessories_table.keys()),
    "Accessories": set(accessories_table.keys()),
    "Characters": set(character_unlock_table.keys() | progressive_character_table.keys()),
    "Upgrades": set(character_upgrade_table.keys() | progressive_character_table.keys()),
    "Materials": set(breakable_material_table.keys() | enemy_material_table.keys() | rare_material_table.keys()),
    "Rare Materials": set(rare_material_table.keys()),
    "Consumables": set(consumables_table.keys()),
    "Weapons": set(weapons_table.keys()),
    "Currency": yen_set,
    "Yen": yen_set,
}
