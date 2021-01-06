import numpy
import pytest

import colorio


@pytest.mark.parametrize(
    "xyz", [numpy.random.rand(3), numpy.random.rand(3, 7), numpy.random.rand(3, 4, 5)]
)
def test_conversion(xyz):
    xyy = colorio.XYY()
    out = xyy.to_xyz100(xyy.from_xyz100(xyz))
    assert numpy.all(abs(xyz - out) < 1.0e-14)
    return
