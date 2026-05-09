
import struct
from typing import TYPE_CHECKING

from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes
from settings import get_settings

if TYPE_CHECKING:
    from . import SonicColoursDSWorld

EU_HASH = "406514E483EE092A89F4298F59FD53A9"
US_HASH = "1996db2bdd78f30082ac003c1bc14a9b"
ROM_NAME = b"SONICCOLORS\0"
PATCHED_NAME = b"SONICCLR:AP\0"

class SonicColoursDSProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Sonic Colours DS"
    hash = EU_HASH
    patch_file_ending = ".apscds"
    result_file_ending = ".nds"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        with open(get_settings().sonic_colours_ds_settings.rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes

def write_tokens(world: "SonicColoursDSWorld", patch: SonicColoursDSProcedurePatch) -> None:
    patch.write_token(
        APTokenTypes.WRITE,
        0x0,
        struct.pack("<12s", PATCHED_NAME)
    )
    patch.write_token(
        APTokenTypes.WRITE,
        0x170,
        struct.pack(f"<16s", world.player_name.encode("ascii", "replace"))
    )

    patch.write_token(
        APTokenTypes.WRITE,
        0x200,
        struct.pack("<20s", world.multiworld.seed_name.encode("ascii", "replace"))
    )

    patch.write_file("token_data.bin", patch.get_token_binary())