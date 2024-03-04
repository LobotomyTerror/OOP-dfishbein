import re


def main(test_str: str) -> bool:
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

    if test_str == "" or new_str == "":
        return False

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
