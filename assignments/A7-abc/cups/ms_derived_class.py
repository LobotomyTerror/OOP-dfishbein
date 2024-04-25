from __future__ import annotations

from collections.abc import MutableSequence, Iterable
from typing import Any, Iterator, Tuple, List, overload, Union


class Sequence(MutableSequence[Tuple[str, int]]):
    def __init__(self, color: str = '', radius: int = 0) -> None:
        super().__init__()
        self._cup_type: List[Tuple[str, int]] = []
        self._color: str = color
        self._radius: int = radius

    def __len__(self) -> int:
        return len(self._cup_type)

    @overload
    def __getitem__(self, index: int) -> Tuple[str, int]: ...

    @overload
    def __getitem__(self, index: slice) -> List[Tuple[str, int]]: ...

    def __getitem__(self, index: int | slice) -> \
            Union[Tuple[str, int], List[Tuple[str, int]]]:
        if isinstance(index, slice):
            return self._cup_type[index]
        return self._cup_type[index]

    @overload
    def __setitem__(self, index: int, cup: Tuple[str, int]) -> None: ...

    @overload
    def __setitem__(self, index: slice, cup: Iterable[Tuple[str, int]]) \
        -> None: ...

    def __setitem__(
        self,
        index: Union[int, slice],
        cup: Union[Tuple[str, int], Iterable[Tuple[str, int]]]
    ) -> None:
        if isinstance(index, int) and isinstance(cup, tuple):
            self._cup_type[index] = cup
        elif isinstance(index, slice) or isinstance(cup, list):
            raise NotImplementedError

    @overload
    def __delitem__(self, index: int) -> None: ...

    @overload
    def __delitem__(self, index: slice) -> None: ...

    def __delitem__(self, index: int | slice) -> None:
        del self._cup_type[index]

    def insert(self, index: int, value: Tuple[str, int]) -> None:
        self._cup_type[index] = value

    def __iter__(self) -> Iterator[Tuple[str, int]]:
        for x in self._cup_type:
            yield x

    def __str__(self) -> str:
        return str(self._cup_type)

    def append(self, value: Tuple[str, int]) -> None:
        self._cup_type.append(value)

    def sort(self, key: Any = None) -> None:
        self._cup_type.sort(key=key)

    @property
    def cup_color(self) -> str:
        return self._color

    @cup_color.setter
    def cup_color(self, color: str) -> None:
        self._color = color

    @property
    def cup_radius(self) -> int:
        return self._radius

    @cup_radius.setter
    def cup_radius(self, radius: int) -> None:
        self._radius = radius


if __name__ == "__main__":
    seq = Sequence(color='red', radius=5)
    print(seq)
