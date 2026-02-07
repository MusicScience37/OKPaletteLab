# OKPaletteLab

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ok_palette_lab)
[![PyPI - Version](https://img.shields.io/pypi/v/ok_palette_lab)](https://pypi.org/project/ok_palette_lab/)
![PyPI - License](https://img.shields.io/pypi/l/ok_palette_lab)
![Gitlab pipeline status](https://img.shields.io/gitlab/pipeline-status/MusicScience37Projects%2Futility-libraries%2FOKPaletteLab?branch=main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

![Icon](docs/icon/icon_for_docs.svg)

Smooth color maps for Plotly and Matplotlib.

- Color maps are designed in the Oklch color space to create smooth gradients and improve data visualization.
- The following types of color maps are provided:
  - **Sequential** color maps for general ranges.
  - **Diverging** color maps for ranges centered at zero.
    This project provides diverging color maps for both light and dark modes.
  - **Cyclic** color maps for periodic ranges.
- Currently supports the following libraries:
  - [Plotly (graphing library for Python)](https://plotly.com/python/)
  - [Matplotlib](https://matplotlib.org/)

## Sample Figures

### Sample Figures in Light Mode

![Sample figure in light mode](docs/images/combined.png)

### Sample Figures in Dark Mode

![Sample figure in dark mode](docs/images/combined_dark.png)

## Installation

You can install the package via pip:

```bash
pip install ok_palette_lab
```

## Basic Usage

- With Plotly:
  - [`ok_palette_lab.plotly` package](https://okpalettelab.musicscience37.com/api/ok_palette_lab.plotly.html)
    provides color maps (called "color scales" in Plotly).
  - Select one and use it as follows:

    ```python
    figure = plotly.graph_objects.Figure()
    figure.add_heatmap(
        # ... your data here ...

        # Specify a color map.
        colorscale=ok_palette_lab.plotly.autumn,
    )
    ```

- With matplotlib:
  - [`ok_palette_lab.matplotlib` package](https://okpalettelab.musicscience37.com/api/ok_palette_lab.matplotlib.html)
    has color maps.
  - Select one and use it as follows:

    ```python
    figure, axes = matplotlib.pyplot.subplots()
    heatmap = axes.imshow(
        # ... your data here ...

        # Specify a color map.
        cmap=ok_palette_lab.matplotlib.autumn,
    )
    ```

## Simple Examples

- [Example of a heatmap using Plotly](https://okpalettelab.musicscience37.com/how_to/plotly/use_in_heatmap.html)
- [Example of a heatmap using matplotlib](https://okpalettelab.musicscience37.com/how_to/matplotlib/use_in_heatmap.html)

## Documentation

Documentation is available at [web site](https://okpalettelab.musicscience37.com/).
Documentation for each version can be viewed using the version switcher at the bottom left of the page.

## Development

This project was created in January 2026 and is under active development.
The following features are planned for future releases:

- Support for more graphing libraries in Python.
- Support for ParaView.

## Repositories

- [Main repository on GitLab](https://gitlab.com/MusicScience37Projects/utility-libraries/OKPaletteLab)
- [Mirror on GitHub](https://github.com/MusicScience37/OKPaletteLab)

## License

This project is licensed under the MIT License.
See [LICENSE.txt](LICENSE.txt) for details.

Graphics created using the color maps in this project can be used freely without restriction.
