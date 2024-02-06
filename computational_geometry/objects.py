class GeometricObject():

    def __init__(self) -> None:
        pass

    @property
    def dimensions() -> int:
        raise NotImplementedError()


class Point(GeometricObject):

    def __init__(self) -> None:
        super().__init__()


class LineSegment(GeometricObject):
    
    def __init__(self) -> None:
        super().__init__()


class Circle(GeometricObject):

    def __init__(self) -> None:
        super().__init__()