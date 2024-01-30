import unittest
import a_zero


class TestNumberSwitch(unittest.TestCase):

    def test_number_switch1(self) -> None:
        num1 = 2005
        num2 = 348

        actual_ans = a_zero.switch_nums(num1, num2)
        expected_ans = num1 < num2

        self.assertTrue(actual_ans, expected_ans)

    def test_number_switch2(self) -> None:
        num1 = 3456
        num2 = 6789

        actual_ans = a_zero.switch_nums(num1, num2)
        expected_ans = num1 < num2

        self.assertTrue(actual_ans, expected_ans)

    def test_number_switch3(self) -> None:
        num1 = 678801
        num2 = 678802

        actual_ans = a_zero.switch_nums(num1, num2)
        expected_ans = num1 < num2

        self.assertTrue(actual_ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
