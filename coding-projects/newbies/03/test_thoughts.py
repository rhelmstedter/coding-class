import inspect
import re

import thoughts


def test_print_my_thoughts():
    expected = 'print("I find it unbearable that there are people out there who think DC is better than Marvel!")'

    # normalize the imported submitted code
    actual_code = inspect.getsource(thoughts).strip()

    # remove 2+ spaces and newlines, and replace single quotes with double quotes
    normalized_code = re.sub(r" {2,}", "", actual_code.replace("\n", "").replace("'", '"'))

    # check if the expected string is in the normalized code
    assert expected in normalized_code

