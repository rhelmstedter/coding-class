import ast
import inspect
import textwrap

import pytest

from tuples import convert_to_tuple


@pytest.mark.parametrize("items", [
    ["Mazda", "McLaren", "Opel", "Toyota", "Honda"],
    [1, 2, 3],
    ["Mon", "Tue", "Wed", "Thu", "Fri"],
    [],
])
def test_returns_matching_tuple(items):
    result = convert_to_tuple(items)
    assert type(result) == tuple
    assert result == tuple(items)


def test_uses_tuple_function():
    tree = ast.parse(textwrap.dedent(inspect.getsource(convert_to_tuple)))
    assert any(
        isinstance(node, ast.Call) and getattr(node.func, "id", None) == "tuple"
        for node in ast.walk(tree)
    ), "Use the tuple() function to convert the list."
