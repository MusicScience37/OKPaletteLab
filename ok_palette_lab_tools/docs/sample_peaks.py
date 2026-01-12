"""Utility functions for samples of peaks function."""

import plotly.graph_objects

import ok_palette_lab.plotly
from ok_palette_lab_tools.test_data.peaks import generate_peaks_data


def _ignore(_):
    """Ignore unused variable."""


def plot_peaks(
    color_palette_names: list[str],
    diverging: bool,
    version: int,
) -> plotly.graph_objects.Figure:
    """Plot samples of peaks function with different color palettes.

    Args:
        color_palette_names (list[str]): List of color palette names to use for plotting.
        diverging (bool): Whether to use diverging color palettes.
        version (int): Version number to prevent reusing cached results when this script is updated.

    Returns:
        plotly.graph_objects.Figure: Figure.
    """
    _ignore(version)

    x, y, z = generate_peaks_data()

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
            zmid=0 if diverging else None,
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
