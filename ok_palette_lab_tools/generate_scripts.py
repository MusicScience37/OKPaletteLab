"""Generate scripts in the library."""

from ok_palette_lab_tools.matplotlib.generate_script import (
    generate_script as generate_matplotlib_script,
)
from ok_palette_lab_tools.plotly.generate_script import (
    generate_script as generate_plotly_script,
)

if __name__ == "__main__":
    generate_plotly_script()
    generate_matplotlib_script()
