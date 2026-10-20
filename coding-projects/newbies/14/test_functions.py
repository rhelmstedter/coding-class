from functions import functions_rule


def test_functions_rule():
    expected = "This is my first function! Woohoo!"
    assert functions_rule() == expected
