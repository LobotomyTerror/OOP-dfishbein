"""Module for unit testing, that checks the
functionality of the public methods in the other
modules
    """
import os
import unittest
from unittest.mock import patch
from io import StringIO
from convexpolygonarea import Polygon
from points import Points


class TestPolygons(unittest.TestCase):
    """Conducts tests of the public methods
    of the other modules checking the final
    output
    """

    def setUp(self) -> None:
        """Setup member function for unit
        testing
        """
        self.poly = Polygon()
        file = os.path.dirname(os.path.abspath(__file__))
        file_1 = os.path.join(file, 'data/sample.in')
        self.input1 = open(file_1, 'r', encoding='utf-8')
        file_2 = os.path.join(file, 'data/sample_2.in')
        self.input2 = open(file_2, 'r', encoding="utf-8")

    def tearDown(self) -> None:
        """Tear down method for cleaning up
        running processes
        """
        self.input1.close()
        self.input2.close()
        return super().tearDown()

    def test_read_data_one(self) -> None:
        """Test read data member function
        """
        self.poly.read_input(self.input1)
        self.assertEqual(self.poly.total_points, 3)
        test_list = [(1, 1), (2, 1), (2, 2)]
        for i, row in enumerate(self.poly.coordinates_set):
            self.assertEqual(
                (row.coordinate_x, row.coordinate_y),
                test_list[i]
            )

    def test_read_data_two(self) -> None:
        """Testing read data member function
        """
        self.poly.read_input(self.input2)
        self.assertEqual(self.poly.total_points, 4)
        test_list = [(0, 0), (10, 0), (13, 5), (10, 8)]
        for i, row in enumerate(self.poly.coordinates_set):
            self.assertEqual(
                (row.coordinate_x, row.coordinate_y),
                test_list[i]
            )

    def test_output_one(self) -> None:
        """Testing output of entire program
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.poly.read_input(self.input1)
            self.assertEqual(mock_stdout.getvalue(), '0.5\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_output_two(self, mock_stdout: StringIO) -> None:
        """Testing output of entire program
        """
        self.poly.read_input(self.input2)
        self.assertEqual(mock_stdout.getvalue(), "52\n")

    @patch('sys.stdin', StringIO("1\n 3 1 1 2 1 2 2\n"))
    def test_main(self) -> None:
        """Testing main function that runs entire
        program
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.poly.main()
            self.assertEqual(mock_stdout.getvalue(), "0.5\n")

    def test_polygon_input_one(self) -> None:
        """Tests polygon calculation
        """
        self.poly.total_points = 12
        self.poly.coordinates_set = [
            Points(0, 0), Points(3, 6), Points(6, 12),
            Points(9, 18), Points(12, 24), Points(15, 30),
            Points(18, 24), Points(21, 18), Points(24, 12),
            Points(27, 6), Points(30, 0), Points(33, -6)
        ]
        actual_ans = abs(self.poly.calc_polygon()) / 2.0
        expected_ans = 540
        self.assertEqual(actual_ans, expected_ans)

    def test_polygon_input_two(self) -> None:
        """Tests polygon calculation
        """
        self.poly.total_points = 100
        self.poly.coordinates_set = [
            Points(0, 0), Points(1, 50), Points(2, 100),
            Points(3, 150), Points(4, 200), Points(5, 250),
            Points(6, 300), Points(7, 350), Points(8, 400),
            Points(9, 450), Points(10, 500), Points(11, 550),
            Points(12, 600), Points(13, 650), Points(14, 700),
            Points(15, 750), Points(16, 800), Points(17, 850),
            Points(18, 900), Points(19, 950), Points(20, 1000),
            Points(21, 1050), Points(22, 1100), Points(23, 1150),
            Points(24, 1200), Points(25, 1250), Points(26, 1300),
            Points(27, 1350), Points(28, 1400), Points(29, 1450),
            Points(30, 1500), Points(31, 1550), Points(32, 1600),
            Points(33, 1650), Points(34, 1700), Points(35, 1750),
            Points(36, 1800), Points(37, 1850), Points(38, 1900),
            Points(39, 1950), Points(40, 2000), Points(41, 2050),
            Points(42, 2100), Points(43, 2150), Points(44, 2200),
            Points(45, 2250), Points(46, 2300), Points(47, 2350),
            Points(48, 2400), Points(49, 2450), Points(50, 2500),
            Points(51, 2450), Points(52, 2400), Points(53, 2350),
            Points(54, 2300), Points(55, 2250), Points(56, 2200),
            Points(57, 2150), Points(58, 2100), Points(59, 2050),
            Points(60, 2000), Points(61, 1950), Points(62, 1900),
            Points(63, 1850), Points(64, 1800), Points(65, 1750),
            Points(66, 1700), Points(67, 1650), Points(68, 1600),
            Points(69, 1550), Points(70, 1500), Points(71, 1450),
            Points(72, 1400), Points(73, 1350), Points(74, 1300),
            Points(75, 1250), Points(76, 1200), Points(77, 1150),
            Points(78, 1100), Points(79, 1050), Points(80, 1000),
            Points(81, 950), Points(82, 900), Points(83, 850),
            Points(84, 800), Points(85, 750), Points(86, 700),
            Points(87, 650), Points(88, 600), Points(89, 550),
            Points(90, 500), Points(91, 450), Points(92, 400),
            Points(93, 350), Points(94, 300), Points(95, 250),
            Points(96, 200), Points(97, 150), Points(98, 100),
            Points(99, 50)
        ]
        actual_ans = abs(self.poly.calc_polygon()) / 2.0
        expected_ans = 122500
        self.assertEqual(actual_ans, expected_ans)

    def test_polygon_input_three(self) -> None:
        """Tests polygon calculation
        """
        self.poly.total_points = 57
        self.poly.coordinates_set = [
            Points(-5000, -5000), Points(-4900, -4900), Points(-4800, -4800),
            Points(-4700, -4700), Points(-4600, -4600), Points(-4500, -4500),
            Points(-4400, -4400), Points(-4300, -4300), Points(-4200, -4200),
            Points(-4100, -4100), Points(-4000, -4000), Points(-3900, -3900),
            Points(-3800, -3800), Points(-3700, -3700), Points(-3600, -3600),
            Points(-3500, -3500), Points(-3400, -3400), Points(-3300, -3300),
            Points(-3200, -3200), Points(-3100, -3100), Points(-3000, -3000),
            Points(-2900, -2900), Points(-2800, -2800), Points(-2700, -2700),
            Points(-2600, -2600), Points(-2500, -2500), Points(-2400, -2400),
            Points(-2300, -2300), Points(-2200, -2200), Points(-2100, -2100),
            Points(-2000, -2000), Points(-1900, -1900), Points(-1800, -1800),
            Points(-1700, -1700), Points(-1600, -1600), Points(-1500, -1500),
            Points(-1400, -1400), Points(-1300, -1300), Points(-1200, -1200),
            Points(-1100, -1100), Points(-1000, -1000), Points(-900, -900),
            Points(-800, -800), Points(-700, -700), Points(-600, -600),
            Points(-500, -500), Points(-400, -400), Points(-300, -300),
            Points(-200, -200), Points(-100, -100), Points(0, 0),
            Points(100, 100), Points(200, 200), Points(300, 300),
            Points(400, 400), Points(500, 500), Points(600, 600),
            Points(700, 700), Points(800, 800), Points(900, 900),
            Points(1000, 1000)
        ]
        actual_ans = abs(self.poly.calc_polygon()) / 2.0
        expected_ans = 0
        self.assertEqual(actual_ans, expected_ans)


if __name__ == "__main__":
    unittest.main()

# Citing - For this module I did utilize Dr. Ram Basnet's
# repo https://github.com/rambasnet/course-container/tree/main
# along with ChatGPT to understand how these methods actually
# worked in the unittest class.
