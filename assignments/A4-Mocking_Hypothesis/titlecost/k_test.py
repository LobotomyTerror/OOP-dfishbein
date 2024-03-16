"""Module that I am using to test against my
own class when using hypothesis. This is used to
compare certain outputs and other details

    Returns:
        None
    """
import sys
from typing import Tuple


def print_cost(cost_of_movie: float) -> None:
    """Prints the cost of the movie

    Args:
        cost_of_movie (float): movie cost
    """
    print(f"{cost_of_movie:.15g}")


def compare_size(movie_title: float, movie_cap: float) -> float:
    """Compares the sizes of the movie title and movie cap as float
    values to see which is less and print out the lower of the two

    Args:
        movie_title (float): length of the movie title as a float
        movie_cap (float): float value of the cost of a movie

    Returns:
        float: either the movie cap or movie length title
        whichever is smallest
    """
    if movie_title > movie_cap:
        return movie_cap
    elif movie_title < movie_cap:
        return movie_title
    else:
        return movie_cap


def get_input() -> Tuple[str, str]:
    """Reads in the input from the file and separates
    them into a list and returns those separated strings

    Returns:
        Tuple[str, str]: List string values from file
    """
    line = sys.stdin.readline().rstrip()
    movie_list = line.split(sep=" ")
    return movie_list[0], movie_list[1]


def main() -> None:
    """Initiates the function calls for reading in the data
    and then runs the other functions for comparison and print
    """
    movie_title, movie_cap = get_input()
    movie_title_float = float(len(movie_title))
    movie_cap_float = float(movie_cap)
    cost_of_movie: float = compare_size(
        movie_title=movie_title_float,
        movie_cap=movie_cap_float
    )
    print_cost(cost_of_movie)


if __name__ == "__main__":
    main()  # pragma: no cover
