"""Data structure of generated color palettes."""

import dataclasses


@dataclasses.dataclass
class ColorPalette:
    """Definition of a color palette.

    Attributes:
        name: Name of the color palette.
        description: Description of the color palette.
        colors: List of (position, hex color) tuples defining the colors
            in the palette.
    """

    name: str
    description: str
    colors: list[tuple[float, str]]
