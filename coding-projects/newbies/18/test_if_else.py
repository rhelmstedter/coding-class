import pytest

from if_else import check_battery

LOW = "Plug in your phone."
OK = "You're good to go."


@pytest.mark.parametrize("percent, expected", [
    (0, LOW), (5, LOW), (19, LOW),
    (20, OK), (21, OK), (64, OK), (100, OK),
])
def test_check_battery(capfd, percent, expected):
    check_battery(percent)
    actual = capfd.readouterr()[0].strip()
    assert actual == expected
