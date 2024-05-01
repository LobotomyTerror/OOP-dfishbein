"""Abstract class that inherits from Kattis class
that overrides the super classes methods to
solve the Kattis problem Stacking Cups

    Returns:
        None
"""

from __future__ import annotations

import sys
from typing import Any, Tuple, List
from kattis import Kattis
from ms_derived_class import Sequence


class Cups(Kattis):
    """Child class that uses a Mutable Sequence class
    to solve the Kattis problem

    Args:
        Kattis (class): Abstract Base Class
    """

    def __init__(self, data_source: Any = sys.stdin) -> None:
        """Initializes super class with stdin passed in to read
        data. Also initializes a class instance with the Mutable
        Sequence class object.

        Args:
            data_source (Any, sys): Any type of value,
            or Defaults to sys.stdin.
        """

        super().__init__(data_source)
        self._data: List[str] = []
        self._answer: List[str] = []
        self._cup_data: Sequence = Sequence()
        self.read_input()

    @staticmethod
    def convert_to_radius(color: str, radius: str) -> Tuple[str, str]:
        """If the color variable is an integer then this function
        sets color to the value of radius which is an actual string.
        Then sets radius to half of color which is a diameter

        Args:
            color (str): Diameter needing to be changed to color
            radius (str): Color that needs to be changed to radius

        Returns:
            Tuple[str, str]: The fixed values of color and radius
        """

        new_radius: int = int(int(color) / 2)
        color, radius = radius, str(new_radius)
        return color, radius

    def read_input(self) -> None:
        """Reads in user input and checks if color is a
        digit, then stores in the class instance _cup_data
        a tuple with a string and int
        """

        data = self._input_source.readlines()
        num_of_cups: int = int(data[0].rstrip())
        data.pop(0)
        self._data = [item.rstrip() for item in data]

        for i in range(num_of_cups):
            color, radius = self._data[i].split()
            if color.isdigit():
                color, radius = \
                    self.convert_to_radius(color, radius)
            self._cup_data.append((color, int(radius)))

    def solve(self) -> None:
        """Sorts the _cup_data list by the int value in the
        second position. Then sets answer to the string values
        from the _cup_data list
        """

        self._cup_data.sort(key=lambda i: i[1])
        self._answer = [item[0] for item in self._cup_data]

    @property
    def data(self) -> List[str]:
        """Returns the data stored in the list _data

        Returns:
            List[str]: Strings from the read in user input
        """
        return self._data

    @property
    def answer(self) -> str:
        """Returns a string representation of the answer for the
        Kattis problem that was sorted previous

        Returns:
            str: String of the sorted colors from smallest to largest
            by radius size
        """
        return '\n'.join(self._answer)

    def print_answer(self) -> None:
        """Prints the answer of the string representation
        """

        sys.stdout.write(self.answer)


if __name__ == "__main__":
    cups = Cups()  # pragma: no cover
    cups.solve()  # pragma: no cover
    cups.print_answer()  # pragma: no cover
