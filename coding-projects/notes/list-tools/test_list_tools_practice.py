"""Tests for the Your Turn section of Python - More List Tools."""
import list_tools_practice


def _get(name):
    func = getattr(list_tools_practice, name, None)
    assert callable(func), f"Define a function called {name}() in the Your Code cell."
    return func


def test_scramble_letters():
    scramble_letters = _get("scramble_letters")
    results = set()
    for _ in range(30):
        result = scramble_letters("KATHERINE")
        assert isinstance(result, list), "Return a list of letters."
        assert sorted(result) == sorted("KATHERINE"), "Use every letter exactly once."
        results.add("".join(result))
    assert len(results) > 1, "Shuffle the letters so the order changes from run to run."


def test_scramble_word():
    scramble_word = _get("scramble_word")
    results = set()
    for _ in range(30):
        result = scramble_word("KATHERINE")
        assert isinstance(result, str), "Return a string, not a list."
        assert sorted(result) == sorted("KATHERINE"), "Use every letter exactly once."
        results.add(result)
    assert len(results) > 1, "Shuffle the letters so the order changes from run to run."


def test_lowest_score():
    lowest_score = _get("lowest_score")
    assert lowest_score([88, 72, 95, 64, 81]) == 64
    assert lowest_score([100]) == 100


def test_highest_score():
    highest_score = _get("highest_score")
    assert highest_score([88, 72, 95, 64, 81]) == 95
    assert highest_score([100]) == 100


def test_print_roster(capfd):
    print_roster = _get("print_roster")
    print_roster(["Ada", "Grace", "Alan"], [88, 72, 95])
    lines = [line for line in capfd.readouterr()[0].splitlines() if line.strip()]
    assert len(lines) == 3, "Print one line for each student."
    for line, name, score in zip(lines, ["Ada", "Grace", "Alan"], [88, 72, 95]):
        assert name in line and str(score) in line, (
            f"Each line should have a name and that student's score. Expected {name} and {score}."
        )


def test_count_matches():
    count_matches = _get("count_matches")
    assert count_matches("CAT", "COT") == 2
    assert count_matches("248", "843") == 1
    assert count_matches("123", "123") == 3
    assert count_matches("123", "456") == 0
