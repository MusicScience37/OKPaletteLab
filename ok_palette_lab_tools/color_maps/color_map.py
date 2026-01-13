"""Data structure of generated color maps."""

import dataclasses


@dataclasses.dataclass
class ColorMap:
    """Definition of a color map.

    Attributes:
        name: Name of the color map.
        description: Description of the color map.
        colors: List of (position, hex color) tuples defining the colors
            in the map.
    """

    name: str
    description: str
    colors: list[tuple[float, str]]
