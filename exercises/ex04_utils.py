"""List utility function exercise."""

__author__ = "730411985"


def all(group: list[int], single: int) -> bool:
    """Check if all numbers in group of int are equal to single int."""
    if not group:  # fix "all - Should return False when list is empty. (Edge Case.) (0/5)" error
        return False
    
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
    if len(first) != len(second):  # lists have same elements but different lengths error
        return False
    
    index: int = 0  # only one index counter for simplicity
    while index < len(first) and index < len(second):
        if first[index] != second[index]:
            return False
        index += 1
    
    return True


def extend(original: list[int], add: list[int]) -> None:
    """Mutate original list by appending second list to end."""
    original.extend(add)

# All errors fixed!!!!