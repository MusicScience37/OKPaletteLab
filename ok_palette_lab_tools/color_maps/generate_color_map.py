"""Generate a color map."""

import colour
import numpy

from ok_palette_lab_tools.color_maps.color_map import ColorMap
from ok_palette_lab_tools.color_maps.color_map_def import (
    ColorMapDef,
    ColorMapSegmentDef,
)


def _lch_to_hex_rgb(lch_colors: numpy.ndarray) -> list[str]:
    """Convert Lch colors to RGB colors in hex format.

    Args:
        lch_colors (numpy.ndarray): Array of Lch colors.

    Returns:
        list[str]: List of RGB colors in hex format.
    """
    rgb_in_float = colour.convert(lch_colors, "oklch", "sRGB")

    rgb_in_bytes = numpy.round(rgb_in_float * 255).astype(int)
    if numpy.any(rgb_in_bytes < 0) or numpy.any(rgb_in_bytes > 255):
        raise ValueError("Color map has saturated colors.")

    rgb_in_hex = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb_in_bytes]

    return rgb_in_hex


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

    return list(zip(positions_interp, _lch_to_hex_rgb(lch_interp)))


def _handle_diverging_light(
    segment: ColorMapSegmentDef, first_position: float
) -> list[tuple[float, str]]:
    """Handle a segment of diverging range with high lightness.

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

    if l_values[0] != l_values[-1]:
        raise ValueError("Diverging segment must have the same lightness at both ends.")

    l_change = 0.0
    l_changes_as_list: list[float] = [l_change]
    for i in range(len(lch_colors) - 1):
        l_change += abs(l_values[i + 1] - l_values[i])
        l_changes_as_list.append(l_change)
    l_changes = numpy.array(l_changes_as_list)

    if segment.width is None:
        raise ValueError("Diverging segment must have 'width' parameter.")
    width = segment.width
    if segment.power is None:
        raise ValueError("Diverging segment must have 'power' parameter.")
    power = segment.power
    additional_length = width - width / power

    def _diverging_position_to_lightness_change(position: float) -> float:
        """Map a position to a value of total changes of lightness.

        Args:
            position (float): Position. Zero is the center.

        Returns:
            float: Total change of lightness. Zero is the center.
        """
        if 0 <= position <= width:
            # Smooth part on positive side.
            return position**power / (power * (width ** (power - 1)))
        if -width <= position < 0:
            # Smooth part on negative side.
            return -((-position) ** power) / (power * (width ** (power - 1)))
        if position > width:
            # Linear part on positive side.
            return position - additional_length
        # Linear part on negative side.
        return position + additional_length

    total_lightness_change = abs(max(l_values) - min(l_values))
    positions_interp = numpy.linspace(
        -total_lightness_change - additional_length,
        total_lightness_change + additional_length,
        segment.num_interpolated_points,
    )
    l_changes_interp = numpy.vectorize(_diverging_position_to_lightness_change)(
        positions_interp
    )
    l_changes_interp -= l_changes_interp[0]
    l_changes_interp[-1] = l_changes[-1]

    l_interp = numpy.interp(l_changes_interp, l_changes, l_values)
    c_interp = numpy.interp(l_changes_interp, l_changes, c_values)
    h_interp = numpy.interp(l_changes_interp, l_changes, h_values)

    lch_interp = numpy.stack([l_interp, c_interp, h_interp], axis=1)
    positions_interp = positions_interp - positions_interp[0] + first_position
    return list(zip(positions_interp, _lch_to_hex_rgb(lch_interp)))


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
        elif segment.type == "diverging_light":
            segment_colors = _handle_diverging_light(segment, last_position)
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
