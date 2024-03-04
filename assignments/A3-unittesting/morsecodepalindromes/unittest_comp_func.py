"""Comparison function that is used to test
against with the unittesting functions

    Returns:
        bool: checks if the string is a palindrome or empty string
"""
import sys
import re


def morse_code_palindrome(test_str: str) -> bool:
    """Creates a dict and runs the string through a pattern
    matcher and removes any characters that match. Once done
    the function sets a new string to the values of the in the
    dict to see if it is a morse code palindrome by comparing to
    a reversed version of the morse code string.

    Args:
        test_str (str): String to test against for any
        characters that are not supposed to be in the
        string.

    Returns:
        bool: returns True if the string is a palindrome
        else it returns False in any other case.
    """
    test_dict = {
        'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••',
        'E': '•', 'F': '••-•', 'G': '--•', 'H': '••••',
        'I': '••', 'J': '•---', 'K': '-•-', 'L': '•-••',
        'M': '--', 'N': '-•', 'O': '---', 'P': '•--•',
        'Q': '--•-', 'R': '•-•', 'S': '•••', 'T': '-',
        'U': '••-', 'V': '•••-', 'W': '•--', 'X': '-••-',
        'Y': '-•--', 'Z': '--••', '0': '-----', '1': '•----',
        '2': '••---', '3': '•••--', '4': '••••-', '5': '•••••',
        '6': '-••••', '7': '--•••', '8': '---••', '9': '----•'
    }

    string_pattern = r"[@:;<=>?\][\\^`–!#$%&')(~*+,\-./\" ]*"
    new_str = re.sub(string_pattern, "", test_str)
    new_str = new_str.upper()

    palindrome = ""
    for _, char in enumerate(new_str):
        for k, v in test_dict.items():
            if char == k:
                palindrome += v
                break
    reversed_palindrome = palindrome[::-1]
    if palindrome == '':
        return False
    if reversed_palindrome == palindrome:
        return True
    return False


def print_results(palindrome: bool) -> None:
    """Once the function morse_code_palindrome has checked
    the string and compared if the reversed version is a palindrome,
    this function prints a 1 or 0 to indicate if it is a palindrome
    or not.

    Args:
        palindrome (bool): variable that is used to check if it
        is True or False.
    """
    if palindrome:
        print(1)
    else:
        print(0)


def str_input() -> str:
    """Reads in the input string and returns the input
    string, stripped of trailing whitespaces.

    Returns:
        str: Input string that was read in through
        the command line.
    """
    str_line: str = sys.stdin.readline()
    return str_line.rstrip()


def main() -> None:
    """This fucntion instaciates the calls to the other
    functions to check if the string is a palindrome.
    """
    test_str: str = str_input()
    palindrome_check = morse_code_palindrome(test_str)
    print_results(palindrome_check)


if __name__ == "__main__":
    main()
