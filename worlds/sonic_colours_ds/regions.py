import typing

from BaseClasses import CollectionState, Region, Entrance, ItemClassification
from worlds.AutoWorld import World
from .locations import *
from .data import LocationNames, ItemNames
from .options import Goal

def create_regions(world: World, active_locations: dict[str, int]) -> None:
    menu_region = create_region(world, "Menu", active_locations, menu_locations)
    tropical_resort_region = create_region(world, LocationNames.tropical_resort_region, active_locations, tropical_resort_region_locations)
    sweet_mountain_region = create_region(world, LocationNames.sweet_mountain_region, active_locations, sweet_mountain_region_locations)
    starlight_carnival_region = create_region(world, LocationNames.starlight_carnival_region, active_locations, starlight_carnival_region_locations)
    planet_wisp_region = create_region(world, LocationNames.planet_wisp_region, active_locations, planet_wisp_region_locations)
    aquarium_park_region = create_region(world, LocationNames.aquarium_park_region, active_locations, aquarium_park_region_locations)
    asteroid_coaster_region = create_region(world, LocationNames.asteroid_coaster_region, active_locations, asteroid_coaster_region_locations)
    terminal_velocity_region = create_region(world, LocationNames.terminal_velocity_region, active_locations, terminal_velocity_region_locations)
    if world.options.goal.value == Goal.option_mother_wisp:
        terminal_velocity_region.locations.append(SonicColoursDSLocation(world.player, LocationNames.nega_mother_wisp, active_locations[LocationNames.nega_mother_wisp], terminal_velocity_region))

    world.multiworld.regions += [
        menu_region,
        tropical_resort_region,
        sweet_mountain_region,
        starlight_carnival_region,
        planet_wisp_region,
        aquarium_park_region,
        asteroid_coaster_region,
        terminal_velocity_region,
    ]

def connect_regions(world: World) -> None:
    connect(world, "Menu", LocationNames.tropical_resort_region, 
            lambda state: state.has(ItemNames.tropical_resort_unlock, world.player))
    connect(world, "Menu", LocationNames.sweet_mountain_region, 
            lambda state: state.has(ItemNames.sweet_mountain_unlock, world.player))
    connect(world, "Menu", LocationNames.starlight_carnival_region, 
            lambda state: state.has(ItemNames.starlight_carnival_unlock, world.player))
    connect(world, "Menu", LocationNames.planet_wisp_region, 
            lambda state: state.has(ItemNames.planet_wisp_unlock, world.player))
    connect(world, "Menu", LocationNames.aquarium_park_region, 
            lambda state: state.has(ItemNames.aquarium_park_unlock, world.player))
    connect(world, "Menu", LocationNames.asteroid_coaster_region, 
            lambda state: state.has(ItemNames.asteroid_coaster_unlock, world.player))
    connect(world, "Menu", LocationNames.terminal_velocity_region, 
            lambda state: state.has(ItemNames.terminal_velocity_unlock, world.player))

def create_region(world: World, name: str, active_locations: dict[str, int], location_set: set[str]) -> Region:
    region = Region(name, world.player, world.multiworld)
    for location in sorted(location_set):
        code = active_locations.get(location, 0)
        if location in active_locations.keys():
            region.locations.append(SonicColoursDSLocation(world.player, location, code, region))
    return region

def connect(world: World, source: str, destination: str, rule: typing.Optional[typing.Callable[[CollectionState],bool]]) -> None:
    source_region = world.multiworld.get_region(source, world.player)
    dest_region = world.multiworld.get_region(destination, world.player)

    entrance = Entrance(world.player, destination, source_region)

    if rule:
        entrance.access_rule = rule
    
    source_region.exits.append(entrance)
    entrance.connect(dest_region)