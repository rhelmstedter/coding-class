import ast

import list_items  # runs the student's code, so an IndexError fails here


def _indexes_used():
    tree = ast.parse(open("list_items.py").read())
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript) and getattr(node.value, "id", None) == "ninjabelts":
            try:
                found.add(ast.literal_eval(node.slice))
            except ValueError:
                pass
    return found


def test_last_belt_counting_from_the_end():
    assert -1 in _indexes_used(), "Get the last belt by counting from the end."


def test_fifth_belt():
    assert 4 in _indexes_used(), "Get the fifth belt. What index is the fifth item?"


def test_first_belt():
    assert 0 in _indexes_used(), "Get the first belt."