"""Functions to generate test data for color palettes."""

import plotly.graph_objects

from ok_palette_lab_tools.color_palettes.tests.general.test_figures import (
    create_color_palette_image as create_color_palette_image_general,
)
from ok_palette_lab_tools.test_data.gaussian import generate_gaussian_data
from ok_palette_lab_tools.test_data.peaks import generate_peaks_data
from ok_palette_lab_tools.test_data.perlin_noise import generate_perlin_noise_data
from ok_palette_lab_tools.test_data.spiral_pattern import generate_spiral_pattern_data


def create_color_palette_image(
    color_palette: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of color palette.

    Args:
        color_palette (list[tuple[float, str]]): Color palette.

    Returns:
        plotly.graph_objects.Figure: Figure of color palette.
    """
    return create_color_palette_image_general(color_palette)


def create_gaussian(
    color_palette: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of Gaussian.

    Args:
        color_palette (list[tuple[float, str]]): Color palette.

    Returns:
        plotly.graph_objects.Figure: Figure of Gaussian.
    """
    x, y, z = generate_gaussian_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_palette,
        zsmooth="best",
        zmid=0,
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
    color_palette: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of peaks function in MATLAB.

    Args:
        color_palette (list[tuple[float, str]]): Color palette.

    Returns:
        plotly.graph_objects.Figure: Figure of peaks function.
    """
    x, y, z = generate_peaks_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_palette,
        zsmooth="best",
        zmid=0,
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
    color_palette: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of Perlin noise.

    Args:
        color_palette (list[tuple[float, str]]): Color palette.

    Returns:
        plotly.graph_objects.Figure: Figure of Perlin noise.
    """
    x, y, z = generate_perlin_noise_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_palette,
        zmid=0,
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
    color_palette: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of spiral pattern.

    Args:
        color_palette (list[tuple[float, str]]): Color palette.

    Returns:
        plotly.graph_objects.Figure: Figure of spiral pattern.
    """
    x, y, z = generate_spiral_pattern_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_palette,
        zsmooth="best",
        zmid=0,
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        height=800,
    )
    return figure
