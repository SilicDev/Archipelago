"""
Option definitions for YOHANE THE PARHELION -BLAZE in the DEEPBLUE-
"""
from dataclasses import dataclass

from Options import (
    Choice,
    DeathLinkMixin,
    DefaultOnToggle,
    FreeText,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    StartInventoryPool,
    Toggle,
    Range
)


class LogicDifficulty(Choice):
    """
    Sets general logic difficulty. Specific skips can be toggled with other settings.

    Easy: No unintended skips are enabled.
    Hard: Various damage boost and similar strats are enabled.
    """
    display_name = "Logic Difficulty"
    option_easy = 0
    option_hard = 2
    default = option_easy

class EarlyChikaBlockMoved(DefaultOnToggle):
    """
    Moves some early Chika blocks to open up the randomizer.
    """
    display_name = "Move Early Chika Blocks"


class EnableYouSkips(DefaultOnToggle):
    """
    If `true` considers using You to fit through 1 tile gaps while in the air in-logic
    """
    display_name = "Enable You Skips"


class ProgressiveCharacterUnlocks(Toggle):
    """
    If `true` places progressive unlocks for characters and upgrades instead of individual ones.

    Example: Two items "Progressive Chika" instead of "Chika" and "Katy's Mask"
    """
    display_name = "Progressive Character Unlocks"


class UpgradeHints(OptionSet):
    """
    The type of hints to create when obtaining a character.

    - Vanilla: Hints what item is at the normal upgrade chest
    - AP: Hints where the upgrade item is located.
    """
    display_name = "Upgrade Hints"
    valid_keys = frozenset({"Vanilla", "AP"})
    default = frozenset({"Vanilla"})

    _option_vanilla = "Vanilla"
    _option_ap = "AP"


class RandomStartingWeapon(Toggle):
    """If `true` replaces the Katar in your starting inventory with a random weapon instead."""
    display_name = "Random Starting Weapon"


class Recipesanity(Toggle):
    """
    If `true` randomizes recipes and adds their normal results to the item pool.

    WARNING: this setting has no logic yet and may result in unbeatable seed.
    """
    display_name = "Recipesanity"


class MaxConsumableIngredientCount(Range):
    """
    If `recipesanity` is enabled, controlls how many of a given consumable can be required for
    a single ingredient.
    """
    range_start = 1
    range_end = 20
    default = 3
    display_name = "Max Consumable Ingredient Count"


class MaxEnemyIngredientCount(Range):
    """
    If `recipesanity` is enabled, controlls how many of a given enemy material can be required for
    a single ingredient.
    """
    range_start = 1
    range_end = 20
    default = 3
    display_name = "Max Enemy Material Ingredient Count"


class MaxBreakableIngredientCount(Range):
    """
    If `recipesanity` is enabled, controlls how many of a given breakable material can be required for
    a single ingredient.
    """
    range_start = 1
    range_end = 20
    default = 5
    display_name = "Max Breakable Material Ingredient Count"


class DeathLinkGroup(FreeText):
    """Death Link only applies to players with an identical Group name.
    Games that don't support the Group option count as having an empty group name."""
    display_name = "Death Link Group"
    rich_text_doc = True


class DamageLink(Toggle):
    """When you take damage, everyone who enabled damage link also takes damage. Of course, the reverse is true too."""
    display_name = "Damage Link"


class DamageLinkGroup(FreeText):
    """Damage Link only applies to players with an identical Group name.
    Games that don't support the Group option count as having an empty group name."""
    display_name = "Damage Link Group"
    rich_text_doc = True


yohane_deepblue_option_groups = [
    OptionGroup("Logic Customization", [
        LogicDifficulty,
        EarlyChikaBlockMoved,
        EnableYouSkips,
    ]),
    OptionGroup("Recipesanity", [
        Recipesanity,
        MaxConsumableIngredientCount,
        MaxEnemyIngredientCount,
        MaxBreakableIngredientCount,
    ]),
]


@dataclass
class DeathLinkGroupMixin(DeathLinkMixin):
    death_link_group: DeathLinkGroup


@dataclass
class DamageLinkMixin:
    damage_link: DamageLink


@dataclass
class DamageLinkGroupMixin(DamageLinkMixin):
    damage_link_group: DamageLinkGroup


@dataclass
class YohaneDeepblueOptions(PerGameCommonOptions, DeathLinkGroupMixin, DamageLinkGroupMixin):
    start_inventory_from_pool: StartInventoryPool

    progressive_character_unlocks: ProgressiveCharacterUnlocks
    upgrade_hints: UpgradeHints
    random_starting_weapon: RandomStartingWeapon

    recipesanity: Recipesanity
    max_consumable_ingredient_count: MaxConsumableIngredientCount
    max_enemy_ingredient_count: MaxEnemyIngredientCount
    max_breakable_ingredient_count: MaxBreakableIngredientCount

    logic_difficulty: LogicDifficulty
    early_chika_blocks_moved: EarlyChikaBlockMoved
    enable_you_skips: EnableYouSkips

