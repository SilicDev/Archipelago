
from typing import TYPE_CHECKING, Dict, Set, Tuple

from NetUtils import ClientStatus
from Options import Toggle
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

from .data import DataMaps, ItemNames, LocationNames
from .locations import location_table, red_rings_table, level_clear_table
from .items import item_table, wisp_unlocks_table, emeralds_table, planet_access_table, wisps_table
from .options import Goal


SCDS_RED_RINGS = 0x119BB4
SCDS_SCORES = 0x119BC0
SCDS_ITEMS_RECEIVED = 0x119C0C # actually this is the score for the nega-mother wisp
SCDS_SPECIAL_STAGE_SCORES = 0x119C58
SCDS_AREA_ID = 0x1207C4
SCDS_LEVEL_ID = 0x1207C8
SCDS_LEVEL_RED_RINGS = 0x1208D7
SCDS_GAME_FLAGS = 0x120890 # not 100% sure what this is for, but seems consistent enough for what we need
SCDS_LIFE_COUNTER = 0x1208E6
SCDS_ACTIVE_WISPS = 0x120900
SCDS_TV_BOSS_FLAGS = 0x1279DC # not 100% sure what this is for, but seems consistent enough for what we need
SCDS_TUTORIAL_FLAGS = 0x1279DE # not 100% sure what this is for, but seems consistent enough for what we need

SCDS_COUNTER_POINTER = 0x163D6C
SCDS_COUNTER_BOOST_OFFSET = 0xE8
SCDS_COUNTER_RINGS_OFFSET = 0x18A
SCDS_COUNTER_TOTAL_RINGS_OFFSET = 0x18C
SCDS_COUNTER_STORED_WISP = 0x37C
SCDS_COUNTER_HAS_STORED_WISP = 0x380

SCDS_SONIC_POINTER = 0x19B19C
SCDS_CHAOS_EMERALDS = 0x119B62
SCDS_STORY_COMPLETION = 0x119B64
SCDS_PLANET_AREA_FLAGS = 0x119B68
SCDS_MISSION_UNLOCK_FLAGS = 0x119B6B
SCDS_SPECIAL_STAGE_UNLOCKED = 0x119B8C
SCDS_WISP_ARMOR_DEFEATED_FLAG_MAYBE = 0x137DD8

SCDS_LEVEL_SELECT_TARGET = 0x19BF34
SCDS_TV_BOSS_WISPS = 0x1A00B4 # five 4 byte values
SCDS_LEVEL_SELECT_PREVIEW = 0x1A098A

SCDS_RAM_START = 0x02000000
SCDS_RAM_SIZE = 0x00400000

EU_HASH = "406514E483EE092A89F4298F59FD53A9"
US_HASH = "1996db2bdd78f30082ac003c1bc14a9b"

class SonicColoursDSClient(BizHawkClient):
    game = "Sonic Colours (DS)"
    system = "NDS"
    patch_suffix = ".apscds"

    local_checked_locations: Set[int]
    local_access_items: Set[str]
    local_active_wisps: int
    local_red_rings: int
    local_emeralds: int
    local_junk_items: list[str]
    last_level: int
    last_area: int
    num_items_received: int

    def initialize_client(self) -> None:
        self.local_checked_locations = set()
        self.local_access_items = set()
        self.local_junk_items = []
        self.last_level = -1
        self.last_area = -1
        self.local_active_wisps = 0
        self.local_red_rings = 0
        self.local_emeralds = 0
        self.num_items_received = 0
        pass

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger

        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.005

        self.initialize_client()
        return True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return
        try:
            guards: Dict[str, Tuple[int, bytes, str]] = {}

            local_checked_locations: set[int] = set()
            
            read_result = await bizhawk.read(
                ctx.bizhawk_ctx, 
                [
                    (SCDS_SONIC_POINTER, 4, "Main RAM"),
                    (SCDS_COUNTER_POINTER, 4, "Main RAM"),
                    (SCDS_AREA_ID, 2, "Main RAM"),
                    (SCDS_LEVEL_ID, 2, "Main RAM"),
                    (SCDS_WISP_ARMOR_DEFEATED_FLAG_MAYBE, 4, "Main RAM")
                ])
            
            guards["SONIC"] = (SCDS_SONIC_POINTER, read_result[0], "Main RAM")
            guards["COUNTERS"] = (SCDS_COUNTER_POINTER, read_result[1], "Main RAM")

            guards["AREA"] = (SCDS_AREA_ID, read_result[2], "Main RAM")
            guards["LEVEL"] = (SCDS_LEVEL_ID, read_result[3], "Main RAM")

            sonic = int.from_bytes(guards["SONIC"][1], "little")
            counters = int.from_bytes(guards["COUNTERS"][1], "little")
            area_id = int.from_bytes(guards["AREA"][1], "little")
            level_id = int.from_bytes(guards["LEVEL"][1], "little")
            wisp_armor_defeated_flag = int.from_bytes(read_result[4], "little")
            if level_id == 6 and wisp_armor_defeated_flag == 0x701:
                if ctx.slot_data["goal"] == Goal.option_wisp_armor:
                    if not ctx.finished_game:
                        ctx.finished_game = True
                        await ctx.send_msgs([{
                            "cmd": "StatusUpdate",
                            "status": ClientStatus.CLIENT_GOAL,
                        }])
                elif ctx.slot_data["goal"] == Goal.option_mother_wisp:
                    local_checked_locations.add(location_table[LocationNames.nega_wisp_armor]) # Nega-Wisp Armor

            if counters > (SCDS_RAM_START + SCDS_RAM_SIZE):
                return # assume invalid

            location_prefix = DataMaps.level_id_to_location[level_id]

            if area_id == 0 and counters < SCDS_RAM_START: # Planet Map
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_LEVEL_SELECT_TARGET, 2, "Main RAM")
                    ],
                    [guards["SONIC"], guards["AREA"]])
                if read_result is not None:
                    level_target = int.from_bytes(read_result[0], "little")
                    if level_target < 7:
                        if DataMaps.level_id_to_access_item[level_target] not in self.local_access_items:
                            for i in range(7):
                                if DataMaps.level_id_to_access_item[i] in self.local_access_items:
                                    await bizhawk.guarded_write(
                                        ctx.bizhawk_ctx,
                                        [
                                            (SCDS_LEVEL_SELECT_TARGET, i.to_bytes(2, "little"), "Main RAM"),
                                            (SCDS_LEVEL_SELECT_PREVIEW, i.to_bytes(2, "little"), "Main RAM")
                                    ], [guards["SONIC"], guards["AREA"]])
                                    break
            if area_id != self.last_area:
                self.last_area = area_id
                await ctx.send_msgs([{
                    "cmd": "Bounce",
                    "slots": [ctx.slot],
                    "data": {
                        "type": "MapUpdate",
                        "mapId": self.last_area,
                    },
                }])
            checked_locations = ctx.checked_locations.copy()
            if ctx.slot_data["redringsanity"] == Toggle.option_true:
                red_ring_storage = 0
                for location in checked_locations:
                    location_name = ctx.location_names.lookup_in_game(location)
                    if location_name in red_rings_table.keys():
                        red_ring_storage |= 1 << (location_table[location_name] - location_table[LocationNames.tropical_resort_act_1_red_ring_1])
                if red_ring_storage != self.local_red_rings:
                    await bizhawk.guarded_write(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_RED_RINGS, red_ring_storage.to_bytes(12, "little"), "Main RAM")
                        ], [guards["SONIC"]])
                    self.local_red_rings = red_ring_storage

            await self.handle_received_items(ctx, guards)
            await self.handle_junk_items(ctx, guards)

            read_result = await bizhawk.guarded_read(
                ctx.bizhawk_ctx,
                [
                    (SCDS_STORY_COMPLETION, 3, "Main RAM")
                ],
                [guards["SONIC"], guards["AREA"]])
            if read_result is not None:
                story_completion = int.from_bytes(read_result[0], "little")
                if story_completion < 0x200000: # during hard reset memory read
                    if level_id in DataMaps.level_id_to_emeralds.keys() and counters > SCDS_RAM_START:
                        await bizhawk.guarded_write(
                            ctx.bizhawk_ctx,
                            [
                                (SCDS_CHAOS_EMERALDS, DataMaps.level_id_to_emeralds[level_id].to_bytes(2, "little"), "Main RAM")
                            ], [guards["SONIC"], guards["AREA"]])
                    if ctx.slot_data["goal"] == Goal.option_wisp_armor:
                        if not ctx.finished_game and story_completion >= 0x100000:
                            ctx.finished_game = True
                            await ctx.send_msgs([{
                                "cmd": "StatusUpdate",
                                "status": ClientStatus.CLIENT_GOAL,
                            }])
                        if not ctx.finished_game and story_completion < 0xF0000:
                            await bizhawk.guarded_write(
                                ctx.bizhawk_ctx,
                                [
                                    (SCDS_STORY_COMPLETION, 0xE4455.to_bytes(3, "little"), "Main RAM"),
                                    (SCDS_PLANET_AREA_FLAGS, 0x777777.to_bytes(3, "little"), "Main RAM"),
                                    (SCDS_MISSION_UNLOCK_FLAGS, 0x3FFFF.to_bytes(3, "little"), "Main RAM")
                                ], [guards["SONIC"], guards["AREA"]])
                    if ctx.slot_data["goal"] == Goal.option_mother_wisp:
                        if story_completion >= 0x100000:
                            local_checked_locations.add(location_table[LocationNames.nega_wisp_armor]) # Nega-Wisp Armor
                        if not ctx.finished_game and story_completion >= 0x120000:
                            ctx.finished_game = True
                            await ctx.send_msgs([{
                                "cmd": "StatusUpdate",
                                "status": ClientStatus.CLIENT_GOAL,
                            }])
                        if not ctx.finished_game:
                            if level_id in DataMaps.level_id_to_emeralds.keys() and counters > SCDS_RAM_START:
                                await bizhawk.guarded_write(
                                    ctx.bizhawk_ctx,
                                    [
                                        (SCDS_CHAOS_EMERALDS, DataMaps.level_id_to_emeralds[level_id].to_bytes(2, "little"), "Main RAM")
                                    ], [guards["SONIC"], guards["AREA"]])
                            else:
                                await bizhawk.guarded_write(
                                    ctx.bizhawk_ctx,
                                    [
                                        (SCDS_CHAOS_EMERALDS, self.local_emeralds.to_bytes(2, "little"), "Main RAM")
                                    ], [guards["SONIC"], guards["AREA"]])
                            if self.local_emeralds == 0x7F and ((story_completion > 0xF0000 and story_completion < 0x110000) or 
                                                                (story_completion < 0xF0000 and location_table[LocationNames.nega_wisp_armor] in self.local_checked_locations)):
                                await bizhawk.guarded_write(
                                    ctx.bizhawk_ctx,
                                    [
                                        (SCDS_STORY_COMPLETION, 0x104455.to_bytes(3, "little"), "Main RAM"), # game handles opening mother wisp from here
                                        (SCDS_PLANET_AREA_FLAGS, 0xFFFFFF.to_bytes(3, "little"), "Main RAM"),
                                        (SCDS_MISSION_UNLOCK_FLAGS, 0xFFFFFF.to_bytes(3, "little"), "Main RAM")
                                    ], [guards["SONIC"], guards["AREA"]])
                            elif story_completion < 0xF0000:
                                await bizhawk.guarded_write(
                                    ctx.bizhawk_ctx,
                                    [
                                        (SCDS_STORY_COMPLETION, 0x0E4455.to_bytes(3, "little"), "Main RAM"),
                                        (SCDS_PLANET_AREA_FLAGS, 0x777777.to_bytes(3, "little"), "Main RAM"),
                                        (SCDS_MISSION_UNLOCK_FLAGS, 0x3FFFF.to_bytes(3, "little"), "Main RAM")
                                    ], [guards["SONIC"], guards["AREA"]])
            
            for i in range(7):
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_SPECIAL_STAGE_SCORES + i * 4, 4, "Main RAM")
                    ],
                    [guards["SONIC"], guards["LEVEL"]])
                if read_result is not None:
                    score = int.from_bytes(read_result[0], "little")
                    if score > 0xF: #ignore rank
                        rank = score & 0xF
                        if rank > ctx.slot_data["rankrequirement"]:
                            local_checked_locations.add(location_table["Special Stage " + str(i + 1)])
            if counters > SCDS_RAM_START and ctx.slot_data["redringsanity"] == Toggle.option_true:
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_LEVEL_RED_RINGS, 5, "Main RAM")
                    ],
                    [guards["SONIC"], guards["LEVEL"]])
                if read_result is not None:
                    for ring in range(len(read_result[0])):
                        if read_result[0][ring] == 1:
                            local_checked_locations.add(location_table[location_prefix + " - Red Star Ring " + str(ring + 1)])
            
            for location in checked_locations:
                location_name = ctx.location_names.lookup_in_game(location)
                if (location >= location_table[LocationNames.tropical_resort_act_1] 
                        and location <= location_table[LocationNames.asteroid_coaster_mission_3] 
                        and location_name in level_clear_table.keys()):
                    offset = (location_table[location_name] - location_table[LocationNames.tropical_resort_act_1]) * 4
                    read_result = await bizhawk.guarded_read(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_SCORES + offset, 4, "Main RAM")
                        ],
                        [guards["SONIC"]])
                    if read_result is not None:
                        score = int.from_bytes(read_result[0], "little")
                        if score == 0:
                            score = ctx.slot_data["rankrequirement"] + 1
                            await bizhawk.guarded_write(
                                ctx.bizhawk_ctx,
                                [
                                    (SCDS_SCORES + offset, score.to_bytes(4, "little"), "Main RAM")
                                ], [guards["SONIC"]])
            
            for location in level_clear_table.keys():
                location_code = level_clear_table[location]
                if location_code <= location_table[LocationNames.asteroid_coaster_mission_3]:
                    offset = (location_code - location_table[LocationNames.tropical_resort_act_1]) * 4
                    read_result = await bizhawk.guarded_read(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_SCORES + offset, 4, "Main RAM")
                        ],
                        [guards["SONIC"]])
                    if read_result is not None:
                        score = int.from_bytes(read_result[0], "little")
                        if score > 0xF: #ignore rank
                            rank = score & 0xF
                            if rank > ctx.slot_data["rankrequirement"]:
                                local_checked_locations.add(location_code)
            read_result = await bizhawk.guarded_read(
                ctx.bizhawk_ctx,
                [
                    (SCDS_TUTORIAL_FLAGS, 2, "Main RAM"),
                    (SCDS_GAME_FLAGS, 2, "Main RAM")
                ],
                [guards["SONIC"]])
            if read_result is not None:
                tutorial_flags = int.from_bytes(read_result[0], "little")
                game_flags = int.from_bytes(read_result[1], "little")
                if tutorial_flags == 0x8 and game_flags == 0x10:
                    if level_id == 15: # movement tutorial
                        local_checked_locations.add(location_table[LocationNames.movement_tutorial])
                    else:
                        local_checked_locations.add(location_table[DataMaps.area_id_to_tutorial[area_id]])

            if level_id == 6:
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_TV_BOSS_FLAGS, 2, "Main RAM")
                    ],
                    [guards["SONIC"]])
                if read_result is not None:
                    tv_flags = int.from_bytes(read_result[0], "little")
                    if tv_flags & 0x2 != 0:
                        write_list = []
                        for i in range(5):
                            if self.local_active_wisps & (1 << (i + 1)) == 0:
                                write_list.append((SCDS_TV_BOSS_WISPS + 4 * i, (0).to_bytes(4, "little"), "Main RAM"))
                        if not len(write_list) == 0:
                            await bizhawk.guarded_write(
                                ctx.bizhawk_ctx,
                                write_list,
                                [guards["SONIC"], guards["COUNTERS"]]
                            )
                        local_checked_locations.add(location_table[LocationNames.terminal_velocity_chase])
            if level_id in DataMaps.boss_level_wisps.keys():
                if self.local_active_wisps & DataMaps.boss_level_wisps[level_id] == 0:
                    if level_id == 30:
                        await bizhawk.guarded_write(
                            ctx.bizhawk_ctx,
                            [
                                (SCDS_ACTIVE_WISPS, (0).to_bytes(1, "little"), "Main RAM")
                            ],
                            [guards["SONIC"], guards["COUNTERS"]]
                        )
                    else:
                        await bizhawk.guarded_write(
                            ctx.bizhawk_ctx,
                            [
                                ((counters + SCDS_COUNTER_STORED_WISP), (-1).to_bytes(4, "little", signed=True), "Main RAM")
                            ],
                            [guards["SONIC"], guards["COUNTERS"]]
                        )
            else:
                await bizhawk.guarded_write(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_ACTIVE_WISPS, [self.local_active_wisps], "Main RAM")
                    ], [guards["SONIC"]])
            
            # Send locations
            if local_checked_locations != self.local_checked_locations:
                self.local_checked_locations = local_checked_locations

                if local_checked_locations is not None:
                    await ctx.check_locations(local_checked_locations)
            
        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
        pass

    async def handle_received_items(self, ctx: "BizHawkClientContext", guards: Dict[str, Tuple[int, bytes, str]]) -> None:
        game_num_items_received = 0
        read_result = await bizhawk.guarded_read(
            ctx.bizhawk_ctx,
            [
                (SCDS_ITEMS_RECEIVED, 4, "Main RAM")
            ], [guards["SONIC"]])
        if read_result is not None:
            game_num_items_received = int.from_bytes(read_result[0], "little") >> 4

        if len(ctx.items_received) > self.num_items_received:
            item = ctx.items_received[self.num_items_received]
            item_name = ctx.item_names.lookup_in_game(item.item)
            if item_name in wisp_unlocks_table.keys():
                self.local_active_wisps |= 1 << (item_table[item_name].code - item_table[ItemNames.white_wisp_unlock].code)
            elif item_name in emeralds_table.keys():
                self.local_emeralds |= 1 << (item_table[item_name].code - item_table[ItemNames.green_emerald].code)
            elif item_name in planet_access_table.keys():
                self.local_access_items.add(item_name)
            else:
                self.local_junk_items.append(item_name)
            if game_num_items_received < self.num_items_received:
                await bizhawk.guarded_write(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_ITEMS_RECEIVED, (self.num_items_received << 4).to_bytes(4, "little"), "Main RAM")
                    ], [guards["SONIC"]])
            self.num_items_received += 1

    async def handle_junk_items(self, ctx: "BizHawkClientContext", guards: Dict[str, Tuple[int, bytes, str]]) -> None:
        counters = int.from_bytes(guards["COUNTERS"][1], "little")
        if counters > SCDS_RAM_START and len(self.local_junk_items) > 0:
            counters &= 0xFFFFFF  # DS uses only 3 bytes for addresses in RAM
            item = self.local_junk_items.pop()
            if item in wisps_table.keys():
                level_id = int.from_bytes(guards["LEVEL"][1], "little")
                if item == ItemNames.white_wisp:
                    read_result = await bizhawk.guarded_read(
                        ctx.bizhawk_ctx,
                        [
                            (counters + SCDS_COUNTER_BOOST_OFFSET, 2, "Main RAM")
                        ], [guards["COUNTERS"]])
                    if read_result is not None:
                        boost = int.from_bytes(read_result[0], "little")
                        await bizhawk.guarded_write(
                            ctx.bizhawk_ctx,
                            [
                                (counters + SCDS_COUNTER_BOOST_OFFSET, (boost + 800).to_bytes(2, "little"), "Main RAM")
                            ], [guards["COUNTERS"]])
                        await bizhawk.display_message(ctx.bizhawk_ctx, "You received a White Wisp")
                        return
                elif item in DataMaps.level_id_to_wisps[level_id]:
                    await bizhawk.guarded_write(
                        ctx.bizhawk_ctx,
                        [
                            (counters + SCDS_COUNTER_STORED_WISP, (item_table[item].code - item_table[ItemNames.red_wisp].code).to_bytes(2, "little"), "Main RAM"),
                            (counters + SCDS_COUNTER_HAS_STORED_WISP, (1).to_bytes(2, "little"), "Main RAM")
                        ], [guards["COUNTERS"]])
                    await bizhawk.display_message(ctx.bizhawk_ctx, f"You received a {item}")
                    return
            elif item == ItemNames.extra_life:
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [
                        (SCDS_LIFE_COUNTER, 2, "Main RAM")
                    ], [guards["COUNTERS"]])
                if read_result is not None:
                    life = int.from_bytes(read_result[0], "little")
                    await bizhawk.guarded_write(
                        ctx.bizhawk_ctx,
                        [
                            (SCDS_LIFE_COUNTER, (life + 1).to_bytes(2, "little"), "Main RAM")
                        ], [guards["COUNTERS"]])
                    return
            else:
                rings_added = DataMaps.item_to_rings[item]
                read_result = await bizhawk.guarded_read(
                    ctx.bizhawk_ctx,
                    [
                        (counters + SCDS_COUNTER_RINGS_OFFSET, 2, "Main RAM"),
                        (counters + SCDS_COUNTER_TOTAL_RINGS_OFFSET, 2, "Main RAM")
                    ], [guards["COUNTERS"]])
                if read_result is not None:
                    rings = int.from_bytes(read_result[0], "little")
                    total_rings = int.from_bytes(read_result[1], "little")
                    await bizhawk.guarded_write(
                        ctx.bizhawk_ctx,
                        [
                            (counters + SCDS_COUNTER_RINGS_OFFSET, (rings + rings_added).to_bytes(2, "little"), "Main RAM"),
                            (counters + SCDS_COUNTER_TOTAL_RINGS_OFFSET, (total_rings + rings_added).to_bytes(2, "little"), "Main RAM")
                        ], [guards["COUNTERS"]])
                    await bizhawk.display_message(ctx.bizhawk_ctx, f"You received {item}")
                    return

            # failed to activate, requeue it
            self.local_junk_items.append(item)
        pass

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        if cmd == "Connected":
            self.initialize_client()