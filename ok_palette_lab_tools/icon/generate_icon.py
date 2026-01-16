"""Generate SVG file of the icon of this project."""

import pathlib

import jinja2

from ok_palette_lab_tools.color_maps.color_map_def import load_color_maps_def
from ok_palette_lab_tools.color_maps.generate_color_map import generate_color_map

THIS_DIR = pathlib.Path(__file__).absolute().parent
TEMPLATE_NAME = "icon.svg.jinja"
OUTPUT_PATH = THIS_DIR.parent.parent / "docs" / "icon" / "design" / "icon_generated.svg"

ICON_SIZE = 32
ICON_MARGIN = 5
ICON_FOREGROUND_RADIUS = 2

COLOR_MAP_NAME = "blue_brown_light"
BACKGROUND_COLOR = "#fbebe3"


def generate_icon() -> None:
    """Generate SVG file of the icon of this project."""
    color_maps_def = load_color_maps_def()
    color_map = generate_color_map(color_maps_def[COLOR_MAP_NAME])

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(THIS_DIR)))
    template = env.get_template(TEMPLATE_NAME)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(str(OUTPUT_PATH), "w", encoding="utf-8") as file:
        file.write(
            template.render(
                size=ICON_SIZE,
                margin=ICON_MARGIN,
                radius=ICON_FOREGROUND_RADIUS,
                background_color=BACKGROUND_COLOR,
                color_map=color_map,
            )
        )
        file.write("\n")


if __name__ == "__main__":
    generate_icon()
