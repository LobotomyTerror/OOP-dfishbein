"""Simple class that stores a float value
that was read in through the command line

    Returns:
        None
    """
import dataclasses


@dataclasses.dataclass
class MovieCap:
    """Class that is used as a dataclass for
    storing and retrieving the data stored in
    class attribute

    Returns:
        None
    """
    __movie_cap: float

    def __init__(self) -> None:
        """Initializes class attribute
        """
        self.__movie_cap = 0.0

    @property
    def movie_cap(self) -> float:
        """Returns class attribute data

        Returns:
            float: class attribute
        """
        return self.__movie_cap

    @movie_cap.setter
    def movie_cap(self, movie_cap: float) -> None:
        """Sets a new value for the class attribute

        Args:
            movie_cap (float): float value that was
            converted to a float
        """
        self.__movie_cap = movie_cap


if __name__ == "__main__":
    MovieCap()  # pragma: no cover
