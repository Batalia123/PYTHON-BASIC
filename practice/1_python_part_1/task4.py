"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]
"""
# because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    list1 = [x**2 for x in ints]
    list_substract = [-x + y for x, y in zip(ints[:-1], list1[:-1])]
    list_substract.insert(0, 0)
    return [x - y for x, y in zip(list1, list_substract)]
