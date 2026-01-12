"""Test data of Perlin noise."""

import noise
import numpy


def generate_perlin_noise_data() -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    """Generate test data of Perlin noise.

    Returns:
        tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: x, y, z data.
    """
    x = numpy.linspace(0.0, 8.0, 401)
    y = numpy.linspace(0.0, 8.0, 401)
    x_grid, y_grid = numpy.meshgrid(x, y)
    z = numpy.vectorize(lambda x, y: noise.pnoise2(x, y, octaves=6))(x_grid, y_grid)
    return x, y, z
