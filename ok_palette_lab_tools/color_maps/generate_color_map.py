"""Generate a color map."""

import colour
import numpy

from ok_palette_lab_tools.color_maps.color_map import ColorMap
from ok_palette_lab_tools.color_maps.color_map_def import (
    ColorMapDef,
    ColorMapSegmentDef,
)


def _handle_linear_lightness(
    segment: ColorMapSegmentDef, first_position: float
) -> list[tuple[float, str]]:
    """Handle a segment of linear lightness.

    Args:
        segment (ColorMapSegmentDef): Definition of the color map segment.
        first_position (float): The starting position for this segment.

    Returns:
        list[tuple[float, str]]: List of (position, hex color) tuples.
    """
    lch_colors = segment.colors
    l_values = numpy.array([lch[0] for lch in lch_colors])
    c_values = numpy.array([lch[1] for lch in lch_colors])
    h_values = numpy.array([lch[2] for lch in lch_colors])

    position = first_position
    positions_as_list = [position]
    for i in range(len(lch_colors) - 1):
        position += abs(l_values[i + 1] - l_values[i])
        positions_as_list.append(position)
    positions = numpy.array(positions_as_list)

    positions_interp = numpy.linspace(
        positions[0], positions[-1], segment.num_interpolated_points
    )

    l_interp = numpy.interp(positions_interp, positions, l_values)
    c_interp = numpy.interp(positions_interp, positions, c_values)
    h_interp = numpy.interp(positions_interp, positions, h_values)

    lch_interp = numpy.stack([l_interp, c_interp, h_interp], axis=1)

    rgb_interp = colour.convert(lch_interp, "oklch", "sRGB")

    rgb_in_bytes = numpy.round(rgb_interp * 255).astype(int)
    if numpy.any(rgb_in_bytes < 0) or numpy.any(rgb_in_bytes > 255):
        raise ValueError("Color map has saturated colors.")

    rgb_in_hex = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb_in_bytes]

    return list(zip(positions_interp, rgb_in_hex))


def generate_color_map(definition: ColorMapDef) -> ColorMap:
    """Generate a color map from its definition.

    Args:
        definition: Definition of the color map.

    Returns:
        Generated color map.
    """
    colors: list[tuple[float, str]] = []
    last_position = 0.0
    for segment in definition.segments:
        if segment.type == "linear_lightness":
            segment_colors = _handle_linear_lightness(segment, last_position)
        else:
            raise ValueError(f"Unknown segment type: {segment.type}")

        if colors:
            # Remove the first color to avoid duplication.
            segment_colors = segment_colors[1:]

        colors.extend(segment_colors)
        last_position = colors[-1][0]

    # Normalize positions.
    colors = [(color[0] / last_position, color[1]) for color in colors]

    return ColorMap(
        name=definition.name,
        description=definition.description,
        colors=colors,
    )
