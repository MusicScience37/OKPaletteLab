"""Utility functions for samples of Gaussian function."""

import plotly.graph_objects

from ok_palette_lab_tools.docs.sample_common import plot_with_color_palettes
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

    Note:
        This function works only with non-diverging color palettes.
    """
    _ignore(version)

    x, y, z = generate_positive_gaussian_data()

    return plot_with_color_palettes(
        x=x,
        y=y,
        z=z,
        color_palette_names=color_palette_names,
        zsmooth="best",
        diverging=False,
    )
