from __future__ import annotations

import sys
from typing import Any, Tuple, List
from kattis import Kattis
from ms_derived_class import Sequence


class Cups(Kattis):
    def __init__(self, data_source: Any = sys.stdin) -> None:
        super().__init__(data_source)
        self._data: List[str] = []
        self._answer: List[str] = []
        self._cup_data: Sequence = Sequence()
        self.read_input()

    @staticmethod
    def convert_to_radius(color: str, radius: str) -> Tuple[str, str]:
        new_radius: int = int(int(color) / 2)
        color, radius = radius, str(new_radius)
        return color, radius

    def read_input(self) -> None:
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
        self._cup_data.sort(key=lambda i: i[1])
        self._answer = [item[0] for item in self._cup_data]

    @property
    def data(self) -> List[str]:
        return self._data

    @property
    def answer(self) -> str:
        return '\n'.join(self._answer)

    def print_answer(self) -> None:
        sys.stdout.write(self.answer)


if __name__ == "__main__":
    cups = Cups()
    cups.solve()
    cups.print_answer()
