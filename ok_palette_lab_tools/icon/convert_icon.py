"""Convert icon files in PNG format.

See `docs/icon/design/note.md` for details.
"""

import pathlib
import subprocess

THIS_DIR = pathlib.Path(__file__).absolute().parent
ICON_DIR = THIS_DIR.parent.parent / "docs" / "icon"


def _execute_command(command: list[str]) -> None:
    """Execute a command.

    Args:
        command (list[str]): Command and its arguments as a list of strings.
    """
    print(f"Executing command: {' '.join(command)}")
    subprocess.run(command, check=True)


def generate_icon_png() -> None:
    """Generate PNG files of the icon."""
    sizes = [192]  # Add more sizes if needed.

    input_png = ICON_DIR / "icon1024.png"
    for size in sizes:
        output_png = ICON_DIR / f"icon{size}.png"
        command = [
            "convert",
            "-density",
            "1024",
            "-quality",
            "90",
            str(input_png),
            "-resize",
            f"{size}x{size}",
            str(output_png),
        ]
        _execute_command(command)


def generate_icon_ico() -> None:
    """Generate ICO file of the icon."""
    input_png = ICON_DIR / "icon1024.png"
    output_ico = ICON_DIR / "icon.ico"
    command = [
        "convert",
        "-define",
        "icon:auto-resize=192,64,48,32,16",
        str(input_png),
        str(output_ico),
    ]
    _execute_command(command)


def main() -> None:
    """Main function."""
    generate_icon_png()
    generate_icon_ico()


if __name__ == "__main__":
    main()
