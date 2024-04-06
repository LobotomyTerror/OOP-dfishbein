import sys
from typing import Any
from listclass import ListClass


class Statistics(ListClass):
    __case_count: int

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.__case_count = 1

    @property
    def case_count(self) -> int:
        return self.__case_count

    @case_count.setter
    def case_count(self, value: int) -> None:
        self.__case_count = value

    def print_case(self) -> None:
        print(
            f"Case {self.case_count}: "
            f"{self[-1]} {self[0]} {self[0] - self[-1]}"
        )

    def remove_first_pos(self) -> None:
        self.pop(0)

    def sort_list(self, rev_list: bool) -> None:
        self.sort(reverse=rev_list)

    def get_input(self, file: Any) -> None:
        for line in file.stdin:
            self.append(line.rstrip())
            self.remove_first_pos()
            self.sort_list(rev_list=True)
            self.print_case()
            self.case_count += 1
            self.clear()

    @staticmethod
    def main() -> None:
        s_list = Statistics()
        s_list.get_input(sys)


if __name__ == "__main__":
    stats = Statistics()
    stats.main()
