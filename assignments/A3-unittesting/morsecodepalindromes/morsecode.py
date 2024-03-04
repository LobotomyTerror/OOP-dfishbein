"""Module that uses a dict to compare characters of a
string to set a new string with the values of each key
match

    Returns:
        str: Returns a string that has been changed into
        the morse code equivalent of all the characters in
        the original string
"""


class MorseCode:
    """Compares characters of a string against a class
    attribute dictionary to set and return a new string
    that contains a morse coded equivalent of the original
    string

    Returns:
        str: Morse coded string formed from an original
        string
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
        """Initializes a class instance from a string that
        is passed in

        Args:
            str_match (str): String that was cleaned up from
            another module and used to set a new morse coded
            string
        """
        self.str_match = str_match

    @property
    def morse_code_str(self) -> str:
        """Returns class instance variable

        Returns:
            str: class instance variable
        """
        return self.morse_code_str

    @morse_code_str.setter
    def morse_code_str(self, morse_code_str: str) -> None:
        """Sets class instance variable

        Args:
            morse_code_str (str): string that is used
            to set class instance variable
        """
        self.morse_code_str = morse_code_str

    @property
    def palindrome_str(self) -> str:
        """Returns private class attribute variable

        Returns:
            str: private class attribute
        """
        return self.__palindrome

    @palindrome_str.setter
    def palindrome_str(self, palindrome: str) -> None:
        """Sets private class attribute variable

        Args:
            palindrome (str): string that is used to set
            the private class attribute
        """
        self.__palindrome = palindrome

    def generate_code_str(self) -> str:
        """Loops through the original string that was set
        as the class instance variable and compares each
        character against the key value in the class dictionary.
        Returning a new string that is the equivalent of the original
        but in morse code

        Returns:
            str: String equivalent of original string in morse code
        """
        for _, char in enumerate(self.str_match):
            for key, value in self.__morse_code_dict.items():
                if char == key:
                    self.palindrome_str += value
                    break
        return self.palindrome_str


if __name__ == "__main__":
    pass
