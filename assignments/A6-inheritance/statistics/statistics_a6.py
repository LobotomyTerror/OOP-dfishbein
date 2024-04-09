"""Class that inherits the ListClass that
uses the actual list class to redefine the
functionality to solve the Statistics Kattis
problem

    Returns:
        None
"""
import sys
from typing import Any
from listclass import ListClass


class Statistics(ListClass):
    """Used to get input from command line and
    build a list from the inherited class ListClass, using
    some rewritten methods to solve the Statistics Kattis
    problem

    Args:
        ListClass (list): Class that inherits the list class

    Returns:
        None
    """
    __case_count: int

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initializes the super class
        """
        super().__init__(*args, **kwargs)
        self.__case_count = 1

    @property
    def case_count(self) -> int:
        """Getter function for the case count of each
        evaluation

        Returns:
            int: the increasing number of cases with each file
        """
        return self.__case_count

    @case_count.setter
    def case_count(self, value: int) -> None:
        """Setter function for case count

        Args:
            value (int): integer value being passed
            as case count increments with each
            evaluation
        """
        self.__case_count = value

    def print_case(self) -> None:
        """Prints the formatted output per the Kattis solution
        """
        print(
            f"Case {self.case_count}: "
            f"{self[-1]} {self[0]} {self[0] - self[-1]}"
        )

    def remove_first_pos(self) -> None:
        """Pops the first element from the list
        """
        self.pop(0)

    def sort_list(self, rev_list: bool) -> None:
        """Sorts a list in reverse order to easily evaluate the
        beginning and end values

        Args:
            rev_list (bool): True or False value for reversing the
            order of the list
        """
        self.sort(reverse=rev_list)

    def get_input(self, file: Any) -> None:
        """Gets the input from the command line to then
        process and return the corrected output of the
        cases

        Args:
            file (Any): IO to get the string value
        """
        for line in file.stdin:
            self.append(line.rstrip())
            self.remove_first_pos()
            self.sort_list(rev_list=True)
            self.print_case()
            self.case_count += 1
            self.clear()

    @staticmethod
    def main() -> None:
        """Main method to call the other methods
        """
        s_list = Statistics()
        s_list.get_input(sys)


if __name__ == "__main__":
    stats = Statistics()  # pragma: no cover
    stats.main()  # pragma: no cover
