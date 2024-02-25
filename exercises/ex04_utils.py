"""List utility function exercise."""

__author__ = "730411985"


def all(group: list[int], single: int) -> bool:
    """Check if all numbers in group of int are equal to single int."""
    index: int = 0
    while index < len(group):
        if group[index] != single:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Return largest in a list of nums."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    high_num: int = input[0]
    while index < len(input):
        if input[index] > high_num:
            high_num = input[index]
        index += 1
    return high_num
    

def is_equal(first: list[int], second: list[int]) -> bool:
    """Determine if all numbers in a list of numbers are equal to all numbers in another list."""
    index_first: int = 0
    index_second: int = 0
    while index_first <= len(first) and index_second <= len(second):
        index_first += 1
        index_second += 1
        if first[index_first] == second[index_second]:
            return True
        else:
            return False


def extend(original: list[int], add: list[int]) -> None:
    """Mutate original list by appending second list to end."""
    original.extend(add)