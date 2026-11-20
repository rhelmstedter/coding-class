"""Tests for the Your Turn section of Python - Docstrings, Type Hints, and Constants."""
import typing

import docstrings_practice


def _get(name):
    func = getattr(docstrings_practice, name, None)
    assert callable(func), f"Define a function called {name}() in the Your Code cell."
    return func


def _is_type(hint, expected):
    return hint is expected or typing.get_origin(hint) is expected


def test_find_longest_word_still_works():
    find_longest_word = _get("find_longest_word")
    assert find_longest_word(["be", "mindful", "proactive"]) == "proactive"
    assert find_longest_word(["Ada", "Grace", "Alan"]) == "Grace"


def test_find_longest_word_has_docstring():
    docstring = (_get("find_longest_word").__doc__ or "").strip()
    assert docstring, "Add a docstring as the first line inside find_longest_word()."
    assert docstring.endswith("."), "End the docstring with a period."


def test_find_longest_word_has_type_hints():
    hints = _get("find_longest_word").__annotations__
    assert "words" in hints, "Add a type hint to the words parameter."
    assert _is_type(hints["words"], list), "words is a list."
    assert "return" in hints, "Add a return type hint with ->."
    assert hints["return"] is str, "find_longest_word() gives back a string."


def test_is_even():
    is_even = _get("is_even")
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(7) is False
    assert is_even(-3) is False


def test_passing_score_constant():
    assert getattr(docstrings_practice, "PASSING_SCORE", None) == 50, (
        "Make a constant called PASSING_SCORE with the value 50."
    )


def test_is_passing():
    is_passing = _get("is_passing")
    assert is_passing(50) is True
    assert is_passing(93) is True
    assert is_passing(49) is False


def test_is_passing_uses_the_constant(monkeypatch):
    is_passing = _get("is_passing")
    monkeypatch.setattr(docstrings_practice, "PASSING_SCORE", 80)
    assert is_passing(70) is False, "is_passing() should use PASSING_SCORE, not the number 50."
    assert is_passing(80) is True, "is_passing() should use PASSING_SCORE, not the number 50."


def test_is_passing_has_type_hints():
    hints = _get("is_passing").__annotations__
    assert hints.get("score") is int, "Add the type hint score: int."
    assert hints.get("return") is bool, "Add the return type hint -> bool."
