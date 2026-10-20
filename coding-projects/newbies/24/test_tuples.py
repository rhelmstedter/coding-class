import inspect

from tuples import convert_to_tuple, car_brands


def test_return_type():
    ret = convert_to_tuple(car_brands)
    assert type(ret) == tuple


def test_source():
    src = inspect.getsource(convert_to_tuple)
    assert 'tuple(' in src
