from letters import get_letters_from_string


def test_discard_numbes_and_exclamation_mark():
    assert get_letters_from_string("123abcABC!") == "a-b-c-A-B-C"


def test_discard_numbes_and_spaces():
    assert get_letters_from_string("Hello World 2024 ") == "H-e-l-l-o-W-o-r-l-d"


def test_discard_other_non_ascii_letter_chars():
    assert get_letters_from_string("@#Sky^Is.Blue@") == "S-k-y-I-s-B-l-u-e"
