import pytest

from dictionaries import ninjabelts, ninjabelt_scores

scores = range(10, 80, 10)


@pytest.mark.parametrize(
    "belt, score", zip(ninjabelts, scores)
)
def test_dictionaries(belt, score):
    assert ninjabelt_scores.get(belt) == score
