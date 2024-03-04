import unittest
# import hypothesis
# from hypothesis.strategies import text, characters
from hypothesis import given, settings, strategies as st
from morsecodepalindrome import Palindrome
from pattern import PatternMatch
# from morsecode import MorseCode
import unittest_comp_func as utcf


class TestPalindromes(unittest.TestCase):
    custom_alphabet = \
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU"\
        "VWXYZ0123456789@:;<=>?][\\^`–!#$%&')(~*+,-./\" "

    def setUp(self) -> None:
        self.palindrome = Palindrome()

    def tearDown(self) -> None:
        return super().tearDown()

    @settings(deadline=None)
    @given(input_str=st.text(alphabet=st.sampled_from(custom_alphabet),
           min_size=0, max_size=80))
    def test_morse_code_func(self, input_str: str) -> None:
        str_pattern = PatternMatch(input_str)
        removed_pattern: str = str_pattern.remove_str_patterns()
        actual_ans = self.palindrome.morse_code_str(
            removed_pattern
        )
        expected_ans = utcf.main(input_str)
        self.assertEqual(actual_ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
