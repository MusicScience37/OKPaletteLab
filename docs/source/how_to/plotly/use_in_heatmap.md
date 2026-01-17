---
file_format: mystnb
---

# Use in Heatmap of Plotly

This page shows how to use a color map from OKPaletteLab library in a heatmap created with Plotly.

```{code-cell}
:tags: ["remove-input"]

# Required to show figures.
import plotly.io
plotly.io.renderers.default = "notebook_connected"
```

## Example of Heatmap

```{code-cell}
import numpy
import plotly.graph_objects

import ok_palette_lab.plotly

# Prepare data
x = numpy.linspace(-2, 3, 101)
y = numpy.linspace(-2, 3, 101)
x_grid, y_grid = numpy.meshgrid(x, y)
z = numpy.exp(-x_grid**2 - y_grid**2)

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.autumn,
    zsmooth="best",
)

figure.show()
```

## Example to Reverse the Order of Colors

```{code-cell}
import numpy
import plotly.graph_objects

import ok_palette_lab.plotly

# Prepare data
x = numpy.linspace(-2, 3, 101)
y = numpy.linspace(-2, 3, 101)
x_grid, y_grid = numpy.meshgrid(x, y)
z = numpy.exp(-x_grid**2 - y_grid**2)

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.autumn,
    # Reverse the order of colors in the color map.
    reversescale=True,
    zsmooth="best",
)

figure.show()
```
