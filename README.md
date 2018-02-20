# colorio

Tools for color models.

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/colorio/master.svg)](https://circleci.com/gh/nschloe/colorio/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/colorio.svg)](https://codecov.io/gh/nschloe/colorio)
[![Codacy grade](https://img.shields.io/codacy/grade/b23fbc2af9884315bd7d6275aa2629b6.svg)](https://app.codacy.com/app/nschloe/colorio/dashboard)
[![awesome](https://img.shields.io/badge/awesome-yes-brightgreen.svg)](https://github.com/nschloe/colorio)
[![PyPi Version](https://img.shields.io/pypi/v/colorio.svg)](https://pypi.python.org/pypi/colorio)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1172995.svg)](https://doi.org/10.5281/zenodo.1172995)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/colorio.svg?style=social&label=Stars)](https://github.com/nschloe/colorio)

All methods in colorio are fully vectorized.

### Color spaces

All color spaces implement the two methods
```python
vals = colorspace.from_xyz100(xyz)
xyz = colorspace.to_xyz100(vals)
```
for conversion from and to XYZ100. Adding new color spaces is as easy as
writing a class that provides those two methods.

The following color spaces are implemented:

 * [XYZ](https://en.wikipedia.org/wiki/CIE_1931_color_space) (`colorio.XYZ()`)
 * [xyY](https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xy_chromaticity_diagram_and_the_CIE_xyY_color_space) (`colorio.XYY()`)
 * [Linear SRGB](https://en.wikipedia.org/wiki/SRGB)  (`colorio.SrgbLinear()`)
   This class has the two additional methods
   ```
   from_srgb1()
   to_srgb1()
   ```
   for conversion from and to standard RGB.
 * [CIELAB](https://en.wikipedia.org/wiki/Lab_color_space) (`colorio.CIELAB()`)
 * [CIELUV](https://en.wikipedia.org/wiki/CIELUV) (`colorio.CIELUV()`)
 * [ICtCp](https://en.wikipedia.org/wiki/ICtCp) (`colorio.ICtCp()`)
 * [IPT](http://www.ingentaconnect.com/content/ist/cic/1998/00001998/00000001/art00003)
   (`colorio.IPT()`)
 * [CIECAM02 / CAM02-UCS](https://en.wikipedia.org/wiki/CIECAM02)
   ```python
   import colorio
   L_A = 64 / numpy.pi / 5
   ciecam02 = colorio.CIECAM02(0.69, 20, L_A)
   cam02 = colorio.CAM02('UCS', 0.69, 20, L_A)
   ```
   The implementation contains a few improvements over the CIECAM02
   specification (see [here](https://arxiv.org/abs/1802.06067)).
 * [CAM16 / CAM16-UCS](https://doi.org/10.1002/col.22131)
   ```python
   import colorio
   L_A = 64 / numpy.pi / 5
   cam16 = colorio.CAM16(0.69, 20, L_A)
   cam16ucs = colorio.CAM16UCS(0.69, 20, L_A)
   ```
   The implementation contains a few improvements over the CAM16
   specification (see [here](https://arxiv.org/abs/1802.06067)).
 * [J<sub>z</sub>a<sub>z</sub>b<sub>z</sub>](https://doi.org/10.1364/OE.25.015131)
   (`colorio.JzAzBz()`)


### Tools

colorio provides a number of useful tools for analyzing and visualizing color
spaces.

#### Visualizing the SRGB gamut

<img src="https://nschloe.github.io/colorio/cielab.png" width="40%">

The SRGB gamut is a perfect cube in SRGB space, and takes curious shapes when
translated into other color spaces. The above image shows the SRGB gamut in XYZ
space. The image data was created with
```python
import colorio

colorspace = colorio.CIELAB()
colorio.show_srgb_gamut(colorspace, 'out.vtu', n=50, cut_000=False)
```
The [VTU](https://www.vtk.org/VTK/img/file-formats.pdf) file can then be opened
in, e.g., ParaView. To see the coloring, select the `srgb` data and disable
`Map Scalars`. You might also want to disable the Light Kit.

The data can be written in all formats supported by
[meshio](https://github.com/nschloe/meshio).

#### Visualizing the visible gamut

<img src="https://nschloe.github.io/colorio/xyz-visible-d65.png" width="40%">

Same as above, but with the gamut visible under a given illuminant.
```python
import colorio

colorspace = colorio.XYZ()
illuminant = colorio.illuminants.d65()
observer = colorio.observers.cie_1931_2()
colorio.show_visible_gamut(colorspace, observer, illuminant, 'visible.vtu')
```
The gamut is shown in grey since SRGB screens are not able to display the
colors.

#### Show experimental data

<img src="https://nschloe.github.io/colorio/ebner_fairchild_jzazbz.png" width="40%">

colorio contains lots of experimental data sets some of which can be used to
assess certain properties of color spaces.

For example
```python
import colorio

colorspace = colorio.JzAzBz()
colorio.show_ebner_fairchild(colorspace)
```
shows constant-hue data from [the Ebner-Fairchild
experiments](https://doi.org/10.1117/12.298269) in the
a<sub>z</sub>b<sub>z</sub>-plane of the J<sub>z</sub>a<sub>z</sub>b<sub>z</sub>
color space. (Ideally, all colors in one set sit on a line.)


#### Color differences

Color differences in any space can be computed with `colorio.delta(a, b)`.

The images below all show the SRGB gamut in the respective color space.


### Installation

colorio is [available from the Python Package Index](https://pypi.python.org/pypi/colorio/), so with
```
pip install -U colorio
```
you can install/upgrade.

### Testing

To run the tests, simply check out this repository and run
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    $ make publish
    ```

### License
colorio is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
