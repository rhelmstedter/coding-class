import ast
import inspect
import textwrap

import pytest

from for_dicts import print_cars


def _tree():
    return ast.parse(textwrap.dedent(inspect.getsource(print_cars)))


def test_uses_a_for_loop_with_items():
    tree = _tree()
    loops = [node for node in ast.walk(tree) if isinstance(node, ast.For)]
    assert loops, "Use a for loop."
    assert any(
        isinstance(loop.iter, ast.Call)
        and isinstance(loop.iter.func, ast.Attribute)
        and loop.iter.func.attr == "items"
        for loop in loops
    ), "Loop over the dictionary's .items()."


@pytest.mark.parametrize("cars", [
    {"Nissan": 2004, "Jeep": 2013, "Mazda": 2016, "Toyota": 2015},
    {"Honda": 2020},
    {"Ford": 1999, "Tesla": 2023},
])
def test_prints_each_car_and_year(capfd, cars):
    print_cars(cars)
    actual = [" ".join(line.split()) for line in capfd.readouterr()[0].strip().splitlines()]
    assert actual == [f"{brand}: {year}" for brand, year in cars.items()]
