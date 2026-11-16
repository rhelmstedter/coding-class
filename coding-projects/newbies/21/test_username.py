from unittest.mock import patch

from username import get_username

PROMPT = "Please type in the name PyBites"


def _asked_with_prompt(input_mock):
    return all(call.args and PROMPT in str(call.args[0]) for call in input_mock.call_args_list)


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
       side_effect=['pybites', 'blabla', '123', 'PyBites'])
def test_get_username_3_failed_then_correct(input_mock, capfd):
    get_username()
    output = capfd.readouterr()[0].strip()
    assert output == '\n'.join(
        ['Invalid username.'] * 3
    )


@patch('builtins.input',
       side_effect=['pybites', 'PyBites'])
def test_uses_input_with_the_prompt(input_mock, capfd):
    get_username()
    assert input_mock.call_count == 2, "Ask for the username with input() each time."
    assert _asked_with_prompt(input_mock), f"Use the prompt: {PROMPT}: "