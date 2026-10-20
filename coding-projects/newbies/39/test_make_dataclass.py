import pytest

from make_dataclass import Rectangle


def test_class():
    rectangle = Rectangle(1, 1)
    assert isinstance(rectangle, Rectangle)


def test_dataclass():
    assert (
        getattr(Rectangle, "__dataclass_fields__") is not None
    ), "Your task is to change your rectangle class into a dataclass. Did you use the @dataclass decorator?"


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
