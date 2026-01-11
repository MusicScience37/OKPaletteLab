"""Plot a color palette."""

import colour
import numpy
import plotly.graph_objects

from ok_palette_lab_tools.color_palettes.color_palette_def import (
    load_color_palettes_def,
)


def plot_color_palettes() -> None:  # pylint: disable=too-many-locals
    """Plot color palettes."""
    # TODO Rewrite this prototype implementation
    color_palettes = load_color_palettes_def()

    x = numpy.linspace(0.0, 1.0, 101)

    figure = plotly.graph_objects.Figure()
    index = 1
    for palette_name, color_palette in color_palettes.items():
        positions = [position for position, _ in color_palette.colors]
        lch_colors = [lch for _, lch in color_palette.colors]

        l_values = [lch[0] for lch in lch_colors]
        c_values = [lch[1] for lch in lch_colors]
        h_values = [lch[2] for lch in lch_colors]

        l_interp = numpy.interp(x, positions, l_values)
        c_interp = numpy.interp(x, positions, c_values)
        h_interp = numpy.interp(x, positions, h_values)

        lch_interp = numpy.stack([l_interp, c_interp, h_interp], axis=1)

        rgb_interp = colour.convert(lch_interp, "oklch", "sRGB")

        rgb_in_bytes = numpy.round(rgb_interp * 255).astype(int)
        if numpy.any(rgb_in_bytes < 0) or numpy.any(rgb_in_bytes > 255):
            print(f"Warning: Color palette '{palette_name}' has out-of-gamut colors.")

        rgb_in_hex = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb_in_bytes]

        figure.add_heatmap(
            z=x,
            x=list(range(len(x))),
            y=[palette_name] * len(x),
            text=rgb_in_hex,
            xaxis=("x" + str(index) if index > 1 else "x"),
            yaxis=("y" + str(index) if index > 1 else "y"),
            coloraxis=("coloraxis" + str(index) if index > 1 else "coloraxis"),
            showscale=False,
            name=palette_name,
        )
        figure.update_layout(
            {
                ("coloraxis" + str(index) if index > 1 else "coloraxis"): {
                    "colorscale": [[pos, color] for pos, color in zip(x, rgb_in_hex)],
                    "cmin": 0,
                    "cmax": 1,
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
