"""Test to plot Gaussian."""

import pathlib

import matplotlib.pyplot
import pytest

import ok_palette_lab.matplotlib
from ok_palette_lab_tools.color_maps.color_map_names import (
    get_diverging_color_map_names,
    get_general_color_map_names,
)
from ok_palette_lab_tools.test_data.gaussian import (
    generate_gaussian_data,
    generate_positive_gaussian_data,
)

THIS_DIR = pathlib.Path(__file__).parent
OUTPUT_DIR = THIS_DIR / "output_plot_gaussian"


@pytest.mark.parametrize(
    "color_map_name",
    get_general_color_map_names(),
)
def test_plot_gaussian_sequential(color_map_name: str) -> None:
    """Test to plot Gaussian with sequential color maps."""
    x, y, z = generate_positive_gaussian_data()

    color_map = getattr(ok_palette_lab.matplotlib, color_map_name)

    figure, axes = matplotlib.pyplot.subplots()
    heatmap = axes.imshow(
        z,
        extent=(x.min(), x.max(), y.min(), y.max()),
        origin="lower",
        cmap=color_map,
        interpolation="bilinear",
    )
    figure.colorbar(heatmap)

    OUTPUT_DIR.mkdir(exist_ok=True)
    figure.savefig(OUTPUT_DIR / f"sequential_{color_map_name}.png")


@pytest.mark.parametrize(
    "color_map_name",
    get_diverging_color_map_names(),
)
def test_plot_gaussian_diverging(color_map_name: str) -> None:
    """Test to plot Gaussian with diverging color maps."""
    x, y, z = generate_gaussian_data()

    color_map = getattr(ok_palette_lab.matplotlib, color_map_name)

    figure, axes = matplotlib.pyplot.subplots()
    heatmap = axes.imshow(
        z,
        extent=(x.min(), x.max(), y.min(), y.max()),
        origin="lower",
        cmap=color_map,
        interpolation="bilinear",
    )
    figure.colorbar(heatmap)

    OUTPUT_DIR.mkdir(exist_ok=True)
    figure.savefig(OUTPUT_DIR / f"diverging_{color_map_name}.png")
