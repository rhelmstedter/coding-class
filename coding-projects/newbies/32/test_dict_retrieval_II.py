import pytest

from dict_retrieval_II import look_up_score


@pytest.mark.parametrize(
    "belt, score",
    [
        ("white", 10),
        ("yellow", 20),
        ("orange", 30),
        ("green", 40),
        ("blue", 50),
        ("brown", 60),
        ("black", 70),
    ],
)
def test_look_up_default_dict(belt, score):
    expected = f"Your {belt} belt has a score of {score}."
    actual = look_up_score(belt)
    assert actual == expected


def test_key_not_in_dict():
    with pytest.raises(KeyError):
        look_up_score("key_not_in_dictionary")
