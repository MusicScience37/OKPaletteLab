---
file_format: mystnb
---

# Samples of Arctan Function in 2D

This page shows some samples of figures using arctan function in 2D.

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

from ok_palette_lab_tools.test_data.arctan_2d import generate_arctan_2d_data
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
x, y, z = generate_arctan_2d_data()

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.equal_hue,
    zmin=0.0,
    zmax=360.0,
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
