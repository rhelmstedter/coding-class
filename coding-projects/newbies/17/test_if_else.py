from if_else import check_payday


def test_check_payday_if_branch(capfd):
    # capfd is a pytest fixture that captures stdout/stderr
    # more info https://docs.pytest.org/en/latest/capture.html
    check_payday("payday")
    actual = capfd.readouterr()[0].strip()
    expected = "Time to pay the rent."
    assert actual == expected


def test_check_payday_else_branch(capfd):
    check_payday("another_day")
    actual = capfd.readouterr()[0].strip()
    expected = "Keep calm and eat two minute noodles."
    assert actual == expected
