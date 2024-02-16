"""Mutating functions."""

__author__ = "730411985"


def manual_append(list_one: list[int], number: int) -> None:
    """Mutate list/list_one by adding number to end."""
    list_one.append(number) 


def double(list_two: list[int]) -> None:
    """Mutate list/list_two by multiplying by 2."""
    index = 0  # use while loop to go through each item
    while index < len(list_two):
        list_two[index] *= 2
        index += 1  # move to next index in list/word_two