import ast
import runpy

SENTENCE = "I find it unbearable that there are people out there who think DC is better than Marvel!"


def test_prints_the_sentence(capsys):
    runpy.run_path("thoughts.py")
    assert capsys.readouterr().out.strip() == SENTENCE


def test_uses_print():
    tree = ast.parse(open("thoughts.py").read())
    calls = [node.func.id for node in ast.walk(tree)
             if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)]
    assert "print" in calls
