"""Dictionary."""

__author__ = "730411985"


def invert(dictionary_original: dict[str, str]) -> dict[str, str]:
    """Invert strings in dictionary."""
    dictionary_inverted: dict[str, str] = {}  # establish empty dictionary for reversed
    for key, value in dictionary_original.items():  # iterate through each key, value in og dictionary items
        if value in dictionary_inverted:  # make sure there are no duplicated by comparing current value looking at to those already swapped
            raise KeyError("Keys are not unique.")
        dictionary_inverted[value] = key  # swap dict value and dict key
    return dictionary_inverted


def favorite_color(dictionary_colors: dict[str, str]) -> str:
    """Return most common color from dictionary of favorite colors by name."""
    common: dict[str, int] = {}  # establish empty dictionary for most common color amt
    for color in dictionary_colors.values():  # iterate over all values (colors) in dictionary
        common[color] = common.get(color, 0) + 1  # add to amount of occurences of specific value **.get found online as method of retrieval for current count

    most = max(common.values())  # the highest value from those collected in the common dictionary
    fav = " "  # if there is no most common + store updated most common # 39/50 update # 48/50 update # 49/50 update
    for color, amount in common.items():  # loop iterates over all colors and amounts collected in dictionary
        if amount == most:  # if most (highest value from common dict) is equal to amount correlating to current color:
            fav = color  # update fav to current color, also triggers exit from while loop
            break  # function found online to exit loop because could not make while loop work
    return fav  # IT WORKED!!!!!


def count(list_input: list[str]) -> dict[str, int]:
    """Count number of appearances of items in a list."""
    dict_output: dict[str, int] = {}  # empty dictionary for string name and times string is in list
    for item in list_input:  # iterate through all items in input list
        if item in dict_output:  # check if already established
            dict_output[item] += 1  # add one to value associated with item/key if bool is true
        else:
            dict_output[item] = 1  # item not in dict already so assign val of 1
    return dict_output  # effectively returns quantity of each item in random list


def alphabetizer(list_to_alphabetize: list[str]) -> dict[str, list[str]]:
    """Group items with the same first letter into separate dictionaries."""
    dict_alphabetized: dict[str, list[str]] = {}
    for item in list_to_alphabetize:  # iterate through all items in list
        letter_one = item[0].lower()  # find first letter in item being looked at
        if letter_one in dict_alphabetized:  # group words with same first letter
            dict_alphabetized[letter_one].append(item)  # add to dictionary with other same first letter
        else:
            dict_alphabetized[letter_one] = [item]  # make new key (first letter) with current item in it
    return dict_alphabetized


def update_attendance(attendance_log: dict[str, list[str]], day: str, students: str) -> dict[str, list[str]]:  # UPDATED FOR EX06
    """Add names to days of the week in a dictionary for attendance."""
    if day in attendance_log:  # if day in existing dictionary
        attendance_log[day].append(students)  # tried using += to add elements to dictionary but did not work, used append to add to list (value)
    else:  # new day
        attendance_log[day] = [students] 
    return attendance_log  # CHANGE MADE FOR EX06 BECAUSE LACK OF RETURN MADE IT SO ASSERTION WOULD NOT WORK 


# 39/50: updates
# removed tests because they were resulting in errors
# attempted to fix "Omitting 2 identical items..." error code
# added docstrings and 2 blank lines after all
# fixed line 18 (str, int) to resolve errors in line 20
# made fav (the return) in favorite_color str = None
        
# 48/50: updates
# made fav an empty string in favorite_colors
    # was stupid and thought they could concatenate but wont because not +=
# accidentally only had one space on inline comment

# 49/50: updates
# did "" instead of " " in line 23
        
# 49/50: updates again
# error was in the lack of a space between fav and =