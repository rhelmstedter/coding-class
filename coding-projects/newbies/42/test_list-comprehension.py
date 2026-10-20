import ast
import inspect

import pytest

from list_comprehension import filter_out_negative_numbers


@pytest.mark.parametrize("numbers, expected", [
    ([-1, 2, 3], [2, 3]),
    ([-1, -2], []),
    ([1, -1, 2, -2, 3], [1, 2, 3]),
    ([0, -1, 0, 2], [2]),
])
def test_filter_out_negative_numbers(numbers, expected):
    assert filter_out_negative_numbers(numbers) == expected


def test_uses_list_comprehension():
    src = inspect.getsource(filter_out_negative_numbers)
    # find listcomp: https://stackoverflow.com/a/35150363
    program = ast.parse(src)
    list_comps = [
        node for node in ast.walk(program)
        if type(node) is ast.ListComp
    ]
    assert len(list_comps) == 1
