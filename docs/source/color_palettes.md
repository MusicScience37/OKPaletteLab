---
file_format: mystnb
---

# Color Palettes

## Color Palettes for General Ranges

```{code-cell}
:tags: ["remove-input"]
from ok_palette_lab_tools.docs.color_palettes import plot_color_palettes
from ok_palette_lab_tools.color_palettes.color_palette_names import (
    get_general_color_palette_names,
)

figure = plot_color_palettes(
    color_palette_names=get_general_color_palette_names(),
    z_range=(0.0, 1.0),
)
figure.update_layout(height=800)
figure.show(renderer="notebook_connected")
```

## Diverging Color Palettes for 0-Centered Ranges

```{code-cell}
:tags: ["remove-input"]
from ok_palette_lab_tools.docs.color_palettes import plot_color_palettes
from ok_palette_lab_tools.color_palettes.color_palette_names import (
    get_diverging_color_palette_names,
)

figure = plot_color_palettes(
    color_palette_names=get_diverging_color_palette_names(),
    z_range=(-1.0, 1.0),
)
figure.update_layout(height=800)
figure.show(renderer="notebook_connected")
```
