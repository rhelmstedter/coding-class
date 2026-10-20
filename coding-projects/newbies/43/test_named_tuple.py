from typing import NamedTuple

from named_tuple import make_namedtuple


def test_type_tuple():
    bite = make_namedtuple(1, "first bite", 6)
    assert isinstance(bite, tuple)


def test_attributes():
    bite = make_namedtuple(1, "first bite", 6)
    fields = getattr(type(bite), "_fields")
    assert fields == ("number", "title", "is_complex")


def test_actual_return():
    bite = make_namedtuple(1, "first bite", 6)
    assert bite.number == 1
    assert bite.title == "first bite"
    assert bite.is_complex == True


def test_another_easy_bite():
    bite = make_namedtuple(2, "2nd bite", 5)
    assert bite.number == 2
    assert bite.title == "2nd bite"
    assert bite.is_complex == False
