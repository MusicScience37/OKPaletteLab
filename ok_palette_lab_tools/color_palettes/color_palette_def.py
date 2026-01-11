"""Data structure of definitions of color palettes."""

import dataclasses
import pathlib

import yaml

THIS_DIR = pathlib.Path(__file__).absolute().parent
COLOR_PALETTES_DEF_PATH = THIS_DIR / "color_palettes_def.yaml"


@dataclasses.dataclass
class ColorPaletteDef:
    """Definition of a color palette.

    Attributes:
        name: Name of the color palette.
        description: Description of the color palette.
        colors: List of (position, (L, c, h)) tuples defining the colors
            in the palette.
        interpolated_points: Number of total interpolated points in the palette.
    """

    name: str
    description: str
    colors: list[tuple[float, tuple[float, float, float]]]
    interpolated_points: int


def load_color_palettes_def() -> dict[str, ColorPaletteDef]:
    """Loads the color palette definitions from the YAML file.

    Returns:
        A dictionary mapping color palette names to their definitions.
    """
    with open(COLOR_PALETTES_DEF_PATH, "r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f)

    color_palettes_def: dict[str, ColorPaletteDef] = {}
    for palette_data in raw_data["color_palettes"]:
        colors = [
            (position, tuple(lch)) for position, lch in palette_data["colors"].items()
        ]
        palette_def = ColorPaletteDef(
            name=palette_data["name"],
            description=palette_data["description"],
            colors=colors,
            interpolated_points=palette_data["interpolated_points"],
        )
        color_palettes_def[palette_def.name] = palette_def

    return color_palettes_def
