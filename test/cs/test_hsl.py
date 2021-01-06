import numpy
import pytest

import colorio

numpy.random.seed(2)


@pytest.mark.parametrize(
    "vals,ref",
    [
        ([10, 20, 30], [210, 0.5, 4 / 51]),
        ([110, 120, 130], [210, 25 / 300, 8 / 17]),
        ([210, 220, 230], [210, 2 / 7, 44 / 51]),
    ],
)
def test_reference_srgb(vals, ref):
    hsl = colorio.cs.HSL()
    assert numpy.all(abs(hsl.from_srgb256(vals) - ref) < 1.0e-14 * numpy.array(ref))


@pytest.mark.parametrize(
    "vals",
    [
        numpy.random.rand(3),
        numpy.random.rand(3, 7),
        numpy.random.rand(3, 4, 5),
        [1.0, 1.0, 1.0],
    ],
)
def test_conversion(vals):
    hsl = colorio.cs.HSL()
    out = hsl.to_srgb1(hsl.from_srgb1(vals))
    assert numpy.all(abs(vals - out) < 1.0e-14)
