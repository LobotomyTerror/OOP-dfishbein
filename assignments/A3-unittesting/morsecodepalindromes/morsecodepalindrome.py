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
    """Class that sets a string to be checked utilizing
    the two modules morsecode and pattern to remove
    unwanted characters and to check if the string is
    either empty or a palindrome.

    Returns:
        bool: Returns True or False if a string is a
        palindrome or not.
    """
    __reversed_str = ""
    __morse_code = ""

    def __init__(self) -> None:
        """Creates a class instance to empty, so it can
        be set later.
        """
        self.str_check = ""

    @property
    def str_input(self) -> str:
        """Returns class instance

        Returns:
            str: class instance
        """
        return self.str_check

    @str_input.setter
    def str_input(self, input_str: str) -> None:
        """Sets the class instance to a passed in
        string

        Args:
            input_str (str): string that is used to set
            class instance
        """
        self.str_check = input_str

    @property
    def string_reversed(self) -> str:
        """Returns a defined private class attribute

        Returns:
            str: private class attribute
        """
        return self.__reversed_str

    @string_reversed.setter
    def string_reversed(self, reversed_str: str) -> None:
        """Sets the private class attribute

        Args:
            reversed_str (str): string that is used
            to set the private class attribute
        """
        self.__reversed_str = reversed_str

    @property
    def morse_coded_str(self) -> str:
        """Returns a defined private class attribute

        Returns:
            str: private class attribute
        """
        return self.__morse_code

    @morse_coded_str.setter
    def morse_coded_str(self, morse_coded_str: str) -> None:
        """Sets the private class attribute

        Args:
            morse_coded_str (str): string that is used
            to set the private class attribute
        """
        self.__morse_code = morse_coded_str

    def morse_code_str(self, removed_patterns: str) -> bool:
        """Returns True or False if the morse coded string is
        a palindrome when reversed

        Args:
            removed_patterns (str): A string that has been checked
            for non-alpha numeric characters and stripped of them

        Returns:
            bool: Returns True if the string is a palindrome. Else
            returns False in any other case
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
        """Sets a string to be checked in the module PatterMatch
        and then creates a new string that doesn't have non-alpha
        numeric characters. Then calls a function to see if the string
        is a palindrome or not
        """
        str_pattern = pat.PatternMatch(self.str_check)
        removed_patterns: str = str_pattern.remove_str_patterns()
        if removed_patterns:
            palindrome_check: bool = self.morse_code_str(removed_patterns)
            self.print_palindrome_match(palindrome_check)
        else:
            self.print_palindrome_match(False)

    def read_in_str(self, file: Any) -> None:
        """Reads in input from the command line
        and strips newline characters from the string

        Args:
            file (Any): sys.stdin for reading in input
        """
        check_str: str = file.readline()
        self.str_check = check_str.rstrip()
        self.check_pattern()

    @staticmethod
    def print_palindrome_match(palindrome_check: bool) -> None:
        """Prints the results of the morse_code_str return
        of either True or False

        Args:
            palindrome_check (bool): Either True or False variable
            from the returned results
        """
        if palindrome_check:
            print(1)
        else:
            print(0)

    @staticmethod
    def main() -> None:
        """Start of the class functions
        """
        palindrome = Palindrome()
        palindrome.read_in_str(sys.stdin)


if __name__ == "__main__":
    Palindrome.main()

# When working on this I did have to look up how to setup my regular
# expression where I used https://regex101.com/ to help build it out.
# Along with this site
# https://codefather.tech/blog/remove-spaces-string-python/
# that led me to the re.sub function to remove a matching
# patterns.
