from string_manipulations import extract_words


def test_example_docstring():
    text = "Today it's a sunny day in LA!"
    assert extract_words(text) == "today-la"


def test_another_text_with_question_mark():
    text = "Python is what we'll code today?"
    assert extract_words(text) == "python-today"


def test_ending_dot_and_uppercase():
    text = "NEWBIE bites are pretty fun."
    assert extract_words(text) == "newbie-fun"
