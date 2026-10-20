import pytest

from default_arguments import calc_rectangle_area, calc_rectangle_perimeter


def test_area_defaults():
    assert calc_rectangle_area() == 1


@pytest.mark.parametrize("base, height, expected", [(1, 8, 8), (9, 8, 72), (3, 3, 9)])
def test_calc_rectangle_area(base, height, expected):
    actual = calc_rectangle_area(base, height)
    assert actual == expected


def test_perimeter_defaults():
    assert calc_rectangle_perimeter() == 4


@pytest.mark.parametrize("base, height, expected", [(1, 8, 18), (9, 8, 34), (3, 3, 12)])
def test_calc_square_perimeter(base, height, expected):
    actual = calc_rectangle_perimeter(base, height)
    assert actual == expected
