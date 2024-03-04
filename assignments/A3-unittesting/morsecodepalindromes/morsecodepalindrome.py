"""Module that takes input in from the command line
and accesses separate module classes to check a string
for patterns that match a regular expression and removes
any matches. Then if the string is not empty it will test
against another class module that has a dictionary with morse
code values to change it too. Once completed this module
checks if the morse code string value is the same as the
reversed morse code string then it prints 1 else 0 for
match/no match
"""
import sys
from typing import Any
import morsecode as mc
import pattern as pat


class Palindrome:
    """_summary_

    Returns:
        _type_: _description_
    """
    __reversed_str = ""
    __morse_code = ""

    def __init__(self) -> None:
        """_summary_
        """
        self.str_check = ""

    @property
    def str_input(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.str_check

    @str_input.setter
    def str_input(self, input_str: str) -> None:
        """_summary_

        Args:
            input_str (str): _description_
        """
        self.str_check = input_str

    @property
    def string_reversed(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__reversed_str

    @string_reversed.setter
    def string_reversed(self, reversed_str: str) -> None:
        """_summary_

        Args:
            reversed_str (str): _description_
        """
        self.__reversed_str = reversed_str

    @property
    def morse_coded_str(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__morse_code

    @morse_coded_str.setter
    def morse_coded_str(self, morse_coded_str: str) -> None:
        """_summary_

        Args:
            morse_coded_str (str): _description_
        """
        self.__morse_code = morse_coded_str

    def morse_code_str(self, removed_patterns: str) -> bool:
        """_summary_

        Args:
            removed_patterns (str): _description_

        Returns:
            bool: _description_
        """
        morse_code_str = mc.MorseCode(removed_patterns.upper())
        self.morse_coded_str = morse_code_str.generate_code_str()
        if self.morse_coded_str == '':
            return False
        self.string_reversed = self.morse_coded_str[::-1]
        if self.string_reversed == self.morse_coded_str:
            return True
        return False

    def check_pattern(self) -> None:
        """_summary_
        """
        str_pattern = pat.PatternMatch(self.str_check)
        removed_patterns = str_pattern.remove_str_patterns()
        if removed_patterns:
            palindrome_check = self.morse_code_str(removed_patterns)
            self.print_palindrome_match(palindrome_check)
        else:
            self.print_palindrome_match(False)

    def read_in_str(self, file: Any) -> None:
        """_summary_

        Args:
            file (Any): _description_
        """
        check_str: str = file.readline()
        self.str_check = check_str.rstrip()
        self.check_pattern()

    @staticmethod
    def print_palindrome_match(palindrome_check: bool) -> None:
        """_summary_

        Args:
            palindrome_check (bool): _description_
        """
        if palindrome_check:
            print(1)
        else:
            print(0)

    @staticmethod
    def main() -> None:
        """_summary_
        """
        palindrome = Palindrome()
        palindrome.read_in_str(sys.stdin)


if __name__ == "__main__":
    Palindrome.main()
