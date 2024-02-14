"""Chat help"""

GRID_SIZE = 4
SECRET_ROW = 3
SECRET_COLUMN = 2

# Function to generate result box (red or white)
def get_result_box(is_hit):
    return "🔴" if is_hit else "⚪️"

# Initialize variables
row_counter = 1

# Loop through rows
while row_counter <= GRID_SIZE:
    emoji_row = ""
    column_counter = 1

    # Check if the user's row guess matches the current row
    if row_counter == SECRET_ROW:
        # Loop through columns for the matched row
        while column_counter <= GRID_SIZE:
            if column_counter == SECRET_COLUMN:
                # Check if the user's column guess matches the current column
                emoji_row += get_result_box(True)
            else:
                emoji_row += "🔵"
            column_counter += 1
    else:
        # Loop through columns for rows without a match
        while column_counter <= GRID_SIZE:
            emoji_row += "🔵"
            column_counter += 1

    # Print the row
    print(emoji_row)
    row_counter += 1

user_row = int(input("Enter your guess for row (1-4): "))
user_column = int(input("Enter your guess for column (1-4): "))

if user_row == SECRET_ROW and user_column == SECRET_COLUMN:
    print("Hit!")
else:
    print("Miss! The grid is only {} by {}. Try again:".format(GRID_SIZE, GRID_SIZE))

#2 attempt to create a function???
if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN :
    hit_correct = True
else:
    hit_correct = False
def result_box(row_guess, SECRET_ROW, column_guess, SECRET_COLUMN):
    if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN:
        return RED_BOX 
    else :
        return WHITE_BOX
