"""Utility functions for samples of Gaussian function."""

import plotly.graph_objects

import ok_palette_lab.plotly
from ok_palette_lab_tools.test_data.gaussian import generate_positive_gaussian_data


def _ignore(_):
    """Ignore unused variable."""


def plot_gaussian(
    color_palette_names: list[str],
    version: int,
) -> plotly.graph_objects.Figure:
    """Plot samples of Gaussian function with different color palettes.

    Args:
        color_palette_names (list[str]): List of color palette names to use for plotting.
        version (int): Version number to prevent reusing cached results when this script is updated.

    Returns:
        plotly.graph_objects.Figure: Figure.
    """
    _ignore(version)

    x, y, z = generate_positive_gaussian_data()

    figure = plotly.graph_objects.Figure()
    for index, color_palette_name in enumerate(color_palette_names):
        index_suffix = str(index + 1) if index > 0 else ""
        figure.add_heatmap(
            z=z,
            x=x,
            y=y,
            xaxis="x" + index_suffix,
            yaxis="y" + index_suffix,
            coloraxis="coloraxis" + index_suffix,
            zsmooth="best",
        )
        figure.update_layout(
            {
                "coloraxis"
                + index_suffix: {
                    "colorscale": getattr(ok_palette_lab.plotly, color_palette_name),
                    "showscale": False,
                }
            }
        )
        figure.add_annotation(
            text=color_palette_name,
            xref="x" + index_suffix + " domain",
            yref="y" + index_suffix + " domain",
            x=0.0,
            y=1.0,
            yshift=25.0,
            align="left",
            font={"size": 16.0},
            showarrow=False,
        )

    figure.update_layout(
        {
            "grid": {
                "columns": 2,
                "rows": (len(color_palette_names) + 1) // 2,
                "pattern": "independent",
            },
        }
    )

    return figure
