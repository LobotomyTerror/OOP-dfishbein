class MovieCap:
    __movie_cap: float

    def __init__(self) -> None:
        self.__movie_cap = 0.0

    @property
    def movie_cap(self) -> float:
        return self.__movie_cap

    @movie_cap.setter
    def movie_cap(self, movie_cap: float) -> None:
        self.__movie_cap = movie_cap


if __name__ == "__main__":
    MovieCap()  # pragma: no cover
