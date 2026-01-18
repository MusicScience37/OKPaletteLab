"""Test to plot arctan function in 2D."""

import pathlib

import plotly.graph_objects
import pytest

import ok_palette_lab.plotly
from ok_palette_lab_tools.color_maps.color_map_names import get_cyclic_color_map_names
from ok_palette_lab_tools.test_data.arctan_2d import generate_arctan_2d_data

THIS_DIR = pathlib.Path(__file__).parent
OUTPUT_DIR = THIS_DIR / "output_plot_arctan_2d"


@pytest.mark.parametrize(
    "color_map_name",
    get_cyclic_color_map_names(),
)
def test_plot_arctan_2d(color_map_name: str) -> None:
    """Test to plot arctan function in 2D with cyclic color maps."""
    x, y, z = generate_arctan_2d_data()

    color_map = getattr(ok_palette_lab.plotly, color_map_name)

    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=color_map,
        zmin=0.0,
        zmax=360.0,
    )
    figure.update_layout(
        yaxis={
            "scaleanchor": "x",
        }
    )

    OUTPUT_DIR.mkdir(exist_ok=True)
    figure.write_image(str(OUTPUT_DIR / f"cyclic_{color_map_name}.png"))
