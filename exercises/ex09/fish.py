"""File to define Fish class."""

__author__ = "730411985"


class Fish:
    """Fish living in river."""
    age: int

    def __init__(self):
        """Fish constructor."""
        self.age: int = 0
        return None
    
    def one_day(self) -> None:
        """Increase fish age by day."""
        self.age += 1
        return None