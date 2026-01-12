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

from ok_palette_lab_tools.test_data.peaks import generate_peaks_data
```

## Example of Plotting a Heatmap

```{code-cell}
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
    # Specify a color palette here.
    colorscale=ok_palette_lab.plotly.blue_red_light,
    # Set zmid=0 for diverging color palettes.
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

# Renderer specification exists to prevent issues in documentation generation.
figure.show(renderer="notebook_connected")
```

## Example of Plotting a Surface Plot

```{code-cell}
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
    # Specify a color palette here.
    colorscale=ok_palette_lab.plotly.autumn,
))
figure.update_layout(
    title="Surface Plot of Peaks Function",
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
from ok_palette_lab_tools.docs.sample_peaks import plot_peaks

figure = plot_peaks(
    color_palette_names=get_general_color_palette_names(),
    diverging=False,
    version=4,
)
figure.update_layout({
    "title": "Peaks Function with General Color Palettes",
    "height": 1300,
})
figure.show(renderer="notebook_connected")
```

```{code-cell}
:tags: ["remove-input"]

from ok_palette_lab_tools.color_palettes.color_palette_names import (
    get_diverging_color_palette_names,
)
from ok_palette_lab_tools.docs.sample_peaks import plot_peaks

figure = plot_peaks(
    color_palette_names=get_diverging_color_palette_names(),
    diverging=True,
    version=4,
)
figure.update_layout({
    "title": "Peaks Function with Diverging Color Palettes",
    "height": 1300,
})
figure.show(renderer="notebook_connected")
```
