from special_chars import multiline_string_with_tabs


def test_multiline_string_with_tabs():
    output = multiline_string_with_tabs()
    # stripping off final newline as not required
    lines = output.rstrip().splitlines()
    assert '\tGood morning!' in lines
    assert '\tToday I will code.' in lines
    assert '\tPython :)' in lines
