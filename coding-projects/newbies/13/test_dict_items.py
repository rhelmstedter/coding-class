import inspect

import dict_items


def test_dict_items():
    src = inspect.getsourcelines(dict_items)
    src = [line.strip() for line in src[0]]

    assert 'ninjabelt_scores.items()' in src
    assert 'ninjabelt_scores.keys()' in src
    assert 'ninjabelt_scores.values()' in src
