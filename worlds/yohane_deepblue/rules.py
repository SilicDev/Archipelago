from rule_builder.rules import CanReachLocation, Filtered, Has, HasAny, OptionFilter
from worlds.AutoWorld import World

from .data import ItemNames, LocationNames
from .options import EarlyChikaBlockMoved, EnableYouSkips

you_enabled_filter = [OptionFilter(EnableYouSkips, EnableYouSkips.option_true)]
chika_blocks_filter = [OptionFilter(EarlyChikaBlockMoved, EarlyChikaBlockMoved.option_false)]

soarshoes_rule = Has(ItemNames.fallen_angels_soarshoes)
gloves_rule = Has(ItemNames.gloves_of_might)
sea_charm_rule = Has(ItemNames.sea_deitys_charm)

lailaps_rule = Has(ItemNames.lailaps_unlock)
chika_rule = Has(ItemNames.chika_unlock)
riko_rule = Has(ItemNames.riko_unlock)
kanan_rule = Has(ItemNames.kanan_unlock)
dia_rule = Has(ItemNames.dia_unlock)
you_rule = Has(ItemNames.you_unlock)
mari_rule = Has(ItemNames.mari_unlock)
hanamaru_rule = Has(ItemNames.hanamaru_unlock)
ruby_rule = Has(ItemNames.ruby_unlock)

upgraded_chika_rule = Has(ItemNames.chika_upgrade) & chika_rule
upgraded_riko_rule = Has(ItemNames.riko_upgrade) & riko_rule
upgraded_kanan_rule = Has(ItemNames.kanan_upgrade) & kanan_rule
upgraded_dia_rule = Has(ItemNames.dia_upgrade) & dia_rule
upgraded_you_rule = Has(ItemNames.you_upgrade) & you_rule
upgraded_mari_rule = Has(ItemNames.mari_upgrade) & mari_rule
upgraded_hanamaru_rule = Has(ItemNames.hanamaru_upgrade) & hanamaru_rule
upgraded_ruby_rule = Has(ItemNames.ruby_upgrade) & ruby_rule

chika_block_rule = chika_rule | upgraded_ruby_rule
ignore_projectile_rule = ruby_rule | upgraded_you_rule | upgraded_mari_rule | upgraded_riko_rule
you_skip_rule = Filtered(you_rule, options=you_enabled_filter, filtered_resolution=False)

big_weapon_rule = HasAny(ItemNames.threaded_blade, ItemNames.shamrock, ItemNames.demon_slayer, ItemNames.claiomh_solais)
boss_token_rule = Has(ItemNames.boss_token, 8)

def set_rules(world: World) -> None:
    set_chest_rules(world)
    world.set_rule(world.get_location(LocationNames.grotto_boss_defeated), sea_charm_rule)
    world.set_rule(world.get_location(LocationNames.sunken_volcano_boss_defeated), soarshoes_rule) # remove for hard logic
    world.set_rule(world.get_location(LocationNames.shipwreck_boss_defeated), ignore_projectile_rule)
    world.set_rule(world.get_location(LocationNames.infernal_altar_boss_defeated), riko_rule & kanan_rule & hanamaru_rule & gloves_rule & soarshoes_rule)
    world.set_rule(world.get_location(LocationNames.chika_rescue), CanReachLocation(LocationNames.sunken_temple_boss_defeated))
    world.set_rule(world.get_location(LocationNames.kanan_rescue), CanReachLocation(LocationNames.ruins_boss_defeated_3))
    world.set_rule(world.get_location(LocationNames.dia_rescue), CanReachLocation(LocationNames.grotto_boss_defeated))
    world.set_rule(world.get_location(LocationNames.ruby_rescue), CanReachLocation(LocationNames.coral_hill_boss_defeated))
    world.set_rule(world.get_location(LocationNames.you_rescue), CanReachLocation(LocationNames.sea_of_trees_boss_defeated))
    world.set_rule(world.get_location(LocationNames.mari_rescue), CanReachLocation(LocationNames.crystalline_grotto_boss_defeated))
    world.set_rule(world.get_location(LocationNames.riko_rescue), CanReachLocation(LocationNames.sunken_temple_boss_defeated))
    world.set_rule(world.get_location(LocationNames.hanamaru_rescue), CanReachLocation(LocationNames.shipwreck_boss_defeated))
    world.set_rule(world.get_location(LocationNames.chika_upgrade_quest), Has(ItemNames.chika_upgrade))
    world.set_rule(world.get_location(LocationNames.kanan_upgrade_quest), Has(ItemNames.kanan_upgrade))
    world.set_rule(world.get_location(LocationNames.dia_upgrade_quest), Has(ItemNames.dia_upgrade))
    world.set_rule(world.get_location(LocationNames.ruby_upgrade_quest), Has(ItemNames.ruby_upgrade))
    world.set_rule(world.get_location(LocationNames.you_upgrade_quest), Has(ItemNames.you_upgrade))
    world.set_rule(world.get_location(LocationNames.mari_upgrade_quest), Has(ItemNames.mari_upgrade))
    world.set_rule(world.get_location(LocationNames.riko_upgrade_quest), Has(ItemNames.riko_upgrade))
    world.set_rule(world.get_location(LocationNames.hanamaru_upgrade_quest), Has(ItemNames.hanamaru_upgrade))
    pass

def set_chest_rules(world: World) -> None:
    # Sunken Temple
    world.set_rule(world.get_location(LocationNames.fishy_archery_chest), gloves_rule | soarshoes_rule)
    world.set_rule(world.get_location(LocationNames.katys_mask_room_chest), chika_rule & (you_skip_rule | (soarshoes_rule & chika_block_rule)))
    world.set_rule(world.get_location(LocationNames.chika_testing_grounds_chest), you_rule)

    # Grotto
    world.set_rule(world.get_location(LocationNames.first_lake_room_chest), sea_charm_rule)
    world.set_rule(world.get_location(LocationNames.spellbook_room_chest), riko_rule)
    world.set_rule(world.get_location(LocationNames.long_waterfall_room_chest), sea_charm_rule)
    world.set_rule(world.get_location(LocationNames.isolated_climb_room_chest), (soarshoes_rule | gloves_rule))
    world.set_rule(world.get_location(LocationNames.small_cave_climb_room_chest), (soarshoes_rule | gloves_rule))

    # Ruins
    world.set_rule(world.get_location(LocationNames.laptop_room_chest), hanamaru_rule & (you_rule | hanamaru_rule))
    world.set_rule(world.get_location(LocationNames.hall_of_shame_chest), (soarshoes_rule | gloves_rule) & you_rule)

    # Sunken Volcano
    world.set_rule(world.get_location(LocationNames.sunken_volcano_next_to_first_save_room_chest), gloves_rule)
    world.set_rule(world.get_location(LocationNames.soarshoes_obligatory_issue_room_chest), soarshoes_rule)
    world.set_rule(world.get_location(LocationNames.tonosamas_parts_room_chest), (big_weapon_rule | dia_rule | upgraded_hanamaru_rule | mari_rule))

    # Shipwreck
    world.set_rule(world.get_location(LocationNames.final_guard_room_chest), you_rule)
    world.set_rule(world.get_location(LocationNames.gloves_of_might_room_chest), chika_rule | you_skip_rule)
    world.set_rule(world.get_location(LocationNames.postal_guild_bag_room), you_rule)

    # Coral Hill
    world.set_rule(world.get_location(LocationNames.lost_monstie_room_chest), mari_rule & upgraded_ruby_rule)

    # Crystalline Grotto
    world.set_rule(world.get_location(LocationNames.isolated_chest_room_chest), (you_rule | soarshoes_rule)) # for easier access
    world.set_rule(world.get_location(LocationNames.looong_slide_room_chest), you_rule & ruby_rule)
    world.set_rule(world.get_location(LocationNames.mari_issue_room_chest), mari_rule)

    # Sea of Trees
    world.set_rule(world.get_location(LocationNames.giant_poison_enemy_crab_room_chest), hanamaru_rule | (you_rule & (soarshoes_rule | gloves_rule)))
    world.set_rule(world.get_location(LocationNames.scarlet_delta_suit_room_chest), dia_rule & riko_rule)
    world.set_rule(world.get_location(LocationNames.golden_snail_room_chest), ignore_projectile_rule) # can remove the ignore projectile rule on harder logic
    world.set_rule(world.get_location(LocationNames.you_testing_grounds_chest), you_rule)

    # Infernal Altar
    world.set_rule(world.get_location(LocationNames.purple_goo_room_chest), you_rule & (soarshoes_rule | gloves_rule))
    world.set_rule(world.get_location(LocationNames.dark_room_chest), you_rule & (soarshoes_rule | gloves_rule))



