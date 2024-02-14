"""One Shot Battleship."""

__author__ = "730411985"
# constants
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
GRID: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2
# 1 user guesses for row and column
row_str: str = input("Guess a row: ")
row_guess: int = int(row_str)
row_invalid: bool = row_guess > GRID or row_guess < 1  # 1 account for invalid inputs and allow for grid range change
row_valid: bool = False
while row_invalid:  # 1 ability to reinput guess instead of exit
    row_str_redo: str = input(f"The grid is only {GRID} by {GRID}. Try again: ")
    row_guess_redo: int = int(row_str_redo)
    if row_guess_redo > 0 and row_guess_redo < GRID + 1:
        row_guess = row_guess_redo  # reset value of row
        row_invalid = row_valid  # exit while loop
column_str: str = input("Guess a column: ")
column_guess: int = int(column_str)
column_invalid: bool = column_guess > GRID or column_guess < 1
column_valid: bool = False
while column_invalid:
    column_str_redo: str = input(f"The grid is only {GRID} by {GRID}. Try again: ")
    column_guess_redo: int = int(column_str_redo)
    if column_guess_redo > 0 and column_guess_redo < GRID + 1:
        column_guess = column_guess_redo
        column_invalid = column_valid
# 2 emoji outputs
row_counter = 1  # 2.2 row int counter variable
while row_counter <= GRID:  # 2.3 while row counter less than or equal to grid to prevent unending loop
    row_output = " "  # 2.3.1 emoji storage
    column_counter = 1  # 2.3.2 column counter
    if row_counter == row_guess:  # 2.3.3 test if guess is in row being assessed
        while column_counter <= GRID:  # 2.3.3.1 keep in grid and prevent unending loop
            if column_counter == column_guess:  # 2.3.3.2 test if guess is in column being assessed
                if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN:  # 2.3.3.3 guess is correct
                    row_output += RED_BOX
                else:  # guess is incorrect
                    row_output += WHITE_BOX
            else:  # 2.3.3.2 guess is not in column being assessed so blue
                row_output += BLUE_BOX
            column_counter += 1
    else:  # 2.3.3 guess is not in row being assessed so blue
        while column_counter <= GRID:  # 2.3.4 not guess so add blue and progress to next column
            row_output += BLUE_BOX
            column_counter += 1
    print(row_output)  # 2.3.5 print emoji blocks generated from loops^
    row_counter += 1  # 2.3.6 increase row counter to move down to next row and rerun loop
# 1 hit or miss statements
# 3 hints
if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN: 
    print("Hit!")
elif column_guess == SECRET_COLUMN:
    print("Close! Correct column, wrong row.")
elif row_guess == SECRET_ROW:
    print("Close! Correct row, wrong column.")
else: 
    print("Miss!")