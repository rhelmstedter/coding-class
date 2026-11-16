import ast
import inspect
import textwrap

import pytest

from for_loops import list_cars


def test_uses_a_for_loop():
    tree = ast.parse(textwrap.dedent(inspect.getsource(list_cars)))
    assert any(isinstance(node, ast.For) for node in ast.walk(tree)), "Use a for loop."


@pytest.mark.parametrize("brands", [
    ["Mazda", "McLaren", "Opel", "Toyota", "Honda"],
    ["Tesla", "Ford"],
    ["Subaru"],
])
def test_prints_each_brand(capfd, brands):
    list_cars(brands)
    actual = [line.strip() for line in capfd.readouterr()[0].strip().splitlines()]
    assert actual == brands
