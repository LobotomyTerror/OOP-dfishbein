"""Module that stores x and y coordinates
that our accessed in the Polygon module

    Returns:
        None: Only instance are created to
        access private members
    """
from typing import Tuple


class Points:
    """Module that allows the Polygon class to create
    x and y coordinates instances for calculating the
    area of a convex polygon
    """

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Initializes the x and y members

        Args:
            x (int): Defaults to 0 or a passed in
            integer
            y (int): Defaults to 0 or a passed in
            integer
        """
        self._x = x
        self._y = y

    @property
    def coordinates(self) -> Tuple[int, int]:
        """Property that returns a tuple of the
        coordinate pair x, y

        Returns:
            Tuple[int, int]: (x, y) coordinate pair
        """
        return self._x, self._y

    @coordinates.setter
    def coordinates(self, x: int, y: int) -> None:
        """Property that sets the coordinate pair x, y

        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        self._x = x
        self._y = y

    @property
    def coordinate_x(self) -> int:
        """Property that returns an instance of an
        x object

        Returns:
            int: the value of that x object
        """
        return self._x

    @coordinate_x.setter
    def coordinate_x(self, x: int) -> None:
        """Property that sets the x object to the
        value of the variable being passed in

        Args:
            x (int): integer value being passed in
            from stdin
        """
        self._x = x

    @property
    def coordinate_y(self) -> int:
        """Property that returns an instance of an
        y object

        Returns:
            int: the value of that y object
        """
        return self._y

    @coordinate_y.setter
    def coordinate_y(self, y: int) -> None:
        """Property that sets the y object to the
        value of the variable being passed in

        Args:
            y (int): integer value being passed in
            from stdin
        """
        self._y = y

# Citing - I ran into issues when I was creating this class
# in the beginning which I utilized ChatGPT to help me understand
# what was happening. It was from the setter and getter declarations
# and I used ChatGPT to help me understand how to implement those class
# methods properly.
