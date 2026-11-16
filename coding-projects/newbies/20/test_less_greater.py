import pytest

from less_greater import speed_check

speeds = [29, 50, 60, 79, 80, 90, 100, 120, 140]
expected = (['Please speed up.'] * 4 +
            ['Thanks for driving safely!'] * 3 +
            ['Please slow down.'] * 2)


@pytest.mark.parametrize(
    "speed, res", list(zip(speeds, expected))
)
def test_speed_check(capfd, speed, res):
    speed_check(speed)
    actual = capfd.readouterr()[0].strip()
    assert actual == res
