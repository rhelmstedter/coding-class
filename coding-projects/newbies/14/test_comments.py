import io
import subprocess
import sys
import tokenize
from pathlib import Path

import pytest

GARBAGE = ["qwpeoriu", "zxmvnbq", "asdfghjkl", "lkjhgfd", "poiuytr mnbvcxz"]
EXPECTED = ["I ate 4 tacos for $12.", "['tacos', 'burritos', 'horchata']"]


def _source():
    return Path("comments.py").read_text()


def _comments():
    """Every comment in the student's file, without the leading #."""
    try:
        tokens = tokenize.generate_tokens(io.StringIO(_source()).readline)
        return [t.string.lstrip("#").strip() for t in tokens if t.type == tokenize.COMMENT]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return []


def _run():
    return subprocess.run([sys.executable, "comments.py"], capture_output=True, text=True)


def test_code_runs():
    result = _run()
    error = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else ""
    assert result.returncode == 0, f"Your code still has an error: {error}. Is there garbage that isn't commented out?"


def test_output():
    lines = [line.strip() for line in _run().stdout.strip().splitlines()]
    assert lines == EXPECTED


@pytest.mark.parametrize("garbage", GARBAGE)
def test_garbage_commented_not_deleted(garbage):
    assert garbage in _source(), f"Don't delete '{garbage}'. Comment it out instead."
    assert any(garbage in c for c in _comments()), f"'{garbage}' should be inside a comment."


def test_wrote_own_comment():
    own = [c for c in _comments() if not any(g in c for g in GARBAGE) and any(ch.isalpha() for ch in c)]
    assert own, "Write at least one comment of your own that explains a line of code."
