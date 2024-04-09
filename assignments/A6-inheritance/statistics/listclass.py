"""Class to inherit the list built-in class
and change the behavior of predefined methods
as well as add methods to accomplish specific tasks

    Returns:
        _type_: _description_
"""
from typing import Any, List, SupportsIndex


class ListClass(list[Any]):
    """Overrides the list class functions to be used for solving
    the kattis problem Statistics.

    Args:
        list (_type_): list class
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initializes an empty array if nothing is passed in
        or an empty list
        """
        super().__init__(*args, **kwargs)

    def __setitem__(self, index: Any, value: Any) -> None:
        """Sets item at a specific index and places the value into
        the list

        Args:
            index (Any): Integer value for indexing
            value (Any): The value to be placed in the list
        """
        super().__setitem__(index, int(value))  # pragma: no cover

    def __getitem__(self, index: SupportsIndex | slice) -> Any:
        """Gets a specific value using either an integer or a slice
        Args:
            index (SupportsIndex | slice): Either a integer or slice

        Returns:
            Any: Returns the location of the specified index
        """
        return super().__getitem__(index)

    def sort(self, *args: Any, **kwargs: Any) -> None:
        """Sorts array
        """
        super().sort(*args, **kwargs)

    def pop(self, index: SupportsIndex = -1) -> Any:
        """Pops the first element from the list

        Args:
            index (SupportsIndex, optional): index to find
            a/the values from a list. Defaults to -1.

        Returns:
            Any: Returns the value that was removed
        """
        return super().pop(index)

    def append(self, item: str) -> None:
        """Customized append method from the list class
        where instead of having to use for loops, it processes
        a string to change it to real numbers

        Args:
            item (str): Value to append to the end of the
            list
        """
        elements: List[str] = item.split()
        for element in elements:
            super().append(int(element))

    def print_list_class(self) -> None:
        """Prints the results of the stored values in this
        class instance
        """
        print(f"Case 1: {self[-1]} {self[0]} {self[0] - self[-1]}")

    @staticmethod
    def l_main(file: str | None) -> None:
        """Main function that calls the rest of the functions
        used mainly for testing

        Args:
            file (str | None): String to be passed in or sets the
            default
        """
        my_list = ListClass()
        if file is not None:
            my_list.append(file)
        else:
            my_list.append('1 0')  # pragma: no cover
        my_list.pop(0)
        my_list.sort(reverse=True)
        my_list.print_list_class()


if __name__ == "__main__":
    ListClass.l_main('2 4 10')  # pragma: no cover
