"""_summary_

    Returns:
        _type_: _description_
"""


class MorseCode:
    """_summary_

    Returns:
        _type_: _description_
    """
    __morse_code_dict = {
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
    __palindrome = ""

    def __init__(self, str_match: str) -> None:
        """_summary_

        Args:
            str_match (str): _description_
        """
        self.str_match = str_match

    @property
    def morse_code_str(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.morse_code_str

    @morse_code_str.setter
    def morse_code_str(self, morse_code_str: str) -> None:
        """_summary_

        Args:
            morse_code_str (str): _description_
        """
        self.morse_code_str = morse_code_str

    @property
    def palindrome_str(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__palindrome

    @palindrome_str.setter
    def palindrome_str(self, palindrome: str) -> None:
        """_summary_

        Args:
            palindrome (str): _description_
        """
        self.__palindrome = palindrome

    def generate_code_str(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        for _, char in enumerate(self.str_match):
            for key, value in self.__morse_code_dict.items():
                if char == key:
                    self.palindrome_str += value
                    break
        return self.palindrome_str


if __name__ == "__main__":
    pass
