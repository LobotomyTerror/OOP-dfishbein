"""Simple dataclass that stores and returns
a class attribute

    Returns:
        float: class attribute
    """
import dataclasses


@dataclasses.dataclass
class MovieTitle:
    """Dataclass used to store the length
    of a movie title as a float

    Returns:
        float: movie title length
    """
    __movie_title: float

    def __init__(self) -> None:
        """Initializes class attribute
        """
        self.__movie_title = 0.0

    @property
    def movie_title(self) -> float:
        """Returns class attribute data

        Returns:
            float: movie title length
        """
        return self.__movie_title

    @movie_title.setter
    def movie_title(self, movie_title: float) -> None:
        """Sets the class attribute to the length of the
        movie title

        Args:
            movie_title (float): movie title that was converted
            to a float value
        """
        self.__movie_title = movie_title


if __name__ == "__main__":
    MovieTitle()  # pragma: no cover
