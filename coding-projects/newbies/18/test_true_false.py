from unittest.mock import patch

from true_false import get_username, print_username


@patch('builtins.input')
def test_get_username(input_mock):
    input_mock.return_value = 'bob'
    assert get_username() == 'bob'


def test_print_username_true(capfd):
    print_username('Julian')
    actual = capfd.readouterr()[0].strip()
    expected = 'Your username is: Julian.'
    assert actual == expected


def test_print_username_another_name(capfd):
    print_username('pybites')
    actual = capfd.readouterr()[0].strip()
    expected = 'Your username is: pybites.'
    assert actual == expected


def test_print_username_false(capfd):
    print_username('')
    actual = capfd.readouterr()[0].strip()
    expected = 'Sorry, no username was defined.'
    assert actual == expected


def test_print_username_another_false(capfd):
    print_username([])
    actual = capfd.readouterr()[0].strip()
    expected = 'Sorry, no username was defined.'
    assert actual == expected
