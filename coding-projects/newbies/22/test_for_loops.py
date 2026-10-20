import inspect
import re

from for_loops import list_cars, car_brands


def test_list_cars_src():
    src = inspect.getsource(list_cars)
    assert re.search('for .* in car_brands', src)


def test_function_output(capfd):
    list_cars(car_brands)
    actual = capfd.readouterr()[0].strip()
    expected = '\n'.join(car_brands)
    assert actual == expected
