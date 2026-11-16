import ast

import pytest

import dict_items  # runs the student's code, so an error fails here


def _methods_called():
    tree = ast.parse(open("dict_items.py").read())
    return {node.func.attr for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and getattr(node.func.value, "id", None) == "ninjabelt_scores"}


@pytest.mark.parametrize("method", ["keys", "values", "items"])
def test_calls_method(method):
    assert method in _methods_called(), f"Call ninjabelt_scores.{method}()"