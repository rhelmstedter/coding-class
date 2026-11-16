import pytest

from make_a_class import Rectangle


def test_class():
    rectangle = Rectangle(1, 1)
    assert isinstance(rectangle, Rectangle)


@pytest.mark.parametrize(
    "base, height, area, perimeter",
    [(3, 5, 15, 16), (1, 1, 1, 4), (115, 350, 40_250, 930)],
)
def test_dimensions(base, height, area, perimeter):
    rectangle = Rectangle(base, height)
    assert rectangle.base == base
    assert rectangle.height == height
    assert rectangle.calc_area() == area
    assert rectangle.calc_perimeter() == perimeter
