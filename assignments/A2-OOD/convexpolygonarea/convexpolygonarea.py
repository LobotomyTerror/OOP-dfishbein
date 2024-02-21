"""Module for calculating the area of a
    convex polygon

    Returns:
        None: Prints out the final calculation
"""
import sys
from typing import Any, List
from points import Points


class Polygon:
    """Reads in the data file and creates a list of
    Points objects that correlate to x and y members
    """

    def __init__(self) -> None:
        """Constructor

        Args:
            Initializes all members to 0 and an
            empty list
        """
        self._num_of_polygons: int = 0
        self._num_of_points: int = 0
        self._coordinates: List[Points] = []

    @property
    def total_points(self) -> int:
        """Property to get the total
        number of coordinate points

        Returns:
            int: The number of coordinate points
        """
        return self._num_of_points

    @total_points.setter
    def total_points(self, points: int) -> None:
        """Property to set total number of coordinates

        Args:
            points (int): Total points read in from stdin
        """
        self._num_of_points = points

    @property
    def coordinates_set(self) -> List[Points]:
        """Property that gets a list of Points objects
        that contains all the x and y coordinate sets
        as tuples

        Returns:
            List[Points]: A list of all the coordinate
            sets
        """
        return self._coordinates

    @coordinates_set.setter
    def coordinates_set(self, coord_set: List[Points]) -> None:
        """Property that sets the list of Points objects that
        contain the x and y coordinate sets

        Args:
            coord_set (List[Points]): list of points that
            were read in from stdin
        """
        self._coordinates = coord_set

    @staticmethod
    def print_calc(final_calc: float) -> None:
        """Method that does the final calculation and
        prints it as a formatted string

        Args:
            final_calc (float): Comes from calc_polygon
            where the shoelace formula is conducted
        """
        final_calc = abs(final_calc) / 2.0
        print(f"{final_calc:0.12g}")

    def calc_polygon(self) -> float:
        """Public method that preforms the shoelace
        formula with the list of coordinate sets from
        the list of Points objects

        Returns:
            float: Returns the final calculation from the
            shoelace formula so it can be printed
        """
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
        """Reads in from stdin and sets private members
        to the specific values

        Args:
            file (Any): The source file that is read in
            from stdin
        """
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
        """Takes in input from stdin and passes
        it to read_input

        Args:
            file (Any): File that is read in from
            stdin
        """
        self.read_input(file)

    @staticmethod
    def main() -> None:
        """Main function to instantiate a Polygon
        instance and pass stdin to other method
        functions
        """
        result = Polygon()
        result.input_file(sys.stdin)


if __name__ == "__main__":
    Polygon.main()

# Citing - For portions of this program I utilized ChatGPT
# to help me understand specific portions of the code along with
# helping me debug an issue with my shoelace formula. I got the
# shoelace formula idea from this website
# https://erkaman.github.io/posts/area_convex_polygon.html.
# I also used some of the details from Dr. Ram Basnet's repo
# https://github.com/rambasnet/course-container/tree/main to
# help me better understand some of the OOD concepts as well.
