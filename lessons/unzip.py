"""Splitting a dictionary into two lists."""

__author__ = "730411985"


def get_keys(keys_and_vals: dict[str, int]) -> list[str]:
    """Gather all keys from a dictionary into a list."""
    list_keys: list[str] = []  # empty list to hold keys
    for key in keys_and_vals.keys():
        list_keys.append(key)  # += does not work, use append stupid
    return list_keys


def get_values(vals_and_keys: dict[str, int]) -> list[int]:
    """Gather all values from a dictionary into a list."""
    list_vals: list[int] = []
    for value in vals_and_keys.values():
        list_vals.append(value)
    return list_vals


# 93/100 updates:
# fixed whitespaces on lines 6 and 17 (14)
# removes tests on lines 14 and 25
# fixed line 16 bc had copied and pasted without fixing str > int
# 99/100 updates:
# accidentally left 3 spaces after get_values fxn