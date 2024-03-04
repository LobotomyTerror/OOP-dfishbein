import re
import sys
from typing import Dict


def get_input() -> str:
    input_text = sys.stdin.readline()
    return input_text.rstrip()


def string_test(morse_str_dict: Dict[str, str]) -> bool:
    test_str = get_input()

    string_pattern = r"[@:;<=>?\][\\^`–!#$%&')(~*+,\-./\" ]*"
    new_str = re.sub(string_pattern, "", test_str)
    new_str = new_str.upper()
    if test_str == "" or new_str == "":
        return False

    palindrome = ""
    for _, char in enumerate(new_str):
        for k, v in morse_str_dict.items():
            if char == k:
                palindrome += v
                break
    reversed_palindrome = palindrome[::-1]

    if reversed_palindrome == palindrome:
        return True
    return False


def main() -> None:
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

    palindrome_check = string_test(test_dict)

    if palindrome_check:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
