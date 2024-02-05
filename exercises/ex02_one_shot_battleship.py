"""One Shot Battleship"""

__author__ = "730411985"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
GRID : int = 4
SECRET_ROW : int = 3
SECRET_COLUMN : int = 2

row_str : str = input("Guess a row: ")
row_guess : int = int(row_str)
row_invalid: bool = row_guess > GRID or row_guess < 1
row_valid: bool = False
while row_invalid :
    row_str_redo : str = input(f"The grid is only {GRID} by {GRID}. Try again: ")
    row_guess_redo : int = int(row_str_redo)
    if row_guess_redo > 0 and row_guess_redo < GRID + 1:
        row_guess = row_guess_redo
        row_invalid = row_valid

column_str : str = input("Guess a column: ")
column_guess : int = int(column_str)
column_invalid: bool = column_guess > GRID or column_guess < 1
column_valid: bool = False
while column_invalid :
    column_str_redo : str = input(f"The grid is only {GRID} by {GRID}. Try again: ")
    column_guess_redo : int = int(column_str_redo)
    if column_guess_redo > 0 and column_guess_redo < GRID + 1:
        column_guess = column_guess_redo
        column_invalid = column_valid

def results(row_guess : int,column_guess : int) -> int
    return RED_BOX if hit_secret 
    else WHITE_BOX
row_counter = 1
while row_counter <= GRID:
    row_output = ""
    column_counter = 1
    if row_counter == SECRET_ROW:
        while column_counter <= GRID:
            if column_counter == SECRET_COLUMN :
              row_output += RED_BOX
            else:
                row_output += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= GRID
            row_output += BLUE_BOX
            column_counter += 1
    print (row_output)
    row_counter += 1
if row_guess == SECRET_ROW and column_guess SECRET_COLUMN:
    hit_secret = True
    
else: 
    hit_secret = False
    

 
if hit_secret = True
    print("Hit!")
else: 
    print("Miss!")