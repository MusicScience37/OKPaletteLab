---
file_format: mystnb
---

# Samples of Spiral Pattern

This page shows some samples of figures using spiral patterns.

Spiral pattern was calculated using polar coordinates as follows:

```{math}
z = e^{-r^2} \sin(3 \theta + 10 r)
```

```{code-cell}
:tags: ["remove-input"]

# Required to show figures.
import plotly.io
plotly.io.renderers.default = "notebook_connected"

# Change default template
plotly.io.templates.default = "plotly_white"
```

```{code-cell}
:tags: ["remove-input"]

from ok_palette_lab_tools.test_data.spiral_pattern import generate_spiral_pattern_data
```

## Example of Plotting a Heatmap

```{code-cell}
---
mystnb:
  figure:
    classes: only-light
---
import plotly.graph_objects
import ok_palette_lab.plotly

# Prepare data
x, y, z = generate_spiral_pattern_data()

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.blue_red_light_wide,
    # Set zmid=0 for diverging color maps.
    zmid=0,
    zsmooth="best",
)
figure.update_layout(
    title="Heatmap of Spiral Pattern",
    yaxis={
        "scaleanchor": "x",
        "scaleratio": 1,
    },
)

figure.show()
```

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-dark
---
figure.update_layout(template="plotly_dark")
figure.show()
```

## Other Color Maps

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-light
---

from ok_palette_lab_tools.color_maps.color_map_names import (
    get_diverging_color_map_names,
)
from ok_palette_lab_tools.docs.sample_spiral_patter import plot_spiral_pattern

figure = plot_spiral_pattern(
    color_map_names=get_diverging_color_map_names(),
    diverging=True,
    version=4,
)
figure.update_layout({
    "title": "Spiral Pattern with Diverging Color Maps",
    "height": 1600,
})
figure.show()
```

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-dark
---
figure.update_layout(template="plotly_dark")
figure.show()
```
