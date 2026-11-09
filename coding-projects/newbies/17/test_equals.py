import pytest

from equals import can_vote, is_too_cold, is_same_name


@pytest.mark.parametrize("age, expected", [
    (0, False), (16, False), (17, False),
    (18, True), (19, True), (65, True),
])
def test_can_vote(age, expected):
    assert can_vote(age) is expected


@pytest.mark.parametrize("temperature, expected", [
    (-5, True), (20, True), (49, True), (49.5, True),
    (50, False), (51, False), (85, False),
])
def test_is_too_cold(temperature, expected):
    assert is_too_cold(temperature) is expected


@pytest.mark.parametrize("name1, name2, expected", [
    ("Ada", "Ada", True), ("Ada", "ada", True), ("ADA", "ada", True), ("bOb", "BoB", True),
    ("Ada", "Bob", False), ("Ada", "Adam", False), ("Ana", "Ada", False),
])
def test_is_same_name(name1, name2, expected):
    assert is_same_name(name1, name2) is expected
