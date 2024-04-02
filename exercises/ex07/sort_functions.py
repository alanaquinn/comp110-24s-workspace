"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:  # part 1b: works
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for i in range(1, len(x)):  # iterate through starting at 2
        current: int = x[i]  # store current
        j: int = i - 1  # index before current element
        while j >= 0 and current < x[j]:
            x[j + 1] = x[j]  # shift to right
            j -= 1  # move backwards
        x[j + 1] = current  # insert current in correct position
    return None


def selection_sort(x: list[int]) -> None:  # part 1a: works
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx: int = 0  # counter variable
    for idx in range(0,len(x)):  # overreaching loop
        min: int = idx  # variable to store the index of the minimum element
        for j in range(idx + 1, len(x)):  # secondary counter
            if x[j] < x[min]:
                min = j
        if min != idx:
            x[idx], x[min] = x[min], x[idx]  # swap variables
        idx +=1
    return None
    