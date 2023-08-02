import math
from typing import List


def get_primes(numbers: List[int]):
    # Iterate over each number in the list
    for num in numbers:
        # Skip numbers less than or equal to 1
        if num <= 1:
            continue
        is_prime = all(num % next_num != 0
                       for next_num in range(2,
                                             int(math.sqrt(num)) + 1))
        if is_prime:
            yield num
# import sympy
#
#
# def get_primes(numbers):
#     for num in numbers:
#         if sympy.isprime(num):
#             yield num
# Test the function
import unittest


class Tests(unittest.TestCase):
    def test_zero(self):
        # Arrange
        numbers = [2, 4, 3, 5, 6, 9, 1, 0]
        # Act
        res = list(get_primes(numbers))
        # Assert
        self.assertEqual(res, [2, 3, 5])


if __name__ == '__main__':
    unittest.main()
