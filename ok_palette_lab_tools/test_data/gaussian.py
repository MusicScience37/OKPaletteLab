"""Test data of Gaussian functions."""

import numpy


def generate_gaussian_data() -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    """Generate Gaussian test data.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: x, y, z data.
    """
    x = numpy.linspace(-3.0, 3.0, 101)
    y = numpy.linspace(-3.0, 3.0, 101)
    x_grid, y_grid = numpy.meshgrid(x, y)
    z = numpy.exp(-0.5 * ((x_grid + 1) ** 2 + (y_grid - 1) ** 2)) - numpy.exp(
        -0.5 * ((x_grid - 1) ** 2 + (y_grid + 1) ** 2)
    )
    return x, y, z


def generate_positive_gaussian_data() -> (
    tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]
):
    """Generate Gaussian test data with only positive values.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: x, y, z data.
    """
    x = numpy.linspace(-3.0, 3.0, 101)
    y = numpy.linspace(-3.0, 3.0, 101)
    x_grid, y_grid = numpy.meshgrid(x, y)
    z = numpy.exp(-0.5 * ((x_grid + 1) ** 2 + (y_grid - 1) ** 2)) + 0.3 * numpy.exp(
        -0.5 * ((x_grid - 1) ** 2 + (y_grid + 1) ** 2)
    )
    return x, y, z
