from BaseClasses import Location
from Options import Toggle
from worlds.AutoWorld import World

from .data import LocationNames
from .options import Goal


class SonicColoursDSLocation(Location):
    game: str = "Sonic Colours (DS)"


tutorial_clear_table = {
    LocationNames.movement_tutorial: 1,
    LocationNames.white_wisp_tutorial: 2,
    LocationNames.red_wisp_tutorial: 3,
    LocationNames.orange_wisp_tutorial: 4,
    LocationNames.yellow_wisp_tutorial: 5,
    LocationNames.cyan_wisp_tutorial: 6,
    LocationNames.violet_wisp_tutorial: 7,
}


level_clear_table = {
    LocationNames.tropical_resort_act_1: 10,
    LocationNames.tropical_resort_act_2: 11,
    LocationNames.tropical_resort_boss: 12,

    LocationNames.sweet_mountain_act_1: 13,
    LocationNames.sweet_mountain_act_2: 14,
    LocationNames.sweet_mountain_boss: 15,

    LocationNames.starlight_carnival_act_1: 16,
    LocationNames.starlight_carnival_act_2: 17,
    LocationNames.starlight_carnival_boss: 18,

    LocationNames.planet_wisp_act_1: 19,
    LocationNames.planet_wisp_act_2: 20,
    LocationNames.planet_wisp_boss: 21,

    LocationNames.aquarium_park_act_1: 22,
    LocationNames.aquarium_park_act_2: 23,
    LocationNames.aquarium_park_boss: 24,

    LocationNames.asteroid_coaster_act_1: 25,
    LocationNames.asteroid_coaster_act_2: 26,
    LocationNames.asteroid_coaster_boss: 27,

    LocationNames.tropical_resort_mission_1: 30,
    LocationNames.tropical_resort_mission_2: 31,
    LocationNames.tropical_resort_mission_3: 32,

    LocationNames.sweet_mountain_mission_1: 33,
    LocationNames.sweet_mountain_mission_2: 34,
    LocationNames.sweet_mountain_mission_3: 35,

    LocationNames.starlight_carnival_mission_1: 36,
    LocationNames.starlight_carnival_mission_2: 37,
    LocationNames.starlight_carnival_mission_3: 38,

    LocationNames.planet_wisp_mission_1: 39,
    LocationNames.planet_wisp_mission_2: 40,
    LocationNames.planet_wisp_mission_3: 41,

    LocationNames.aquarium_park_mission_1: 42,
    LocationNames.aquarium_park_mission_2: 43,
    LocationNames.aquarium_park_mission_3: 44,

    LocationNames.asteroid_coaster_mission_1: 45,
    LocationNames.asteroid_coaster_mission_2: 46,
    LocationNames.asteroid_coaster_mission_3: 47,

    LocationNames.terminal_velocity_chase: 70,
    LocationNames.nega_wisp_armor: 80
}


red_rings_table = {
    LocationNames.tropical_resort_act_1_red_ring_1: 100,
    LocationNames.tropical_resort_act_1_red_ring_2: 101,
    LocationNames.tropical_resort_act_1_red_ring_3: 102,
    LocationNames.tropical_resort_act_1_red_ring_4: 103,
    LocationNames.tropical_resort_act_1_red_ring_5: 104,

    LocationNames.tropical_resort_act_2_red_ring_1: 105,
    LocationNames.tropical_resort_act_2_red_ring_2: 106,
    LocationNames.tropical_resort_act_2_red_ring_3: 107,
    LocationNames.tropical_resort_act_2_red_ring_4: 108,
    LocationNames.tropical_resort_act_2_red_ring_5: 109,

    LocationNames.sweet_mountain_act_1_red_ring_1: 110,
    LocationNames.sweet_mountain_act_1_red_ring_2: 111,
    LocationNames.sweet_mountain_act_1_red_ring_3: 112,
    LocationNames.sweet_mountain_act_1_red_ring_4: 113,
    LocationNames.sweet_mountain_act_1_red_ring_5: 114,

    LocationNames.sweet_mountain_act_2_red_ring_1: 115,
    LocationNames.sweet_mountain_act_2_red_ring_2: 116,
    LocationNames.sweet_mountain_act_2_red_ring_3: 117,
    LocationNames.sweet_mountain_act_2_red_ring_4: 118,
    LocationNames.sweet_mountain_act_2_red_ring_5: 119,

    LocationNames.starlight_carnival_act_1_red_ring_1: 120,
    LocationNames.starlight_carnival_act_1_red_ring_2: 121,
    LocationNames.starlight_carnival_act_1_red_ring_3: 122,
    LocationNames.starlight_carnival_act_1_red_ring_4: 123,
    LocationNames.starlight_carnival_act_1_red_ring_5: 124,

    LocationNames.starlight_carnival_act_2_red_ring_1: 125,
    LocationNames.starlight_carnival_act_2_red_ring_2: 126,
    LocationNames.starlight_carnival_act_2_red_ring_3: 127,
    LocationNames.starlight_carnival_act_2_red_ring_4: 128,
    LocationNames.starlight_carnival_act_2_red_ring_5: 129,

    LocationNames.planet_wisp_act_1_red_ring_1: 130,
    LocationNames.planet_wisp_act_1_red_ring_2: 131,
    LocationNames.planet_wisp_act_1_red_ring_3: 132,
    LocationNames.planet_wisp_act_1_red_ring_4: 133,
    LocationNames.planet_wisp_act_1_red_ring_5: 134,

    LocationNames.planet_wisp_act_2_red_ring_1: 135,
    LocationNames.planet_wisp_act_2_red_ring_2: 136,
    LocationNames.planet_wisp_act_2_red_ring_3: 137,
    LocationNames.planet_wisp_act_2_red_ring_4: 138,
    LocationNames.planet_wisp_act_2_red_ring_5: 139,

    LocationNames.aquarium_park_act_1_red_ring_1: 140,
    LocationNames.aquarium_park_act_1_red_ring_2: 141,
    LocationNames.aquarium_park_act_1_red_ring_3: 142,
    LocationNames.aquarium_park_act_1_red_ring_4: 143,
    LocationNames.aquarium_park_act_1_red_ring_5: 144,

    LocationNames.aquarium_park_act_2_red_ring_1: 145,
    LocationNames.aquarium_park_act_2_red_ring_2: 146,
    LocationNames.aquarium_park_act_2_red_ring_3: 147,
    LocationNames.aquarium_park_act_2_red_ring_4: 148,
    LocationNames.aquarium_park_act_2_red_ring_5: 149,

    LocationNames.asteroid_coaster_act_1_red_ring_1: 150,
    LocationNames.asteroid_coaster_act_1_red_ring_2: 151,
    LocationNames.asteroid_coaster_act_1_red_ring_3: 152,
    LocationNames.asteroid_coaster_act_1_red_ring_4: 153,
    LocationNames.asteroid_coaster_act_1_red_ring_5: 154,

    LocationNames.asteroid_coaster_act_2_red_ring_1: 155,
    LocationNames.asteroid_coaster_act_2_red_ring_2: 156,
    LocationNames.asteroid_coaster_act_2_red_ring_3: 157,
    LocationNames.asteroid_coaster_act_2_red_ring_4: 158,
    LocationNames.asteroid_coaster_act_2_red_ring_5: 159,

    LocationNames.tropical_resort_mission_1_red_ring_1: 160,
    LocationNames.tropical_resort_mission_1_red_ring_2: 161,
    LocationNames.tropical_resort_mission_2_red_ring_1: 162,
    LocationNames.tropical_resort_mission_2_red_ring_2: 163,
    LocationNames.tropical_resort_mission_3_red_ring_1: 164,
    LocationNames.tropical_resort_mission_3_red_ring_2: 165,

    LocationNames.sweet_mountain_mission_1_red_ring_1: 166,
    LocationNames.sweet_mountain_mission_1_red_ring_2: 167,
    LocationNames.sweet_mountain_mission_2_red_ring_1: 168,
    LocationNames.sweet_mountain_mission_2_red_ring_2: 169,
    LocationNames.sweet_mountain_mission_3_red_ring_1: 170,
    LocationNames.sweet_mountain_mission_3_red_ring_2: 171,

    LocationNames.starlight_carnival_mission_1_red_ring_1: 172,
    LocationNames.starlight_carnival_mission_1_red_ring_2: 173,
    LocationNames.starlight_carnival_mission_2_red_ring_1: 174,
    LocationNames.starlight_carnival_mission_2_red_ring_2: 175,
    LocationNames.starlight_carnival_mission_3_red_ring_1: 176,
    LocationNames.starlight_carnival_mission_3_red_ring_2: 177,

    LocationNames.planet_wisp_mission_1_red_ring_1: 178,
    LocationNames.planet_wisp_mission_1_red_ring_2: 179,
    LocationNames.planet_wisp_mission_2_red_ring_1: 180,
    LocationNames.planet_wisp_mission_2_red_ring_2: 181,
    LocationNames.planet_wisp_mission_3_red_ring_1: 182,
    LocationNames.planet_wisp_mission_3_red_ring_2: 183,

    LocationNames.aquarium_park_mission_1_red_ring_1: 184,
    LocationNames.aquarium_park_mission_1_red_ring_2: 185,
    LocationNames.aquarium_park_mission_2_red_ring_1: 186,
    LocationNames.aquarium_park_mission_2_red_ring_2: 187,
    LocationNames.aquarium_park_mission_3_red_ring_1: 188,
    LocationNames.aquarium_park_mission_3_red_ring_2: 189,

    LocationNames.asteroid_coaster_mission_1_red_ring_1: 190,
    LocationNames.asteroid_coaster_mission_1_red_ring_2: 191,
    LocationNames.asteroid_coaster_mission_2_red_ring_1: 192,
    LocationNames.asteroid_coaster_mission_2_red_ring_2: 193,
    LocationNames.asteroid_coaster_mission_3_red_ring_1: 194,
    LocationNames.asteroid_coaster_mission_3_red_ring_2: 195,
}


special_stage_table = {
    LocationNames.special_stage_1: 200,
    LocationNames.special_stage_2: 201,
    LocationNames.special_stage_3: 202,
    LocationNames.special_stage_4: 203,
    LocationNames.special_stage_5: 204,
    LocationNames.special_stage_6: 205,
    LocationNames.special_stage_7: 206,
}


location_table = {
    **tutorial_clear_table,
    **level_clear_table,
    **red_rings_table,
    **special_stage_table,
}


menu_locations = {
    LocationNames.special_stage_7,
}


tropical_resort_region_locations = {
    LocationNames.movement_tutorial,
    LocationNames.white_wisp_tutorial,

    LocationNames.tropical_resort_act_1,
    LocationNames.tropical_resort_act_1_red_ring_1,
    LocationNames.tropical_resort_act_1_red_ring_2,
    LocationNames.tropical_resort_act_1_red_ring_3,
    LocationNames.tropical_resort_act_1_red_ring_4,
    LocationNames.tropical_resort_act_1_red_ring_5,

    LocationNames.tropical_resort_act_2,
    LocationNames.tropical_resort_act_2_red_ring_1,
    LocationNames.tropical_resort_act_2_red_ring_2,
    LocationNames.tropical_resort_act_2_red_ring_3,
    LocationNames.tropical_resort_act_2_red_ring_4,
    LocationNames.tropical_resort_act_2_red_ring_5,

    LocationNames.tropical_resort_mission_1,
    LocationNames.tropical_resort_mission_1_red_ring_1,
    LocationNames.tropical_resort_mission_1_red_ring_2,

    LocationNames.tropical_resort_mission_2,
    LocationNames.tropical_resort_mission_2_red_ring_1,
    LocationNames.tropical_resort_mission_2_red_ring_2,

    LocationNames.tropical_resort_mission_3,
    LocationNames.tropical_resort_mission_3_red_ring_1,
    LocationNames.tropical_resort_mission_3_red_ring_2,

    LocationNames.tropical_resort_boss,
    LocationNames.special_stage_1,
}


sweet_mountain_region_locations = {
    LocationNames.red_wisp_tutorial,

    LocationNames.sweet_mountain_act_1,
    LocationNames.sweet_mountain_act_1_red_ring_1,
    LocationNames.sweet_mountain_act_1_red_ring_2,
    LocationNames.sweet_mountain_act_1_red_ring_3,
    LocationNames.sweet_mountain_act_1_red_ring_4,
    LocationNames.sweet_mountain_act_1_red_ring_5,

    LocationNames.sweet_mountain_act_2,
    LocationNames.sweet_mountain_act_2_red_ring_1,
    LocationNames.sweet_mountain_act_2_red_ring_2,
    LocationNames.sweet_mountain_act_2_red_ring_3,
    LocationNames.sweet_mountain_act_2_red_ring_4,
    LocationNames.sweet_mountain_act_2_red_ring_5,

    LocationNames.sweet_mountain_mission_1,
    LocationNames.sweet_mountain_mission_1_red_ring_1,
    LocationNames.sweet_mountain_mission_1_red_ring_2,

    LocationNames.sweet_mountain_mission_2,
    LocationNames.sweet_mountain_mission_2_red_ring_1,
    LocationNames.sweet_mountain_mission_2_red_ring_2,

    LocationNames.sweet_mountain_mission_3,
    LocationNames.sweet_mountain_mission_3_red_ring_1,
    LocationNames.sweet_mountain_mission_3_red_ring_2,

    LocationNames.sweet_mountain_boss,
    LocationNames.special_stage_2,
}


starlight_carnival_region_locations = {
    LocationNames.orange_wisp_tutorial,

    LocationNames.starlight_carnival_act_1,
    LocationNames.starlight_carnival_act_1_red_ring_1,
    LocationNames.starlight_carnival_act_1_red_ring_2,
    LocationNames.starlight_carnival_act_1_red_ring_3,
    LocationNames.starlight_carnival_act_1_red_ring_4,
    LocationNames.starlight_carnival_act_1_red_ring_5,

    LocationNames.starlight_carnival_act_2,
    LocationNames.starlight_carnival_act_2_red_ring_1,
    LocationNames.starlight_carnival_act_2_red_ring_2,
    LocationNames.starlight_carnival_act_2_red_ring_3,
    LocationNames.starlight_carnival_act_2_red_ring_4,
    LocationNames.starlight_carnival_act_2_red_ring_5,

    LocationNames.starlight_carnival_mission_1,
    LocationNames.starlight_carnival_mission_1_red_ring_1,
    LocationNames.starlight_carnival_mission_1_red_ring_2,

    LocationNames.starlight_carnival_mission_2,
    LocationNames.starlight_carnival_mission_2_red_ring_1,
    LocationNames.starlight_carnival_mission_2_red_ring_2,

    LocationNames.starlight_carnival_mission_3,
    LocationNames.starlight_carnival_mission_3_red_ring_1,
    LocationNames.starlight_carnival_mission_3_red_ring_2,

    LocationNames.starlight_carnival_boss,
    LocationNames.special_stage_3,
}


planet_wisp_region_locations = {
    LocationNames.yellow_wisp_tutorial,

    LocationNames.planet_wisp_act_1,
    LocationNames.planet_wisp_act_1_red_ring_1,
    LocationNames.planet_wisp_act_1_red_ring_2,
    LocationNames.planet_wisp_act_1_red_ring_3,
    LocationNames.planet_wisp_act_1_red_ring_4,
    LocationNames.planet_wisp_act_1_red_ring_5,

    LocationNames.planet_wisp_act_2,
    LocationNames.planet_wisp_act_2_red_ring_1,
    LocationNames.planet_wisp_act_2_red_ring_2,
    LocationNames.planet_wisp_act_2_red_ring_3,
    LocationNames.planet_wisp_act_2_red_ring_4,
    LocationNames.planet_wisp_act_2_red_ring_5,

    LocationNames.planet_wisp_mission_1,
    LocationNames.planet_wisp_mission_1_red_ring_1,
    LocationNames.planet_wisp_mission_1_red_ring_2,

    LocationNames.planet_wisp_mission_2,
    LocationNames.planet_wisp_mission_2_red_ring_1,
    LocationNames.planet_wisp_mission_2_red_ring_2,

    LocationNames.planet_wisp_mission_3,
    LocationNames.planet_wisp_mission_3_red_ring_1,
    LocationNames.planet_wisp_mission_3_red_ring_2,

    LocationNames.planet_wisp_boss,
    LocationNames.special_stage_4,
}


aquarium_park_region_locations = {
    LocationNames.cyan_wisp_tutorial,

    LocationNames.aquarium_park_act_1,
    LocationNames.aquarium_park_act_1_red_ring_1,
    LocationNames.aquarium_park_act_1_red_ring_2,
    LocationNames.aquarium_park_act_1_red_ring_3,
    LocationNames.aquarium_park_act_1_red_ring_4,
    LocationNames.aquarium_park_act_1_red_ring_5,

    LocationNames.aquarium_park_act_2,
    LocationNames.aquarium_park_act_2_red_ring_1,
    LocationNames.aquarium_park_act_2_red_ring_2,
    LocationNames.aquarium_park_act_2_red_ring_3,
    LocationNames.aquarium_park_act_2_red_ring_4,
    LocationNames.aquarium_park_act_2_red_ring_5,

    LocationNames.aquarium_park_mission_1,
    LocationNames.aquarium_park_mission_1_red_ring_1,
    LocationNames.aquarium_park_mission_1_red_ring_2,

    LocationNames.aquarium_park_mission_2,
    LocationNames.aquarium_park_mission_2_red_ring_1,
    LocationNames.aquarium_park_mission_2_red_ring_2,

    LocationNames.aquarium_park_mission_3,
    LocationNames.aquarium_park_mission_3_red_ring_1,
    LocationNames.aquarium_park_mission_3_red_ring_2,

    LocationNames.aquarium_park_boss,
    LocationNames.special_stage_5,
}


asteroid_coaster_region_locations = {
    LocationNames.violet_wisp_tutorial,

    LocationNames.asteroid_coaster_act_1,
    LocationNames.asteroid_coaster_act_1_red_ring_1,
    LocationNames.asteroid_coaster_act_1_red_ring_2,
    LocationNames.asteroid_coaster_act_1_red_ring_3,
    LocationNames.asteroid_coaster_act_1_red_ring_4,
    LocationNames.asteroid_coaster_act_1_red_ring_5,

    LocationNames.asteroid_coaster_act_2,
    LocationNames.asteroid_coaster_act_2_red_ring_1,
    LocationNames.asteroid_coaster_act_2_red_ring_2,
    LocationNames.asteroid_coaster_act_2_red_ring_3,
    LocationNames.asteroid_coaster_act_2_red_ring_4,
    LocationNames.asteroid_coaster_act_2_red_ring_5,

    LocationNames.asteroid_coaster_mission_1,
    LocationNames.asteroid_coaster_mission_1_red_ring_1,
    LocationNames.asteroid_coaster_mission_1_red_ring_2,

    LocationNames.asteroid_coaster_mission_2,
    LocationNames.asteroid_coaster_mission_2_red_ring_1,
    LocationNames.asteroid_coaster_mission_2_red_ring_2,

    LocationNames.asteroid_coaster_mission_3,
    LocationNames.asteroid_coaster_mission_3_red_ring_1,
    LocationNames.asteroid_coaster_mission_3_red_ring_2,

    LocationNames.asteroid_coaster_boss,
    LocationNames.special_stage_6,
}


terminal_velocity_region_locations = {
    LocationNames.terminal_velocity_chase,
    LocationNames.nega_wisp_armor,
}


planet_boss_locations = {
    LocationNames.tropical_resort_boss,
    LocationNames.sweet_mountain_boss,
    LocationNames.starlight_carnival_boss,
    LocationNames.planet_wisp_boss,
    LocationNames.aquarium_park_boss,
    LocationNames.asteroid_coaster_boss,
}


def setup_locations(world: World, player: int):
    locations = {}

    locations.update({**tutorial_clear_table})
    locations.update({**level_clear_table})
    locations.update({**special_stage_table})

    if world.options.redringsanity == Toggle.option_true:
        locations.update({**red_rings_table})
    if world.options.goal.value == Goal.option_wisp_armor:
        locations.update({LocationNames.nega_wisp_armor: None})
    elif world.options.goal.value == Goal.option_mother_wisp:
        locations.update({
            LocationNames.nega_wisp_armor: 80,
            LocationNames.nega_mother_wisp: None
        })

    return locations

lookup_id_to_name: dict[int, str] = {idx: name for name, idx in location_table.items()}

location_groups: dict[str, set[str]] = {
    "Level Clear": set(level_clear_table.keys()),
    "Red Rings": set(red_rings_table.keys()),
    "Special Stage": set(special_stage_table.keys()),
    "Tutorial": set(tutorial_clear_table.keys()),
    "Planet Boss": planet_boss_locations,
    "Tropical Resort": tropical_resort_region_locations,
    "Sweet Mountain": sweet_mountain_region_locations,
    "Starlight Carnival": starlight_carnival_region_locations,
    "Planet Wisp": planet_wisp_region_locations,
    "Aquarium Park": aquarium_park_region_locations,
    "Asteroid Coaster": asteroid_coaster_region_locations,
    "Terminal Velocity": terminal_velocity_region_locations,
}
