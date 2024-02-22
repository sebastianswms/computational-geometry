from computational_geometry import objects as o
import math
import pytest

def test_point():
    my_point = o.Point(dimensions=2, coordinates=(3,4))
    assert my_point.get_dimensions() == 2
    assert my_point.get_coordinates() == (3,4)
    assert my_point.get_coordinates(dimension=0) == 3
    assert my_point.get_coordinates(dimension=1) == 4

    assert math.isclose(o.Point.distance_between(my_point), 5.0)
    another_point = o.Point(dimensions=2, coordinates=(8,16))
    assert math.isclose(o.Point.distance_between(my_point, another_point), 13.0)

    with pytest.raises(ValueError):
        my_point.get_coordinates(dimension=2)
    with pytest.raises(ValueError):
        o.Point(dimensions=2, coordinates=(3,4,5))

def test_circle():
    center_point = o.Point(dimensions=2, coordinates=(3, 4))
    my_circle = o.Circle(center=center_point, radius=5)
    assert my_circle.get_center() == center_point
    assert my_circle.get_radius() == 5
    assert math.isclose(my_circle.area(), 25 * math.pi)
    assert math.isclose(my_circle.circumference(), 10 * math.pi)
    assert math.isclose(my_circle.diameter(), 10)
