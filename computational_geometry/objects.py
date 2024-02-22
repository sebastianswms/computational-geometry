from typing import Optional
import math

class GeometricObject():

    def __init__(self) -> None:
        pass

    def get_dimensions() -> int:
        raise NotImplementedError()


class Point(GeometricObject):

    def __init__(self, dimensions: int, coordinates: tuple[int]) -> None:
        if dimensions != len(coordinates):
            raise ValueError("Number of coordinates must be equal to dimensions.")
        
        self._dimensions: int = dimensions
        self._coordinates: tuple[int] = coordinates

    def get_dimensions(self) -> int:
        return self._dimensions
    
    def get_coordinates(self, dimension: Optional[int] = None) -> int:
        if dimension is None:
            return self._coordinates
        if dimension > self.get_dimensions() - 1:
            raise ValueError(
                f"Maximum value for `dimension` is {self.get_dimensions() - 1}"
            )
        return self._coordinates[dimension]
    
    @staticmethod
    def distance_between(point_a: "Point", point_b: Optional["Point"] = None) -> float:
        if point_b is None:
            point_b = Point(
                dimensions=point_a.get_dimensions(),
                coordinates=tuple(0 for _ in range(point_a.get_dimensions()))
            )
        
        if point_a.get_dimensions() != point_b.get_dimensions():
            raise ValueError("Both points must have the same dimensions.")
        
        a_coords = point_a.get_coordinates()
        b_coords = point_b.get_coordinates()
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(a_coords, b_coords)))


class LineSegment(GeometricObject):

    def __init__(self, point_a: Point, point_b: Point) -> None:
        super().__init__()
        self._point_a: Point = point_a
        self._point_b: Point = point_b
        if point_a.get_dimensions() != point_b.get_dimensions():
            raise ValueError("Start and end points must have the same dimensions.")

    def get_start_point(self) -> Point:
        return self._point_a

    def get_end_point(self) -> Point:
        return self._point_b

    def length(self) -> float:
        return Point.distance_between(self._point_a, self._point_b)


class Circle(GeometricObject):

    def __init__(self) -> None:
        super().__init__()