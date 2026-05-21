from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule

from .data import ItemNames, LocationNames


def set_rules(world: World) -> None:
    if world.options.goal.value == 1:
        set_rule(world.get_location(LocationNames.nega_mother_wisp),
                lambda state: state.has_all([
                    ItemNames.white_emerald,
                    ItemNames.red_emerald,
                    ItemNames.cyan_emerald,
                    ItemNames.purple_emerald,
                    ItemNames.green_emerald,
                    ItemNames.yellow_emerald,
                    ItemNames.blue_emerald,
                ], world.player))
    set_rule(world.get_location(LocationNames.nega_wisp_armor),
             lambda state: state.has_all([
                ItemNames.red_wisp_unlock,
                ItemNames.orange_wisp_unlock,
                ItemNames.yellow_wisp_unlock,
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
             ], world.player))
    if world.options.redringsanity:
        set_red_ring_rules(world)

    set_level_rules(world)

    set_rule(world.get_location(LocationNames.special_stage_1),
             lambda state: state.can_reach_location(LocationNames.tropical_resort_act_1, world.player) or
                        state.can_reach_location(LocationNames.tropical_resort_act_2, world.player))
    set_rule(world.get_location(LocationNames.special_stage_2),
             lambda state: state.can_reach_location(LocationNames.sweet_mountain_act_1, world.player) or
                        state.can_reach_location(LocationNames.sweet_mountain_act_2, world.player))
    set_rule(world.get_location(LocationNames.special_stage_3),
             lambda state: state.can_reach_location(LocationNames.starlight_carnival_act_1, world.player) or
                        state.can_reach_location(LocationNames.starlight_carnival_act_2, world.player))
    set_rule(world.get_location(LocationNames.special_stage_4),
             lambda state: state.can_reach_location(LocationNames.planet_wisp_act_1, world.player) or
                        state.can_reach_location(LocationNames.planet_wisp_act_2, world.player))
    set_rule(world.get_location(LocationNames.special_stage_5),
             lambda state: state.can_reach_location(LocationNames.aquarium_park_act_1, world.player) or
                        state.can_reach_location(LocationNames.aquarium_park_act_2, world.player))
    set_rule(world.get_location(LocationNames.special_stage_6),
             lambda state: state.can_reach_location(LocationNames.asteroid_coaster_act_1, world.player) or
                        state.can_reach_location(LocationNames.asteroid_coaster_act_2, world.player))
    #set_rule(world.get_location(LocationNames.special_stage_7),
            #lambda state: state.has(ItemNames.white_wisp_unlock, world.player))

def set_level_rules(world: World) -> None:
    # Tropical Resort
    set_rule(world.get_location(LocationNames.white_wisp_tutorial),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_mission_1),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_mission_2),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_mission_3),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))

    # Sweet Mountain
    set_rule(world.get_location(LocationNames.red_wisp_tutorial),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_1),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_2),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_boss),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_1),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_2),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_3),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))

    # Starlight Carnival
    set_rule(world.get_location(LocationNames.orange_wisp_tutorial),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_1),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_2),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_1),
            lambda state: state.has_any([
                ItemNames.white_wisp_unlock,
                ItemNames.orange_wisp_unlock
            ], world.player)) # TODO: Make both dependent on Rando Difficulty
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_2),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player) or state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock
            ], world.player)) # TODO: Make Boost + Laser dependent on Rando Difficulty
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_3),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.orange_wisp_unlock
            ], world.player))

    # Planet Wisp
    set_rule(world.get_location(LocationNames.yellow_wisp_tutorial),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_1),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_2),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_boss),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.yellow_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_1),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_2),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.yellow_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_3),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))

    # Aquarium Park
    set_rule(world.get_location(LocationNames.cyan_wisp_tutorial),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_act_2),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_mission_1),
            lambda state: state.has_any([
                ItemNames.white_wisp_unlock,
                ItemNames.yellow_wisp_unlock,
                ItemNames.cyan_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_mission_2),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_mission_3),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock
            ], world.player))

    # Asteroid Coaster
    set_rule(world.get_location(LocationNames.violet_wisp_tutorial),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_1),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player)) # TODO: Make Boost dependent on Rando Difficulty
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_2),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player)) # TODO: Make Boost/Laser dependent on Rando Difficulty
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_1),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_2),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_3),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player) or state.has_all([
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player)) # TODO: Make Boost/Laser dependent on Rando Difficulty

    # Terminal Velocity
    set_rule(world.get_location(LocationNames.terminal_velocity_chase),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player)) # TODO: Make this dependent on Rando Difficulty

def set_red_ring_rules(world: World) -> None:
    # Tropical Resort Act 1
    set_rule(world.get_location(LocationNames.tropical_resort_act_1_red_ring_2),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))

    # Tropical Resort Act 2
    set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_1),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_2),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_3),
            lambda state: state.has_any([
                ItemNames.white_wisp_unlock,
                ItemNames.red_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_act_2_red_ring_5),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))

    # Tropical Resort Missions
    set_rule(world.get_location(LocationNames.tropical_resort_mission_1_red_ring_1),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_mission_2_red_ring_1),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_mission_2_red_ring_2),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.red_wisp_unlock
        ], world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_mission_3_red_ring_1),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.tropical_resort_mission_3_red_ring_2),
            lambda state: state.has(ItemNames.white_wisp_unlock, world.player))

    # Sweet Mountain Act 1
    set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_2),
            lambda state: state.has_any([
                ItemNames.white_wisp_unlock,
                ItemNames.red_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_3),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_4),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_1_red_ring_5),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))

    # Sweet Mountain Act 2
    set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_1),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_2),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_3),
            lambda state: state.has_all([
                ItemNames.red_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_4),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_act_2_red_ring_5),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))

    # Sweet Mountain Missions
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_1_red_ring_1),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_1_red_ring_2),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_2_red_ring_1),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_3_red_ring_1),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.sweet_mountain_mission_3_red_ring_2),
            lambda state: state.has(ItemNames.red_wisp_unlock, world.player))

    # Starlight Carnival Act 1
    set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_2),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_3),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_4),
            lambda state: state.has_all([
                ItemNames.orange_wisp_unlock,
                ItemNames.cyan_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_1_red_ring_5),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))

    # Starlight Carnival Act 2
    set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_2),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_3),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_4),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_act_2_red_ring_5),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))

    # Starlight Carnival Missions
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_1_red_ring_2),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_2_red_ring_1),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_2_red_ring_2),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player) or state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock
            ], world.player)) # TODO: Make Boost + Laser dependent on Rando Difficulty
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_3_red_ring_1),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.starlight_carnival_mission_3_red_ring_2),
            lambda state: state.has(ItemNames.orange_wisp_unlock, world.player))

    # Planet Wisp Act 1
    set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_1),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_2),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_3),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_4),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_1_red_ring_5),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))

    # Planet Wisp Act 2
    set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_1),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_2),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_3),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_4),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_act_2_red_ring_5),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))

    # Planet Wisp Missions
    set_rule(world.get_location(LocationNames.planet_wisp_mission_1_red_ring_1),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_1_red_ring_2),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_2_red_ring_1),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_2_red_ring_2),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_3_red_ring_1),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.planet_wisp_mission_3_red_ring_2),
            lambda state: state.has(ItemNames.yellow_wisp_unlock, world.player))

    # Aquarium Park Act 1
    set_rule(world.get_location(LocationNames.aquarium_park_act_1_red_ring_2),
            lambda state: state.has_any([
                ItemNames.yellow_wisp_unlock,
                ItemNames.cyan_wisp_unlock
                ], world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_act_1_red_ring_5),
            lambda state: state.has_any([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock
                ], world.player))

    # Aquarium Park Act 2
    set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_1),
            lambda state: state.has_any([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock
                ], world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_2),
            lambda state: state.has_all([
                ItemNames.yellow_wisp_unlock,
                ItemNames.cyan_wisp_unlock
                ], world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_3),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_4),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_act_2_red_ring_5),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))

    # Aquarium Park Missions
    set_rule(world.get_location(LocationNames.aquarium_park_mission_2_red_ring_1),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_mission_2_red_ring_2),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.aquarium_park_mission_3_red_ring_2),
            lambda state: state.has(ItemNames.cyan_wisp_unlock, world.player))

    # Asteroid Coaster Act 1
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_1),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_2),
            lambda state: state.has_all([
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_3),
            lambda state: state.has_any([
                ItemNames.white_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_4),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_1_red_ring_5),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player)) # TODO: Make Boost dependent on Rando Difficulty

    # Asteroid Coaster Act 2
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_1),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_2),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_3),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player)) # TODO: Make Boost dependent on Rando Difficulty
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_4),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player)) # TODO: Make Boost/Laser dependent on Rando Difficulty
    set_rule(world.get_location(LocationNames.asteroid_coaster_act_2_red_ring_5),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player)) # TODO: Make Boost/Laser dependent on Rando Difficulty

    # Asteroid Coaster Missions
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_1_red_ring_1),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_1_red_ring_2),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_2_red_ring_1),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_2_red_ring_2),
            lambda state: state.has(ItemNames.violet_wisp_unlock, world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_3_red_ring_1),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player))
    set_rule(world.get_location(LocationNames.asteroid_coaster_mission_3_red_ring_2),
            lambda state: state.has_all([
                ItemNames.white_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player) or state.has_all([
                ItemNames.cyan_wisp_unlock,
                ItemNames.violet_wisp_unlock
            ], world.player))
