from rule_builder.rules import CanReachLocation, Has, HasAll
from worlds.AutoWorld import World
from worlds.sonic_colours_ds.options import Goal

from .data import ItemNames, LocationNames

all_emeralds_rule = HasAll(ItemNames.white_emerald,
                           ItemNames.red_emerald,
                           ItemNames.cyan_emerald,
                           ItemNames.purple_emerald,
                           ItemNames.green_emerald,
                           ItemNames.yellow_emerald,
                           ItemNames.blue_emerald)

white_wisp_rule = Has(ItemNames.white_wisp_unlock)
red_wisp_rule = Has(ItemNames.red_wisp_unlock)
orange_wisp_rule = Has(ItemNames.orange_wisp_unlock)
yellow_wisp_rule = Has(ItemNames.yellow_wisp_unlock)
cyan_wisp_rule = Has(ItemNames.cyan_wisp_unlock)
violet_wisp_rule = Has(ItemNames.violet_wisp_unlock)

tropical_resort_rule = Has(ItemNames.tropical_resort_unlock)
sweet_mountain_rule = Has(ItemNames.sweet_mountain_unlock)
starlight_carnival_rule = Has(ItemNames.starlight_carnival_unlock)
planet_wisp_rule = Has(ItemNames.planet_wisp_unlock)
aquarium_park_rule = Has(ItemNames.aquarium_park_unlock)
asteroid_coaster_rule = Has(ItemNames.asteroid_coaster_unlock)
terminal_velocity_rule = Has(ItemNames.terminal_velocity_unlock)

def set_rules(world: World) -> None:
    goal = world.options.goal.value
    if goal == Goal.option_wisp_armor:
        world.set_completion_rule(Has(ItemNames.park_keys))
    elif goal == Goal.option_mother_wisp:
        world.set_completion_rule(Has(ItemNames.mother_wisp))

        world.set_rule(world.get_location(LocationNames.nega_mother_wisp), all_emeralds_rule)

    world.set_rule(world.get_location(LocationNames.nega_wisp_armor), (white_wisp_rule & red_wisp_rule &
                                                                       orange_wisp_rule & yellow_wisp_rule &
                                                                       cyan_wisp_rule & violet_wisp_rule))
    if world.options.redringsanity:
        set_red_ring_rules(world)

    set_level_rules(world)

    world.set_rule(world.get_location(LocationNames.special_stage_1),
                   CanReachLocation(LocationNames.tropical_resort_act_1) |
                   CanReachLocation(LocationNames.tropical_resort_act_2))
    world.set_rule(world.get_location(LocationNames.special_stage_2),
                   CanReachLocation(LocationNames.sweet_mountain_act_1) |
                   CanReachLocation(LocationNames.sweet_mountain_act_2))
    world.set_rule(world.get_location(LocationNames.special_stage_3),
                   CanReachLocation(LocationNames.starlight_carnival_act_1) |
                   CanReachLocation(LocationNames.starlight_carnival_act_2))
    world.set_rule(world.get_location(LocationNames.special_stage_4),
                   CanReachLocation(LocationNames.planet_wisp_act_1) |
                   CanReachLocation(LocationNames.planet_wisp_act_2))
    world.set_rule(world.get_location(LocationNames.special_stage_5),
                   CanReachLocation(LocationNames.aquarium_park_act_1) |
                   CanReachLocation(LocationNames.aquarium_park_act_2))
    world.set_rule(world.get_location(LocationNames.special_stage_6),
                   CanReachLocation(LocationNames.asteroid_coaster_act_1) |
                   CanReachLocation(LocationNames.asteroid_coaster_act_2))
    #world.set_rule(world.get_location(LocationNames.special_stage_7), white_wisp_rule)


def set_level_rules(world: World) -> None:
    # Tropical Resort
    world.set_rule(world.get_location(LocationNames.white_wisp_tutorial), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_1), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_2), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_3), white_wisp_rule)

    # Sweet Mountain
    world.set_rule(world.get_location(LocationNames.red_wisp_tutorial), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_1), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_2), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_boss), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_1), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_2), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_3), red_wisp_rule)

    # Starlight Carnival
    world.set_rule(world.get_location(LocationNames.orange_wisp_tutorial), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_1), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_2), orange_wisp_rule)
    # TODO: Make both dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_1), white_wisp_rule | orange_wisp_rule)
    # TODO: Make Boost + Laser dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_2),
                   orange_wisp_rule | (white_wisp_rule & cyan_wisp_rule))
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_3), white_wisp_rule & orange_wisp_rule)

    # Planet Wisp
    world.set_rule(world.get_location(LocationNames.yellow_wisp_tutorial), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_1), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_2), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_boss), white_wisp_rule & yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_1), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_2), white_wisp_rule & yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_3), yellow_wisp_rule)

    # Aquarium Park
    world.set_rule(world.get_location(LocationNames.cyan_wisp_tutorial), cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_2), cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_mission_1),
                   white_wisp_rule | yellow_wisp_rule | cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_mission_2), cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_mission_3), white_wisp_rule & cyan_wisp_rule)

    # Asteroid Coaster
    world.set_rule(world.get_location(LocationNames.violet_wisp_tutorial), violet_wisp_rule)
    # TODO: Make Boost dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_1), white_wisp_rule & violet_wisp_rule)
    # TODO: Make Boost/Laser dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_2),
                   white_wisp_rule & cyan_wisp_rule & violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_1), violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_2), violet_wisp_rule)
    # TODO: Make Boost/Laser dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_3),
                   violet_wisp_rule & (white_wisp_rule | cyan_wisp_rule))

    # Terminal Velocity
    # TODO: Make this dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.terminal_velocity_chase), white_wisp_rule)


def set_red_ring_rules(world: World) -> None:
    # Tropical Resort Act 1
    world.set_rule(world.get_location(LocationNames.tropical_resort_act_1_red_ring_2), red_wisp_rule)

    # Tropical Resort Act 2
    world.set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_1), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_2), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_3), white_wisp_rule | red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_5), red_wisp_rule)

    # Tropical Resort Missions
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_1_red_ring_1), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_2_red_ring_1), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_2_red_ring_2),
                   white_wisp_rule & red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_3_red_ring_1), white_wisp_rule)
    world.set_rule(world.get_location(LocationNames.tropical_resort_mission_3_red_ring_2), white_wisp_rule)

    # Sweet Mountain Act 1
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_2), white_wisp_rule | red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_3), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_4), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_5), red_wisp_rule)

    # Sweet Mountain Act 2
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_1), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_2), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_3), red_wisp_rule & violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_4), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_5), red_wisp_rule)

    # Sweet Mountain Missions
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_1_red_ring_1), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_1_red_ring_2), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_2_red_ring_1), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_3_red_ring_1), red_wisp_rule)
    world.set_rule(world.get_location(LocationNames.sweet_mountain_mission_3_red_ring_2), red_wisp_rule)

    # Starlight Carnival Act 1
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_2), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_3), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_4),
                   orange_wisp_rule & cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_5), orange_wisp_rule)

    # Starlight Carnival Act 2
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_2), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_3), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_4), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_5), orange_wisp_rule)

    # Starlight Carnival Missions
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_1_red_ring_2), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_2_red_ring_1), orange_wisp_rule)
    # TODO: Make Boost + Laser dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_2_red_ring_2),
                   white_wisp_rule & cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_3_red_ring_1), orange_wisp_rule)
    world.set_rule(world.get_location(LocationNames.starlight_carnival_mission_3_red_ring_2), orange_wisp_rule)

    # Planet Wisp Act 1
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_1), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_2), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_3), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_4), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_5), yellow_wisp_rule)

    # Planet Wisp Act 2
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_1), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_2), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_3), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_4), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_5), yellow_wisp_rule)

    # Planet Wisp Missions
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_1_red_ring_1), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_1_red_ring_2), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_2_red_ring_1), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_2_red_ring_2), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_3_red_ring_1), yellow_wisp_rule)
    world.set_rule(world.get_location(LocationNames.planet_wisp_mission_3_red_ring_2), yellow_wisp_rule)

    # Aquarium Park Act 1
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_1_red_ring_2), yellow_wisp_rule | cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_1_red_ring_5), white_wisp_rule | cyan_wisp_rule)

    # Aquarium Park Act 2
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_1), white_wisp_rule | cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_2), yellow_wisp_rule & cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_3), cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_4), cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_5), cyan_wisp_rule)

    # Aquarium Park Missions
    world.set_rule(world.get_location(LocationNames.aquarium_park_mission_2_red_ring_1), cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_mission_2_red_ring_2), cyan_wisp_rule)
    world.set_rule(world.get_location(LocationNames.aquarium_park_mission_3_red_ring_2), cyan_wisp_rule)

    # Asteroid Coaster Act 1
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_1), violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_2),
                   cyan_wisp_rule & violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_3),
                   white_wisp_rule | violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_4), violet_wisp_rule)
    # TODO: Make Boost dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_5),
                   white_wisp_rule & violet_wisp_rule)

    # Asteroid Coaster Act 2
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_1), violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_2), violet_wisp_rule)
    # TODO: Make Boost dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_3),
                   white_wisp_rule & violet_wisp_rule)
    # TODO: Make Boost/Laser dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_4),
                   white_wisp_rule & cyan_wisp_rule & violet_wisp_rule)
    # TODO: Make Boost/Laser dependent on Rando Difficulty
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_5),
                   white_wisp_rule & cyan_wisp_rule & violet_wisp_rule)

    # Asteroid Coaster Missions
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_1_red_ring_1), violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_1_red_ring_2), violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_2_red_ring_1), violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_2_red_ring_2), violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_3_red_ring_1),
                   white_wisp_rule & violet_wisp_rule)
    world.set_rule(world.get_location(LocationNames.asteroid_coaster_mission_3_red_ring_2),
                   violet_wisp_rule & (white_wisp_rule | cyan_wisp_rule))
