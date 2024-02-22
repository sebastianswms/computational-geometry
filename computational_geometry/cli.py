"""A practice project for CS4910 with computational geometry. """

from typing import List, Optional
import argparse


class Manager():

    def __init__(self, args) -> None:
        self.args = args


def main():
    # Set up parser description and arguments.
    desc = "A practice project for CS4910 with computational geometry."
    parser = argparse.ArgumentParser(description=desc)
    exmp_help = "Example arg help"
    parser.add_argument("-e", help=exmp_help, required=True, type=int)

    args = parser.parse_args()
    my_manager = Manager(args)

    # Execute Manager() functions

    # Print output.
    print("Program has executed")


def intersection(line1: LineSegment, line2: LineSegment) -> Optional[Point]:
    p1 = line1.get_start_point().get_coordinates()
    p2 = line1.get_end_point().get_coordinates()
    p3 = line2.get_start_point().get_coordinates()
    p4 = line2.get_end_point().get_coordinates()

    dimensions = len(p1)

    denominator = 0
    for i in range(dimensions):
        denominator += (p4[i] - p3[i]) * (p2[(i + 1) % dimensions] - p1[(i + 1) % dimensions]) - (
                    p4[(i + 1) % dimensions] - p3[(i + 1) % dimensions]) * (p2[i] - p1[i])

    if denominator == 0:
        return None

    ua = [0] * dimensions
    ub = [0] * dimensions
    for i in range(dimensions):
        ua[i] = ((p4[i] - p3[i]) * (p1[(i + 1) % dimensions] - p3[(i + 1) % dimensions]) - (
                    p4[(i + 1) % dimensions] - p3[(i + 1) % dimensions]) * (p1[i] - p3[i])) / denominator
        ub[i] = ((p2[i] - p1[i]) * (p1[(i + 1) % dimensions] - p3[(i + 1) % dimensions]) - (
                    p2[(i + 1) % dimensions] - p1[(i + 1) % dimensions]) * (p1[i] - p3[i])) / denominator

    for i in range(dimensions):
        if not (0 <= ua[i] <= 1 and 0 <= ub[i] <= 1):
            return None

    intersection_coords = []
    for i in range(dimensions):
        intersection_coords.append(p1[i] + ua[i] * (p2[i] - p1[i]))

    return Point(dimensions=dimensions, coordinates=tuple(intersection_coords))


def find_intersections(lines: List[LineSegment]) -> List[Point]:
    intersections = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            intersect = intersection(lines[i], lines[j])
            if intersect:
                intersections.append(intersect)
    return intersections
