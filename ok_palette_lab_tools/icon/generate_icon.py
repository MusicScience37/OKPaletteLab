"""Generate SVG file of the icon of this project."""

import pathlib

import jinja2

from ok_palette_lab_tools.color_maps.color_map_def import load_color_maps_def
from ok_palette_lab_tools.color_maps.generate_color_map import generate_color_map

THIS_DIR = pathlib.Path(__file__).absolute().parent
OUTPUT_DIR = THIS_DIR.parent.parent / "docs" / "icon" / "design"

ICON_SIZE = 32
ICON_FOR_DOCS_SIZE = 128
ICON_MARGIN = 5
ICON_FOREGROUND_RADIUS = 2

COLOR_MAP_NAME = "blue_red_light"
DARK_COLOR_MAP_NAME = "blue_orange_dark"
BACKGROUND_COLOR = "#fbebe3"


def generate_icon() -> None:
    """Generate SVG file of the icon of this project."""
    color_maps_def = load_color_maps_def()
    color_map = generate_color_map(color_maps_def[COLOR_MAP_NAME])
    dark_color_map = generate_color_map(color_maps_def[DARK_COLOR_MAP_NAME])

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(THIS_DIR)))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(str(OUTPUT_DIR / "icon.svg"), "w", encoding="utf-8") as file:
        template = env.get_template("icon.svg.jinja")
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

    with open(str(OUTPUT_DIR / "icon_for_docs.svg"), "w", encoding="utf-8") as file:
        template = env.get_template("icon_for_docs.svg.jinja")
        rate = int(ICON_FOR_DOCS_SIZE / ICON_SIZE)
        file.write(
            template.render(
                size=ICON_FOR_DOCS_SIZE,
                margin=ICON_MARGIN,  # margin is not scaled intentionally
                radius=ICON_FOREGROUND_RADIUS * rate,
                background_color=BACKGROUND_COLOR,
                color_map=color_map,
            )
        )
        file.write("\n")

    with open(
        str(OUTPUT_DIR / "icon_for_docs_dark.svg"), "w", encoding="utf-8"
    ) as file:
        template = env.get_template("icon_for_docs.svg.jinja")
        rate = int(ICON_FOR_DOCS_SIZE / ICON_SIZE)
        file.write(
            template.render(
                size=ICON_FOR_DOCS_SIZE,
                margin=ICON_MARGIN,  # margin is not scaled intentionally
                radius=ICON_FOREGROUND_RADIUS * rate,
                background_color=BACKGROUND_COLOR,
                color_map=dark_color_map,
            )
        )
        file.write("\n")


if __name__ == "__main__":
    generate_icon()
