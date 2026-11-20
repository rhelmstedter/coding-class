"""Tests for the Your Turn section of Python - The main() Function."""
import ast
import importlib
import sys
from unittest.mock import patch


def _fresh_import(module_name):
    """Import the student's file from scratch, failing if it asks for input."""
    sys.modules.pop(module_name, None)
    with patch("builtins.input", side_effect=AssertionError(
        f"Importing {module_name}.py asked for input. "
        "Start the program with the if __name__ == \"__main__\": idiom."
    )):
        return importlib.import_module(module_name)


def _tree(module_name):
    with open(f"{module_name}.py") as file:
        return ast.parse(file.read())


def _functions(tree):
    return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]


def _ends_with_idiom(tree):
    last = tree.body[-1] if tree.body else None
    if not isinstance(last, ast.If):
        return False
    test = last.test
    if not (isinstance(test, ast.Compare) and isinstance(test.left, ast.Name)
            and test.left.id == "__name__"):
        return False
    calls = [node for node in ast.walk(last) if isinstance(node, ast.Call)]
    return any(isinstance(call.func, ast.Name) and call.func.id == "main" for call in calls)


# 1. area.py


def test_area_import_does_not_run_program(capfd):
    _fresh_import("area")
    assert capfd.readouterr()[0] == "", "Importing area.py should not print anything."


def test_area_has_main():
    area = _fresh_import("area")
    assert callable(getattr(area, "main", None)), "Define a function called main()."


def test_area_ends_with_idiom():
    assert _ends_with_idiom(_tree("area")), (
        'End the file with the if __name__ == "__main__": idiom that calls main().'
    )


def test_area_still_works(capfd):
    area = _fresh_import("area")
    with patch("builtins.input", side_effect=["3", "4"]):
        area.main()
    assert "12" in capfd.readouterr()[0], "main() should still print the area."


def test_area_calculate_area_unchanged():
    area = _fresh_import("area")
    assert area.calculate_area(3, 4) == 12
    assert area.calculate_area(5, 10) == 50


# 2. my_program.py


def test_my_program_import_does_not_run_program(capfd):
    my_program = _fresh_import("my_program")
    assert callable(getattr(my_program, "main", None)), "Define a function called main()."
    assert capfd.readouterr()[0] == "", "Importing my_program.py should not print anything."


def test_my_program_main_is_first():
    functions = _functions(_tree("my_program"))
    assert "main" in functions, "Define a function called main()."
    assert functions[0] == "main", "Define main() first, above the functions it calls."


def test_my_program_has_two_more_functions():
    functions = _functions(_tree("my_program"))
    others = [name for name in functions if name != "main"]
    assert len(others) >= 2, "Write at least two functions besides main()."


def test_my_program_main_calls_them():
    tree = _tree("my_program")
    others = set(_functions(tree)) - {"main"}
    main = next(node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name == "main")
    called = {node.func.id for node in ast.walk(main)
              if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)}
    assert len(called & others) >= 2, "main() should call at least two of your other functions."


def test_my_program_ends_with_idiom():
    assert _ends_with_idiom(_tree("my_program")), (
        'End the file with the if __name__ == "__main__": idiom that calls main().'
    )
