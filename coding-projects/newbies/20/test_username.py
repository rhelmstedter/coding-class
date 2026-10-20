import inspect
import re
from unittest.mock import patch

from username import get_username


@patch('builtins.input',
       side_effect=['PyBites'])
def test_get_username_right_at_first_attempt(input_mock, capfd):
    get_username()
    output = capfd.readouterr()[0].strip()
    # program breaks
    assert output == ''


@patch('builtins.input',
       side_effect=['pybites', 'PyBites'])
def test_get_username_one_failed_then_right(input_mock, capfd):
    get_username()
    output = capfd.readouterr()[0].strip()
    assert output == 'Invalid username.'


@patch('builtins.input',
       side_effect=['pybites', 'blabla', 123, 'PyBites'])
def test_get_username_3_failed_then_correct(input_mock, capfd):
    get_username()
    output = capfd.readouterr()[0].strip()
    assert output == '\n'.join(
        ['Invalid username.'] * 3
    )


def test_uses_input_builtin_to_ask_username():
    src = inspect.getsource(get_username)
    regex = r'''input\(.*Please type in the name.*PyBites.*:'''
    assert re.search(regex, src)
