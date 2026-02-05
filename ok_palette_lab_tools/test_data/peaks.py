"""Test data of peaks function in MATLAB."""

import numpy


def generate_peaks_data() -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    """Generate test data of peaks function in MATLAB.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: x, y, z data.
    """
    x = numpy.linspace(-3.0, 3.0, 101)
    y = numpy.linspace(-3.0, 3.0, 101)
    x_grid, y_grid = numpy.meshgrid(x, y)
    z = (
        3 * (1 - x_grid) ** 2 * numpy.exp(-(x_grid**2) - (y_grid + 1) ** 2)
        - 10
        * (x_grid / 5 - x_grid**3 - y_grid**5)
        * numpy.exp(-(x_grid**2) - y_grid**2)
        - 1 / 3 * numpy.exp(-((x_grid + 1) ** 2) - y_grid**2)
    )
    return x, y, z
