"""
Option definitions for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
"""
import typing
from dataclasses import dataclass

from Options import (
    Choice,
    DeathLinkMixin,
    DefaultOnToggle,
    FreeText,
    OptionError,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    Range,
    Removed,
    StartInventoryPool,
    Toggle,
)


class MainLevelSelection(Choice):
    """
    Sets which main and boss levels are available for the randomizer.

    Mania: all base levels
    Encore: all encore levels (requires DLC)
    All: all levels (requires DLC)
    """
    display_name = "Main Level Selection"
    option_mania = 0
    option_encore = 1
    option_all = 2
    default = option_mania

class SpecialStageSelection(Choice):
    """
    Sets which special stages are available for the randomizer.

    Mania: all base special stages
    Encore: all encore special stages (requires DLC)
    All: all special stages (requires DLC)
    """
    display_name = "Special Stage Selection"
    option_mania = 0
    option_encore = 1
    option_all = 2
    default = option_mania

class BluespheresInLogic(Range):
    """
    Sets how many bluesphere stages have to be beaten.
    """
    range_start = 0
    range_end = 32
    default = 16

sonic_mania_gamma_option_groups = []

@dataclass
class SonicManiaGammaOptions(PerGameCommonOptions, DeathLinkMixin):
    main_level_selection: MainLevelSelection
    special_stage_selection: SpecialStageSelection
    bluespheres_in_logic: BluespheresInLogic
    pass
