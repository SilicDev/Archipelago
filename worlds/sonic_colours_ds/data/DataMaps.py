from . import ItemNames, LocationNames

level_id_to_location = [
    LocationNames.tropical_resort_region,
    LocationNames.sweet_mountain_region,
    LocationNames.starlight_carnival_region,
    LocationNames.planet_wisp_region,
    LocationNames.aquarium_park_region,
    LocationNames.asteroid_coaster_region,
    LocationNames.terminal_velocity_region,
    LocationNames.nega_mother_wisp,
    LocationNames.game_land_region,

    LocationNames.tropical_resort_act_1,
    LocationNames.tropical_resort_act_2,
    LocationNames.tropical_resort_boss,
    LocationNames.tropical_resort_mission_1,
    LocationNames.tropical_resort_mission_2,
    LocationNames.tropical_resort_mission_3,

    LocationNames.movement_tutorial,

    LocationNames.sweet_mountain_act_1,
    LocationNames.sweet_mountain_act_2,
    LocationNames.sweet_mountain_boss,
    LocationNames.sweet_mountain_mission_1,
    LocationNames.sweet_mountain_mission_2,
    LocationNames.sweet_mountain_mission_3,

    LocationNames.starlight_carnival_act_1,
    LocationNames.starlight_carnival_act_2,
    LocationNames.starlight_carnival_boss,
    LocationNames.starlight_carnival_mission_1,
    LocationNames.starlight_carnival_mission_2,
    LocationNames.starlight_carnival_mission_3,

    LocationNames.planet_wisp_act_1,
    LocationNames.planet_wisp_act_2,
    LocationNames.planet_wisp_boss,
    LocationNames.planet_wisp_mission_1,
    LocationNames.planet_wisp_mission_2,
    LocationNames.planet_wisp_mission_3,

    LocationNames.aquarium_park_act_1,
    LocationNames.aquarium_park_act_2,
    LocationNames.aquarium_park_boss,
    LocationNames.aquarium_park_mission_1,
    LocationNames.aquarium_park_mission_2,
    LocationNames.aquarium_park_mission_3,

    LocationNames.asteroid_coaster_act_1,
    LocationNames.asteroid_coaster_act_2,
    LocationNames.asteroid_coaster_boss,
    LocationNames.asteroid_coaster_mission_1,
    LocationNames.asteroid_coaster_mission_2,
    LocationNames.asteroid_coaster_mission_3,
]

level_id_to_access_item = [ # only use for planet map
    ItemNames.tropical_resort_unlock,
    ItemNames.sweet_mountain_unlock,
    ItemNames.starlight_carnival_unlock,
    ItemNames.planet_wisp_unlock,
    ItemNames.aquarium_park_unlock,
    ItemNames.asteroid_coaster_unlock,
    ItemNames.terminal_velocity_unlock,
]

access_item_to_offset = {
    ItemNames.tropical_resort_unlock: 0,
    ItemNames.sweet_mountain_unlock: 1,
    ItemNames.starlight_carnival_unlock: 2,
    ItemNames.planet_wisp_unlock: 3,
    ItemNames.aquarium_park_unlock: 4,
    ItemNames.asteroid_coaster_unlock: 5,
    ItemNames.terminal_velocity_unlock: 6,
}

area_id_to_tutorial = [
    None,
    LocationNames.white_wisp_tutorial,
    LocationNames.red_wisp_tutorial,
    LocationNames.orange_wisp_tutorial,
    LocationNames.yellow_wisp_tutorial,
    LocationNames.cyan_wisp_tutorial,
    LocationNames.violet_wisp_tutorial,
]

level_id_to_wisps = {
    9: [ItemNames.red_wisp],
    10: [ItemNames.red_wisp],
    11: [ItemNames.red_wisp],
    12: [ItemNames.red_wisp],
    13: [ItemNames.red_wisp],
    14: [ItemNames.red_wisp],
    16: [ItemNames.red_wisp, ItemNames.violet_wisp],
    17: [ItemNames.red_wisp, ItemNames.violet_wisp],
    18: [ItemNames.red_wisp],
    19: [ItemNames.red_wisp, ItemNames.violet_wisp],
    20: [ItemNames.red_wisp, ItemNames.violet_wisp],
    21: [ItemNames.red_wisp, ItemNames.violet_wisp],
    22: [ItemNames.orange_wisp, ItemNames.cyan_wisp],
    23: [ItemNames.orange_wisp, ItemNames.cyan_wisp],
    24: [ItemNames.orange_wisp],
    25: [ItemNames.orange_wisp, ItemNames.cyan_wisp],
    26: [ItemNames.orange_wisp, ItemNames.cyan_wisp],
    27: [ItemNames.orange_wisp, ItemNames.cyan_wisp],
    28: [ItemNames.orange_wisp, ItemNames.yellow_wisp],
    29: [ItemNames.orange_wisp, ItemNames.yellow_wisp],
    30: [ItemNames.yellow_wisp],
    31: [ItemNames.orange_wisp, ItemNames.yellow_wisp],
    32: [ItemNames.orange_wisp, ItemNames.yellow_wisp],
    33: [ItemNames.orange_wisp, ItemNames.yellow_wisp],
    34: [ItemNames.yellow_wisp, ItemNames.cyan_wisp],
    35: [ItemNames.yellow_wisp, ItemNames.cyan_wisp],
    36: [ItemNames.cyan_wisp],
    37: [ItemNames.yellow_wisp, ItemNames.cyan_wisp],
    38: [ItemNames.yellow_wisp, ItemNames.cyan_wisp],
    39: [ItemNames.yellow_wisp, ItemNames.cyan_wisp],
    40: [ItemNames.cyan_wisp, ItemNames.violet_wisp],
    41: [ItemNames.cyan_wisp, ItemNames.violet_wisp],
    42: [ItemNames.violet_wisp],
    43: [ItemNames.cyan_wisp, ItemNames.violet_wisp],
    44: [ItemNames.cyan_wisp, ItemNames.violet_wisp],
    45: [ItemNames.cyan_wisp, ItemNames.violet_wisp],
}

boss_level_wisps = {
    11: 0x02,
    18: 0x02,
    24: 0x04,
    30: 0x08,
    36: 0x10,
    42: 0x20,
}

level_id_to_emeralds = {
    8: 0x3F,
    9: 0x00,
    10: 0x00,
    16: 0x01,
    17: 0x01,
    22: 0x03,
    23: 0x03,
    28: 0x07,
    29: 0x07,
    34: 0x0F,
    35: 0x0F,
    40: 0x1F,
    41: 0x1F
}

item_to_rings = {
    ItemNames.five_rings: 5,
    ItemNames.ten_rings: 10,
    ItemNames.twenty_rings: 20,
}

planet_names_to_unlock = {
    "Tropical Resort": ItemNames.tropical_resort_unlock,
    "Sweet Mountain": ItemNames.sweet_mountain_unlock,
    "Starlight Carnival": ItemNames.starlight_carnival_unlock,
    "Planet Wisp": ItemNames.planet_wisp_unlock,
    "Aquarium Park": ItemNames.aquarium_park_unlock,
    "Asteroid Coaster": ItemNames.asteroid_coaster_unlock,
}
