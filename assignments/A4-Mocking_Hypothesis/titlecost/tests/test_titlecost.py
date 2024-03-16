"""Module that is used to test the different classes
throughout this program
"""
import unittest
from unittest.mock import patch
from io import StringIO
from hypothesis import given, settings, strategies as st, Verbosity
from titlecost import TitleCost
import k_test


class TestTitleCost(unittest.TestCase):
    """Unittest class to test against the other module
    classes for this specific program

    Args:
        unittest (_type_): unittesting module
    """
    __custom_alphabet = \
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def setUp(self) -> None:
        """Setup function for easily accessing classes
        and testing modules
        """
        self.title_cost = TitleCost()
        self.test_mod = k_test

    @settings(
        deadline=None,
        max_examples=100,
        derandomize=False,
        verbosity=Verbosity.normal
    )
    @given(st.text(
        alphabet=st.sampled_from(__custom_alphabet),
        min_size=1,
        max_size=30
    ), st.floats(min_value=0.0, max_value=100.0))
    def test_output(self, input_str: str, float_input: float) -> None:
        """Tests against the output from the main program and the
        testing module. It also utilizes the custom alphabet to
        create a usable string along with hypothesis to generate
        random strings and float values

        Args:
            input_str (str): randomly generated string from hypothesis
            float_input (float): randomly generated float from hypothesis
        """
        with patch(
            'sys.stdin',
                new=StringIO(input_str + ' ' + str(float_input))):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.title_cost.main()
                expected_ans: str = mock_stdout.getvalue().strip()

        with patch('sys.stdin',
                   new=StringIO(input_str + ' ' + str(float_input))
                   ):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.test_mod.main()
                actual_ans: str = mock_stdout.getvalue().strip()
        self.assertEqual(expected_ans, actual_ans)

    def test_compare_size(self) -> None:
        """Just tests against the overall size making sure
        that it is printing out the correct value from the
        function
        """
        self.assertEqual(k_test.compare_size(15.0, 5.43), 5.43)
        self.assertEqual(k_test.compare_size(5.0, 45.43), 5.0)
        self.assertEqual(k_test.compare_size(15.0, 15.0), 15.0)

    def test_main(self) -> None:
        """Tests the overall program run and uses patching
        and mocking to check for the correct output
        """
        with patch('sys.stdin', new=StringIO(
            "GoneWithTheWind 13.341\n")
        ):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                k_test.main()
                captured_out = mock_stdout.getvalue().strip()
        self.assertEqual(captured_out, '13.341')

    def test_titlecost_compare(self) -> None:
        """Using patching and mocking this test function
        compare from the class module
        """
        with patch(
            'sys.stdin',
            new=StringIO("GoneWithTheWind 15.0\n")
        ):
            with patch(
                    'sys.stdout',
                    new=StringIO()) as mock_stdout:
                self.title_cost.main()
                expected_ans = mock_stdout.getvalue().strip()
        self.assertEqual(expected_ans, '15')


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
