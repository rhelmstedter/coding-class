import pytest

from failing_tests import perfect_squares_to_20


def test_proper_length():
    assert len(perfect_squares_to_20()) == 21


@pytest.mark.parametrize("key, value", [(16, 256), (3, 9), (19, 361), (21, None)])
def test_perfect_squares(key, value):
    actual = perfect_squares_to_20()
    assert actual.get(key) == value
