class MovieTitle:
    __movie_title: float

    def __init__(self) -> None:
        self.__movie_title = 0.0

    @property
    def movie_title(self) -> float:
        return self.__movie_title

    @movie_title.setter
    def movie_title(self, movie_title: float) -> None:
        self.__movie_title = movie_title


if __name__ == "__main__":
    MovieTitle()
