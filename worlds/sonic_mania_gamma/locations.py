from BaseClasses import Location
from worlds.AutoWorld import World

from .data import LocationNames
from .data.constants import GAME_NAME
from .options import MainLevelSelection, SpecialStageSelection


class SonicManiaGammaLocation(Location):
    game = GAME_NAME

menu_region_locations = set()

level_clear_locations = {
    LocationNames.green_hill_1_clear: 0x01,
    LocationNames.green_hill_2_clear: 0x02,
    LocationNames.chemical_plant_1_clear: 0x03,
    LocationNames.chemical_plant_2_clear: 0x04,
    LocationNames.studiopolis_1_clear: 0x05,
    LocationNames.studiopolis_2_clear: 0x06,
    LocationNames.flying_battery_1_clear: 0x07,
    LocationNames.flying_battery_2_clear: 0x08,
    LocationNames.press_garden_1_clear: 0x09,
    LocationNames.press_garden_2_clear: 0x0A,
    LocationNames.stardust_speedway_1_clear: 0x0B,
    LocationNames.stardust_speedway_2_clear: 0x0C,

    LocationNames.hydrocity_1_clear: 0x0E,
    LocationNames.hydrocity_2_clear: 0x0F,
    LocationNames.mirage_saloon_1_clear: 0x10,
    LocationNames.mirage_saloon_1k_clear: 0x11,
    LocationNames.mirage_saloon_2_clear: 0x12,
    LocationNames.oil_ocean_1_clear: 0x13,
    LocationNames.oil_ocean_2_clear: 0x14,
    LocationNames.lava_reef_1_clear: 0x15,
    LocationNames.lava_reef_2_clear: 0x16,

    LocationNames.metallic_madness_1_clear: 0x18,
    LocationNames.metallic_madness_2_clear: 0x19,
    LocationNames.titanic_monarch_1_clear: 0x1A,
    LocationNames.titanic_monarch_2_clear: 0x1B,
}

encore_level_clear_locations = {
    LocationNames.green_hill_1e_clear: 0x1E,
    LocationNames.green_hill_2e_clear: 0x1F,
    LocationNames.chemical_plant_1e_clear: 0x20,
    LocationNames.chemical_plant_2e_clear: 0x21,
    LocationNames.studiopolis_1e_clear: 0x22,
    LocationNames.studiopolis_2e_clear: 0x23,
    LocationNames.flying_battery_1e_clear: 0x24,
    LocationNames.flying_battery_2e_clear: 0x25,
    LocationNames.press_garden_1e_clear: 0x26,
    LocationNames.press_garden_2e_clear: 0x27,
    LocationNames.stardust_speedway_1e_clear: 0x28,
    LocationNames.stardust_speedway_2e_clear: 0x29,

    LocationNames.hydrocity_1e_clear: 0x2B,
    LocationNames.hydrocity_2e_clear: 0x2C,
    LocationNames.mirage_saloon_1e_clear: 0x2D,
    LocationNames.mirage_saloon_2e_clear: 0x2E,
    LocationNames.oil_ocean_1e_clear: 0x2F,
    LocationNames.oil_ocean_2e_clear: 0x30,
    LocationNames.lava_reef_1e_clear: 0x31,
    LocationNames.lava_reef_2e_clear: 0x32,

    LocationNames.metallic_madness_1e_clear: 0x34,
    LocationNames.metallic_madness_2e_clear: 0x35,
    LocationNames.titanic_monarch_1e_clear: 0x36,
    LocationNames.titanic_monarch_2e_clear: 0x37,
}

special_stage_clear_locations = {
    LocationNames.special_stage_1_clear: 0x38,
    LocationNames.special_stage_2_clear: 0x39,
    LocationNames.special_stage_3_clear: 0x3A,
    LocationNames.special_stage_4_clear: 0x3B,
    LocationNames.special_stage_5_clear: 0x3C,
    LocationNames.special_stage_6_clear: 0x3D,
    LocationNames.special_stage_7_clear: 0x3E,
}

encore_special_stage_clear_locations = {
    LocationNames.special_stage_1e_clear: 0x3F,
    LocationNames.special_stage_2e_clear: 0x40,
    LocationNames.special_stage_3e_clear: 0x41,
    LocationNames.special_stage_4e_clear: 0x42,
    LocationNames.special_stage_5e_clear: 0x43,
    LocationNames.special_stage_6e_clear: 0x44,
    LocationNames.special_stage_7e_clear: 0x45,
}

boss_clear_locations = {
    LocationNames.boss_metal_sonic_clear: 0x0D,
    LocationNames.boss_heavy_rider_clear: 0x17,
    LocationNames.titanic_monarch_boss_clear: 0x1C,
    LocationNames.egg_reverie_clear: 0x1D,
    LocationNames.boss_heavy_king_clear: 0x33,
}

bluespheres_locations = {
    LocationNames.bluespheres_01_clear: 0x46,
    LocationNames.bluespheres_02_clear: 0x47,
    LocationNames.bluespheres_03_clear: 0x48,
    LocationNames.bluespheres_04_clear: 0x49,
    LocationNames.bluespheres_05_clear: 0x4A,
    LocationNames.bluespheres_06_clear: 0x4B,
    LocationNames.bluespheres_07_clear: 0x4C,
    LocationNames.bluespheres_08_clear: 0x4D,
    LocationNames.bluespheres_09_clear: 0x4E,
    LocationNames.bluespheres_10_clear: 0x4F,
    LocationNames.bluespheres_11_clear: 0x50,
    LocationNames.bluespheres_12_clear: 0x51,
    LocationNames.bluespheres_13_clear: 0x52,
    LocationNames.bluespheres_14_clear: 0x53,
    LocationNames.bluespheres_15_clear: 0x54,
    LocationNames.bluespheres_16_clear: 0x55,
    LocationNames.bluespheres_17_clear: 0x56,
    LocationNames.bluespheres_18_clear: 0x57,
    LocationNames.bluespheres_19_clear: 0x58,
    LocationNames.bluespheres_20_clear: 0x59,
    LocationNames.bluespheres_21_clear: 0x5A,
    LocationNames.bluespheres_22_clear: 0x5B,
    LocationNames.bluespheres_23_clear: 0x5C,
    LocationNames.bluespheres_24_clear: 0x5D,
    LocationNames.bluespheres_25_clear: 0x5E,
    LocationNames.bluespheres_26_clear: 0x5F,
    LocationNames.bluespheres_27_clear: 0x60,
    LocationNames.bluespheres_28_clear: 0x61,
    LocationNames.bluespheres_29_clear: 0x62,
    LocationNames.bluespheres_30_clear: 0x63,
    LocationNames.bluespheres_31_clear: 0x64,
    LocationNames.bluespheres_32_clear: 0x65,
}

event_locations = {
    LocationNames.victory: None
}

location_table: dict[str, int | None] = {
    **event_locations,
    **level_clear_locations,
    **encore_level_clear_locations,
    **special_stage_clear_locations,
    **encore_special_stage_clear_locations,
    **boss_clear_locations,
    **bluespheres_locations,
}

def setup_locations(world: World, player: int) -> dict[str, int | None]:
    is_ut = getattr(world.multiworld, "generation_is_fake", False)
    if is_ut:
        return location_table
    locations: dict[str, int | None] = {}
    if world.options.main_level_selection.value != MainLevelSelection.option_encore:
        locations.update(**level_clear_locations)
    if world.options.main_level_selection.value >= MainLevelSelection.option_encore:
        locations.update(**encore_level_clear_locations)
    if world.options.special_stage_selection.value != SpecialStageSelection.option_encore:
        locations.update(**special_stage_clear_locations)
    if world.options.special_stage_selection.value >= SpecialStageSelection.option_encore:
        locations.update(**encore_special_stage_clear_locations)
    locations.update(**boss_clear_locations)
    locations.update(**bluespheres_locations)
    locations.update(**event_locations)
    return locations

lookup_id_to_name: dict[int, str] = {idx: name for name, idx in location_table.items() if idx is not None}

location_groups = {}
