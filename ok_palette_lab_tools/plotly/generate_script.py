"""Generate script for Plotly color palettes."""

import pathlib
import subprocess

import jinja2

from ok_palette_lab_tools.color_palettes.color_palette_def import (
    load_color_palettes_def,
)
from ok_palette_lab_tools.color_palettes.generate_color_palette import (
    generate_color_palette,
)

THIS_DIR = pathlib.Path(__file__).absolute().parent


def generate_script() -> None:
    """Generate script for Plotly color palettes."""
    color_palettes_def = load_color_palettes_def()
    color_palettes = [
        generate_color_palette(definition) for definition in color_palettes_def.values()
    ]

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(THIS_DIR)))
    template = env.get_template("plotly.py.jinja")
    output_path = THIS_DIR.parent.parent / "ok_palette_lab" / "plotly.py"
    with open(str(output_path), "w", encoding="utf-8") as file:
        file.write(
            template.render(
                color_palettes=color_palettes,
            )
        )
        file.write("\n")
    subprocess.run(["black", str(output_path)], check=True)


if __name__ == "__main__":
    generate_script()
