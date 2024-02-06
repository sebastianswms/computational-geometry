from computational_geometry import objects
import math
import pytest

def test_point():
    my_point = objects.Point(dimensions=2, coordinates=[3,4])
    assert my_point.dimensions == 2
    assert my_point.coordinate() == [3,4]
    assert my_point.coordinate(dimension=0) == 3
    assert my_point.coordinate(dimension=1) == 4
    assert math.isclose(my_point.distance_from(0,0), 5)

    with pytest.raises(Exception):
        my_point.distance_from(12)
    with pytest.raises(Exception):
        my_point.coordinate(dimension=2)
    with pytest.raises(Exception):
        objects.Point(dimensions=2, coordinates=[3,4,5])