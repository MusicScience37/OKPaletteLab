"""Functions to generate test data for color palettes."""

import noise
import numpy
import plotly.graph_objects

from ok_palette_lab_tools.color_palettes.tests.general.test_figures import (
    create_color_palette_image as create_color_palette_image_general,
)


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
    x = numpy.linspace(-3.0, 3.0, 301)
    y = numpy.linspace(-3.0, 3.0, 301)
    x_grid, y_grid = numpy.meshgrid(x, y)
    z = numpy.exp(-0.5 * ((x_grid + 1) ** 2 + (y_grid - 1) ** 2)) - numpy.exp(
        -0.5 * ((x_grid - 1) ** 2 + (y_grid + 1) ** 2)
    )

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
    x = numpy.linspace(-3.0, 3.0, 301)
    y = numpy.linspace(-3.0, 3.0, 301)
    x_grid, y_grid = numpy.meshgrid(x, y)
    z = (
        3 * (1 - x_grid) ** 2 * numpy.exp(-(x_grid**2) - (y_grid + 1) ** 2)
        - 10
        * (x_grid / 5 - x_grid**3 - y_grid**5)
        * numpy.exp(-(x_grid**2) - y_grid**2)
        - 1 / 3 * numpy.exp(-((x_grid + 1) ** 2) - y_grid**2)
    )

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
    x = numpy.linspace(0.0, 8.0, 401)
    y = numpy.linspace(0.0, 8.0, 401)
    x_grid, y_grid = numpy.meshgrid(x, y)
    z = numpy.vectorize(lambda x, y: noise.pnoise2(x, y, octaves=6))(x_grid, y_grid)

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
    x = numpy.linspace(-2.0, 2.0, 401)
    y = numpy.linspace(-2.0, 2.0, 401)
    x_grid, y_grid = numpy.meshgrid(x, y)

    r = numpy.sqrt(x_grid**2 + y_grid**2)
    t = numpy.arctan2(y_grid, x_grid)
    z = numpy.sin(3 * t + 10 * r) * numpy.exp(-(r**2))

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
