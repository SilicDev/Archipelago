from BaseClasses import CollectionState
from rule_builder.rules import (
    CanReachLocation,
    CanReachRegion,
    False_,
    Filtered,
    Has,
    HasAny,
    OptionFilter,
    Or,
    Rule,
    TWorld,
    WrapperRule,
)
from worlds.AutoWorld import World

from .data import ItemNames, LocationNames


def set_rules(world: World) -> None:
    world.set_completion_rule(Has(ItemNames.victory))
    pass
