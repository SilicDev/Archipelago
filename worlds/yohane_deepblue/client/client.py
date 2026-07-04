import asyncio
import ctypes
import enum
import struct
import time
from argparse import Namespace
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, ClassVar

import colorama
from pymem import pymem

import Utils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, handle_url_arg, logger, server_loop
from NetUtils import ClientStatus, NetworkItem
from Options import Toggle
from Utils import gui_enabled

from ..data import DataMaps, ItemNames
from ..items import (
    accessories_table,
    character_upgrade_table,
    equips_set,
    item_table,
    stackables_set,
    unique_accessories_table,
    weapons_table,
    yen_set,
)
from ..items import lookup_id_to_name as item_id_to_name
from ..locations import location_table
from ..locations import lookup_id_to_name as location_id_to_name
from ..options import UpgradeHints
from ..pymem_ex import PymemEX
from . import addresses

if TYPE_CHECKING:
    import kvui  # noqa: F401


class ConnectionStatus(enum.IntEnum):
    NOT_CONNECTED = 1
    CONNECTED = 2


class YohaneDeepblueCommandProcessor(ClientCommandProcessor):
    ctx: "YohaneDeepblueContext"

    def _cmd_patch(self) -> None:
        """
        Manually patch the game.
        """
        if self.ctx.game_process is not None:
            from .patch import apply_patches
            apply_patches(self.ctx, self.ctx.game_process)
            logger.info("Patches applied")
        else:
            logger.warning("Must be connected to the game!")


    def _cmd_debug(self) -> None:
        """
        Toggle debug logging.
        """
        self.ctx.debug_log = not self.ctx.debug_log
        if self.ctx.debug_log:
            logger.info("Enabled debug logging")
        else:
            logger.info("Disabled debug logging")

    def _cmd_deathlink(self):
        """Toggles Deathlink"""
        if self.ctx.stored_data.get("_read_race_mode"):
            self.output("Death Link cannot be toggled manually during a race!")
            return
        if self.ctx.deathlink_enabled:
            self.ctx.deathlink_enabled = False
            self.output("Death Link turned off")
        else:
            self.ctx.deathlink_enabled = True
            self.output("Death Link turned on")

    async def _cmd_deathlink_group(self, group: str = ""):
        """Sets Deathlink group"""
        if self.ctx.stored_data.get("_read_race_mode"):
            self.output("Death Link Group cannot be changed manually during a race!")
            return
        if group != self.ctx.death_link_group:
            await self.ctx.update_death_link_group(group)
            if group == "":
                self.output("Death Link group changed to global default group")
            else:
                self.output(f"Death Link group changed to '{group}'")
        else:
            self.output(f"Already in Death Link group '{group}'")

    def _cmd_damagelink(self):
        """Toggles Damagelink"""
        if self.ctx.stored_data.get("_read_race_mode"):
            self.output("Damage Link cannot be toggled manually during a race!")
            return
        if self.ctx.damagelink_enabled:
            self.ctx.damagelink_enabled = False
            self.output("Damage Link turned off")
        else:
            self.ctx.damagelink_enabled = True
            self.output("Damage Link turned on")

    async def _cmd_damagelink_group(self, group: str = ""):
        """Sets Damagelink group"""
        if self.ctx.stored_data.get("_read_race_mode"):
            self.output("Damage Link Group cannot be changed manually during a race!")
            return
        if group != self.ctx.damage_link_group:
            await self.ctx.update_damage_link_group(group)
            if group == "":
                self.output("Damage Link group changed to global default group")
            else:
                self.output(f"Damage Link group changed to '{group}'")
        else:
            self.output(f"Already in Damage Link group '{group}'")

    def _cmd_gamestatus(self):
        """Print information about the game's status"""
        game_process = "None"
        if self.ctx.game_process is not None:
            game_process = "Found"
        game_connected = "false"
        if self.ctx.game_connected:
            game_connected = "true"
        server_connection = "Not Connected"
        if self.ctx.connection_status == ConnectionStatus.CONNECTED:
            server_connection = "Connected"
        self.output(f"Game: {game_process}, Client connection: {game_connected}, Server: {server_connection}")

    def _cmd_musicalscores(self):
        """Check how many musical scores are currently queued"""
        self.output(f"The client currently has {self.ctx.stored_musical_scores} Musical Score(s) stored.")

    def _cmd_resync(self):
        """Force the client to resend every important item to the game."""
        self.ctx.highest_received_item_index = 0
        self.ctx.local_received_items = {}


class YohaneDeepblueContext(CommonContext):
    game = "YOHANE THE PARHELION -BLAZE in the DEEPBLUE-"
    items_handling = 0b111  # full remote

    client_loop: asyncio.Task[None]

    last_connected_slot: int | None = None

    slot_data: dict[str, Any]

    connection_status: ConnectionStatus = ConnectionStatus.NOT_CONNECTED
    game_connected = False
    game_process: pymem.Pymem | None = None

    highest_processed_item_index: int = 0
    highest_received_item_index: int = 0
    queued_locations: list[int]
    local_received_items: dict[str, int]
    local_accessories_enabled: int = 0
    hinted_quest_flags: int = 0
    location_info_received: list[NetworkItem]
    received_upgrade_locations: list[tuple[int, int]]
    thread: int = -1

    last_map_area = -1
    last_map_room = -1
    in_parlor = False

    stored_musical_scores = 0

    kernel32: pymem.ressources.structure.MODULEINFO | None
    threadstack0: int = -1
    yohane_pointer: int = -1 # the pointer is unstable so we cache it
    last_health: int = 0
    last_max_health: int = 0

    recipes: bytes
    recipesanity: bool = False
    craftsanity: bool = False

    debug_log = not Utils.is_frozen()
    game_patched = False
    valid_slot = True

    deathlink_enabled = False
    can_send_deathlink = False
    death_link_group: str
    """Group to use when participating in DeathLink"""
    damagelink_enabled = False
    can_send_damagelink = False
    damage_link_group: str
    """Group to use when participating in DamageLink"""
    last_damage_link: float = time.time()

    command_processor = YohaneDeepblueCommandProcessor

    def __init__(self, server_address: str | None = None, password: str | None = None) -> None:
        super().__init__(server_address, password)

        self.location_info_received = []
        self.queued_locations = []
        self.local_received_items = {}
        self.received_upgrade_locations = []
        self.slot_data = {}
        self.death_link_group = ""
        self.damage_link_group = ""
        self.kernel32 = None

    async def server_auth(self, password_requested: bool = False) -> None:
        await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game=self.game)

    async def game_watcher(self):
        while not self.exit_event.is_set():
            if self.game_connected and self.connection_status == ConnectionStatus.CONNECTED and self.valid_slot:
                if ((self.deathlink_enabled and f"DeathLink{self.death_link_group}" not in self.tags) or
                        (not self.deathlink_enabled and f"DeathLink{self.death_link_group}" in self.tags)):
                    await self.update_death_link_group(self.death_link_group)
                    await self.update_death_link(self.deathlink_enabled)
                if ((self.damagelink_enabled and f"SharedDamage{self.damage_link_group}" not in self.tags) or
                        (not self.damagelink_enabled and f"SharedDamage{self.damage_link_group}" in self.tags)):
                    await self.update_damage_link_group(self.damage_link_group)
                    await self.update_damage_link(self.damagelink_enabled)

                if self.game_process is None:
                    logger.info("ERROR: Game process was none during main loop! Reconnecting...")
                    self.game_connected = False
                    await asyncio.sleep(1)
                    continue
                try:
                    flags_struct = _resolve_pointer(self, self.get_base_address(addresses.FLAGS_STRUCT_BASE_OFFSET), addresses.PTR_FLAGS_STRUCT)
                    if flags_struct == -1:
                        logger.info("ERROR: Couldn't find flags struct!")
                        await asyncio.sleep(1)
                        continue

                    ingame_time = int(self.game_process.read_uint(flags_struct + addresses.OFFSET_INGAME_TIME))
                    if ingame_time <= 0:
                        await asyncio.sleep(0.1)
                        continue

                    main_struct = self.get_base_address(addresses.MAIN_BASE_OFFSET)
                    if main_struct == -1:
                        logger.info("ERROR: Couldn't find main data struct!")
                        await asyncio.sleep(1)
                        continue
                    save_game = main_struct + addresses.CURRENT_SAVE_OFFSET

                    slot_name = str(self.game_process.read_string(save_game + addresses.SLOT_NAME_OFFSET, 16))
                    if len(slot_name) != 0 and slot_name != self.slot_info[self.slot].name:
                        self.valid_slot = False
                        logger.warning("Savefile slot name doesn't match slot name! Restart the client to retry")
                        continue
                    seed_name = str(self.game_process.read_string(save_game + addresses.SEED_NAME_OFFSET, addresses.ITEM_STRUCT_SIZE*2))
                    if len(seed_name) != 0 and seed_name != self.seed_name[:addresses.ITEM_STRUCT_SIZE*2]:
                        self.valid_slot = False
                        logger.warning("Savefile seed name doesn't match seed name! Restart the client to retry")
                        continue
                    game_progression_flags = int(self.game_process.read_ushort(save_game + addresses.GAME_PROGRESSION_FLAGS_OFFSET))
                    if len(slot_name) == 0 and len(seed_name) == 0:
                        if game_progression_flags <= 6:
                            self.game_process.write_string(save_game + addresses.SLOT_NAME_OFFSET, self.slot_info[self.slot].name)
                            self.game_process.write_string(save_game + addresses.SEED_NAME_OFFSET, self.seed_name[:addresses.ITEM_STRUCT_SIZE*2])
                        else:
                            self.valid_slot = False
                            logger.warning("Loaded non-empty save! Restart the client to retry")
                            continue

                    if not self.game_patched:
                        self.patch_game()

                    is_dead = self.game_process.read_uchar(flags_struct + addresses.OFFSET_IS_DEAD)
                    if self.deathlink_enabled:
                        if not is_dead and not self.can_send_deathlink:
                            self.can_send_deathlink = True
                        elif is_dead and self.can_send_deathlink:
                            await self.send_death()
                            self.can_send_deathlink = False

                    threadstack = self.get_threadstack0()
                    if threadstack is not None:
                        self.threadstack0 = threadstack
                    await self.detect_damage(self.game_process)

                    map_area = int(self.game_process.read_uchar(save_game + addresses.MAP_AREA_OFFSET))
                    map_room = int(self.game_process.read_uchar(save_game + addresses.MAP_ROOM_OFFSET))
                    await self.handle_map_update(map_area, map_room)
                    game_flags = int(self.game_process.read_uchar(save_game + addresses.GAME_FLAGS_OFFSET))
                    in_parlor = game_flags & 0x8 != 0
                    if in_parlor != self.in_parlor:
                        if in_parlor:
                            logger.info("Yohane safely arrived in her Fortune Parlor")
                        self.in_parlor = in_parlor

                    dungeon_flags = int(self.game_process.read_uchar(save_game + addresses.DUNGEON_FLAGS_OFFSET))
                    if self.slot_data["early_chika_blocks_moved"] == Toggle.option_true and dungeon_flags & 0x2 == 0:
                        if self.debug_log:
                            logger.info("Setting Chika Block flags")
                        dungeon_flags |= 0x2
                        self.game_process.write_uchar(save_game + addresses.DUNGEON_FLAGS_OFFSET, dungeon_flags)

                    for location in DataMaps.character_rescue_flag_map:
                        if location_table[location] in self.checked_locations:
                            game_progression_flags |= DataMaps.character_rescue_flag_map[location]
                        elif game_progression_flags & DataMaps.character_rescue_flag_map[location] != 0:
                            self.queued_locations.append(location_table[location])
                    game_progression_flags &= 0x7FFF
                    if (map_area == 1 and map_room in [9, 10] and ItemNames.boss_token in self.local_received_items and
                            self.local_received_items[ItemNames.boss_token] >= 8):
                        game_progression_flags |= 0x8000 # Spawns Infernal Altar cutscene
                    self.game_process.write_ushort(save_game + addresses.GAME_PROGRESSION_FLAGS_OFFSET, game_progression_flags)

                    boss_defeated_flags = int(self.game_process.read_uint(save_game + addresses.BOSS_DEFEATED_FLAGS))
                    for location in DataMaps.boss_defeated_flag_map:
                        if location_table[location] in self.checked_locations:
                            continue
                        if boss_defeated_flags & DataMaps.boss_defeated_flag_map[location] != 0:
                            self.queued_locations.append(location_table[location])

                    await self.handle_characters(self.game_process, save_game)

                    self.handle_character_upgrades(self.game_process, save_game, map_area, map_room)

                    self.handle_unique_accessories(self.game_process, save_game)

                    self.handle_chest_locations(self.game_process, save_game)

                    recipes = int.from_bytes(self.game_process.read_bytes(save_game + addresses.RECIPE_CRAFTED_OFFSET, 12), "little")
                    for i in range(93):
                        if 1 << (i + 1) & recipes != 0:
                            self.queued_locations.append(701+i)

                    while self.queued_locations:
                        location = self.queued_locations.pop(0)
                        self.locations_checked.add(location)
                        await self.check_locations({location})

                    stored_musical_scores_addr = save_game + addresses.STORED_MUSICAL_SCORE_COUNTER_OFFSET + addresses.ITEM_COUNT_OFFSET
                    self.stored_musical_scores = int(self.game_process.read_uchar(stored_musical_scores_addr))
                    inventory_musical_score_addr = save_game + addresses.MUSICAL_SCORES_INVENTORY_OFFSET + addresses.ITEM_COUNT_OFFSET
                    musical_scores = int(self.game_process.read_uchar(inventory_musical_score_addr))
                    if musical_scores == 0 and self.stored_musical_scores > 0:
                        self.game_process.write_uchar(inventory_musical_score_addr, 1)
                        self.stored_musical_scores -= 1

                    self.handle_items_received(self.game_process, save_game)

                    self.handle_remotely_cleared_locations(self.game_process, save_game,
                                                     game_progression_flags, boss_defeated_flags)

                    in_credits = self.game_process.read_uchar(flags_struct + addresses.OFFSET_IN_CREDITS)
                    if (in_credits != 0 or game_flags & 0x1 != 0) and not self.finished_game:
                        await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                        self.finished_game = True
                except (pymem.exception.MemoryReadError, pymem.exception.ProcessError) as me:
                    self.game_connected = False
                    if self.debug_log:
                        logger.exception(me)
                except Exception as e:
                    self.game_connected = False
                    logger.exception(e)
                    logger.error("Unexpected client error!\nThis may be due to a host and client APWorld version mismatch.")
                    await asyncio.sleep(5)
                pass # game specific logic
            elif ((not self.game_connected or self.game_process is None)
                  and self.connection_status == ConnectionStatus.CONNECTED):
                logger.info("Connection to the game lost!")
                # connect game
                self.game_process = None
                while ((not self.game_connected or self.game_process is None)
                       and self.connection_status == ConnectionStatus.CONNECTED):
                    try:
                        self.game_process = PymemEX(process_name="game.exe", exact_match=True)
                        if self.game_process is not None:
                            self.game_patched = False
                            self.game_connected = True
                            logger.info("Reconnected!")
                    except Exception as _:
                        await asyncio.sleep(1)
                pass
            else:
                # server disconnected?
                pass

            await asyncio.sleep(0.1)


    async def handle_characters(self, game: pymem.Pymem, save_game: int):
        character_quest_flags = int(game.read_uint(save_game + addresses.CHARACTER_QUEST_FLAGS_OFFSET))
        for location in DataMaps.character_quest_flag_map:
            if location_table[location] in self.checked_locations:
                continue
            flag = DataMaps.character_quest_flag_map[location]
            if character_quest_flags & flag != 0 and self.hinted_quest_flags & flag == 0:
                self.hinted_quest_flags |= flag
                if UpgradeHints._option_vanilla in self.slot_data["upgrade_hints"]:
                    await self.send_msgs([{"cmd": "CreateHints", "locations": [location_table[location]]}])
                if UpgradeHints._option_ap in self.slot_data["upgrade_hints"]:
                    item = DataMaps.chest_data_map[location].vanilla_item
                    if item not in self.local_received_items:
                        real_locations = self.slot_data["upgrades"][item_table[item].code - 1]
                        for real_location in real_locations:
                            if real_location[1] is not None:
                                found = False
                                for upgrade_location in self.received_upgrade_locations:
                                    if (real_location[0] == upgrade_location[0] and
                                        real_location[1] == upgrade_location[1]):
                                        found = True
                                        break
                                if not found:
                                    await self.send_msgs([{
                                                    "cmd": "CreateHints",
                                                    "player": real_location[0],
                                                    "locations": [real_location[1]]
                                                }])
        character_quest_flags &= 0xDB6DB6FF # Disable collection flags

        character_unlock_flags = int(game.read_uint(save_game + addresses.CHARACTER_UNLOCK_FLAGS_OFFSET))
        character_unlock_flags &= 0xFFD5555F
        for item in DataMaps.character_item_flags_map:
            flag = DataMaps.character_item_flags_map[item]
            if item in self.local_received_items:
                character_unlock_flags |= flag
                if item in DataMaps.character_item_to_quest_map.keys():
                    character_quest_flags |= DataMaps.character_item_to_quest_map[item]
            if character_unlock_flags & (flag << 1) != 0:
                upgrade = DataMaps.character_to_upgrade_map[item]
                if upgrade is not None:
                    self.queued_locations.append(location_table[DataMaps.upgrade_item_to_quest_location_map[upgrade]])

        game.write_uint(save_game + addresses.CHARACTER_UNLOCK_FLAGS_OFFSET, character_unlock_flags)
        game.write_uint(save_game + addresses.CHARACTER_QUEST_FLAGS_OFFSET, character_quest_flags)


    def handle_character_upgrades(self, game: pymem.Pymem, save_game: int, map_area: int, map_room: int):
        for item in character_upgrade_table.keys():
            item_data = character_upgrade_table[item]
            if item_data.code is not None: # events aren't real
                offset = addresses.INVENTORY_OFFSET + (addresses.ITEM_STRUCT_SIZE * item_data.code)
                room = DataMaps.character_upgrade_to_area_room[item]
                if (item in self.local_received_items and
                                (not (room[0] == map_area and map_room in room[1]) or
                                    location_table[room[2]] in self.checked_locations)):
                    game.write_uchar(save_game + offset + addresses.ITEM_COUNT_OFFSET, 1)
                else:
                    game.write_uchar(save_game + offset + addresses.ITEM_COUNT_OFFSET, 0)


    def handle_unique_accessories(self, game: pymem.Pymem, save_game: int):
        for item in unique_accessories_table.keys():
            item_data = unique_accessories_table[item]
            if item_data.code is not None: # events aren't real
                offset = addresses.INVENTORY_OFFSET + (addresses.ITEM_STRUCT_SIZE * item_data.code)
                addr = save_game + offset + addresses.ITEM_COUNT_OFFSET
                if item in self.local_received_items:
                    game.write_uchar(addr, 1)
                    if item == ItemNames.extra_accessory_slot:
                        if self.local_received_items[item] > 1:
                            game.write_uchar(addr + addresses.ITEM_STRUCT_SIZE, 1)
                        else:
                            game.write_uchar(addr + addresses.ITEM_STRUCT_SIZE, 0)
                else:
                    game.write_uchar(addr, 0)
                    if item == ItemNames.extra_accessory_slot:
                        game.write_uchar(addr + addresses.ITEM_STRUCT_SIZE, 0)


    def handle_chest_locations(self, game: pymem.Pymem, save_game: int):
        cache: dict[int, int] = {}
        for location in DataMaps.chest_data_map.keys():
            if location_table[location] in self.checked_locations:
                continue
            data = DataMaps.chest_data_map[location]
            value = 0
            if data.offset in cache:
                value = cache[data.offset]
            else:
                value = int(game.read_uchar(save_game + data.offset))
                cache[data.offset] = value
            if value & data.mask != 0:
                self.queued_locations.append(location_table[location])
                vanilla_item_code = item_table[data.vanilla_item].code
                if data.vanilla_item in stackables_set and vanilla_item_code is not None:
                    item_offset = addresses.INVENTORY_OFFSET + (addresses.ITEM_STRUCT_SIZE * vanilla_item_code)
                    item_count = int(game.read_uchar(save_game + item_offset + addresses.ITEM_COUNT_OFFSET))
                    if item_count != 0:
                        item_count -= 1
                    game.write_uchar(save_game + item_offset + addresses.ITEM_COUNT_OFFSET, item_count)
                    game.write_ushort(save_game + item_offset, item_count << 8 + item_count)
            if location in DataMaps.important_item_chests:
                addr = save_game + addresses.EQUIPPED_ABILITIES_FLAGS_OFFSET
                accessories_enabled = int(game.read_uchar(addr))
                accessories_enabled &= (0xF8 | self.local_accessories_enabled)
                game.write_uchar(addr, accessories_enabled)


    async def detect_damage(self, game: pymem.Pymem):
        if self.threadstack0 >= 0:
            try:
                self.yohane_pointer = _resolve_pointer(self, self.threadstack0, addresses.YOHANE_PTR)
            except Exception: # threadstack doesn't always point to this
                            #logger.info(e)
                pass
        if self.yohane_pointer >= 0:
            try:
                health = int(game.read_ulong(self.yohane_pointer + addresses.CURRENT_HP_OFFSET))
                max_health = int(game.read_ulong(self.yohane_pointer + addresses.MAX_HP_OFFSET))
                if self.damagelink_enabled:
                    if (health < self.last_health and max_health == self.last_max_health and
                                        self.can_send_damagelink):
                        await self.send_damage(self.last_health - health)
                        self.can_send_damagelink = False
                    else:
                        self.can_send_damagelink = True
                    self.last_health = health
                    self.last_max_health = max_health
            except Exception:
                pass


    def handle_items_received(self, game: pymem.Pymem, save_game: int):
        received_items_addr = save_game + addresses.RECEIVED_ITEMS_COUNTER_OFFSET + addresses.ITEM_COUNT_OFFSET
        self.highest_processed_item_index = int(game.read_uint(received_items_addr))

        new_items = self.items_received[self.highest_received_item_index :]
        for item in new_items:
            new_item = self.highest_received_item_index >= self.highest_processed_item_index
            if new_item:
                self.highest_processed_item_index += 1
            self.highest_received_item_index += 1

            item_name = item_id_to_name[item.item]
            if item_name not in self.local_received_items.keys():
                self.local_received_items[item_name] = 1
            else:
                self.local_received_items[item_name] += 1
            if item_name in DataMaps.progressive_to_character_item_map:
                self.received_upgrade_locations.append((item.player, item.location))
                items = DataMaps.progressive_to_character_item_map[item_name]
                if self.local_received_items[item_name] > 0:
                    self.local_received_items[items[0]] = 1
                if self.local_received_items[item_name] > 1:
                    self.local_received_items[items[1]] = 1

            if item.location in range(701, 800) and item.item < 1000:
                if item_name == ItemNames.musical_score:
                    self.stored_musical_scores += 1

                new_item = False # local crafting, no real item

            # receive item
            if new_item:
                self.thread = self.start_thread(game.base_address + addresses.AP_ADDITEM_FUNC, item.item)
                if item_name == ItemNames.musical_score:
                    self.stored_musical_scores += 1
                elif item_name in stackables_set:
                    if item_name in accessories_table.keys():
                        slots = 1
                        if ItemNames.extra_accessory_slot in self.local_received_items:
                            slots += self.local_received_items[ItemNames.extra_accessory_slot]
                        for i in range(min(slots, 3)):
                            accessory = int(game.read_ushort(save_game + addresses.EQUIPPED_ABILITIES_FLAGS_OFFSET + 8 + (i*4)))
                            if accessory == 0:
                                game.write_ushort(save_game + addresses.EQUIPPED_ABILITIES_FLAGS_OFFSET + 8 + (i*4), item.item)
                                break
                elif item_name in yen_set:
                    amount = 0
                    match (item_name):
                        case ItemNames.small_yen:
                            amount = 10000
                        case ItemNames.medium_yen:
                            amount = 25000
                        case ItemNames.big_yen:
                            amount = 50000
                        case _:
                            raise ValueError(f"Unknown yen item '{item_name}' received!")
                    yen = int(game.read_uint(save_game + addresses.YEN_OFFSET))
                    yen += amount
                    game.write_uint(save_game + addresses.YEN_OFFSET, yen)
                    #self.thread = game.start_thread(game.base_address + addresses.DISPLAY_YEN_MESSAGE_FUNC, amount)

            if item_name in weapons_table.keys():
                weapon = int(game.read_ushort(save_game + addresses.EQUIPPED_ABILITIES_FLAGS_OFFSET + 4))
                if weapon == 0:
                    game.write_ushort(save_game + addresses.EQUIPPED_ABILITIES_FLAGS_OFFSET + 4, item.item)


            accessories_changed = 0
            if item_name == ItemNames.fallen_angels_soarshoes:
                accessories_changed |= 0x01
            elif item_name == ItemNames.gloves_of_might:
                accessories_changed |= 0x02
            elif item_name == ItemNames.sea_deitys_charm:
                accessories_changed |= 0x04
            if accessories_changed != 0:
                accessories_enabled = int(game.read_uchar(save_game + addresses.EQUIPPED_ABILITIES_FLAGS_OFFSET))
                accessories_enabled &= (0xFF ^ accessories_changed)
                self.local_accessories_enabled |= accessories_changed
                game.write_uchar(save_game + addresses.EQUIPPED_ABILITIES_FLAGS_OFFSET,
                                                           accessories_enabled | accessories_changed)
        game.write_uint(save_game + addresses.RECEIVED_ITEMS_COUNTER_OFFSET + addresses.ITEM_COUNT_OFFSET,
                                                 self.highest_processed_item_index)
        game.write_uchar(save_game + addresses.STORED_MUSICAL_SCORE_COUNTER_OFFSET + addresses.ITEM_COUNT_OFFSET,
                                                  self.stored_musical_scores)


    def handle_remotely_cleared_locations(self, game: pymem.Pymem, save_game: int,
                                                game_progression_flags: int, boss_defeated_flags: int):
        for new_remotely_cleared_location in self.checked_locations - self.locations_checked:
                        # other game collected item, clear location
            location_name = location_id_to_name[new_remotely_cleared_location]
            if location_name in DataMaps.chest_data_map.keys():
                data = DataMaps.chest_data_map[location_name]
                value = int(game.read_uchar(save_game + data.offset))
                value |= data.mask
                game.write_uchar(save_game + data.offset, value)
            elif location_name in DataMaps.character_rescue_flag_map.keys():
                flag = DataMaps.character_rescue_flag_map[location_name]
                game_progression_flags |= flag
                game.write_ushort(save_game + addresses.GAME_PROGRESSION_FLAGS_OFFSET,
                                                           game_progression_flags)
            elif location_name in DataMaps.boss_defeated_flag_map.keys():
                flag = DataMaps.boss_defeated_flag_map[location_name]
                boss_defeated_flags |= flag
                game.write_uint(save_game + addresses.BOSS_DEFEATED_FLAGS, boss_defeated_flags)
            elif new_remotely_cleared_location in range(701, 800):
                offset = addresses.INVENTORY_OFFSET + (addresses.ITEM_STRUCT_SIZE * new_remotely_cleared_location)
                game.write_uchar(save_game + offset + addresses.ITEM_COUNT_OFFSET, 1)
                game.write_uchar(save_game + offset + addresses.ITEM_NEW_OFFSET, 0)
                game.write_ushort(save_game + offset, 1 << 8 + 1)
                offset = save_game + addresses.RECIPE_CRAFTED_OFFSET
                recipes = int.from_bytes(game.read_bytes(offset, 12), "little")
                recipes |= 1 << (new_remotely_cleared_location - 700)
                game.write_bytes(offset, recipes.to_bytes(12, "little"), 12)
            self.locations_checked.add(new_remotely_cleared_location)
            pass


    async def handle_map_update(self, map_area: int, map_room: int):
        if self.last_map_area != map_area or self.last_map_room != map_room:
            if self.debug_log:
                logger.info("Entering room %d in area %d", map_room, map_area)
            if self.last_map_area != map_area:
                await self.send_msgs([{ # Update package for trackers
                                "cmd": "Bounce",
                                "slots": [self.slot],
                                "data": {
                                    "type": "MapUpdate",
                                    "mapId": map_area,
                                },
                            }])
            self.last_map_area = map_area
            self.last_map_room = map_room


    def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "Connected":
            if self.last_connected_slot is not None and self.last_connected_slot != self.slot:
                self.valid_slot = False
                logger.warning("Connected to a different slot than last, aborting! Restart the client to retry")
                return

            self.last_connected_slot = self.slot

            self.connection_status = ConnectionStatus.NOT_CONNECTED

            self.slot_data = args["slot_data"]
            self.highest_received_item_index = 0
            self.local_received_items = {}
            self.hinted_quest_flags = 0
            #self.locations_checked = set(args["checked_locations"])
            self.deathlink_enabled = self.slot_data.get("death_link", False)
            self.death_link_group = self.slot_data.get("death_link_group", "")
            self.damagelink_enabled = self.slot_data.get("damage_link", False)
            self.damage_link_group = self.slot_data.get("damage_link_group", "")
            self.recipesanity = self.slot_data.get("recipesanity", False)
            self.craftsanity = self.slot_data.get("craftsanity", False)
            self.recipes = bytes.fromhex(self.slot_data.get("recipes", ""))
            location_scouts = []
            if self.craftsanity:
                location_scouts.extend(set(range(701, 794)))
            if len(location_scouts) != 0:
                Utils.async_start(self.send_msgs([{
                        "cmd": "LocationScouts",
                        "locations": location_scouts
                }]))
                self.locations_scouted.update(location_scouts)

            self.valid_slot = True
            self.connection_status = ConnectionStatus.CONNECTED
            self.connect_to_game()
        elif cmd == "Bounced":
            tags = args.get("tags", [])
            # we can skip checking "DeathLink" in ctx.tags, as otherwise we wouldn't have been send this
            if f"DeathLink{self.death_link_group}" in tags and self.last_death_link != args["data"]["time"]:
                self.on_deathlink(args["data"])
            # we can skip checking "SharedDamage" in ctx.tags, as otherwise we wouldn't have been send this
            if f"SharedDamage{self.damage_link_group}" in tags and self.last_damage_link != args["data"]["time"]:
                self.on_damagelink(args["data"])
        elif cmd == "LocationInfo":
            self.location_info_received = args["locations"]
        elif cmd == "RoomInfo":
            if self.seed_name is None:
                self.seed_name = args["seed_name"]
            elif self.seed_name != args["seed_name"]:
                self.valid_slot = False
                logger.warning("Connected to a different seed than last, aborting! Restart the client to retry")


    async def send_death(self, death_text: str = ""):
        """Helper function to send a deathlink using death_text as the unique death cause string."""
        if self.server and self.server.socket:
            logger.info("DeathLink: Sending death to your friends...")
            self.last_death_link = time.time()
            await self.send_msgs([{
                "cmd": "Bounce", "tags": [f"DeathLink{self.death_link_group}"],
                "data": {
                    "time": self.last_death_link,
                    "source": self.player_names[self.slot],
                    "cause": death_text
                }
            }])

    async def update_death_link(self, death_link: bool):
        """Helper function to set Death Link connection tag on/off and update the connection if already connected."""
        old_tags = self.tags.copy()
        if death_link:
            self.tags.add(f"DeathLink{self.death_link_group}")
        else:
            self.tags -= {f"DeathLink{self.death_link_group}"}
        if old_tags != self.tags and self.server and not self.server.socket.closed:
            await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])

    async def update_death_link_group(self, group_name: str):
        """Helper function to change the Death Link group, updating the connection tag as needed if already connected."""
        death_link: bool = f"DeathLink{self.death_link_group}" in self.tags
        if death_link:
            self.tags -= {f"DeathLink{self.death_link_group}"}
        self.death_link_group = group_name
        if death_link:
            self.tags.add(f"DeathLink{self.death_link_group}")
            if self.server and not self.server.socket.closed:
                await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])

    def on_deathlink(self, data: dict[str, Any]) -> None:
        if self.game_process is not None:
            _text = data.get("cause", "") # for ingame display
            flags_struct = _resolve_pointer(self, self.get_base_address(addresses.FLAGS_STRUCT_BASE_OFFSET), addresses.PTR_FLAGS_STRUCT)
            self.game_process.write_uchar(flags_struct + addresses.OFFSET_IS_DEAD, 1)
            self.game_process.write_uchar(flags_struct + addresses.OFFSET_AREA_RELOAD, 1)
            self.can_send_deathlink = False
        return super().on_deathlink(data)

    async def send_damage(self, damage: int, damage_text: str = ""):
        """Helper function to send a damagelink using damage_text as the unique damage cause string."""
        if self.server and self.server.socket:
            logger.info(f"DamageLink: Sending {damage} damage to your friends...")
            self.last_damage_link = time.time()
            await self.send_msgs([{
                "cmd": "Bounce", "tags": [f"SharedDamage{self.damage_link_group}"],
                "data": {
                    "time": time.time(),
                    "uuid": Utils.get_unique_identifier(),
                    "source": self.player_names[self.slot],
                    "damage_points": damage,
                    "cause": damage_text
                },
            }])

    async def update_damage_link(self, damage_link: bool):
        """Helper function to set Damage Link connection tag on/off and update the connection if already connected."""
        old_tags = self.tags.copy()
        if damage_link:
            self.tags.add(f"SharedDamage{self.damage_link_group}")
        else:
            self.tags -= {f"SharedDamage{self.damage_link_group}"}
        if old_tags != self.tags and self.server and not self.server.socket.closed:
            await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])

    async def update_damage_link_group(self, group_name: str):
        """Helper function to change the Damage Link group, updating the connection tag as needed if already connected."""
        damage_link: bool = f"SharedDamage{self.damage_link_group}" in self.tags
        if damage_link:
            self.tags -= {f"SharedDamage{self.damage_link_group}"}
        self.damage_link_group = group_name
        if damage_link:
            self.tags.add(f"SharedDamage{self.damage_link_group}")
            if self.server and not self.server.socket.closed:
                await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])

    def on_damagelink(self, data: dict[str, Any]) -> None:
        if self.game_process is not None:
            _text = data.get("cause", "") # for ingame display
            damage = data.get("damage_points", 0)
            try:
                health = int(self.game_process.read_ulong(self.yohane_pointer + addresses.CURRENT_HP_OFFSET))
                health = max(0, health - damage)
                self.game_process.write_ulong(self.yohane_pointer + addresses.CURRENT_HP_OFFSET, health)
                self.can_send_damagelink = False
            except (pymem.exception.MemoryReadError, pymem.exception.ProcessError) as me:
                pass

    async def disconnect(self, *args: Any, **kwargs: Any) -> None:
        self.game_connected = False
        self.locations_checked = set()
        self.connection_status = ConnectionStatus.NOT_CONNECTED
        await super().disconnect(*args, **kwargs)

    async def connection_closed(self):
        self.game_connected = False
        self.locations_checked = set()
        self.connection_status = ConnectionStatus.NOT_CONNECTED
        return await super().connection_closed()

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class YohaneDeepblueManager(GameManager):
            logging_pairs: ClassVar[list[tuple[str, str]]] = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Yohane BiD Client"

        self.ui = YohaneDeepblueManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def connect_to_game(self) -> None:
        try:
            self.game_process = PymemEX(process_name="game.exe", exact_match=True)
            if self.game_process is not None:
                self.game_patched = False
                self.game_connected = True
                logger.info("Successfully connected to %s.", self.game)
        except Exception as _:
            if self.game_connected:
                self.game_connected = False
            logger.info("%s is not open. If it is open run the launcher/client as admin.", self.game)
        pass

    def patch_game(self) -> None:
        if self.game_process is not None and self.valid_slot:
            from .patch import apply_patches
            self.game_patched = apply_patches(self, self.game_process)


    def get_base_address(self, base_offset: int) -> int:
        if not self.game_connected or self.game_process is None:
            raise Exception("Must be connected to the game!")
        return _read_address(self, self.game_process.base_address + base_offset)


    def get_threadstack0(self) -> int | None:
        if not self.game_connected or self.game_process is None:
            raise Exception("Must be connected to the game!")
        if self.kernel32 is None:
            self.kernel32 = pymem.process.module_from_name(self.game_process.process_handle, "kernel32.dll")
        if self.kernel32 is not None:
            try:
                main_thread = self.game_process.main_thread
                for i in range(main_thread._query_teb().NtTib.StackBase - 8,
                                           main_thread._query_teb().NtTib.StackLimit, -8):
                    try:
                        value = int(self.game_process.read_ulonglong(i))
                        if (value > self.kernel32.lpBaseOfDll and
                                            value < self.kernel32.lpBaseOfDll + self.kernel32.SizeOfImage):
                            return i
                            break
                    except Exception:
                        return None
            except Exception:
                #logger.info(e)
                return None
        return None

    def start_thread(self, address:int, params: int|None) -> int:
        if self.game_process is None:
            return -1
        if self.thread != -1:
            pymem.ressources.kernel32.CloseHandle(self.thread)
        params = params or 0
        NULL_SECURITY_ATTRIBUTES = ctypes.cast(0, pymem.ressources.structure.LPSECURITY_ATTRIBUTES)
        thread_h = pymem.ressources.kernel32.CreateRemoteThread(
            self.game_process.process_handle,
            NULL_SECURITY_ATTRIBUTES,
            0,
            address,
            params,
            0,
            ctypes.byref(ctypes.c_ulong(0))
        )
        last_error = ctypes.windll.kernel32.GetLastError()
        if last_error:
            pymem.logger.warning(f"Got an error in start thread, code: {last_error}")
        return thread_h


def launch_client(*args: Sequence[str]) -> None:
    parser = get_base_parser(description="Yohane BiD Client")
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    launch_args = handle_url_arg(parser.parse_args(args))

    colorama.just_fix_windows_console()

    asyncio.run(main(launch_args))
    colorama.deinit()


async def main(args: Namespace) -> None:
    ctx = YohaneDeepblueContext(args.connect, args.password)
    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    ctx.client_loop = asyncio.create_task(ctx.game_watcher(), name="Client Loop")

    await ctx.exit_event.wait()
    await ctx.shutdown()

def _read_address(ctx: YohaneDeepblueContext, address: int) -> int:
    if not ctx.game_connected or ctx.game_process is None:
        raise Exception("Must be connected to the game!")
    result = ctx.game_process.read_ctype(address, ctypes.c_void_p())
    if result is None:
        raise Exception("Must be connected to the game!")
    return int(result)

def _resolve_pointer(ctx: YohaneDeepblueContext, base_address: int, pointer: list[int]) -> int:
    if not ctx.game_connected or ctx.game_process is None:
        raise Exception("Must be connected to the game!")
    address = base_address
    for offset in pointer:
        try:
            address = _read_address(ctx, address + offset)
        except Exception:
            return -1
    return address

