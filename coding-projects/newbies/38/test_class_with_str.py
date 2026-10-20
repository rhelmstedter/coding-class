import pytest

from class_with_str import Rectangle


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


@pytest.mark.parametrize(
    "base, height",
    [(3, 5), (1, 1), (115, 350)],
)
def test_str(base, height):
    rectangle = Rectangle(base, height)
    assert (
        str(rectangle) == f"A rectangle with a base of {base} and a height of {height}."
    )
