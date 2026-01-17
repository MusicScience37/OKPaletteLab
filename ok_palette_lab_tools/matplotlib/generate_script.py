"""Generate script for matplotlib color maps."""

import pathlib
import subprocess

import jinja2

from ok_palette_lab_tools.color_maps.color_map_def import load_color_maps_def
from ok_palette_lab_tools.color_maps.generate_color_map import generate_color_map

THIS_DIR = pathlib.Path(__file__).absolute().parent


def generate_script() -> None:
    """Generate script for matplotlib color maps."""
    color_maps_def = load_color_maps_def()
    color_maps = [
        generate_color_map(definition) for definition in color_maps_def.values()
    ]

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(THIS_DIR)))
    template = env.get_template("matplotlib.py.jinja")
    output_path = THIS_DIR.parent.parent / "ok_palette_lab" / "matplotlib.py"
    with open(str(output_path), "w", encoding="utf-8") as file:
        file.write(
            template.render(
                color_maps=color_maps,
            )
        )
        file.write("\n")
    subprocess.run(["black", str(output_path)], check=True)


if __name__ == "__main__":
    generate_script()
