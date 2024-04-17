"""File to define Bear class."""

__author__ = "730411985"


class Bear:
    """Bears living in river."""
    age: int
    hunger_score: int 

    def __init__(self):
        """Bear constructor."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self) -> None:
        """Increase bear age and decrease bear hunger daily."""
        self.age += 1
        self.hunger_score -= 1  # 2/2.1
        return None
    
    def eat(self, num_fish: int) -> None:  # 2/2.2
        """Bear hunger increase by number of fish."""
        self.hunger_score += num_fish
        return None