import ast
import inspect
import textwrap

import pytest

from calling_functions import print_report_card


def test_calls_get_letter_grade():
    tree = ast.parse(textwrap.dedent(inspect.getsource(print_report_card)))
    assert any(
        isinstance(node, ast.Call) and getattr(node.func, "id", None) == "get_letter_grade"
        for node in ast.walk(tree)
    ), "print_report_card should call get_letter_grade."


@pytest.mark.parametrize("scores, expected", [
    ({"Ada": 95, "Grace": 74}, ["Ada: A", "Grace: C"]),
    ({"Alan": 80, "Katherine": 89, "Linus": 59, "Margaret": 60},
     ["Alan: B", "Katherine: B", "Linus: F", "Margaret: D"]),
    ({"Guido": 100}, ["Guido: A"]),
])
def test_prints_report_card(capfd, scores, expected):
    print_report_card(scores)
    actual = [" ".join(line.split()) for line in capfd.readouterr()[0].strip().splitlines()]
    assert actual == expected
