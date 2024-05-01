"""Module that is used to test against the Cups classes
output to see if the outputs are correct. Tests the entire
program

    Returns:
        None
"""
import sys
from typing import Any, List, Tuple


def convert_radius(color: str, radius: str) -> Tuple[str, str]:
    """Converts the color if the color is a digit instead of a
    actual color. Also converts it from the diameter to the radius

    Args:
        color (str): Diameter instead of a color
        radius (str): Color instead of the radius

    Returns:
        Tuple[str, str]: The corrected format (color, radius) as
        strings
    """
    new_radius: int = int(int(color) / 2)
    color, radius = radius, str(new_radius)
    return color, radius


def print_ans(cup_data: List[Tuple[str, int]]) -> None:
    """Sorts the cup_data list by the tuples int value then
    stores the color strings in the ans list to print out the
    colors from smallest to largest

    Args:
        cup_data (List[Tuple[str, int]]): List of tuples that
        contains the unsorted tuples
    """
    cup_data.sort(key=lambda i: i[1])
    ans: List[str] = [item[0] for item in cup_data]
    '\n'.join(ans)
    for item in ans:
        print(item)


def solve(cups_desc: List[str]) -> None:
    """Takes the cups_desc from the input and does the
    necessary fixes to insert a tuple with a string and integer

    Args:
        cups_desc (List[str]): List of strings from that was read in
        and split
    """
    amount_of_cups: int = int(cups_desc[0].rstrip())
    cups_desc.pop(0)
    cup_data = []

    for i in range(amount_of_cups):
        color, radius = cups_desc[i].rstrip().split()
        if color.isdigit():
            color, radius = convert_radius(color, radius)
        cup_data.append((color, int(radius)))
    print_ans(cup_data)


def get_input(file: Any) -> List[str]:
    """Gets the input from the terminal to read all the lines
    and then returns it to be processed

    Args:
        file (Any): Text input/output from the terminal

    Returns:
        List[str]: The list of strings from the read of the terminal
    """
    lines: List[str] = file.readlines()
    return lines


def main() -> None:
    """Main entry point for the program to solve the
    Kattis problem Stacking Cups and for testing
    """
    cups_desc: List[str] = get_input(sys.stdin)
    solve(cups_desc)


if __name__ == "__main__":
    main()
