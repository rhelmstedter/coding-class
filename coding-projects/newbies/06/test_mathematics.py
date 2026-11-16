import inspect

import mathematics


def test_mathematics_operations():
    # allowing for spaces or not (e.g. a - b or a-b)
    src_lines = [line.strip().replace(' ', '')
                 for line in
                 inspect.getsourcelines(mathematics)[0]]
    assert "subtraction=a-b" in src_lines
    assert "multiplication=a*b" in src_lines
    assert "division=a/b" in src_lines


def test_mathematics_variables_values():
    assert mathematics.subtraction == 5
    assert mathematics.multiplication == 50
    assert mathematics.division == 2
