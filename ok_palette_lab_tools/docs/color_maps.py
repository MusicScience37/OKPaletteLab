"""Generate a figure of color maps."""

import numpy
import plotly.graph_objects

import ok_palette_lab.plotly


def plot_color_maps(
    color_map_names: list[str], z_range: tuple[float, float]
) -> plotly.graph_objects.Figure:
    """Plot color maps.

    Args:
        color_map_names (list[str]): A list of color map names.
        z_range (tuple[float, float]): The range of the values to plot.

    Returns:
        plotly.graph_objects.Figure: The figure of color maps.
    """
    x = numpy.linspace(z_range[0], z_range[1], 101)
    figure = plotly.graph_objects.Figure()
    for index, color_map_name in enumerate(color_map_names):
        color_map = getattr(ok_palette_lab.plotly, color_map_name)

        figure.add_heatmap(
            z=x,
            x=x,
            y=[color_map_name] * len(x),
            xaxis=("x" + str(index + 1) if index > 0 else "x"),
            yaxis=("y" + str(index + 1) if index > 0 else "y"),
            coloraxis=("coloraxis" + str(index + 1) if index > 0 else "coloraxis"),
            showscale=False,
            name=color_map_name,
            zsmooth="best",
        )
        figure.update_layout(
            {
                ("coloraxis" + str(index + 1) if index > 0 else "coloraxis"): {
                    "colorscale": color_map,
                    "cmin": z_range[0],
                    "cmax": z_range[1],
                    "showscale": False,
                }
            }
        )

    figure.update_layout(
        grid={
            "rows": len(color_map_names),
            "columns": 1,
            "pattern": "independent",
        }
    )

    return figure
