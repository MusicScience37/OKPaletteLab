---
file_format: mystnb
---

# Samples of Peaks Function

This page shows some samples of figures using [peaks function in MATLAB](https://jp.mathworks.com/help/matlab/ref/peaks.html).

```{math}
z = 3(1-x)^2 e^{-x^2 - (y+1)^2}
    -10 \left(\frac{x}{5} - x^3 - y^5 \right) e^{-x^2-y^2}
    -\frac{1}{3} e^{-(x+1)^2 - y^2}
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

from ok_palette_lab_tools.test_data.peaks import generate_peaks_data
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
x, y, z = generate_peaks_data()

# Create a heatmap
figure = plotly.graph_objects.Figure()
figure.add_heatmap(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.tea,
    # Set zmid=0 for diverging color maps.
    zmid=0,
    zsmooth="best",
)
figure.update_layout(
    title="Heatmap of Peaks Function",
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
x, y, z = generate_peaks_data()

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
    title="Heatmap of Peaks Function",
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

## Example of Plotting a Surface Plot

```{code-cell}
---
mystnb:
  figure:
    classes: only-light
---
import plotly.graph_objects
import ok_palette_lab.plotly

# Prepare data
x, y, z = generate_peaks_data()

# Create a surface plot
figure = plotly.graph_objects.Figure()
figure.add_trace(plotly.graph_objects.Surface(
    z=z,
    x=x,
    y=y,
    # Specify a color map here.
    colorscale=ok_palette_lab.plotly.autumn,
))
figure.update_layout(
    title="Surface Plot of Peaks Function",
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
from ok_palette_lab_tools.docs.sample_peaks import plot_peaks

figure = plot_peaks(
    color_map_names=get_general_color_map_names(),
    diverging=False,
    version=4,
)
figure.update_layout({
    "title": "Peaks Function with Sequential Color Maps",
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
from ok_palette_lab_tools.docs.sample_peaks import plot_peaks

figure = plot_peaks(
    color_map_names=get_diverging_color_map_names(),
    diverging=True,
    version=4,
)
figure.update_layout({
    "title": "Peaks Function with Diverging Color Maps",
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
