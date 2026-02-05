---
file_format: mystnb
---

# Color Maps

```{code-cell}
:tags: ["remove-input"]

# Required to show figures.
import plotly.io
plotly.io.renderers.default = "notebook_connected"
```

## Sequential Color Maps for General Ranges

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-light
---
from ok_palette_lab_tools.docs.color_maps import plot_color_maps
from ok_palette_lab_tools.color_maps.color_map_names import (
    get_general_color_map_names,
)

figure = plot_color_maps(
    color_map_names=get_general_color_map_names(),
    z_range=(0.0, 1.0),
)
figure.update_layout(height=1000)
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

## Diverging Color Maps for 0-Centered Ranges

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-light
---
from ok_palette_lab_tools.docs.color_maps import plot_color_maps
from ok_palette_lab_tools.color_maps.color_map_names import (
    get_diverging_color_map_names,
)

figure = plot_color_maps(
    color_map_names=get_diverging_color_map_names(),
    z_range=(-1.0, 1.0),
)
figure.update_layout(height=900)
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

## Cyclic Color Maps for Circular Ranges

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-light
---
from ok_palette_lab_tools.docs.color_maps import plot_color_maps
from ok_palette_lab_tools.color_maps.color_map_names import (
    get_cyclic_color_map_names,
)

figure = plot_color_maps(
    color_map_names=get_cyclic_color_map_names(),
    z_range=(0.0, 1.0),
)
figure.update_layout(height=250)
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
