import inspect

import pytest


def _can_import():
    try:
        import comments  # noqa F401
        return True
    except IndentationError:
        return False


def test_import_fails_because_not_all_garbage_commented():
    if not _can_import():
        raise pytest.fail(
            ("comments.py raised an IndentationError,"
             " did you comment it properly?")
        )


@pytest.mark.skipif(not _can_import(),
                    reason="Only running this test if import works")
def test_output_time_printer_with_time_arg_returns_string(capfd):
    """At this point code can be imported,
       let's see the output of the function"""
    from comments import time_printer
    time_printer('12:11')
    output = capfd.readouterr()[0].strip()
    assert output == 'The time is 12:11.'


@pytest.mark.skipif(not _can_import(),
                    reason="Only running this test if import works")
def test_output_time_printer_else_branch_no_output(capfd):
    from comments import time_printer
    time_printer(None)
    output = capfd.readouterr()[0].strip()
    assert output == ''


@pytest.mark.skipif(not _can_import(),
                    reason="Only running this test if import works")
@pytest.mark.parametrize("comment", [
    "xafjiwjaf", "QWEPOQOPKF", "IHHPHJFDQ", "JIQJWE"
])
def test_comments(comment):
    """Still want to make sure comments were not deleted"""
    from comments import time_printer
    source_code = inspect.getsource(time_printer)
    assert comment in source_code
