"""Utility functions for samples of peaks function."""

import plotly.graph_objects

from ok_palette_lab_tools.docs.sample_common import plot_with_color_palettes
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

    return plot_with_color_palettes(
        x=x,
        y=y,
        z=z,
        color_palette_names=color_palette_names,
        zsmooth="best",
        diverging=diverging,
    )
