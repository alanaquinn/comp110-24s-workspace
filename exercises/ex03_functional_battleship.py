"""Functional Battleship."""

__author__ = "730411985"
# constants
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
# 1 input_guess function definition
def input_guess(grid_size: int, row_column: str):
    """Prompt for and return user's row or column guess."""
    assert row_column == "row" or row_column == "column"
    if row_column == "row":
           guess = input(f"Guess a {row_column}: ")
           while int(guess) <= 0 or int(guess) > grid_size:
               guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else:
        guess = input(f"Guess a {row_column}: ")
        while int(guess) <= 0 or int(guess) > grid_size:
            guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    return int(guess) 
# 2 print_grid function definition
row_counter = 1
def print_grid(grid_size: int, row_guess: int, column_guess: int, is_correct: bool) -> None:
    for i in range(grid_size):
        for j in range (grid_size):
            if i == row_guess - 1 and j == column_guess - 1: #kept adding one to the output so did -1
                if is_correct:
                    print(RED_BOX, end="")
                else:
                    print(WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
        print()
# 3 correct_guess function definition
def correct_guess(correct_row: int, correct_column: int, row_guess: int, column_guess: int) -> bool:
    return correct_row == row_guess and correct_column == column_guess
# 4 main function definition
def main(grid_size: int, correct_row: int, correct_column: int) -> None:
    