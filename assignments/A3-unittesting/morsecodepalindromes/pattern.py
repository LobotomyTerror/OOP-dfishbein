"""_summary_

    Returns:
        _type_: _description_
    """
import re


class PatternMatch:
    """_summary_

    Returns:
        _type_: _description_
    """
    __pattern_str = r"[@:;<=>?\][\\^`–!#$%&')(~*+,\-./\" ]*"

    def __init__(self, check_str: str) -> None:
        """_summary_

        Args:
            check_str (str): _description_
        """
        self.input_str = check_str

    @property
    def string_property(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.input_str

    @string_property.setter
    def string_property(self, input_str: str) -> None:
        """_summary_

        Args:
            input_str (str): _description_
        """
        self.input_str = input_str

    def remove_str_patterns(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return re.sub(self.__pattern_str, "", self.input_str)


if __name__ == "__main__":
    pass
