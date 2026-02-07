"""Generate images for documentation."""

import pathlib

import matplotlib.pyplot
import numpy
import PIL

import ok_palette_lab.matplotlib
from ok_palette_lab_tools.test_data.gaussian import (
    generate_gaussian_data,
    generate_positive_gaussian_data,
)
from ok_palette_lab_tools.test_data.perlin_noise import generate_perlin_noise_data

THIS_DIR = pathlib.Path(__file__).absolute().parent
OUTPUT_DIR = THIS_DIR.parent.parent / "docs" / "images"


def generate_gaussian_image(*, is_light: bool) -> None:
    """Generate an image of Gaussian function for documentation.

    Args:
        is_light: Whether to use light theme.
    """
    x, y, z = generate_gaussian_data()
    max_abs = numpy.abs(z).max()

    if is_light:
        matplotlib.pyplot.style.use("default")
        file_name_suffix = ""
        color_map = ok_palette_lab.matplotlib.blue_red_light
    else:
        matplotlib.pyplot.style.use("dark_background")
        file_name_suffix = "_dark"
        color_map = ok_palette_lab.matplotlib.blue_red_dark

    figure, axes = matplotlib.pyplot.subplots()
    heatmap = axes.imshow(
        z,
        extent=(x.min(), x.max(), y.min(), y.max()),
        origin="lower",
        cmap=color_map,
        vmin=-max_abs,
        vmax=max_abs,
        interpolation="bilinear",
    )
    figure.colorbar(heatmap)
    figure.set_size_inches(4.5, 3.5)

    OUTPUT_DIR.mkdir(exist_ok=True)
    figure.savefig(OUTPUT_DIR / f"gaussian{file_name_suffix}.png")


def generate_positive_gaussian_image(*, is_light: bool) -> None:
    """Generate an image of positive Gaussian function for documentation.

    Args:
        is_light: Whether to use light theme.
    """
    x, y, z = generate_positive_gaussian_data()

    if is_light:
        matplotlib.pyplot.style.use("default")
        file_name_suffix = ""
        color_map = ok_palette_lab.matplotlib.autumn_wide.reversed()
    else:
        matplotlib.pyplot.style.use("dark_background")
        file_name_suffix = "_dark"
        color_map = ok_palette_lab.matplotlib.autumn_wide

    figure, axes = matplotlib.pyplot.subplots()
    heatmap = axes.imshow(
        z,
        extent=(x.min(), x.max(), y.min(), y.max()),
        origin="lower",
        cmap=color_map,
        vmin=0.0,
        vmax=z.max(),
        interpolation="bilinear",
    )
    figure.colorbar(heatmap)
    figure.set_size_inches(4.5, 3.5)

    OUTPUT_DIR.mkdir(exist_ok=True)
    figure.savefig(OUTPUT_DIR / f"positive_gaussian{file_name_suffix}.png")


def generate_perlin_noise_image(*, is_light: bool) -> None:
    """Generate an image of Perlin noise for documentation.

    Args:
        is_light: Whether to use light theme.
    """
    x, y, z = generate_perlin_noise_data()
    max_abs = numpy.abs(z).max()

    if is_light:
        matplotlib.pyplot.style.use("default")
        file_name_suffix = ""
        color_map = ok_palette_lab.matplotlib.blue_brown_light_wide
    else:
        matplotlib.pyplot.style.use("dark_background")
        file_name_suffix = "_dark"
        color_map = ok_palette_lab.matplotlib.blue_orange_dark_wide

    figure, axes = matplotlib.pyplot.subplots()
    heatmap = axes.imshow(
        z,
        extent=(x.min(), x.max(), y.min(), y.max()),
        origin="lower",
        cmap=color_map,
        vmin=-max_abs,
        vmax=max_abs,
        interpolation="bilinear",
    )
    figure.colorbar(heatmap)
    axes.set_xlim(0.0, 7.0)
    axes.set_ylim(0.0, 3.0)
    figure.set_size_inches(9.0, 3.5)

    OUTPUT_DIR.mkdir(exist_ok=True)
    figure.savefig(OUTPUT_DIR / f"perlin_noise{file_name_suffix}.png")


def generate_combined_image(*, is_light: bool) -> None:
    """Generate a combined image for documentation.

    This function generates a combined image with
    two images at the top row and one image at the bottom row.

    Args:
        is_light: Whether to use light theme.
    """
    if is_light:
        file_name_suffix = ""
    else:
        file_name_suffix = "_dark"

    img_top_left = PIL.Image.open(OUTPUT_DIR / f"gaussian{file_name_suffix}.png")
    img_top_right = PIL.Image.open(
        OUTPUT_DIR / f"positive_gaussian{file_name_suffix}.png"
    )
    img_bottom = PIL.Image.open(OUTPUT_DIR / f"perlin_noise{file_name_suffix}.png")

    top_left_width, top_left_height = img_top_left.size
    top_right_width, top_right_height = img_top_right.size
    bottom_width, bottom_height = img_bottom.size

    top_row_width = top_left_width + top_right_width
    top_row_height = max(top_left_height, top_right_height)

    total_width = max(top_row_width, bottom_width)
    total_height = top_row_height + bottom_height

    combined = PIL.Image.new("RGB", (total_width, total_height), color="white")

    combined.paste(img_top_left, (0, 0))
    combined.paste(img_top_right, (top_left_width, 0))
    combined.paste(img_bottom, (0, top_row_height))

    combined.save(OUTPUT_DIR / f"combined{file_name_suffix}.png")


def generate_images() -> None:
    """Generate images for documentation."""
    for is_light in (True, False):
        generate_gaussian_image(is_light=is_light)
        generate_positive_gaussian_image(is_light=is_light)
        generate_perlin_noise_image(is_light=is_light)
        generate_combined_image(is_light=is_light)


if __name__ == "__main__":
    generate_images()
