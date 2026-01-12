"""Common functions for plotting samples."""

import numpy
import plotly.graph_objects

import ok_palette_lab.plotly


def plot_with_color_palettes(
    *,
    x: numpy.ndarray,
    y: numpy.ndarray,
    z: numpy.ndarray,
    color_palette_names: list[str],
    zsmooth: str | None,
    diverging: bool,
) -> plotly.graph_objects.Figure:
    """Plot a figure with color palettes.

    Args:
        x (numpy.ndarray): X coordinates.
        y (numpy.ndarray): Y coordinates.
        z (numpy.ndarray): Z coordinates.
        color_palette_names (list[str]): List of color palette names.
        zsmooth (str | None): Specification of smoothness of z coordinates.
        diverging (bool): Whether to use diverging color palettes.

    Returns:
        plotly.graph_objects.Figure: Created figure.
    """
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
            zsmooth=zsmooth,
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
        if index > 0:
            figure.update_layout(
                {
                    "xaxis"
                    + index_suffix: {
                        "matches": "x",
                    },
                    "yaxis"
                    + index_suffix: {
                        "matches": "y",
                    },
                }
            )
        if diverging:
            figure.update_layout(
                {
                    "coloraxis"
                    + index_suffix: {
                        "cmid": 0,
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
