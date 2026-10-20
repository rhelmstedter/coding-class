import random
from unittest.mock import patch

from random_module import guess_my_number

random.seed(0)


@patch(
    "builtins.input",
    side_effect=[
        50,
    ],
)
def test_correct_guess(input_mock):
    actual = guess_my_number()
    assert actual == "You got it!"


@patch(
    "builtins.input",
    side_effect=[
        1,
    ],
)
def test_guess_my_number(input_mock):
    actual = guess_my_number()
    assert actual == "Your guess is too low."


@patch(
    "builtins.input",
    side_effect=[
        100,
    ],
)
def test_guess_too_high(input_mock):
    actual = guess_my_number()
    assert actual == "Your guess is too high."
