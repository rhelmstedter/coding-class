import pytest

from reading_errors import get_belts_above


def test_belt_cutoff():
    expected = {"brown": 60, "black": 70}
    actual = get_belts_above(50)
    assert actual == expected
