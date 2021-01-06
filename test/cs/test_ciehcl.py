import numpy
import pytest

import colorio


@pytest.mark.parametrize(
    "xyz", [numpy.random.rand(3), numpy.random.rand(3, 7), numpy.random.rand(3, 4, 5)]
)
def test_conversion(xyz):
    ciehcl = colorio.CIEHCL()
    out = ciehcl.to_xyz100(ciehcl.from_xyz100(xyz))
    assert numpy.all(abs(xyz - out) < 1.0e-14)
    return
