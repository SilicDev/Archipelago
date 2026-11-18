from collections.abc import Callable

from BaseClasses import CollectionState, Entrance, EntranceType, Region
from rule_builder.rules import CanReachLocation, CanReachRegion, Filtered, Has, HasAll, Rule
from worlds.AutoWorld import World

from . import locations
from .data import ItemNames, LocationNames
from .items import SonicManiaGammaItem
from .locations import SonicManiaGammaLocation


# TODO: regions
def create_regions(world: World, active_locations: dict[str, int]) -> None:
    menu_region = create_region(world, world.origin_region_name, active_locations, set(active_locations.keys()))#locations.menu_region_locations)

    world.multiworld.regions += [
        menu_region,
    ]

def connect_regions(world: World) -> None:
    pass

def create_region(world: World, name: str, active_locations: dict[str, int], location_set: set[str]) -> Region:
    region = Region(name, world.player, world.multiworld)
    for location in sorted(location_set):
        code = active_locations.get(location, 0)
        if location in active_locations.keys():
            region.locations.append(SonicManiaGammaLocation(world.player, location, code, region))
    return region

def connect(world: World, source: str, destination: str, rule: Rule | Callable[[CollectionState], bool] | None,
            one_way: bool = False, randomization_group: int = 0) -> None:
    source_region = world.multiworld.get_region(source, world.player)
    dest_region = world.multiworld.get_region(destination, world.player)

    entrance_name = source
    randomization_type = EntranceType.ONE_WAY
    if one_way:
        entrance_name += " -> "
    else:
        randomization_type = EntranceType.TWO_WAY
        entrance_name += " <-> "
    entrance_name += destination
    entrance = Entrance(world.player, entrance_name, source_region, randomization_group, randomization_type)

    if rule is not None:
        world.set_rule(entrance, rule)

    source_region.exits.append(entrance)
    entrance.connect(dest_region)
    if not one_way:
        entrance_name = destination + " <-> " + source
        entrance = Entrance(world.player, entrance_name, dest_region, randomization_group, randomization_type)
        if rule is not None:
            world.set_rule(entrance, rule)
        dest_region.exits.append(entrance)
        entrance.connect(source_region)
