"""Data structure of definitions of color maps."""

import dataclasses
import pathlib

import yaml

THIS_DIR = pathlib.Path(__file__).absolute().parent
COLOR_MAPS_DEF_PATH = THIS_DIR / "color_maps_def.yaml"


@dataclasses.dataclass
class ColorMapDef:
    """Definition of a color map.

    Attributes:
        name: Name of the color map.
        description: Description of the color map.
        colors: List of (position, (L, c, h)) tuples defining the colors
            in the map.
        num_interpolated_points: Number of total interpolated points in the map.
    """

    name: str
    description: str
    colors: list[tuple[float, tuple[float, float, float]]]
    num_interpolated_points: int


def load_color_maps_def() -> dict[str, ColorMapDef]:
    """Loads the color map definitions from the YAML file.

    Returns:
        A dictionary mapping color map names to their definitions.
    """
    with open(COLOR_MAPS_DEF_PATH, "r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f)

    color_maps_def: dict[str, ColorMapDef] = {}
    for map_data in raw_data["color_maps"]:
        colors = [
            (position, tuple(lch)) for position, lch in map_data["colors"].items()
        ]
        map_def = ColorMapDef(
            name=map_data["name"],
            description=map_data["description"],
            colors=colors,
            num_interpolated_points=map_data["num_interpolated_points"],
        )
        color_maps_def[map_def.name] = map_def

    return color_maps_def
