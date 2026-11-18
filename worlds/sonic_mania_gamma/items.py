import typing

from BaseClasses import Item

from .data import ItemNames
from .data.constants import GAME_NAME


class ItemData(typing.NamedTuple):
    code: int | None
    progression: bool
    trap: bool = False
    quantity: int = 1

class SonicManiaGammaItem(Item):
    game = GAME_NAME

junk_table = {
    ItemNames.five_rings: ItemData(1, False),
    ItemNames.ten_rings: ItemData(2, False),
    ItemNames.twenty_rings: ItemData(4, False),
    ItemNames.extra_life: ItemData(8, False),
    ItemNames.shield: ItemData(0x10, False),
    ItemNames.lightning_shield: ItemData(0x11, False),
    ItemNames.bubble_shield: ItemData(0x12, False),
    ItemNames.flame_shield: ItemData(0x13, False),
}

character_table = {
    ItemNames.sonic: ItemData(0x20, True),
    ItemNames.tails: ItemData(0x21, True),
    ItemNames.knuckles: ItemData(0x22, True),
}

encore_character_table = {
    ItemNames.ray: ItemData(0x23, True),
    ItemNames.mighty: ItemData(0x24, True),
}

chaos_emerald_table = {
    ItemNames.green_chaos_emerald: ItemData(0x30, True),
    ItemNames.yellow_chaos_emerald: ItemData(0x31, True),
    ItemNames.blue_chaos_emerald: ItemData(0x32, True),
    ItemNames.purple_chaos_emerald: ItemData(0x33, True),
    ItemNames.white_chaos_emerald: ItemData(0x34, True),
    ItemNames.cyan_chaos_emerald: ItemData(0x35, True),
    ItemNames.red_chaos_emerald: ItemData(0x36, True),
}

level_unlock_table = {
    ItemNames.green_hill_1_unlock: ItemData(0x100, True),
    ItemNames.green_hill_2_unlock: ItemData(0x101, True),
    ItemNames.chemical_plant_1_unlock: ItemData(0x102, True),
    ItemNames.chemical_plant_2_unlock: ItemData(0x103, True),
    ItemNames.studiopolis_1_unlock: ItemData(0x104, True),
    ItemNames.studiopolis_2_unlock: ItemData(0x105, True),
    ItemNames.flying_battery_1_unlock: ItemData(0x106, True),
    ItemNames.flying_battery_2_unlock: ItemData(0x107, True),
    ItemNames.press_garden_1_unlock: ItemData(0x108, True),
    ItemNames.press_garden_2_unlock: ItemData(0x109, True),
    ItemNames.stardust_speedway_1_unlock: ItemData(0x10A, True),
    ItemNames.stardust_speedway_2_unlock: ItemData(0x10B, True),

    ItemNames.hydrocity_1_unlock: ItemData(0x10D, True),
    ItemNames.hydrocity_2_unlock: ItemData(0x10E, True),
    ItemNames.mirage_saloon_1_unlock: ItemData(0x10F, True),
    ItemNames.mirage_saloon_1k_unlock: ItemData(0x110, True),
    ItemNames.mirage_saloon_2_unlock: ItemData(0x111, True),
    ItemNames.oil_ocean_1_unlock: ItemData(0x112, True),
    ItemNames.oil_ocean_2_unlock: ItemData(0x113, True),
    ItemNames.lava_reef_1_unlock: ItemData(0x114, True),
    ItemNames.lava_reef_2_unlock: ItemData(0x115, True),

    ItemNames.metallic_madness_1_unlock: ItemData(0x117, True),
    ItemNames.metallic_madness_2_unlock: ItemData(0x118, True),
    ItemNames.titanic_monarch_1_unlock: ItemData(0x119, True),
    ItemNames.titanic_monarch_2_unlock: ItemData(0x11A, True),

    ItemNames.egg_reverie_unlock: ItemData(0x11C, True),
}

encore_level_unlock_table = {
    ItemNames.green_hill_1e_unlock: ItemData(0x11D, True),
    ItemNames.green_hill_2e_unlock: ItemData(0x11E, True),
    ItemNames.chemical_plant_1e_unlock: ItemData(0x11F, True),
    ItemNames.chemical_plant_2e_unlock: ItemData(0x120, True),
    ItemNames.studiopolis_1e_unlock: ItemData(0x121, True),
    ItemNames.studiopolis_2e_unlock: ItemData(0x122, True),
    ItemNames.flying_battery_1e_unlock: ItemData(0x123, True),
    ItemNames.flying_battery_2e_unlock: ItemData(0x124, True),
    ItemNames.press_garden_1e_unlock: ItemData(0x125, True),
    ItemNames.press_garden_2e_unlock: ItemData(0x126, True),
    ItemNames.stardust_speedway_1e_unlock: ItemData(0x127, True),
    ItemNames.stardust_speedway_2e_unlock: ItemData(0x128, True),

    ItemNames.hydrocity_1e_unlock: ItemData(0x12A, True),
    ItemNames.hydrocity_2e_unlock: ItemData(0x12B, True),
    ItemNames.mirage_saloon_1e_unlock: ItemData(0x12C, True),
    ItemNames.mirage_saloon_2e_unlock: ItemData(0x12D, True),
    ItemNames.oil_ocean_1e_unlock: ItemData(0x12E, True),
    ItemNames.oil_ocean_2e_unlock: ItemData(0x12F, True),
    ItemNames.lava_reef_1e_unlock: ItemData(0x130, True),
    ItemNames.lava_reef_2e_unlock: ItemData(0x131, True),

    ItemNames.metallic_madness_1e_unlock: ItemData(0x133, True),
    ItemNames.metallic_madness_2e_unlock: ItemData(0x134, True),
    ItemNames.titanic_monarch_1e_unlock: ItemData(0x135, True),
    ItemNames.titanic_monarch_2e_unlock: ItemData(0x136, True),
}

special_stage_unlock_table = {
    ItemNames.special_stage_1_unlock: ItemData(0x137, True),
    ItemNames.special_stage_2_unlock: ItemData(0x138, True),
    ItemNames.special_stage_3_unlock: ItemData(0x139, True),
    ItemNames.special_stage_4_unlock: ItemData(0x13A, True),
    ItemNames.special_stage_5_unlock: ItemData(0x13B, True),
    ItemNames.special_stage_6_unlock: ItemData(0x13C, True),
    ItemNames.special_stage_7_unlock: ItemData(0x13D, True),
}

encore_special_stage_unlock_table = {
    ItemNames.special_stage_1e_unlock: ItemData(0x13E, True),
    ItemNames.special_stage_2e_unlock: ItemData(0x13F, True),
    ItemNames.special_stage_3e_unlock: ItemData(0x140, True),
    ItemNames.special_stage_4e_unlock: ItemData(0x141, True),
    ItemNames.special_stage_5e_unlock: ItemData(0x142, True),
    ItemNames.special_stage_6e_unlock: ItemData(0x143, True),
    ItemNames.special_stage_7e_unlock: ItemData(0x144, True),
}

event_table: dict[str, ItemData] = {
    ItemNames.victory: ItemData(None, True),
}

item_table: dict[str, ItemData] = {
    **junk_table,
    **character_table,
    **encore_character_table,
    **level_unlock_table,
    **encore_level_unlock_table,
    **special_stage_unlock_table,
    **encore_special_stage_unlock_table,
}

lookup_id_to_name: dict[int, str] = {idx: name for name, idx in item_table.items() if idx is not None}

item_groups = {}
