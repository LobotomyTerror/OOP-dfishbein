"""Unittesting module for Statistics and ListClass
classes and modules

    Returns:
        None
"""
import unittest
from typing import Any, List
from unittest.mock import patch
from io import StringIO
from hypothesis import given, settings, strategies as st, Verbosity
from statistics_a6 import Statistics
from listclass import ListClass


class TestStatistics(unittest.TestCase):
    """Unittesting class for testing output of both
    Statistics and ListClass modules

    Args:
        unittest (_type_): unittest TestCase class
    """

    def setUp(self) -> None:
        """Sets up the case count and test_list class
        instance variables
        """
        self.case_count: int = 1
        self.test_list: ListClass = ListClass()

    @staticmethod
    @st.composite
    def file_content_strategy(draw: Any) -> str:
        """Used to generate the number of test cases, the
        number of integers on a single line, and the random
        variables to fill that line. Copying the Kattis problem
        Statistics

        Args:
            draw (Any): Turns integers from strategies module into
            an actual integer

        Returns:
            str: Returns a string representation created from a list
        """
        num_of_test_cases: Any = draw(st.integers(min_value=1, max_value=10))
        main_lines: List[Any] = []

        for _ in range(num_of_test_cases):
            lines: List[Any] = []
            number_of_ints: Any = draw(st.integers(min_value=1, max_value=30))
            lines.append(str(number_of_ints))
            for _ in range(number_of_ints):
                range_of_ints: Any = draw(st.lists(st.integers(
                    min_value=-1000000,
                    max_value=1000000
                ), min_size=1, max_size=1))
                lines.append(''.join(map(str, range_of_ints)))
            main_lines.append(' '.join(lines) + '\n')
        return ''.join(main_lines)

    @settings(
        max_examples=10,
        deadline=None,
        derandomize=False,
        verbosity=Verbosity.normal
    )
    @given(file_content=file_content_strategy())
    def test_main(self, file_content: Any) -> None:
        """Tests Statistics class main output with the above
        function to mimic the Kattis problem's specifics

        Args:
            file_content (Any): Strategy function above to mimic
            kattis problem
        """
        expected_out = StringIO()
        with patch('sys.stdin', new=StringIO(file_content)), \
                patch('sys.stdout', new=StringIO()):
            Statistics.main()
        expected_out.seek(0)
        expected_lines: List[str] = expected_out.readlines()
        file = StringIO(file_content)
        for expected_line, actual_line in zip(expected_lines, file):
            self.assertEqual(expected_line.strip(), actual_line.split())

    def test_list_class(self) -> None:
        """Tests the list class main, testing its output
        """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            file: str = '2 4 10'
            self.test_list.l_main(file)
            expected_ans = "Case 1: 4 10 6"
            actual_ans = mock_stdout.getvalue().strip()
        self.assertEqual(expected_ans, actual_ans)

    @staticmethod
    @st.composite
    def file_content_strategy_2(draw: Any) -> str:
        """Same strategy as above but just for a single
        line instead of multiple

        Args:
            draw (Any): Turns integers from strategies module into
            an actual integer

        Returns:
            str: Returns a string representation created from a list
        """
        number_of_ints: Any = draw(st.integers(min_value=1, max_value=30))
        lines: List[Any] = []
        lines.append(str(number_of_ints))
        for _ in range(number_of_ints):
            range_of_ints: Any = draw(st.lists(st.integers(
                min_value=-1000000,
                max_value=1000000
            ), min_size=1, max_size=1))
            lines.append(''.join(map(str, range_of_ints)))
        return ' '.join(lines) + '\n'

    @settings(
        max_examples=10,
        derandomize=False,
        deadline=None,
        verbosity=Verbosity.normal
    )
    @given(file_content=file_content_strategy_2())
    def test_list_class_2(self, file_content: Any) -> None:
        """Uses the function above to generate a single string
        matching what one line would be in the kattis problem

        Args:
            file_content (Any): Mimics a single line as the kattis
            problem Statistics
        """
        file: str = file_content.strip()
        test_list: List[Any] = file.split()
        test_list = [
            int(elem) for elem in test_list
        ]
        test_list.pop(0)
        test_list.sort(reverse=True)
        expected_out = \
            f"Case 1: {test_list[-1]} {test_list[0]} " \
            f"{test_list[0] - test_list[-1]}"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.test_list.l_main(file)
            actual_ans = mock_stdout.getvalue().strip()
        self.assertEqual(expected_out, actual_ans)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
