from inop import count_matching_items


def test_count_matching_items():
    # to keep it simple, we'll assume that the items are unique
    assert count_matching_items([1, 2, 3, 4, 5], [3, 4]) == 2
    assert count_matching_items(['apple', 'banana', 'cherry'], ['banana', 'cherry']) == 2
    assert count_matching_items(['apple', 'banana', 'cherry'], ['orange', 'cherry']) == 1
    assert count_matching_items(['apple', 'banana', 'cherry'], ['date', 'fig']) == 0

