import inspect

from for_dicts import print_cars, my_cars

EXPECTED = """Nissan: 2004
Jeep: 2013
Mazda: 2016
Toyota: 2015"""


def test_print_cars_src():
    src = inspect.getsource(print_cars)
    assert 'my_cars.items()' in src


def test_function_output(capfd):
    print_cars(my_cars)
    actual = capfd.readouterr()[0].strip()
    assert actual == EXPECTED
