"""Data structure of definitions of color maps."""

import dataclasses
import pathlib

import yaml

THIS_DIR = pathlib.Path(__file__).absolute().parent
COLOR_MAPS_DEF_PATH = THIS_DIR / "color_maps_def.yaml"


@dataclasses.dataclass
class ColorMapSegmentDef:
    """Definition of a color map segment.

    Attributes:
        type: Type of the segment (e.g., 'linear_lightness').
        colors: List of (L, c, h) tuples defining the colors in the segment.
        num_interpolated_points: Number of total interpolated points in the segment.
        width: Width parameter for diverging segments (optional).
        power: Power parameter for diverging segments (optional).
    """

    type: str
    colors: list[tuple[float, float, float]]
    num_interpolated_points: int
    width: float | None
    power: float | None


@dataclasses.dataclass
class ColorMapDef:
    """Definition of a color map.

    Attributes:
        name: Name of the color map.
        description: Description of the color map.
        segments: List of segments defining the colors in the map.
        reverse: Whether the color map should be reversed.
    """

    name: str
    description: str
    segments: list[ColorMapSegmentDef]
    reverse: bool


def load_color_maps_def() -> dict[str, ColorMapDef]:
    """Loads the color map definitions from the YAML file.

    Returns:
        A dictionary mapping color map names to their definitions.
    """
    with open(COLOR_MAPS_DEF_PATH, "r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f)

    color_maps_def: dict[str, ColorMapDef] = {}
    for map_data in raw_data["color_maps"]:
        segments: list[ColorMapSegmentDef] = []
        for segment in map_data["segments"]:
            seg_type = segment["type"]
            raw_colors = segment["colors"]
            colors = [
                (float(color[0]), float(color[1]), float(color[2]))
                for color in raw_colors
            ]
            num_points = segment["num_interpolated_points"]
            width = segment.get("width", None)
            power = segment.get("power", None)
            segments.append(
                ColorMapSegmentDef(
                    type=seg_type,
                    colors=colors,
                    num_interpolated_points=int(num_points),
                    width=float(width) if width is not None else None,
                    power=float(power) if power is not None else None,
                )
            )

        reverse = False
        if "reverse" in map_data:
            reverse = bool(map_data["reverse"])
        map_def = ColorMapDef(
            name=map_data["name"],
            description=map_data["description"],
            segments=segments,
            reverse=reverse,
        )
        color_maps_def[map_def.name] = map_def

    return color_maps_def
