"""Dictionary."""

__author__ = "730411985"


def invert(dictionary_original: dict[str, str]) -> dict[str, str]:
    dictionary_inverted: dict[str, str] = {}  # establish empty dictionary for reversed
    for key, value in dictionary_original.items():  # iterate through each key, value in og dictionary items
        if value in dictionary_inverted:  # make sure there are no duplicated by comparing current value looking at to those already swapped
            raise KeyError("Keys are not unique.")
        dictionary_inverted[value] = key  # swap dict value and dict key
    return dictionary_inverted

print(invert({'a': 'z', 'b': 'y', 'c': 'x'}))  # works
print(invert({'apple': 'cat'}))  # works
# other test worked but would not continue to other functions 


def favorite_color(dictionary_colors: dict[str, str]) -> str:
    common: dict[str, str] = {}  # establish empty dictionary for most common color amt
    for color in dictionary_colors.values():  # iterate over all values (colors) in dictionary
        common[color] = common.get(color, 0) + 1  # add to amount of occurences of specific value **.get found online as method of retrieval for current count

    most = max(common.values())  # the highest value from those collected in the common dictionary
    fav = None  # if there is no most common + store updated most common
    for color, amount in common.items():  # loop iterates over all colors and amounts collected in dictionary
        if amount == most:  # if most (highest value from common dict) is equal to amount correlating to current color:
            fav = color  # update fav to current color, also triggers exit from while loop
            break  # function found online to exit loop because could not make while loop work
    return fav  # IT WORKED!!!!!

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(list_input: list[str]) -> dict[str, int]:
    dict_output: dict[str, int] = {}  # empty dictionary for string name and times string is in list
    for item in list_input:  # iterate through all items in input list
        if item in dict_output:  # check if already established
            dict_output[item] += 1  # add one to value associated with item/key if bool is true
        else:
            dict_output[item] = 1  # item not in dict already so assign val of 1
    return dict_output  # effectively returns quantity of each item in random list


def alphabetizer(list_to_alphabetize: list[str]) -> dict[str, list[str]]:
    dict_alphabetized: dict[str, list[str]] = {}
    for item in list_to_alphabetize:  # iterate through all items in list
        letter_one = item[0].lower()  # find first letter in item being looked at
        if letter_one in dict_alphabetized:  # group words with same first letter
            dict_alphabetized[letter_one].append(item)  # add to dictionary with other same first letter
        else:
            dict_alphabetized[letter_one] = [item]  # make new key (first letter) with current item in it
    return dict_alphabetized

print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))
print(alphabetizer(["Python", "sugar", "Turtle", "party", "table"]))


def update_attendance(attendance_log: dict[str, list[str]], day: str, students: str) -> None:
    if day in attendance_log:  # if day in existing dictionary
        attendance_log[day].append(students)  # tried using += to add elements to dictionary but did not work, used append to add to list (value)
    else:  # new day
        attendance_log[day] = students

attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday" , "Vrinda")
update_attendance(attendance_log, "Wednesday" , "Kaleb")
print(attendance_log)