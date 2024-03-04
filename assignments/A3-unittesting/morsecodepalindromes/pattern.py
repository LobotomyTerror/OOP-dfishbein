"""Module that creates an class instance variable of a string
to check if that string matches any of the patterns in the
classes private attribute. Removing any of the non-alpha
numeric characters and returns a new string.

    Returns:
        str: returns a new string where the original is
        compared against a regex string and removes all
        matching patterns.
    """
import re


class PatternMatch:
    """Class that creates an instance variable to compare
    against a regex class attribute and then returns a
    cleaned up new string.

    Returns:
        str: Returns a new string from a comparison with
        a regex string to remove any specified characters.
    """
    __pattern_str = r"[@:;<=>?\][\\^`–!#$%&')(~*+,\-./\" ]*"

    def __init__(self, check_str: str) -> None:
        """Initializes a string to be checked by the
        regex class attribute.

        Args:
            check_str (str): String instance to check.
        """
        self.input_str = check_str

    @property
    def string_property(self) -> str:
        """Returns class instance variable string

        Returns:
            str: class instance string to be checked
        """
        return self.input_str

    @string_property.setter
    def string_property(self, input_str: str) -> None:
        """Sets the class instance variable

        Args:
            input_str (str): String that is used to
            check for patterns
        """
        self.input_str = input_str

    def remove_str_patterns(self) -> str:
        """Removes all non-alpha numeric characters
        from class instance string using private
        class attribute regex string.

        Returns:
            str: A new string after the cleanup from
            the comparison.
        """
        return re.sub(self.__pattern_str, "", self.input_str)


if __name__ == "__main__":
    pass
