"""Tests for the Your Turn section of Python - Joining Strings with .join()."""
from unittest.mock import patch

import join_practice


def _get(name):
    func = getattr(join_practice, name, None)
    assert callable(func), f"Define a function called {name}() in the Your Code cell."
    return func


def test_dash_date():
    dash_date = _get("dash_date")
    assert dash_date(["2026", "11", "16"]) == "2026-11-16"
    assert dash_date(["1999", "12", "31"]) == "1999-12-31"


def test_slash_date():
    slash_date = _get("slash_date")
    assert slash_date(["2026", "11", "16"]) == "2026/11/16"
    assert slash_date(["1999", "12", "31"]) == "1999/12/31"


@patch("builtins.input", side_effect=["be", "less", "helpful"])
def test_print_sentence(input_mock, capfd):
    print_sentence = _get("print_sentence")
    print_sentence()
    assert input_mock.call_count == 3, "Ask for exactly three words with input()."
    output = capfd.readouterr()[0]
    assert "be less helpful" in output, "Print the three words with one space between them."


def test_remove_letter():
    remove_letter = _get("remove_letter")
    assert remove_letter("mississippi", "s") == "miiippi"
    assert remove_letter("mississippi", "i") == "msssspp"
    assert remove_letter("bagels", "z") == "bagels"


def test_make_acronym():
    make_acronym = _get("make_acronym")
    assert make_acronym(["portable", "network", "graphics"]) == "PNG"
    assert make_acronym(["Del", "Sol", "High", "School"]) == "DSHS"
    assert make_acronym(["be"]) == "B"
