import sys
from typing import Any, List
from points import Points


class Polygon:
    def __init__(self) -> None:
        self._num_of_polygons: int = 0
        self._num_of_points: int = 0
        self._coordinates: List[Points] = []

    @property
    def total_points(self) -> int:
        return self._num_of_points

    @total_points.setter
    def total_points(self, points: int) -> None:
        self._num_of_points = points

    @property
    def coordinates_set(self) -> List[Points]:
        return self._coordinates

    @coordinates_set.setter
    def coordinates_set(self, coord_set: List[Points]) -> None:
        self._coordinates = coord_set

    @staticmethod
    def print_calc(final_calc: float) -> None:
        final_calc = abs(final_calc) / 2.0
        print(f"{final_calc:0.12g}")

    def calc_polygon(self) -> float:
        final_count: float = 0
        coord = self._coordinates
        for i in range(self._num_of_points):
            if i == self._num_of_points - 1:
                final_count += (
                    coord[i].coordinate_x * coord[i - i].coordinate_y -
                    coord[i].coordinate_y * coord[i - i].coordinate_x
                )
            else:
                final_count += (
                    coord[i].coordinate_x * coord[i + 1].coordinate_y -
                    coord[i].coordinate_y * coord[i + 1].coordinate_x
                )
        return final_count

    def read_input(self, file: Any) -> None:
        poly_data: str = file.readlines()
        self._num_of_polygons = int(poly_data[0].rstrip())

        for i in range(self._num_of_polygons):
            self._num_of_points = int(poly_data[i + 1].split()[0])
            data = poly_data[i + 1].split()[1:]
            self._coordinates = [
                Points(x, y) for x, y in zip(
                    map(int, data[::2]),
                    map(int, data[1::2])
                )
            ]
            final_calc = self.calc_polygon()
            self.print_calc(final_calc)

    def input_file(self, file: Any) -> None:
        self.read_input(file)

    @staticmethod
    def main() -> None:
        result = Polygon()
        result.input_file(sys.stdin)


if __name__ == "__main__":
    Polygon.main()
