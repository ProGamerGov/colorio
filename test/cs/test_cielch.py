import numpy
import pytest

import colorio


@pytest.mark.parametrize(
    "xyz,ref",
    [
        ([10, 20, 30], [51.8372, 57.8800, 193.1636]),
        ([80, 90, 10], [95.9968, 103.4134, 95.9163]),
    ],
)
def test_reference_xyz(xyz, ref):
    cs = colorio.cs.CIELCH()
    xyz = numpy.array(xyz)
    ref = numpy.array(ref)
    assert numpy.all(abs(cs.from_xyz100(xyz) - ref) < 1.0e-4 * ref)


@pytest.mark.parametrize(
    "vals,ref",
    [
        ([10, 20, 30], [51.8372, 63.0026, 204.1543]),
        ([80, 90, 10], [95.9968, 95.0085, 97.8122]),
    ],
)
def test_reference_xyz_d50(vals, ref):
    cs = colorio.cs.CIELCH(whitepoint=numpy.array([96.422, 100, 82.521]) / 100)
    xyz = numpy.array(vals) / 100
    assert numpy.all(abs(cs.from_xyz100(xyz) - ref) < 1.0e-6 * abs(numpy.array(ref)))
