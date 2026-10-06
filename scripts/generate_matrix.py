import json
from pathlib import Path

# === CONFIGURATION ===
board = "nice_nano//zmk"
# automatically find all *.keymap filenames under ../config/keymap
keymap_dir = Path(__file__).parent.parent / "config" / "keymap"
keymaps = sorted(p.stem for p in keymap_dir.glob("*.keymap"))

# Map each format to the shields it should build
format_shields = {
    "bt": ["charybdis_left", "charybdis_right"],
    "dongle": ["charybdis_left", "charybdis_right", "charybdis_dongle"],
    "left_debug": ["charybdis_left"],
    "reset": ["settings_reset"],
}

# Which boards/shields/<dir> holds the overlays for each format.
format_shield_dir = {
    "bt": "charybdis_bt",
    "dongle": "charybdis_dongle",
    "left_debug": "charybdis_bt",
    "reset": "",
}

groups = []
for keymap in keymaps:
    for fmt in ["bt", "dongle", "left_debug"]:
        groups.append({
            "keymap": keymap,
            "format": fmt,
            "name": f"{keymap}-{fmt}",
            "board": board,
            "shield_dir": format_shield_dir[fmt],
        })

# single reset entry
groups.append({
    "keymap": "default",
    "format": "reset",
    "name": "reset-nanov2",
    "board": board,
    "shield_dir": format_shield_dir["reset"],
})

# Dump matrix as compact JSON (GitHub expects it this way)
print(json.dumps(groups))
