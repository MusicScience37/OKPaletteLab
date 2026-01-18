"""Test data of arctan function in 2D."""

import numpy


def generate_arctan_2d_data() -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    """Generate test data of arctan function in 2D.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: x, y, z data.
    """
    x = numpy.linspace(-1.0, 1.0, 200)
    y = numpy.linspace(-1.0, 1.0, 200)
    x_grid, y_grid = numpy.meshgrid(x, y)

    z = numpy.arctan2(y_grid, x_grid)

    # Change the range to [0, 2pi].
    z[z < 0] += 2.0 * numpy.pi
    # Normalize to [0, 360].
    z = z * (360.0 / (2.0 * numpy.pi))

    return x, y, z
