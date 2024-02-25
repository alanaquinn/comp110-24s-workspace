"""List utility function exercise."""

__author__ = "730411985"


def all(group: list[int], single: int) -> bool:
    """Check if all numbers in group of int are equal to single int."""
    index: int = 0
    same: bool = True
    while index <= len(group):
        if group[index] != single:
            same = False
        index += 1
    return same



def max(nums: list[int]) -> int:
    """Return largest in a list of nums."""
    index: int = 0
    high_num: int = 0
    while index <= len(nums):
        if nums[index] > high_num:
            high_num = nums[index]
        index += 1
    if nums[index] < 0:
        print("ValueError: max() arg is an empty List")
    
