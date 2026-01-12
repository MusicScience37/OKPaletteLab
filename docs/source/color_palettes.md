---
file_format: mystnb
---

# Color Palettes

## Color Palettes for General Ranges

```{code-cell}
:tags: ["remove-input"]
from ok_palette_lab_tools.docs.color_palettes import plot_color_palettes

figure = plot_color_palettes(
    color_palette_names=[
        "autumn",
        "autumn_wide",
        "ocean",
        "ocean_wide",
        "red",
        "red_wide",
    ],
    z_range=(0.0, 1.0),
)
figure.update_layout(height=600)
figure.show(renderer="notebook_connected")
```

## Diverging Color Palettes for 0-Centered Ranges

```{code-cell}
:tags: ["remove-input"]
from ok_palette_lab_tools.docs.color_palettes import plot_color_palettes

figure = plot_color_palettes(
    color_palette_names=[
        "blue_brown_white",
        "blue_brown_white_wide",
        "blue_brown_light",
        "blue_brown_light_wide",
        "blue_red_white",
        "blue_red_white_wide",
        "blue_red_light",
        "blue_red_light_wide",
    ],
    z_range=(-1.0, 1.0),
)
figure.update_layout(height=800)
figure.show(renderer="notebook_connected")
```
