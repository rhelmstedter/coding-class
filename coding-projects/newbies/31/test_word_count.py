import pytest

from word_count import prince_of_py, line_count, word_count

ZEN_OF_PYTHON = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


@pytest.mark.parametrize("text, words", [(prince_of_py, 37), (ZEN_OF_PYTHON, 144)])
def test_word_count(text, words):
    expected = words
    actual = word_count(text)
    assert actual == expected


@pytest.mark.parametrize("text, lines", [(prince_of_py, 4), (ZEN_OF_PYTHON, 21)])
def test_line_count(text, lines):
    expected = lines
    actual = line_count(text)
    assert actual == expected
