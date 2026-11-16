from unittest.mock import patch

import pytest
from exceptions import PI, get_number, calculate_circle_area


@patch("builtins.input", return_value="2.3")
def test_good_number(input_mock):
    assert get_number() == 2.3


@patch("builtins.input", return_value="2a3")
def test_bad_number(input_mock):
    assert get_number() == "You can only enter numbers here."


def test_calculate_circle_area():
    assert calculate_circle_area(1) == PI


def test_calculate_circle_area_negative_radius():
    with pytest.raises(ValueError, match="The radius must be positive."):
        calculate_circle_area(-1)
