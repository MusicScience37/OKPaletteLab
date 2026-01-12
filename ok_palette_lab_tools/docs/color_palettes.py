"""Generate a figure of color palettes."""

import numpy
import plotly.graph_objects

import ok_palette_lab.plotly


def plot_color_palettes(
    color_palette_names: list[str], z_range: tuple[float, float]
) -> plotly.graph_objects.Figure:
    """Plot color palettes.

    Args:
        color_palette_names (list[str]): A list of color palette names.
        z_range (tuple[float, float]): The range of the values to plot.

    Returns:
        plotly.graph_objects.Figure: The figure of color palettes.
    """
    x = numpy.linspace(z_range[0], z_range[1], 101)
    figure = plotly.graph_objects.Figure()
    for index, color_palette_name in enumerate(color_palette_names):
        color_palette = getattr(ok_palette_lab.plotly, color_palette_name)

        figure.add_heatmap(
            z=x,
            x=x,
            y=[color_palette_name] * len(x),
            xaxis=("x" + str(index + 1) if index > 0 else "x"),
            yaxis=("y" + str(index + 1) if index > 0 else "y"),
            coloraxis=("coloraxis" + str(index + 1) if index > 0 else "coloraxis"),
            showscale=False,
            name=color_palette_name,
            zsmooth="best",
        )
        figure.update_layout(
            {
                ("coloraxis" + str(index + 1) if index > 0 else "coloraxis"): {
                    "colorscale": color_palette,
                    "cmin": z_range[0],
                    "cmax": z_range[1],
                    "showscale": False,
                }
            }
        )

    figure.update_layout(
        grid={
            "rows": len(color_palette_names),
            "columns": 1,
            "pattern": "independent",
        }
    )

    return figure
