import inspect

from calling_functions import (print_tuples,
                               car_brands)


def test_return_value(capfd):
    try:
        print_tuples()
    except TypeError:
        # support passing in the list
        print_tuples(car_brands)
    actual = capfd.readouterr()[0].strip()
    expected = "('Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda')"
    assert actual == expected


def test_call_of_function():
    src = inspect.getsource(print_tuples)
    assert 'convert_to_tuple(' in src
