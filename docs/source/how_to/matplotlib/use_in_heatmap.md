---
file_format: mystnb
---

# Use in Heatmap of Matplotlib

This page shows how to use a color map from OKPaletteLab library in a heatmap created with matplotlib.

## Example of Heatmap

```{code-cell}
---
mystnb:
  figure:
    classes: only-light
---
import numpy
import matplotlib.pyplot

import ok_palette_lab.matplotlib

# Prepare data
x = numpy.linspace(-2, 3, 101)
y = numpy.linspace(-2, 3, 101)
x_grid, y_grid = numpy.meshgrid(x, y)
z = numpy.exp(-x_grid**2 - y_grid**2)

# Create a heatmap
figure, axes = matplotlib.pyplot.subplots()
heatmap = axes.imshow(
    z,
    extent=(x.min(), x.max(), y.min(), y.max()),
    origin="lower",
    # Specify a color map here.
    cmap=ok_palette_lab.matplotlib.autumn,
    interpolation="bilinear",
)
figure.colorbar(heatmap)
matplotlib.pyplot.show()
```

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-dark
---
matplotlib.pyplot.style.use("dark_background")
figure, axes = matplotlib.pyplot.subplots()
heatmap = axes.imshow(
    z,
    extent=(x.min(), x.max(), y.min(), y.max()),
    origin="lower",
    # Specify a color map here.
    cmap=ok_palette_lab.matplotlib.autumn,
    interpolation="bilinear",
)
figure.colorbar(heatmap)
matplotlib.pyplot.show()
```

```{code-cell}
:tags: [remove-input]
matplotlib.pyplot.style.use("default")
```

## Example to Reverse the Order of Colors

```{code-cell}
---
mystnb:
  figure:
    classes: only-light
---
import numpy
import matplotlib.pyplot

import ok_palette_lab.matplotlib

# Prepare data
x = numpy.linspace(-2, 3, 101)
y = numpy.linspace(-2, 3, 101)
x_grid, y_grid = numpy.meshgrid(x, y)
z = numpy.exp(-x_grid**2 - y_grid**2)

# Create a heatmap
figure, axes = matplotlib.pyplot.subplots()
heatmap = axes.imshow(
    z,
    extent=(x.min(), x.max(), y.min(), y.max()),
    origin="lower",
    # Specify a color map here with reversed order.
    cmap=ok_palette_lab.matplotlib.autumn.reversed(),
    interpolation="bilinear",
)
figure.colorbar(heatmap)
matplotlib.pyplot.show()
```

```{code-cell}
---
tags: [remove-input]
mystnb:
  figure:
    classes: only-dark
---
matplotlib.pyplot.style.use("dark_background")
figure, axes = matplotlib.pyplot.subplots()
heatmap = axes.imshow(
    z,
    extent=(x.min(), x.max(), y.min(), y.max()),
    origin="lower",
    # Specify a color map here.
    cmap=ok_palette_lab.matplotlib.autumn.reversed(),
    interpolation="bilinear",
)
figure.colorbar(heatmap)
matplotlib.pyplot.show()
```

```{code-cell}
:tags: [remove-input]
matplotlib.pyplot.style.use("default")
```

## Next Steps

- See [Color Maps](../../color_maps.md) for other color maps available in OKPaletteLab.
