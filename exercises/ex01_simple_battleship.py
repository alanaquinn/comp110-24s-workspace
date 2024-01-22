"""EX01 - Simple Battleship - A cute step towards Battleship."""

__author__ = "730411985"
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
user1_input: str = input("Pick a secret boat location between 1 and 4: ")
user_number: int = int(user1_input)
if user_number > 4:
    print(f"Error! {user1_input} too high!")
    exit()
if user_number < 1:
    print(f"Error! {user1_input} too low!")
    exit()
user2_input: str = input("Guess a number between 1 and 4: ")
user_number: int = int(user2_input)
if user_number > 4:
    print(f"Error! {user2_input} too high!")
    exit()
if user_number < 1:
    print(f"Error! {user2_input} too low!") 
    exit()
if user2_input == user1_input:
    if user2_input == "1":
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if user2_input == "2":
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    if user2_input == "3":
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    if user2_input == "4":
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship.")
else:
    if user2_input == "1":
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if user2_input == "2":
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
    if user2_input == "3":
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
    if user2_input == "4":
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
    print("Incorrect! You missed the ship.")