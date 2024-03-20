"""Dictionary."""

__author__ = "730411985"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest

def test_invert_word() -> None:  # 1.1 USE unit test- failed () vs [], passed!!
    """Test the basic function of invert by reversing the orders of 2 sets of words."""
    original_dict: dict[str, str] = {"bean" : "green", "pepper" : "bell"}
    inverted_dict: dict[str, str] = invert(original_dict)
    assert inverted_dict == {'green' : 'bean', 'bell' : 'pepper'}


def test_invert_letter_and_num() -> None:  # 1.2 USE unit test- passed!!
    """Test the basic function of invert using numbers and words."""
    original_dict: dict[str, str] = {'5' : 'vanilla', '3' : 'strawberry', '8' : 'chocolate'}
    inverted_dict: dict[str, str] = invert(original_dict)
    assert inverted_dict == {'vanilla' : '5', 'strawberry' : '3', 'chocolate' : '8'}


def test_invert_key_error() -> None:  # 1.3 EDGE unit test- (failed num and word reverse), passed!!
    """Test to make sure KeyError is raised in response to duplicates."""
    with pytest.raises(KeyError):
        repeat_dict= {'vanilla' : '4', 'strawberry' : '4'}
        invert(repeat_dict)


def test_favorite_color_friends() -> None:  # 2.1 USE unit test- passed!!
    """Test basic function of favorite_color using friends' favorites"""
    friends: dict[str, str] = {'Melody' : 'blue', 'Laura' : 'red', 'Mackie' : 'green', 'Christine' : 'blue'}
    assert favorite_color(friends) == 'blue'


def test_favorite_color_coworkers() -> None:  # 2.2 USE unit test- passed!!
    """Test basic function of favorite_color using coworkers' favorites"""
    coworkers: dict[str, str] = {'Jack' : 'red', 'Marie' : 'orange', 'Zack' : 'orange', 'Jamie' : 'blue'}
    assert favorite_color(coworkers) == 'orange'


def test_favorite_color_tie() -> None:  # 2.3 EDGE unit test- passed!!
    """Edge test for favorite_color for tie functionality"""
    tie: dict[str, str] = {'Ann' : 'green', 'Kyla' : 'red', 'Heather' : 'red', 'Garrett' : 'green'}
    assert favorite_color(tie) == 'green'  # should return first item in dictionary, not first that gets 2


def test_count_colors() -> None:  # 3.1 USE unit test- passed!!
    """Test basic use of count by finding amount each color shows up in favorite colors."""
    colors_from_friends_coworkers_and_tie: list[str] = ['blue', 'red', 'green', 'blue', 'red', 'orange', 'orange', 'blue', 'green', 'red', 'red', 'green']
    assert count(colors_from_friends_coworkers_and_tie) == {'blue' : 3, 'red' : 4, 'green' : 3, 'orange' : 2}


def test_count_excrescence() -> None:  # USE 3.2 unit test- failed (used curly braces for list), passed!!
    """Test basic use of count by finding amount each letter in the word excrescence."""
    excrescence_by_letter: list[str] = ['e', 'x', 'c', 'r', 'e', 's', 'c', 'e', 'n', 'c', 'e']
    assert count(excrescence_by_letter) == {'e' : 4, 'x' : 1, 'c' : 3, 'r' : 1, 's' : 1, 'n' : 1}


def test_count_single_letter() -> None:  # 3.3 EDGE unit test- passed!!
    """Test edge use of count by finding amount single letter."""
    single_letter: list[str] = {'a'}
    assert count(single_letter) == {'a' : 1}


def test_alphabetizer_grocery() -> None:  # 4.1 USE unit test- passed!!
    """Test basic use of aphabetizer using grocery list."""
    groceries: list[str] = ['bread', 'chips', 'snacks', 'bacon', 'sausage', 'chicken', 'bananas', 'soda', 'butter', 'cookies']
    assert alphabetizer(groceries) == {'b' : ['bread', 'bacon', 'bananas', 'butter'], 'c' : ['chips', 'chicken', 'cookies'], 's' : ['snacks', 'sausage', 'soda']}


def test_alphabetizer_animals() -> None:  # 4.2 USE unit test- passed!!
    """Test basic use of aphabetizer using animals."""
    animals: list[str] = ['deer', 'alligator', 'eagle', 'alpaca', 'ant', 'dolphin', 'elephant', 'dog', 'duck', 'emu']
    assert alphabetizer(animals) == {'d' : ['deer', 'dolphin', 'dog', 'duck'], 'a' : ['alligator', 'alpaca', 'ant'], 'e' : ['eagle', 'elephant', 'emu']}


def test_alphabetizer_characters() -> None:  # 4.3 EDGE unit test- passed!!
    """Test edge use of aphabetizer with special characters."""
    special_characters: list[str] = ['!dog', '$dog', 'dog', '$duck', '!duck', 'duck', 'deer', '!deer', '$deer', '!dolphin']
    assert alphabetizer(special_characters) == {'!' : ['!dog', '!duck', '!deer', '!dolphin'], '$' : ['$dog', '$duck', '$deer'], 'd' : ['dog', 'duck', 'deer']}


def test_update_attendance_add_to_existing() -> None:  # 5.1 USE unit test- failed (original function did not return anything), passed!!
    """Test basic use of update_attendance by adding names of friends who were present for each night."""
    movie_week: dict = {'Monday' : ['Melody', 'Laura', 'Garrett', 'Gavin'], 'Wednesday' : ['Melody', 'Laura']}
    attendance_log: dict[str, list[str]] = update_attendance(movie_week, 'Wednesday', 'Zoe')
    assert attendance_log == {'Monday' : ['Melody', 'Laura', 'Garrett', 'Gavin'], 'Wednesday' : ['Melody', 'Laura', 'Zoe']}


def test_update_attendance_add_day() -> None:  # 5.2 USE unit test- passed!!
    """Test basic use of update_attendance by adding new day and attendee to log."""
    movie_week_updated: dict = {'Monday' : ['Melody', 'Laura', 'Garrett', 'Gavin'], 'Wednesday' : ['Melody', 'Laura', 'Zoe']}
    attendance_log_two: dict[str, list[str]] = update_attendance(movie_week_updated, 'Friday', 'Garrett')
    assert attendance_log_two == {'Monday' : ['Melody', 'Laura', 'Garrett', 'Gavin'], 'Wednesday' : ['Melody', 'Laura', 'Zoe'], 'Friday' : ['Garrett']}


def test_update_attendance_empty_num_multiple() -> None:  # 5.3 EDGE unit test- failed (should use [[]] to hold student numbers), passed!!
    """Test edge use for empty initial list, student number instead of names, and adding multiple student numbers in single line of code."""
    empty_log: dict = {}
    add_day_and_student_no: dict[str, list[str]] = update_attendance(empty_log, 'Monday', ['311', '457', '126', '945'])
    assert add_day_and_student_no == {'Monday' : [['311', '457', '126', '945']]}