import unittest
from collections import deque
from day07 import check_line  # Replace 'your_module_name' with the actual module name


class TestCheckLineFunction(unittest.TestCase):

    def test_exact_match_with_addition(self):
        """Test when the target is achieved using only addition."""
        target = 15
        nums = deque([5, 5, 5])
        self.assertTrue(check_line(target, nums, 0))

    def test_exact_match_with_multiplication(self):
        """Test when the target is achieved using only multiplication."""
        target = 36
        nums = deque([2, 3, 6])
        self.assertTrue(check_line(target, nums, 1))

    def test_mixed_operations(self):
        """Test when the target is achieved using a mix of addition and multiplication."""
        target = 20
        nums = deque([3, 7, 2])
        self.assertTrue(check_line(target, nums, 0))  # (3 + 7) * 2 = 20

    def test_no_solution(self):
        """Test when no combination of operations achieves the target."""
        target = 21
        nums = deque([3, 7, 2])
        self.assertFalse(check_line(target, nums, 0))  # No valid combination results in 21

    def test_single_number_equal_target(self):
        """Test when the list contains a single number equal to the target."""
        target = 10
        nums = deque([10])
        self.assertTrue(check_line(target, nums, 0))

    def test_single_number_not_target(self):
        """Test when the list contains a single number not equal to the target."""
        target = 10
        nums = deque([5])
        self.assertFalse(check_line(target, nums, 0))

    def test_large_numbers(self):
        """Test with large numbers."""
        target = 100000
        nums = deque([10, 20, 5000])
        self.assertFalse(check_line(target, nums, 0))

    def test_impossible_case(self):
        """Test when the target is clearly impossible."""
        target = 1
        nums = deque([10, 20, 30])
        self.assertFalse(check_line(target, nums, 0))


if __name__ == '__main__':
    unittest.main()
