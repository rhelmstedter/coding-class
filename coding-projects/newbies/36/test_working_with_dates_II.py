import inspect

import working_with_dates_II
from working_with_dates_II import get_pybites_first_day


def test_get_pybites_first_day():
    assert get_pybites_first_day() == "Monday"


def test_using_modules():
    func_src = inspect.getsource(get_pybites_first_day)
    assert "date" in func_src


def test_import_method():
    mod_src = inspect.getsource(working_with_dates_II)
    assert "from datetime import date" in mod_src
    assert "import datetime" not in mod_src
