import sys
from typing import Tuple


def print_cost(cost_of_movie: float) -> None:
    print(f"{cost_of_movie:.15g}")


def compare_size(movie_title: float, movie_cap: float) -> float:
    if movie_title > movie_cap:
        return movie_cap
    elif movie_title < movie_cap:
        return float(movie_title)
    else:
        return movie_cap


def get_input() -> Tuple[str, str]:
    line = sys.stdin.readline().rstrip()
    movie_list = line.split(sep=" ")
    return movie_list[0], movie_list[1]


def main() -> None:
    movie_title, movie_cap = get_input()
    movie_title_float = float(len(movie_title))
    movie_cap_float = float(movie_cap)
    cost_of_movie: float = compare_size(
        movie_title=movie_title_float,
        movie_cap=movie_cap_float
    )
    print_cost(cost_of_movie)


if __name__ == "__main__":
    main()
