from constants import PI, Circle


def test_constant():
    assert PI == 3.14159


def test_calculate_area():
    circle = Circle(1)
    assert circle.calc_area() == PI


def test_calculate_area_different_radius():
    circle = Circle(2)
    expected_area = 12.56636  # This is 3.14159 * 2 * 2
    assert circle.calc_area() == expected_area


def test_calculate_circumference():
    circle = Circle(1)
    assert circle.calc_circumference() == 2 * PI
