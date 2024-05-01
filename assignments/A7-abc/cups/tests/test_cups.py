"""Test module to test module output and various methods
of the derived class

    Returns:
        None
"""

import unittest
from typing import Any
from unittest.mock import patch
from io import StringIO
from hypothesis import given, settings, strategies as st, Verbosity
from cups import Cups
import cups_test as cup_t
from ms_derived_class import Sequence


class TestCups(unittest.TestCase):
    """Unittesting class for module output and various methods
    of the derived class. Uses a separate module that compares
    output of main program

    Args:
        unittest (TestCase): TestCase class for single test instances
    """

    def setUp(self) -> None:
        """Sets up various class instance variables for testing
        """
        self._test_mod = cup_t
        self._seq = Sequence()

    @staticmethod
    @st.composite
    def generate_str(draw: Any) -> str:
        """Defined strategy for program testing of main, mocking the
        Kattis problem Stacking Cups to see if output matches against
        test module

        Args:
            draw (Any): Used for creating actual types instead of just
            a strategy

        Returns:
            str: Returns a string that mimics the input of the Kattis
            problem
        """
        num_of_test_cases = draw(st.integers(min_value=1, max_value=20))
        lines = []

        lines.append(str(num_of_test_cases) + '\n')
        for _ in range(num_of_test_cases):
            desc = st.one_of(
                st.tuples(st.text(
                    alphabet=st.characters(
                        min_codepoint=97, max_codepoint=122),
                    min_size=1,
                    max_size=20),
                    st.integers(min_value=1, max_value=999)),
                st.tuples(st.integers(min_value=1, max_value=999),
                          st.text(alphabet=st.characters(
                              min_codepoint=97,
                              max_codepoint=122
                          ),
                    min_size=1,
                    max_size=20)
                )
            )
            desc_list = draw(desc)
            if isinstance(desc_list[0], int):
                lines.append(f"{desc_list[0] * 2} {desc_list[1]}\n")
            else:
                lines.append(f"{desc_list[0]} {desc_list[1]}\n")

        f_str = ''.join(lines)
        return f_str

    @settings(
        deadline=None,
        derandomize=False,
        max_examples=10,
        verbosity=Verbosity.normal
    )
    @given(content=generate_str())
    def test_module_1(self, content: Any) -> None:
        """Hypothesis method that uses the above method to test
        the main program output against a separate test module

        Args:
            content (Any): The search strategy parameter returned from
            the above method
        """
        with patch('sys.stdin', new=StringIO(content)) as mock_stdin:
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                cups = Cups(mock_stdin)
                cups.solve()
                cups.print_answer()
                expected_ans: str = mock_stdout.getvalue()

        with patch('sys.stdin', new=StringIO(content)):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self._test_mod.main()
                actual_ans: str = mock_stdout.getvalue().rstrip()
        self.assertEqual(expected_ans, actual_ans)

    def test_ms_module_1(self) -> None:
        """Tests the derived Sequence classes insert method
        """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            expected_ans = "[('b', 2)]"
            self._seq.append(('a', 1))
            self._seq.insert(0, ('b', 2))
            print(self._seq)
            actual_ans = mock_stdout.getvalue().strip()

        self.assertEqual(actual_ans, expected_ans)

    def test_ms_module_2(self) -> None:
        """Tests the derived Sequence classes delete method
        """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            expected_ans: str = '[]'
            self._seq.append(('a', 1))
            del self._seq[0]
            print(self._seq)
            actual_ans: str = mock_stdout.getvalue().strip()
        self.assertEqual(actual_ans, expected_ans)

    def test_ms_module_3(self) -> None:
        """Tests the Sequence classes length method
        """
        expected_ans: int = 1
        self._seq.append(('a', 1))
        actual_ans = len(self._seq)
        self.assertEqual(actual_ans, expected_ans)

    def test_ms_module_4(self) -> None:
        """Tests the Sequence classes get_item method with
        a specific index and slicing
        """
        self._seq.append(('a', 1))
        self._seq.append(('b', 2))
        self._seq.append(('c', 3))

        self.assertEqual(self._seq[0], ('a', 1))
        self.assertEqual(self._seq[1], ('b', 2))

        self.assertEqual(self._seq[:2], [('a', 1), ('b', 2)])
        self.assertEqual(self._seq[1:2], [('b', 2)])
        self.assertEqual(self._seq[-1:], [('c', 3)])

    def test_ms_module_5(self) -> None:
        """Tests the Sequence classes set_item method with
        a specific index and slicing (slicing is not implemented)
        """
        self._seq.append(('a', 1))
        self._seq.append(('b', 2))
        self._seq.append(('c', 3))
        self._seq[0] = ('b', 2)
        self.assertEqual(self._seq[0], ('b', 2))

        with self.assertRaises(NotImplementedError):
            self._seq[:] = [('d', 4), ('g', 5)]


if __name__ == "__main__":
    unittest.main()
