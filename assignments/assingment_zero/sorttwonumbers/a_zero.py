import sys
from typing import Tuple


def print_nums(num1: int, num2: int) -> None:
    """Prints the numbers after they have been
    sorted from the switch_nums function

    Args:
        num1 (int): first number that was entered
        num2 (int): second number that was entered
    """
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
    """Function to get the numbers that are
    entered

    Returns:
        Tuple[int, int]: Changes the numbers 
        from strings to ints
    """
    line = sys.stdin.readline()
    num1, num2 = line.split()
    return int(num1), int(num2)


def main() -> None:
    """Main function that does all the calling of the
    separate functions
    """
    in_num1, in_num2 = get_nums()
    num1, num2 = switch_nums(in_num1, in_num2)
    print_nums(num1, num2)


if __name__ == "__main__":
    main()
