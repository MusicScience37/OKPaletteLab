"""Functions to generate test data for color maps."""

import numpy
import plotly.graph_objects

from ok_palette_lab_tools.test_data.gaussian import (
    generate_gaussian_data,
    generate_positive_gaussian_data,
)
from ok_palette_lab_tools.test_data.peaks import generate_peaks_data
from ok_palette_lab_tools.test_data.perlin_noise import generate_perlin_noise_data
from ok_palette_lab_tools.test_data.spiral_pattern import generate_spiral_pattern_data


def create_color_map_image(
    color_map: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of color map.

    Args:
        color_map (list[tuple[float, str]]): Color map.

    Returns:
        plotly.graph_objects.Figure: Figure of color map.
    """
    x = numpy.linspace(0.0, 1.0, 101)
    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=x,
        x=x,
        y=[0] * len(x),
        colorscale=color_map,
        zsmooth="best",
    )
    return figure


def create_gaussian(
    color_map: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of Gaussian.

    Args:
        color_map (list[tuple[float, str]]): Color map.

    Returns:
        plotly.graph_objects.Figure: Figure of Gaussian.
    """
    x, y, z = generate_gaussian_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_map,
        zsmooth="best",
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        height=800,
    )
    return figure


def create_positive_gaussian(
    color_map: list[tuple[float, str]],
    reverse: bool = False,
) -> plotly.graph_objects.Figure:
    """Create a figure of Gaussian with only positive values.

    Args:
        color_map (list[tuple[float, str]]): Color map.
        reverse (bool): Whether to reverse the color map.

    Returns:
        plotly.graph_objects.Figure: Figure of Gaussian.
    """
    x, y, z = generate_positive_gaussian_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_map,
        reversescale=reverse,
        zsmooth="best",
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        height=800,
    )
    return figure


def create_peaks(
    color_map: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of peaks function in MATLAB.

    Args:
        color_map (list[tuple[float, str]]): Color map.

    Returns:
        plotly.graph_objects.Figure: Figure of peaks function.
    """
    x, y, z = generate_peaks_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_map,
        zsmooth="best",
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        height=800,
    )
    return figure


def create_perlin_noise(
    color_map: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of Perlin noise.

    Args:
        color_map (list[tuple[float, str]]): Color map.

    Returns:
        plotly.graph_objects.Figure: Figure of Perlin noise.
    """
    x, y, z = generate_perlin_noise_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_map,
        zsmooth="best",
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        height=800,
    )
    return figure


def create_spiral_pattern(
    color_map: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of spiral pattern.

    Args:
        color_map (list[tuple[float, str]]): Color map.

    Returns:
        plotly.graph_objects.Figure: Figure of spiral pattern.
    """
    x, y, z = generate_spiral_pattern_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_map,
        zsmooth="best",
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        height=800,
    )
    return figure
