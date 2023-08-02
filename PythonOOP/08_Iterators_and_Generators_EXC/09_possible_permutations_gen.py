from typing import List
from itertools import permutations


def possible_permutations(numbers: List[int]):
    # Generate all possible permutations of the numbers list
    for number in list(permutations(numbers)):
        # Yield each permutation as a list
        yield list(number)
# Print each permutation returned by possible_permutations
for permutation in possible_permutations([1, 2, 3]):
    print(permutation)
