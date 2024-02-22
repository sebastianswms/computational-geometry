"""A practice project for CS4910 with computational geometry. """

import argparse
from computational_geometry import objects


def main():
    # Set up parser description and arguments.
    desc = "A practice project for CS4910 with computational geometry."
    parser = argparse.ArgumentParser(description=desc)
    exmp_help = "Example arg help"
    parser.add_argument("-e", help=exmp_help, required=True, type=int)

    args = parser.parse_args()
    my_manager = objects.Manager(args)

    # Execute Manager() functions

    # Print output.
    print("Program has executed")
