"""Class to inherit the list built-in class
and change the behavior of predefined methods
as well as add methods to accomplish specific tasks

    Returns:
        _type_: _description_
"""
from typing import Any, List, SupportsIndex


class ListClass(list[Any]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def __setitem__(self, index: Any, value: Any) -> None:
        super().__setitem__(index, int(value))

    def __getitem__(self, index: SupportsIndex | slice) -> Any:
        return super().__getitem__(index)

    def sort(self, *args: Any, **kwargs: Any) -> None:
        super().sort(*args, **kwargs)

    def pop(self, index: SupportsIndex = -1) -> Any:
        return super().pop(index)

    def append(self, item: str) -> None:
        elements: List[str] = item.split()
        for element in elements:
            super().append(int(element))


if __name__ == "__main__":
    my_list = ListClass()
    my_list.append('2 4 10')
    my_list.sort(reverse=True)
    print(f"Case 1: {my_list}")
    my_list.clear()
