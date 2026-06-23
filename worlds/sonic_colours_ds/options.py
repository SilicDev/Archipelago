"""
Option definitions for Sonic Colours (DS)
"""
from dataclasses import dataclass

from BaseClasses import PlandoOptions
from Options import (
    Choice,
    OptionError,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    Toggle,
)
from worlds.AutoWorld import World

from .data import DataMaps


class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Nega-Wisp Armor: Beat Eggman at the end of Terminal Velocity (requires all Wisps)
    - Nega-Mother Wisp: Beat the Nega-Mother Wisp after collecting all seven Chaos Emeralds
    """
    display_name = "Goal"
    default = 0
    option_wisp_armor = 0
    option_mother_wisp = 1


class RankRequirement(Choice):
    """
    The rank required to consider a level beaten.
    """
    display_name = "Rank Requirement"
    default = 0
    option_rank_d = 0
    option_rank_c = 1
    option_rank_b = 2
    option_rank_a = 3
    option_rank_s = 4


class StartingPlanets(OptionSet):
    """
    The planets that are accessible from the start.

    Note that Planet Wisp alone will lead to very restrictive starts and generation failures.
    """
    display_name = "Starting Planets"
    valid_keys = frozenset(DataMaps.planet_names_to_unlock.keys())
    default = frozenset({"Tropical Resort"})

    def verify(self, world: type[World], player_name: str, plando_options: PlandoOptions) -> None:
        super().verify(world, player_name, plando_options)
        if len(self.value) == 0:
            raise OptionError("At least one key has to be selected for option StartingPlanets!")


class RedRingSanity(Toggle):
    """
    Collecting a Red Star Ring gives you an item.
    """
    display_name = "Red Ring Sanity"


scds_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
        RankRequirement
    ]),
    OptionGroup("Sanity Options", [
        RedRingSanity
    ])
]


@dataclass
class SonicColoursDSOptions(PerGameCommonOptions):
    goal: Goal
    rankrequirement: RankRequirement

    starting_planets: StartingPlanets

    redringsanity: RedRingSanity
