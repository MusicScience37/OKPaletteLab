"""Generate JSON files for ParaView color maps."""

import json
import pathlib

from ok_palette_lab_tools.color_maps.color_map_def import load_color_maps_def
from ok_palette_lab_tools.color_maps.generate_color_map import generate_color_map

THIS_DIR = pathlib.Path(__file__).absolute().parent


def _hex_color_to_rgb(hex_color: str) -> tuple[float, float, float]:
    """Convert a hex color to RGB in [0, 1].

    Args:
        hex_color (str): Hex color.

    Returns:
        tuple[float, float, float]: RGB in [0, 1].
    """
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return r / 255.0, g / 255.0, b / 255.0


def generate_json() -> None:
    """Generate JSON files for ParaView color maps."""
    color_maps_def = load_color_maps_def()

    output_dir = THIS_DIR.parent.parent / "ok_palette_lab_paraview"
    output_dir.mkdir(parents=True, exist_ok=True)

    for color_map_def in color_maps_def.values():
        color_map = generate_color_map(color_map_def)
        points_json: list[float] = []
        for position, hex_color in color_map.colors:
            r, g, b = _hex_color_to_rgb(hex_color)
            points_json = points_json + [position, r, g, b]
        json_data = [
            {
                "Name": color_map.name,
                "ColorSpace": "RGB",
                "RGBPoints": points_json,
                "NanColor": [0.0, 0.0, 0.0],
            }
        ]
        output_path = output_dir / f"{color_map.name}.json"
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)


if __name__ == "__main__":
    generate_json()
