---
file_format: mystnb
---

# Sample of Gaussian (Positive and Negative Values)

This page shows some samples of figures using Gaussian function as follows:

```{math}
z = e^{-0.5((x+1)^2 + (y-1)^2)} - e^{-0.5((x-1)^2 + (y+1)^2)}
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

from ok_palette_lab_tools.test_data.gaussian import generate_gaussian_data
```

## Example of Plotting a Heatmap with a Sequential Color Map

```{code-cell}
---
mystnb:
  figure:
    classes: only-light
---
import plotly.graph_objects
import ok_palette_lab.plotly

# Prepare data
x, y, z = generate_gaussian_data()

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.tea,
    zsmooth="best",
)
figure.update_layout(
    title="Heatmap of Gaussian Function",
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

## Example of Plotting a Heatmap with a Diverging Color Map

```{code-cell}
---
mystnb:
  figure:
    classes: only-light
---
import plotly.graph_objects
import ok_palette_lab.plotly

# Prepare data
x, y, z = generate_gaussian_data()

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.blue_red_light,
    # Set zmid=0 for diverging color maps.
    zmid=0,
    zsmooth="best",
)
figure.update_layout(
    title="Heatmap of Gaussian Function",
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
    get_general_color_map_names,
)
from ok_palette_lab_tools.docs.sample_gaussian import plot_gaussian

figure = plot_gaussian(
    color_map_names=get_general_color_map_names(),
    diverging=False,
    version=1,
)
figure.update_layout({
    "title": "Gaussian Function with Sequential Color Maps",
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
from ok_palette_lab_tools.docs.sample_gaussian import plot_gaussian

figure = plot_gaussian(
    color_map_names=get_diverging_color_map_names(),
    diverging=True,
    version=4,
)
figure.update_layout({
    "title": "Gaussian Function with Diverging Color Maps",
    "height": 2200,
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
