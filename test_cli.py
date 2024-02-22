from computational_geometry import objects
from computational_geometry.cli import find_intersections
import math
import pytest

from computational_geometry.objects import LineSegment, Point


def test_find_intersections():
    segment1 = LineSegment(Point(dimensions=2, coordinates=(0, 0)), Point(dimensions=2, coordinates=(2, 2)))
    segment2 = LineSegment(Point(dimensions=2, coordinates=(0, 2)), Point(dimensions=2, coordinates=(2, 0)))
    segment3 = LineSegment(Point(dimensions=2, coordinates=(1, 1)), Point(dimensions=2, coordinates=(3, 3)))

    expected_intersections = [
        Point(dimensions=2, coordinates=(1, 1)),
        Point(dimensions=2, coordinates=(1, 1))
    ]

    with pytest.raises(ValueError):
        assert find_intersections([segment1, segment2, segment3]) == expected_intersections
