from unittest.mock import patch
import inspect
import re


@patch('builtins.input')
def test_user_input(input_mock):
    import user_input
    src_lines = [line.replace("? ", "?").strip() for line in
                 inspect.getsourcelines(user_input)[0]]

    pattern = re.compile(r'month\s*=\s*input\("What\'s the name of the 12th month '
                         r'of the calendar year\? ?"\)')

    assert any(pattern.match(line) for line in src_lines)
