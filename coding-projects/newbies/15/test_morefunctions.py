from unittest.mock import patch

from morefunctions import (multiply_numbers,
                           enter_name,
                           a, b)


def test_multiply_numbers():
    assert multiply_numbers(a, b) == 50
    assert multiply_numbers(10, 10) == 100
    assert multiply_numbers(5, -2) == -10
    assert multiply_numbers(-3, -2) == 6


@patch('builtins.input')
def test_enter_name(input_mock):
    input_mock.return_value = 'bob'
    assert enter_name() == 'bob'
