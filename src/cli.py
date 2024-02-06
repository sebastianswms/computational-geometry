"""A practice project for CS4910 with computational geometry. """

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