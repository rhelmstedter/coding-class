import ast

import addition


def test_values():
    assert addition.a == 7
    assert addition.b == 3
    assert addition.answer == 10


def test_answer_uses_the_object_names():
    tree = ast.parse(open("addition.py").read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "answer" for t in node.targets):
            value = node.value
            assert isinstance(value, ast.BinOp) and isinstance(value.op, ast.Add), "answer should be a plus b."
            assert {getattr(value.left, "id", None), getattr(value.right, "id", None)} == {"a", "b"}, \
                "Use the object names a and b, not the numbers."
            return
    assert False, "Create an object named answer."
