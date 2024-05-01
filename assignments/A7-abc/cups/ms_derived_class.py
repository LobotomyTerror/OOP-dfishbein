"""Class that derives from the Mutable Sequence
class to implement specific functionality

    Raises:
        NotImplementedError: Slice feature for list
        is not implemented

    Returns:
        None

    Yields:
        Sequence: Overridden base class iterator
"""

from __future__ import annotations

from collections.abc import MutableSequence, Iterable
from typing import Any, Iterator, Tuple, List, overload, Union


class Sequence(MutableSequence[Tuple[str, int]]):
    """Overridden super class for base class to implement
    specific functionality

    Args:
        MutableSequence (tuple(str, int)): Contains a list of
        tuples that contains a string and integer
    """

    def __init__(self) -> None:
        """Initializes class instance variable
        _cup_type to be a list that contains a tuple
        """

        super().__init__()
        self._cup_type: List[Tuple[str, int]] = []

    def __len__(self) -> int:
        """Returns the length of the list

        Returns:
            int: Length of list
        """

        return len(self._cup_type)

    @overload
    def __getitem__(self, index: int) -> Tuple[str, int]:
        """Overridden get function of list to get specific
        element from list

        Args:
            index (int): Index position of the list

        Returns:
            Tuple[str, int]: Specified tuple at that indexed
            location
        """
        ...  # pragma: no cover

    @overload
    def __getitem__(self, index: slice) -> List[Tuple[str, int]]:
        """Slice method of get function to see multiple elements
        in the list

        Args:
            index (slice): Multiple integers that define what
            part of the list you want returned

        Returns:
            List[Tuple[str, int]]: A new list of the specified index
            values
        """
        ...  # pragma: no cover

    def __getitem__(self, index: int | slice) -> \
            Union[Tuple[str, int], List[Tuple[str, int]]]:
        """Checks if index is an integer or slice and returns
        the appropriate type based on the criteria

        Returns:
            Tuple[str, int] | List[Tuple[str, int]]:
            returns either a tuple or a list of tuples specified by
            the index
        """

        if isinstance(index, slice):
            return self._cup_type[index]
        return self._cup_type[index]

    @overload
    def __setitem__(self, index: int, cup: Tuple[str, int]) -> None:
        """Sets an item based on the index

        Args:
            index (int): index position in the list
            cup (Tuple[str, int]): Tuple containing a string and int
        """

        ...  # pragma: no cover

    @overload
    def __setitem__(
            self, index: slice,
            cup: Iterable[Tuple[str, int]]) -> None:
        """Sets items at specified index positions with a slice

        Args:
            index (slice): Integer range to place tuples in a list
            cup (Iterable[Tuple[str, int]]): An iterable of tuples to
            be placed in the list
        """
        ...  # pragma: no cover

    def __setitem__(
        self,
        index: Union[int, slice],
        cup: Union[Tuple[str, int], Iterable[Tuple[str, int]]]
    ) -> None:
        """Sets the item based on the index type and returns
        the appropriate type requested (Slice functionality is not
        implemented yet)

        Args:
            index (Union[int, slice]): Either a slice from the list
            or a specific index position from the list
            cup (Union[Tuple[str, int], Iterable[Tuple[str, int]]]):
            The item or items that are be put into the list

        Raises:
            NotImplementedError: Slice functionality is not implemented
            at the moment
        """

        if isinstance(index, int) and isinstance(cup, tuple):
            self._cup_type[index] = cup
        elif isinstance(index, slice) or isinstance(cup, list):
            raise NotImplementedError

    @overload
    def __delitem__(self, index: int) -> None:
        """Deletes an item from the list specified at the
        index location

        Args:
            index (int): Location in the list to delete from
        """

        ...  # pragma: no cover

    @overload
    def __delitem__(self, index: slice) -> None:
        """Deletes a portion from the list specified by the
        integer range

        Args:
            index (slice): Integer range to delete items
            from the list
        """

        ...  # pragma: no cover

    def __delitem__(self, index: int | slice) -> None:
        """Deletes items from the list at either the specified
        index location or the the range of positions in the list

        Args:
            index (int | slice): Either an single integer or a
            range of integers
        """

        del self._cup_type[index]

    def insert(self, index: int, value: Tuple[str, int]) -> None:
        """Inserts a tuple at a specified index in the list

        Args:
            index (int): Specific index location
            value (Tuple[str, int]): Tuple that contains a string
            and integer
        """

        self._cup_type[index] = value

    def __iter__(self) -> Iterator[Tuple[str, int]]:
        """Iterator method that returns all the values in
        the list

        Yields:
            Iterator[Tuple[str, int]]: Values contained in the list
        """

        for x in self._cup_type:
            yield x

    def __str__(self) -> str:
        """String method that returns a string representation
        of the list

        Returns:
            str: List as a string interpretation
        """

        return str(self._cup_type)

    def append(self, value: Tuple[str, int]) -> None:
        """Appends a value to the end of the list

        Args:
            value (Tuple[str, int]): Item to add to the
            end of the list
        """

        self._cup_type.append(value)

    def sort(self, key: Any = None) -> None:
        """Sorts the objects based on the key positioning

        Args:
            key (Any, optional): Specific key positioning, defaults to None.
        """

        self._cup_type.sort(key=key)


if __name__ == "__main__":
    seq = Sequence()  # pragma: no cover
    print(seq)  # pragma: no cover
