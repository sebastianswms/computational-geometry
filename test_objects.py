from computational_geometry import objects
import math
import pytest

def test_point():
    my_point = objects.Point(dimensions=2, coordinates=(3,4))
    assert my_point.get_dimensions() == 2
    assert my_point.get_coordinates() == (3,4)
    assert my_point.get_coordinates(dimension=0) == 3
    assert my_point.get_coordinates(dimension=1) == 4

    assert math.isclose(objects.Point.distance_between(my_point), 5.0)
    another_point = objects.Point(dimensions=2, coordinates=(8,16))
    assert math.isclose(objects.Point.distance_between(my_point, another_point), 13.0)

    with pytest.raises(ValueError):
        my_point.get_coordinates(dimension=2)
    with pytest.raises(ValueError):
        objects.Point(dimensions=2, coordinates=(3,4,5))