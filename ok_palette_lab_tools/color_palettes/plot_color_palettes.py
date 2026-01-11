"""Plot a color palette."""

import numpy
import plotly.graph_objects

from ok_palette_lab_tools.color_palettes.color_palette_def import (
    load_color_palettes_def,
)
from ok_palette_lab_tools.color_palettes.generate_color_palette import (
    generate_color_palette,
)


def plot_color_palettes() -> None:
    """Plot color palettes."""
    color_palettes = load_color_palettes_def()

    x = numpy.linspace(0.0, 1.0, 101)

    figure = plotly.graph_objects.Figure()
    index = 1
    for palette_name, color_palette_def in color_palettes.items():
        color_palette = generate_color_palette(color_palette_def)

        figure.add_heatmap(
            z=x,
            x=x,
            y=[palette_name] * len(x),
            xaxis=("x" + str(index) if index > 1 else "x"),
            yaxis=("y" + str(index) if index > 1 else "y"),
            coloraxis=("coloraxis" + str(index) if index > 1 else "coloraxis"),
            showscale=False,
            name=palette_name,
        )
        figure.update_layout(
            {
                ("coloraxis" + str(index) if index > 1 else "coloraxis"): {
                    "colorscale": color_palette.colors,
                    "cmin": 0,
                    "cmax": 1,
                    "showscale": False,
                }
            }
        )
        index += 1

    figure.update_layout(
        grid={
            "rows": len(color_palettes),
            "columns": 1,
            "pattern": "independent",
        }
    )

    figure.write_html("color_palettes.html")


if __name__ == "__main__":
    plot_color_palettes()
