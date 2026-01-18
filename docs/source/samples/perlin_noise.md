---
file_format: mystnb
---

# Samples of Perlin Noise

This page shows some samples of figures using Perlin noise.

Perlin noise was generated using
[noise](https://github.com/caseman/noise) package.

```{code-cell}
:tags: ["remove-input"]

# Required to show figures.
import plotly.io
plotly.io.renderers.default = "notebook_connected"
```

```{code-cell}
:tags: ["remove-input"]

from ok_palette_lab_tools.test_data.perlin_noise import generate_perlin_noise_data
```

## Example of Plotting a Heatmap

```{code-cell}
import plotly.graph_objects
import ok_palette_lab.plotly

# Prepare data
x, y, z = generate_perlin_noise_data()

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.blue_brown_light,
    # Set zmid=0 for diverging color maps.
    zmid=0,
)
figure.update_layout(
    title="Heatmap of Perlin Noise",
    yaxis={
        "scaleanchor": "x",
        "scaleratio": 1,
    },
)

figure.show()
```

## Other Color Maps

```{code-cell}
:tags: ["remove-input"]

from ok_palette_lab_tools.color_maps.color_map_names import (
    get_general_color_map_names,
)
from ok_palette_lab_tools.docs.sample_perlin_noise import plot_perlin_noise

figure = plot_perlin_noise(
    color_map_names=get_general_color_map_names(),
    diverging=False,
    version=4,
)
figure.update_layout({
    "title": "Perlin Noise with General Color Maps",
    "height": 1600,
})
figure.show()
```

```{code-cell}
:tags: ["remove-input"]

from ok_palette_lab_tools.color_maps.color_map_names import (
    get_diverging_color_map_names,
)
from ok_palette_lab_tools.docs.sample_perlin_noise import plot_perlin_noise

figure = plot_perlin_noise(
    color_map_names=get_diverging_color_map_names(),
    diverging=True,
    version=4,
)
figure.update_layout({
    "title": "Perlin Noise with Diverging Color Maps",
    "height": 1600,
})
figure.show()
```
