"""Build a Colab notebook for one newbie bite from its bite.md, template, and test.

Usage: python make_nb.py <newbies dir> <bite number, e.g. 07> <output .ipynb>

```python fences in bite.md become runnable code cells; other fences stay markdown.
The Run Tests cell downloads the test from BRANCH on GitHub.
"""
import json, re, sys
from pathlib import Path

BRANCH = "newbie-bites"

root = Path(sys.argv[1])
bite = sys.argv[2]
out = Path(sys.argv[3])
d = root / bite
md = (d / "bite.md").read_text(encoding="utf-8")
md = re.sub(r"\A\s*---.*?---\s*", "", md, flags=re.S)
md = md.replace("# Bite Description", f"# Newbie Bite {int(bite)}", 1)
templates = list(d.glob("*template*.py"))
template = templates[0].read_text(encoding="utf-8") if templates else "# Enter your code below this line:\n"
test = next(d.glob("test_*.py")).name
module = test[len("test_"):]
test_src = (d / test).read_text(encoding="utf-8")
# A bite asks for functions when its test calls something it imports from the student's module.
imported = re.findall(rf"from {module[:-3]} import (\([^)]*\)|[^\n]+)", test_src)
names = {n.strip(" \n()") for group in imported for n in group.split(",") if n.strip(" \n()")}
defines_functions = any(re.search(rf"\b{n}\(", test_src) for n in names)
if defines_functions:
    run_note = ("The cell above only *saves* your code. Run the cell below to load it. "
                "Your code defines functions, so nothing will print until you call one. "
                "To try it out, add a code cell under the **Run your code** cell and call your function with your own values.")
else:
    run_note = "The cell above only *saves* your code. Run the cell below to actually run it and see the output."
url = f"https://raw.githubusercontent.com/rhelmstedter/coding-class/{BRANCH}/coding-projects/newbies/{bite}/{test}"
conftest_url = f"https://raw.githubusercontent.com/rhelmstedter/coding-class/{BRANCH}/coding-projects/newbies/conftest.py"
# Signing in lets conftest.py report the student's school email with their results.
# If sign-in fails or hangs (Stop pressed), the student types their email instead.
RUN_TESTS = """import os
try:
    from google.colab import auth
    auth.authenticate_user()
except BaseException:
    while "@" not in os.environ.get("STUDENT_EMAIL", ""):
        os.environ["STUDENT_EMAIL"] = input("Sign-in didn't work. Type your school email: ").strip()
!curl -sO {conftest}
!curl -sO {url}
!BITE={bite} python -m pytest {test}"""


def cell(kind, src, title=None):
    if title:
        src = f"# @title {title}\n{src}"
    c = {"cell_type": kind, "metadata": {}, "source": src.strip("\n").splitlines(keepends=True)}
    if kind == "code":
        c.update(execution_count=None, outputs=[])
        if title:
            c["metadata"]["cellView"] = "form"
    return c


# ```python fences become runnable code cells; everything else stays markdown.
cells = []
for i, part in enumerate(re.split(r"^```python\n(.*?)^```\n?", md, flags=re.S | re.M)):
    if part.strip():
        cells.append(cell("code" if i % 2 else "markdown", part))

# "### Your Task" gets its own "## Your Task" cell, apart from the instructional material.
for k, c in enumerate(cells):
    src = "".join(c["source"])
    m = re.search(r"^### Your Task\n", src, flags=re.M)
    if c["cell_type"] == "markdown" and m:
        before, task = src[:m.start()], "## Your Task\n" + src[m.end():]
        cells[k:k + 1] = ([cell("markdown", before)] if before.strip() else []) + [cell("markdown", task)]
        break

# Students start from a bare code cell: drop comment-only lines from the template.
template = "\n".join(l for l in template.splitlines() if not l.lstrip().startswith("#")).strip("\n")
template = template + "\n" if template else ""

cells += [
    cell("markdown", "### Your Code\n\nWrite your solution in the cell below. Run the cell to save your code.\n\n**Keep the `%%writefile` line at the top!** It saves your code to a file so the tests can find it."),
    cell("code", f"%%writefile {module}\n{template}"),
    cell("markdown", run_note),
    cell("code", f"%run {module}", title="Run your code"),
    cell("markdown", "Run the cell below to check your code against the tests. If a test fails, read the output carefully. It tells you what was expected and what your code actually did."),
    cell("code", RUN_TESTS.format(conftest=conftest_url, url=url, bite=bite, test=test), title="Run Tests"),
]
nb = {
    "cells": cells,
    "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"display_name": "Python 3", "name": "python3"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 0,
}
out.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
print(out, f"{len(cells)} cells")
