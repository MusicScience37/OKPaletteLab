"""Test data of spiral pattern."""

import numpy


def generate_spiral_pattern_data() -> (
    tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]
):
    """Generate test data of spiral pattern.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: x, y, z data.
    """
    x = numpy.linspace(-2.0, 2.0, 401)
    y = numpy.linspace(-2.0, 2.0, 401)
    x_grid, y_grid = numpy.meshgrid(x, y)

    r = numpy.sqrt(x_grid**2 + y_grid**2)
    t = numpy.arctan2(y_grid, x_grid)
    z = numpy.sin(3 * t + 10 * r) * numpy.exp(-(r**2))

    return x, y, z
