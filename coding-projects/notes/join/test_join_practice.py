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


def test_pick_three():
    pick_three = _get("pick_three")
    results = set()
    for _ in range(30):
        result = pick_three(list("0123456789"))
        assert isinstance(result, str), "Return a string, not a list."
        assert len(result) == 3, "Return exactly three characters."
        assert len(set(result)) == 3, "No character should repeat."
        assert all(char in "0123456789" for char in result)
        results.add(result)
    assert len(results) > 1, "Shuffle the list so the result changes from run to run."
