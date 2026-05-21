import typing

from BaseClasses import Item

from .data import ItemNames


class ItemData(typing.NamedTuple):
    code: int | None
    progression: bool
    quantity: int = 1

class SonicColoursDSItem(Item):
    game: str = "Sonic Colours (DS)"

junk_table = {
    ItemNames.five_rings: ItemData(1, False),
    ItemNames.ten_rings: ItemData(2, False),
    ItemNames.twenty_rings: ItemData(3, False),
    ItemNames.extra_life: ItemData(4, False),
}

emeralds_table = {
    ItemNames.green_emerald: ItemData(10, True),
    ItemNames.yellow_emerald: ItemData(11, True),
    ItemNames.white_emerald: ItemData(12, True),
    ItemNames.red_emerald: ItemData(13, True),
    ItemNames.purple_emerald: ItemData(14, True),
    ItemNames.blue_emerald: ItemData(15, True),
    ItemNames.cyan_emerald: ItemData(16, True),
}

wisps_table = {
    ItemNames.white_wisp: ItemData(20, False),
    ItemNames.red_wisp: ItemData(21, False),
    ItemNames.orange_wisp: ItemData(22, False),
    ItemNames.yellow_wisp: ItemData(23, False),
    ItemNames.cyan_wisp: ItemData(24, False),
    ItemNames.violet_wisp: ItemData(25, False)
}

wisp_unlocks_table = {
    ItemNames.white_wisp_unlock: ItemData(30, True),
    ItemNames.red_wisp_unlock: ItemData(31, True),
    ItemNames.orange_wisp_unlock: ItemData(32, True),
    ItemNames.yellow_wisp_unlock: ItemData(33, True),
    ItemNames.cyan_wisp_unlock: ItemData(34, True),
    ItemNames.violet_wisp_unlock: ItemData(35, True)
}

planet_access_table = {
    ItemNames.tropical_resort_unlock: ItemData(40, True),
    ItemNames.sweet_mountain_unlock: ItemData(41, True),
    ItemNames.starlight_carnival_unlock: ItemData(42, True),
    ItemNames.planet_wisp_unlock: ItemData(43, True),
    ItemNames.aquarium_park_unlock: ItemData(44, True),
    ItemNames.asteroid_coaster_unlock: ItemData(45, True),
    ItemNames.terminal_velocity_unlock: ItemData(46, True),
}

event_table = {
    ItemNames.park_keys: ItemData(None, True),
    ItemNames.mother_wisp: ItemData(None, True)
}

item_table = {
    **junk_table,
    **emeralds_table,
    **wisps_table,
    **wisp_unlocks_table,
    **planet_access_table
}

lookup_id_to_name: dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}

item_groups: dict[str, set[str]] = {
    "Chaos Emeralds": set(emeralds_table.keys()),
    "Wisps": set(wisps_table.keys()),
    "Wisp Unlocks": set(wisp_unlocks_table.keys()),
    "Planet Access": set(planet_access_table.keys()),
}
