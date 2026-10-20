import inspect

import printing


def test_printing():
    src_lines = [line.strip() for line in
                 inspect.getsourcelines(printing)[0]]
    # allow for both single and double quotes
    assert (
        """print(f'{name} was founded in {month} {year}.')"""
        in src_lines
        or
        """print(f"{name} was founded in {month} {year}.")"""
        in src_lines
    )
