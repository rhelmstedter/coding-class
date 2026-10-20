import pytest

from dict_retrieval_III import look_up_score_advanced


@pytest.mark.parametrize(
    "belt, score",
    [
        ("yellow", 20),
        ("blue", 50),
        ("brown", 60),
    ],
)
def test_look_up_default_dict(belt, score):
    expected = f"Your {belt} belt has a score of {score}."
    actual = look_up_score_advanced(belt)
    assert actual == expected


def test_look_up_bad_belt_color():
    expected = "A turquoise belt does not exist."
    actual = look_up_score_advanced("turquoise")
    assert actual == expected
