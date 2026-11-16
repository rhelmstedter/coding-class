import runpy
from unittest.mock import patch

QUESTION = "What's the name of the 12th month of the calendar year?"


def test_asks_the_question_and_stores_the_answer():
    prompts = []

    def fake_input(prompt=""):
        prompts.append(prompt)
        return "December"

    with patch("builtins.input", fake_input):
        result = runpy.run_path("user_input.py")

    assert len(prompts) == 1, "Call input() exactly once."
    assert prompts[0].rstrip() == QUESTION, "Check the question for typos."
    assert result.get("month") == "December", "Store the answer in an object called month."
