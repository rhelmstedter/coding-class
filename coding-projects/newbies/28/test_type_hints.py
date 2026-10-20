from typing import get_type_hints

from type_hints import date_formatter


def test_type_hints():
    types = get_type_hints(date_formatter)

    assert len(types) == 4
    assert issubclass(types["day"], int)
    assert issubclass(types["month"], str)
    assert issubclass(types["year"], int)
    assert issubclass(types["return"], str)


def test_date_formatter():
    actual = date_formatter(1, "January", 2023)
    expected = "The date is January 1, 2023."
    assert actual == expected
