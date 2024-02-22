from computational_geometry.cli import find_intersections
from computational_geometry.objects import Point, LineSegment
import math
import pytest


def test_find_intersections():
    # Test find_intersections function
    lines = [
        LineSegment(Point(dimensions=2, coordinates=(0, 0)), Point(dimensions=2, coordinates=(2, 2))),
        LineSegment(Point(dimensions=2, coordinates=(0, 2)), Point(dimensions=2, coordinates=(2, 0))),
        LineSegment(Point(dimensions=2, coordinates=(1, 1)), Point(dimensions=2, coordinates=(3, 3)))
    ]
    assert find_intersections(lines) == [Point(dimensions=2, coordinates=(1, 1))]
