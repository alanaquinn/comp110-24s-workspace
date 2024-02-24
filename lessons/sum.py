"""Summing the elements of a list using different loops."""

__author__ = "730411985"


def w_sum(vals: list[float]) -> float:
    """Return sum of vals using while loop."""
    sum: float = 0.0
    index: int = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Return sum of vals using for... in... loop."""
    sum: float = 0.0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculate and return sum of all vals using for... in range... loop."""
    sum: float = 0.0
    for index in range(len(vals)):
        sum += vals[index]
    return sum