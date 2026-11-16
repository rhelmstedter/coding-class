import ast

from list_adding import ninjabelts


def test_list_adding():
    expected = ['white', 'yellow', 'orange', 'green',
                'brown', 'black', 'bronze']
    assert ninjabelts == expected


def test_uses_list_methods():
    tree = ast.parse(open("list_adding.py").read())
    calls = set()
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and getattr(node.func.value, "id", None) == "ninjabelts"
                and len(node.args) == 1 and isinstance(node.args[0], ast.Constant)):
            calls.add((node.func.attr, node.args[0].value))
    assert ("append", "bronze") in calls, "Use a list method to add 'bronze'."
    assert ("remove", "blue") in calls or ("pop", 4) in calls, "Use a list method to remove 'blue'."