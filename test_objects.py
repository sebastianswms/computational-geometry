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

def test_closest_pair()

    a = o.Point(2,(0,0))
    b = o.Point(2,(3,4))
    c = o.Point(2,(0,8))
    d = o.Point(2,(8,5))
    e = o.Point(2,(12,3))
    f = o.Point(2,(9,16))
    g = o.Point(2,(9,16))

    manager = Manager("args")
    with pytest.raises(ValueError):
        assert manager.closest_pair(set(a))
    assert manager.closest_pair(set(a,b)) == set(a,b)
    with pytest.raises(RuntimeError):
        assert manager.closest_pair(set(a,b,c))
    assert manager.closest_pair(set(a,b,c,d,e,f)) == set(d,e)
    assert manager.closest_pair(set(a,b,c,d,e,f,g)) == set(f,g)