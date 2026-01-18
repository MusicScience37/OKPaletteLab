"""Functions to generate test data for color maps."""

import plotly.graph_objects

from ok_palette_lab_tools.color_maps.tests.general.test_figures import (
    create_color_map_image as create_color_map_image_general,
)
from ok_palette_lab_tools.test_data.arctan_2d import generate_arctan_2d_data


def create_color_map_image(
    color_map: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of color map.

    Args:
        color_map (list[tuple[float, str]]): Color map.

    Returns:
        plotly.graph_objects.Figure: Figure of color map.
    """
    return create_color_map_image_general(color_map)


def create_arctan_2d(
    color_map: list[tuple[float, str]],
) -> plotly.graph_objects.Figure:
    """Create a figure of arctan function in 2D.

    Args:
        color_map (list[tuple[float, str]]): Color map.

    Returns:
        plotly.graph_objects.Figure: Figure of arctan function in 2D.

    Note:
        Color map is assumed to be cyclic.
    """
    x, y, z = generate_arctan_2d_data()

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_map,
        zmin=0,
        zmax=360,
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
            "scaleratio": 1,
        },
        height=800,
    )
    return figure
