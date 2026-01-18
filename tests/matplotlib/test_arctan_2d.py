"""Test to plot arctan function in 2D."""

import pathlib

import matplotlib.pyplot
import pytest

import ok_palette_lab.matplotlib
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

    color_map = getattr(ok_palette_lab.matplotlib, color_map_name)

    figure, axes = matplotlib.pyplot.subplots()
    heatmap = axes.imshow(
        z,
        extent=(x.min(), x.max(), y.min(), y.max()),
        origin="lower",
        cmap=color_map,
        vmin=0.0,
        vmax=360.0,
    )
    figure.colorbar(heatmap)

    OUTPUT_DIR.mkdir(exist_ok=True)
    figure.savefig(OUTPUT_DIR / f"cyclic_{color_map_name}.png")
