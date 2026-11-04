import pytest

from dictionaries import ninjabelt_scores

BELT_SCORES = [
    ("white", 10), ("yellow", 20), ("orange", 30), ("green", 40),
    ("blue", 50), ("brown", 60), ("black", 70),
]


@pytest.mark.parametrize("belt, score", BELT_SCORES)
def test_dictionaries(belt, score):
    assert ninjabelt_scores.get(belt) == score