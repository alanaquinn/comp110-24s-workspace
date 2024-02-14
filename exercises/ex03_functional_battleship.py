"""Functional Battleship."""

__author__ = "730411985"

# 1 input_guess function definition
def input_guess(grid_size: int, ROW_COLUMN: str):
    """Prompt for and return user's row or column guess."""
    assert ROW_COLUMN == "row" or ROW_COLUMN == "column"
   
    if ROW_COLUMN == "row":
        guess = input(f"Guess a {ROW_COLUMN}:  ")
        while int(guess) <= 0 or int(guess) > grid_size:
            guess = input(f"The grid is only {grid_size} by {grid_size}. Try again:  ")
    else:
        guess = input(f"Guess a {ROW_COLUMN}:  ")
        while int(guess) <= 0 or int(guess) > grid_size:
            guess = input(f"The grid is only {grid_size} by {grid_size}. Try again:  ")
    return int(guess) 
           