import struct

from pymem import pymem

from ..data import ItemNames
from ..items import item_table
from ..locations import location_table
from . import addresses
from .client import YohaneDeepblueContext

RECIPE_PATCH_LOCATION = 0x6a3b6c
RECIPE_PATCH = b"\xe9\x97\xa6\x66\x00"
RECIPE_END_PATCH_LOCATION = 0xd0e200
#     Patch:          ----------------------------------------------------------------
RECIPE_END_PATCH = (b"\x34\x66\x13\x41\x01\x00\x00\x00\x48\x8b\x44\x24\x38\x8b\x58\x2c"
                    b"\x49\xc7\xc0\x18\x00\x00\x00\x48\xc7\xc0\xe6\x00\x00\x00\x4c\x0f"
                    b"\xaf\xc0\x89\xd8\x83\xf8\x40\x7c\x07\x49\x83\xc0\x08\x83\xe8\x40"
                    b"\x51\x88\xc1\xb8\x01\x00\x00\x00\x48\xd3\xe0\x49\x01\xf0\x49\x8b"
                    b"\x08\x48\x09\xc8\x49\x89\x00\x59\x48\x8b\x05\x51\x13\x47\x00\x0f"
                    b"\xaf\x58\x04\x48\x03\x1d\x56\x13\x47\x00\x4c\x8b\x05\x9f\xff\xff"
                    b"\xff\x49\x89\x18\xe9\x1e\x59\x99\xff\xcc\xcc\xcc")

ITEM_NAME_PATCH_LOCATION = 0x93d3e0
ITEM_NAME_PATCH = b"\x48\xe9\xb6\x0e\x3d\x00"
ITEM_NAME_END_PATCH_LOCATION = 0xd0e26c
ITEM_NAME_END_PATCH = (b"\x00\x00\x00\x00\x00\x00\x00\x00\x53\x52\x48\x83\xec\x30\x48\x8b"
                       b"\x05\xeb\xff\xff\xff\x81\xf9\xff\x0f\x00\x00\x7f\x0b\xba\x80\x00"
                       b"\x00\x00\x0f\xaf\xd1\x48\x01\xd0\x48\x83\xc4\x30\x5a\x5b\xc3\xcc"
                       b"\x48\x2b\x0d\x4d\x13\x47\x00\x48\x8b\x05\x36\x13\x47\x00\x8b\x40"
                       b"\x04\x48\x89\xc3\x48\x89\xc8\x48\x31\xd2\x48\xf7\xfb\x48\x89\xc1"
                       b"\xe8\xb3\xff\xff\xff\x48\x8b\x4c\x24\x60\x48\x31\xe1\xe8\x22\xb8"
                       b"\xf6\xff\x48\x8b\x9c\x24\x88\x00\x00\x00\x48\x83\xc4\x70\x5f\xc3")

SAVEFILE_PATCH_1_LOCATION = 0x9b8718
SAVEFILE_PATCH_1 = b"\x48\x8b\x15\x95\x5c\x35\x00"
SAVEFILE_PATCH_2_LOCATION = 0x9b9b61
SAVEFILE_PATCH_2 = b"\x48\x8b\x15\x4c\x48\x35\x00"

ITEMGET_END_PATCH_LOCATION = 0xd0e2dc
ITEMGET_END_PATCH = (b"\x48\x89\xd9\x53\x57\x48\x81\xec\x88\x00\x00\x00\x48\x8b\x05\x11"
                     b"\x52\x42\x00\x48\x31\xe0\x48\x89\x44\x24\x70\x89\xcb\xe8\x76\xff"
                     b"\xff\xff\x0f\x57\xc0\x0f\x11\x44\x24\x30\x66\x0f\x6f\x0d\x42\x66"
                     b"\x25\x00\xf3\x0f\x7f\x4c\x24\x40\xc6\x44\x24\x30\x00\x48\x85\xc0"
                     b"\x74\x16\x49\xc7\xc0\xff\xff\xff\xff\x49\xff\xc0\x42\x80\x3c\x00"
                     b"\x00\x75\xf6\x48\x89\xc2\xeb\x0a\x4d\x31\xc0\x48\x8d\x15\x02\xf9"
                     b"\x13\x00\x48\x8d\x4c\x24\x30\xe8\x18\xd0\x3a\xff\xc7\x44\x24\x54"
                     b"\x01\x00\x00\x00\xc7\x44\x24\x60\x0a\x00\x00\x00\x49\xc7\xc0\x01"
                     b"\x00\x00\x00\x89\xda\x48\x8b\x3d\xb0\xd0\x95\x00\x48\x8d\x8f\x60"
                     b"\x25\x05\x00\xe8\xac\xcc\x76\xff\x48\x8d\x4c\x24\x30\xe8\x82\x05"
                     b"\x3d\xff\x48\x8d\x4c\x24\x30\x48\x83\x7c\x24\x40\x10\x48\x0f\x43"
                     b"\x4c\x24\x30\xe8\xec\xff\x96\xff\x48\x8d\x4c\x24\x30\xe8\x22\xda"
                     b"\x3a\xff\x48\x8b\x4c\x24\x70\x48\x31\xe1\xe8\x45\xb7\xf6\xff\x48"
                     b"\x83\xc4\x68\x5f\x5b\xeb\xfe\xcc")

item_name_table = -1
location_item_name_table = -1
ITEM_NAME_LEN = 0x80
save_game_name = 0xd0e3b4
string_table = -1

def apply_prepatch(ctx: YohaneDeepblueContext, game: pymem.Pymem) -> bool:
    try:
        main_struct = int(game.read_longlong(game.base_address + addresses.MAIN_BASE_OFFSET))
        #game.write_bytes(main_struct + 0x1c00, (0).to_bytes(0x7c00*10, "little"), 0x7c00*10)
        #game.write_bytes(game.base_address + SAVEFILE_PATCH_1_LOCATION, SAVEFILE_PATCH_1, len(SAVEFILE_PATCH_1))
        #game.write_bytes(game.base_address + SAVEFILE_PATCH_2_LOCATION, SAVEFILE_PATCH_2, len(SAVEFILE_PATCH_2))
        #string_table = game.allocate(0x1000)
        #game.write_longlong(game.base_address + save_game_name, string_table)
        #game.write_string(string_table, f"yhnGame%03d_P{ctx.slot}_{ctx.seed_name}")
    except (pymem.exception.MemoryWriteError, pymem.exception.ProcessError) as _:
        return False
    return True

def apply_patches(ctx: YohaneDeepblueContext, game: pymem.Pymem) -> bool:
    #with open("./worlds/yohane_deepblue/test/recipe_dump.bin", "w") as f:
        #recipe_offset = self.game_process.base_address + LAST_RECIPE
        #for i in range(93):
            #result = self.game_process.read_ushort(recipe_offset + (i+1)*0x30 + 0x8)
            #f.write(f"{result}\n")
            #for j in range(4):
                #id = self.game_process.read_ushort(recipe_offset + (i+1)*0x30 + 0x10 + j*8)
                #count = self.game_process.read_ushort(recipe_offset + (i+1)*0x30 + 0x14 + j*8)
                #f.write(f"{id}\t{count}\n")
            #f.write("\n")
    try:
        max_id = sorted([item.code for item in item_table.values() if item.code is not None], reverse=True)[0]
        size = 0x1000
        while size <= max_id:
            size *= 2
        item_name_table = game.allocate(ITEM_NAME_LEN * size)
        for item_name in item_table:
            item = item_table[item_name]
            if item.code is not None:
                game.write_string(item_name_table + item.code * ITEM_NAME_LEN, item_name)
        # Hack to fix the two Fashion for Dummies having different IDs
        game.write_string(item_name_table + 10 * ITEM_NAME_LEN, ItemNames.extra_accessory_slot)
        game.write_string(item_name_table, "---") # Fallback/Empty

        game.write_bytes(game.base_address + ITEM_NAME_PATCH_LOCATION, ITEM_NAME_PATCH, len(ITEM_NAME_PATCH))
        game.write_bytes(game.base_address + ITEM_NAME_END_PATCH_LOCATION,
                         ITEM_NAME_END_PATCH, len(ITEM_NAME_END_PATCH))
        game.write_longlong(game.base_address + ITEM_NAME_END_PATCH_LOCATION, item_name_table)

        game.write_bytes(game.base_address + RECIPE_PATCH_LOCATION, RECIPE_PATCH, len(RECIPE_PATCH))
        game.write_bytes(game.base_address + RECIPE_END_PATCH_LOCATION, RECIPE_END_PATCH, len(RECIPE_END_PATCH))
        game.write_longlong(game.base_address + RECIPE_END_PATCH_LOCATION, game.base_address + addresses.LAST_RECIPE)
        recipe_offset = game.base_address + addresses.LAST_RECIPE
        if ctx.recipesanity:
            for i in range(93):
                ingredients = struct.unpack_from("<hhhh", ctx.recipes, i*8)
                for j in range(len(ingredients)):
                    ingredient = (ingredients[j] & 0x3FF) | ((ingredients[j] & 0xFC00) << (6 + 16))
                    game.write_ulonglong(recipe_offset + (i+1)*0x30 + 0x10 + j*8, ingredient)

        max_id = sorted([location for location in location_table.values() if location is not None], reverse=True)[0]
        size = 0x800
        while size <= max_id:
            size *= 2
        location_item_name_table = game.allocate(ITEM_NAME_LEN * size)

        for item in ctx.location_info_received:
            item_name = ctx.item_names.lookup_in_slot(item.item, item.player)
            if item.player != ctx.slot:
                item_name = f"{ctx.slot_info[item.player].name}'s {item_name}"
            game.write_string(location_item_name_table + item.location * ITEM_NAME_LEN, item_name[:ITEM_NAME_LEN - 1])
            if item.location in range(701, 800):
                if item.player == ctx.slot and item.item < 1000:
                    game.write_int(recipe_offset + (item.location - 700)*0x30 + 0x8, item.item)
                else:
                    game.write_int(recipe_offset + (item.location - 700)*0x30 + 0x8, item.location)
                game.write_string(item_name_table + item.location * ITEM_NAME_LEN,
                                                f"{item.location - 700}) " + item_name[:ITEM_NAME_LEN - 5])
        game.write_bytes(game.base_address + ITEMGET_END_PATCH_LOCATION, ITEMGET_END_PATCH, len(ITEMGET_END_PATCH))
    except (pymem.exception.MemoryWriteError, pymem.exception.ProcessError) as _:
        return False
    return True
