import inspect

import addition


def test_addition():
    src_lines = [line.strip() for line in
                 inspect.getsourcelines(addition)[0]]
    assert "a = 7" in src_lines
    assert "b = 3" in src_lines
    assert "answer = a + b" in src_lines
