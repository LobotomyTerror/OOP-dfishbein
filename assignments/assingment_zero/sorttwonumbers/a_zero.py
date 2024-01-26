import sys
from typing import Tuple


def print_nums(num1: int, num2: int) -> None:
    print(f"{num1} {num2}")


def switch_nums(num1: int, num2: int) -> Tuple[int, int]:
    """Function for swapping two numbers if
    one is greater than the other

    Args:
        num1 (int): first number entered
        num2 (int): second numbered entered

    Returns:
        Tuple[int, int]: returns the sorted numbers
        sorted from smallest to largest
    """
    if num1 > num2:
        num1, num2 = num2, num1
    return num1, num2


def get_nums() -> Tuple[int, int]:
    line = sys.stdin.readline()
    num1, num2 = line.split()
    return int(num1), int(num2)


def main() -> None:
    in_num1, in_num2 = get_nums()
    num1, num2 = switch_nums(in_num1, in_num2)
    print_nums(num1, num2)


if __name__ == "__main__":
    main()
