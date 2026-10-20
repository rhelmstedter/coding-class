import inspect

import list_items


def test_list_items():
    src = inspect.getsourcelines(list_items)
    src = [line.strip() for line in src[0]]

    assert 'ninjabelts[-1]' in src
    assert 'ninjabelts[4]' in src
    assert 'ninjabelts[0]' in src
