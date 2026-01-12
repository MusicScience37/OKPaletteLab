"""Generate a color palette."""

import colour
import numpy

from ok_palette_lab_tools.color_palettes.color_palette import ColorPalette
from ok_palette_lab_tools.color_palettes.color_palette_def import ColorPaletteDef


def generate_color_palette(definition: ColorPaletteDef) -> ColorPalette:
    """Generate a color palette from its definition.

    Args:
        definition: Definition of the color palette.

    Returns:
        Generated color palette.
    """
    positions = numpy.array([position for position, _ in definition.colors])
    lch_colors = [lch for _, lch in definition.colors]

    positions_interp = numpy.linspace(0.0, 1.0, definition.num_interpolated_points)

    l_values = numpy.array([lch[0] for lch in lch_colors])
    c_values = numpy.array([lch[1] for lch in lch_colors])
    h_values = numpy.array([lch[2] for lch in lch_colors])

    l_interp = numpy.interp(positions_interp, positions, l_values)
    c_interp = numpy.interp(positions_interp, positions, c_values)
    h_interp = numpy.interp(positions_interp, positions, h_values)

    lch_interp = numpy.stack([l_interp, c_interp, h_interp], axis=1)

    rgb_interp = colour.convert(lch_interp, "oklch", "sRGB")

    rgb_in_bytes = numpy.round(rgb_interp * 255).astype(int)
    if numpy.any(rgb_in_bytes < 0) or numpy.any(rgb_in_bytes > 255):
        print(f"Warning: Color palette '{definition.name}' has out-of-gamut colors.")

    rgb_in_hex = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb_in_bytes]

    return ColorPalette(
        name=definition.name,
        description=definition.description,
        colors=list(zip(positions_interp, rgb_in_hex)),
    )
