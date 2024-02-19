
from typing import Tuple


class Points:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self._x, self._y

    @coordinates.setter
    def coordinates(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def coordinate_x(self) -> int:
        return self._x

    @coordinate_x.setter
    def coordinate_x(self, x: int) -> None:
        self._x = x

    @property
    def coordinate_y(self) -> int:
        return self._y

    @coordinate_y.setter
    def coordinate_y(self, y: int) -> None:
        self._y = y
