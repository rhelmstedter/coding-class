import ast
import runpy


def test_prints_the_sentence(capsys):
    runpy.run_path("printing.py")
    assert capsys.readouterr().out.strip() == "PyBites was founded in December 2016."


def test_uses_one_f_string_with_the_objects():
    tree = ast.parse(open("printing.py").read())
    prints = [node for node in ast.walk(tree)
              if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "print"]
    assert len(prints) == 1, "Use exactly one print()."
    fstrings = [arg for arg in prints[0].args if isinstance(arg, ast.JoinedStr)]
    assert fstrings, "Put an f-string inside print()."
    names = [part.value.id for part in fstrings[0].values
             if isinstance(part, ast.FormattedValue) and isinstance(part.value, ast.Name)]
    assert names == ["name", "month", "year"], "Fill the sentence with {name}, {month}, and {year}."
