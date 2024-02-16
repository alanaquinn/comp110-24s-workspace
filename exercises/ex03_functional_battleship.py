"""Functional Battleship."""

__author__ = "730411985"
import random  # for __name__ == "__main__"
# constants
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


# 1 input_guess function definition
def input_guess(grid_size: int, row_column: str) -> int:
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


def print_grid(grid_size: int, row_guess: int, column_guess: int, win_or_lose: bool) -> None:
    """Print game board boxes."""
    for i in range(grid_size):  # i represents row number in python
        for j in range(grid_size):  # j represents column number in python
            if i == row_guess - 1 and j == column_guess - 1:  # kept adding one to the output so did -1
                if win_or_lose:
                    print(RED_BOX, end="")
                else:
                    print(WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
        print()


# 3 correct_guess function definition
def correct_guess(correct_row: int, correct_column: int, row_guess: int, column_guess: int) -> bool:
    """Assess correct location vs guess to determine if correct."""
    return correct_row == row_guess and correct_column == column_guess


# 4 main function definition
def main(grid_size: int, correct_row: int, correct_column: int) -> None:
    """Put together all functions for game to run and respond corrrectly."""
    guesses = 1  # keep track of how many turns
    available_guesses = 5  # make game flexible to changes
    win = False  # stop asking if correct guess made
    while guesses <= available_guesses and not win:
        print(f"=== Turn {guesses}/{available_guesses} ===")
        row_guess = input_guess(grid_size, "row")  # call input_guess from part 1 for row and column (in bounds)
        column_guess = input_guess(grid_size, "column")
        
        win_or_lose = correct_guess(correct_row, correct_column, row_guess, column_guess)  # call correct_guess to verify
        print_grid(grid_size, row_guess, column_guess, win_or_lose)  # call print_grid for emojis of guess
        
        if win_or_lose:  # use correct_guess function to control words output
            print("Hit!")
            print(f"You won in {guesses}/{available_guesses} turns!")
            win = True  # exit while loop
        else:
            print("Miss!")
            guesses += 1
    if not win:  # used all turns without win_or_lose so lost
        print("X/5 - Better luck next time!")
# EVERYTHING WORKING FINALLY!!!!
# run as module, play with random grid and locations, other modules can import
        

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))