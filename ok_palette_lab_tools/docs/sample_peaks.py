"""Utility functions for samples of peaks function."""

import plotly.graph_objects

from ok_palette_lab_tools.docs.sample_common import plot_with_color_maps
from ok_palette_lab_tools.test_data.peaks import generate_peaks_data


def _ignore(_):
    """Ignore unused variable."""


def plot_peaks(
    color_map_names: list[str],
    diverging: bool,
    version: int,
) -> plotly.graph_objects.Figure:
    """Plot samples of peaks function with different color maps.

    Args:
        color_map_names (list[str]): List of color map names to use for plotting.
        diverging (bool): Whether to use diverging color maps.
        version (int): Version number to prevent reusing cached results when this script is updated.

    Returns:
        plotly.graph_objects.Figure: Figure.
    """
    _ignore(version)

    x, y, z = generate_peaks_data()

    return plot_with_color_maps(
        x=x,
        y=y,
        z=z,
        color_map_names=color_map_names,
        zsmooth="best",
        diverging=diverging,
    )
