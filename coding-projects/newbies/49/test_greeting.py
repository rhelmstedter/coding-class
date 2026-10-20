from greeting import create_greeting


def test_create_greeting_alice():
    assert create_greeting('Alice', 30) == "Hello, Alice! You are 30 years old."


def test_create_greeting_bob():
    assert create_greeting('Bob', 22) == "Hello, Bob! You are 22 years old."
