import unittest
from hypothesis import given, settings, strategies as st, Verbosity
from unittest.mock import patch
from io import StringIO
from titlecost import TitleCost
import k_test


class TestTitleCost(unittest.TestCase):
    __custom_alphabet = \
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def setUp(self) -> None:
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


if __name__ == "__main__":
    unittest.main()
