"""Tests for the Your Turn section of Python - Modulo."""
import re

import modulo_practice


def _get(name):
    func = getattr(modulo_practice, name, None)
    assert callable(func), f"Define a function called {name}() in the Your Code cell."
    return func


def _numbers_in(text):
    return [int(number) for number in re.findall(r"\d+", str(text))]


def test_hours_and_minutes():
    hours_and_minutes = _get("hours_and_minutes")
    assert _numbers_in(hours_and_minutes(137)) == [2, 17]
    assert _numbers_in(hours_and_minutes(95)) == [1, 35]
    assert _numbers_in(hours_and_minutes(180)) == [3, 0]


def test_pass_to_middle_of_table():
    pass_to = _get("pass_to")
    people = ["Ada", "Grace", "Alan", "Katherine", "Linus"]
    assert pass_to(people, "Ada") == "Grace"
    assert pass_to(people, "Alan") == "Katherine"


def test_pass_to_wraps_around():
    pass_to = _get("pass_to")
    assert pass_to(["Ada", "Grace", "Alan", "Katherine", "Linus"], "Linus") == "Ada"
    assert pass_to(["Mon", "Tue", "Wed"], "Wed") == "Mon"


def test_shift_vowel_forward():
    shift_vowel = _get("shift_vowel")
    assert shift_vowel("A", 1) == "E"
    assert shift_vowel("E", 2) == "O"
    assert shift_vowel("A", 0) == "A"


def test_shift_vowel_wraps_around():
    shift_vowel = _get("shift_vowel")
    assert shift_vowel("U", 1) == "A"
    assert shift_vowel("O", 3) == "E"
    assert shift_vowel("I", 10) == "I"


def test_shift_vowel_backwards():
    shift_vowel = _get("shift_vowel")
    assert shift_vowel("E", -1) == "A"
    assert shift_vowel("A", -1) == "U"


def test_shift_vowel_not_a_vowel():
    shift_vowel = _get("shift_vowel")
    assert shift_vowel("B", 1) == "B", "A letter that is not a vowel comes back unchanged."
    assert shift_vowel("Z", 3) == "Z", "A letter that is not a vowel comes back unchanged."
