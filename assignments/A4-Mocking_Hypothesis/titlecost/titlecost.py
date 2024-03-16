"""Module that compares the length of two pieces of
data(?) by comparing their lengths and outputting the
smaller of the two as the overall cost

    Returns:
        None
    """
import sys
from typing import Any, Tuple
from movie_title import MovieTitle
from movie_cap import MovieCap


class TitleCost:
    """Class that takes in the input and converts the two inputs
    to floats, so that the inputs can be compared against each
    other. Then outputs the cost of the lowest input

    Returns:
        None
    """
    __movie_title: MovieTitle
    __movie_cap: MovieCap

    def __init__(self) -> None:
        """Initializes class attributes as instances of
        the other classes
        """
        self.__movie_title = MovieTitle()
        self.__movie_cap = MovieCap()

    @property
    def movie_title(self) -> float:
        """Returns the dataclass movie title class
        attribute

        Returns:
            float: class attribute of the movie
            title class
        """
        return self.__movie_title.movie_title

    @movie_title.setter
    def movie_title(self, movie_title: float) -> None:
        """Sets the dataclass movie title class attribute based
        off of the length after being converted to a float

        Args:
            movie_title (float): movie title length after
            being converted
        """
        self.__movie_title.movie_title = movie_title

    @property
    def movie_cap(self) -> float:
        """Returns the dataclass movie cap class
        attribute

        Returns:
            float: movie cap class attribute data
        """
        return self.__movie_cap.movie_cap

    @movie_cap.setter
    def movie_cap(self, movie_cap: float) -> None:
        """Sets the dataclass movie cap class attribute after
        the string has been converted

        Args:
            movie_cap (float): movie cap after being converted to
            a float
        """
        self.__movie_cap.movie_cap = movie_cap

    def compare_movie_data(self) -> None:
        """Compares the length of the movie cap
        and the movie title then which ever to
        a print member function
        """
        if self.movie_title > self.movie_cap:
            self.print_cost(self.movie_cap)
        elif self.movie_title < self.movie_cap:
            self.print_cost(self.movie_title)
        else:
            self.print_cost(self.movie_cap)

    def set_movie_data(self, movie_title: str, movie_cap: str) -> None:
        """Sets the movie title and movie cap as actual float
        values for easy comparison. Then calls compare function

        Args:
            movie_title (str): variable read in from file
            movie_cap (str): variable read in from file
        """
        self.movie_title = float(len(movie_title))
        self.movie_cap = float(movie_cap)
        self.compare_movie_data()

    @staticmethod
    def print_cost(movie_cost: float) -> None:
        """Prints the the total cost of the movie
        at an accuracy of 15 decimal positions

        Args:
            movie_cost (float): float value of the total
            movie cost
        """
        print(f"{movie_cost:.15g}")

    @staticmethod
    def movie_data(file: Any) -> Tuple[str, str]:
        """Reads in the file data and creates a list that
        of the separated strings. Then returns their values
        separately

        Args:
            file (Any): sys.stdin for allowing input from
            the user

        Returns:
            Tuple[str, str]: Returns the separate values that
            are in the list
        """
        line: str = file.readline().rstrip()
        movie_data_list = line.split(sep=' ')
        return movie_data_list[0], movie_data_list[1]

    @staticmethod
    def main() -> None:
        """Begins the program run when called from function
        guard
        """
        print_cost = TitleCost()
        movie_title, movie_cap = print_cost.movie_data(sys.stdin)
        print_cost.set_movie_data(movie_title, movie_cap)


if __name__ == "__main__":
    TitleCost.main()  # pragma: no cover
