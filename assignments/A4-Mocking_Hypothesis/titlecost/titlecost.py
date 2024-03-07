import sys
from typing import Any, Tuple
from movie_title import MovieTitle
from movie_cap import MovieCap


class TitleCost:
    __movie_title: MovieTitle
    __movie_cap: MovieCap

    def __init__(self) -> None:
        self.__movie_title = MovieTitle()
        self.__movie_cap = MovieCap()

    @property
    def movie_title(self) -> float:
        return self.__movie_title.movie_title

    @movie_title.setter
    def movie_title(self, movie_title: float) -> None:
        self.__movie_title.movie_title = movie_title

    @property
    def movie_cap(self) -> float:
        return self.__movie_cap.movie_cap

    @movie_cap.setter
    def movie_cap(self, movie_cap: float) -> None:
        self.__movie_cap.movie_cap = movie_cap

    def compare_movie_data(self) -> None:
        if self.movie_title > self.movie_cap:
            self.print_cost(self.movie_cap)
        elif self.movie_title < self.movie_cap:
            self.print_cost(self.movie_title)
        else:
            self.print_cost(self.movie_cap)

    def set_movie_data(self, movie_title: str, movie_cap: str) -> None:
        self.movie_title = float(len(movie_title))
        self.movie_cap = float(movie_cap)
        self.compare_movie_data()

    @staticmethod
    def print_cost(movie_cost: float) -> None:
        print(f"{movie_cost:.15g}")

    @staticmethod
    def movie_data(file: Any) -> Tuple[str, str]:
        line: str = file.readline().rstrip()
        movie_data_list = line.split(sep=' ')
        return movie_data_list[0], movie_data_list[1]

    @staticmethod
    def main() -> None:
        print_cost = TitleCost()
        movie_title, movie_cap = print_cost.movie_data(sys.stdin)
        print_cost.set_movie_data(movie_title, movie_cap)


if __name__ == "__main__":
    TitleCost.main()  # pragma: no cover
