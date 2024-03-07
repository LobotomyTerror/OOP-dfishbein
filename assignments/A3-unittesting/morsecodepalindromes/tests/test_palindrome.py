"""Module that tests against the two modules to see if the
results are True or False using hypothesis. As well as, it
compares the outputs of these two modules to see if the
outputs are the same.

    Returns:
        None
"""

import unittest
import re
from hypothesis import given, settings, strategies as st
from unittest.mock import patch
from io import StringIO
from morsecodepalindrome import Palindrome
from pattern import PatternMatch
import unittest_comp_func as utcf


class TestPalindromes(unittest.TestCase):
    """Class that uses the unittest module for
    running tests on the other Modules that are
    provided.

    Args:
        unittest: unittest module

    Returns:
        None
    """
    custom_alphabet: str = \
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU"\
        "VWXYZ0123456789@:;<=>?][\\^`–!#$%&')(~*+,-./\" "

    def setUp(self) -> None:
        """Sets up the class
        """
        self.palindrome = Palindrome()

    def tearDown(self) -> None:
        """Stops any running processes

        Returns:
            super: deconstructs the module
        """
        return super().tearDown()

    @settings(deadline=None)
    @given(input_str=st.text(alphabet=st.sampled_from(custom_alphabet),
           min_size=0, max_size=80))
    def test_morse_code_func(self, input_str: str) -> None:
        """Checks if the operation in the MorseCodePalindrome
        module is returning correctly by comparing it against the
        utcf module if it True or False.

        Args:
            input_str (str): Hypothesis generated string based off
            the supplied alphabet that is provided above.
        """
        str_pattern: PatternMatch = PatternMatch(input_str)
        removed_pattern: str = str_pattern.remove_str_patterns()
        actual_ans: bool = self.palindrome.morse_code_str(
            removed_pattern
        )
        expected_ans: bool = utcf.morse_code_palindrome(input_str)
        self.assertEqual(actual_ans, expected_ans)

    @settings(deadline=None)
    @given(input_str=st.text(alphabet=st.sampled_from(custom_alphabet),
                             min_size=0, max_size=80))
    def test_morse_code_module(self, input_str: str) -> None:
        """This function checks against the MorseCodePalindrome
        output and compares the output of the utcf against it to
        make sure that they are printing out the same results.

        Args:
            input_str (str): Hypothesis generated string based off
            the supplied alphabet that is provided above.
        """
        with patch('sys.stdin', new=StringIO(input_str)):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.palindrome.main()
                expected_ans: str = mock_stdout.getvalue().strip()

        with patch('sys.stdin', new=StringIO(input_str)):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                utcf.main()
                actual_ans: str = mock_stdout.getvalue().strip()

        self.assertEqual(expected_ans, actual_ans)

    @settings(deadline=None)
    @given(input_str=st.text(alphabet=st.sampled_from(custom_alphabet),
                             min_size=0, max_size=80))
    def test_pattern_remover(self, input_str: str) -> None:
        """Checks if the regular expression removal is operating
        properly in the Module class comparing against a separate
        regex string

        Args:
            input_str (str): Hypothesis generated string based off
            the supplied alphabet that is provided above.
        """
        str_pattern: PatternMatch = PatternMatch(input_str)
        expected_ans: str = str_pattern.remove_str_patterns()
        regex_str = r"[@:;<=>?\][\\^`–!#$%&')(~*+,\-./\" ]*"
        actual_ans: str = re.sub(
            regex_str,
            "",
            input_str
        )
        self.assertEqual(expected_ans, actual_ans)


if __name__ == "__main__":
    unittest.main()

# I did have some trouble understanding how to setup the hypothesis
# portions to develop strings for me to test with. In that instance
# I did enlist the help of ChatGPT to help me understand how to
# setup hypothesis. Along with there site
# https://hypothesis.readthedocs.io/en/latest/quickstart.html to
# see about their documentation.
