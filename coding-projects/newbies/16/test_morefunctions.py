from unittest.mock import patch

import pytest

from morefunctions import multiply_numbers, enter_name


@pytest.mark.parametrize("x, y, product", [
    (10, 5, 50), (10, 10, 100), (5, -2, -10), (-3, -2, 6), (7, 0, 0), (2.5, 4, 10),
])
def test_multiply_numbers(x, y, product):
    assert multiply_numbers(x, y) == product


@patch("builtins.input")
def test_enter_name(input_mock):
    input_mock.return_value = "bob"
    assert enter_name() == "bob"
    input_mock.return_value = "Ada"
    assert enter_name() == "Ada"
