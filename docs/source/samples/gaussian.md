---
file_format: mystnb
---

# Samples of Gaussian (Positive Values)

This page show some samples of figures using Gaussian function as follows:

```{math}
z = e^{-((x+1)^2 + (y-1)^2)/2} + 0.3 e^{-((x-1)^2 + (y+1)^2)/2}
```

```{code-cell}
:tags: ["remove-input"]

from ok_palette_lab_tools.test_data.gaussian import generate_positive_gaussian_data
```

## Example of Plotting a Heatmap

```{code-cell}
import plotly.graph_objects
import ok_palette_lab.plotly

# Prepare data
x, y, z = generate_positive_gaussian_data()

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color palette here.
    colorscale=ok_palette_lab.plotly.purple_green_yellow,
    zsmooth="best",
)
figure.update_layout(
    title="Heatmap of Gaussian Function",
    yaxis={
        "scaleanchor": "x",
        "scaleratio": 1,
    },
)

# Renderer specification exists to prevent issues in documentation generation.
figure.show(renderer="notebook_connected")
```

## Other Color Palettes

```{code-cell}
:tags: ["remove-input"]

from ok_palette_lab_tools.color_palettes.color_palette_names import (
    get_general_color_palette_names,
)
from ok_palette_lab_tools.docs.sample_gaussian import plot_gaussian

figure = plot_gaussian(
    color_palette_names=get_general_color_palette_names(),
    version=1,
)
figure.update_layout({
    "title": "Gaussian Function with General Color Palettes",
    "height": 1300,
})
figure.show(renderer="notebook_connected")
```
