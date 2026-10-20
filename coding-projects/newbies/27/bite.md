---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): debugging, testing, pytest
Path:
Related Bites:
---

# Bite Description

Your last Newbie Bite! 🎉

As you continue your coding journey on our platform, it's essential to become proficient in reading and interpreting failing test outputs. Understanding how to read test failures is a crucial skill in software development as well, because it helps you identify and fix issues in your code.

In this Bite, you'll practice reading and interpreting failing test outputs to debug and correct your code. This ability not only helps in resolving issues here but also in any real-world programming scenarios.

### Understanding Test Failures

When tests fail, they provide valuable information about what went wrong. The test output typically includes:
- The name of the test that failed.
- The reason for the failure, including any assertion errors.
- The expected vs. actual values.

By carefully reading this information, you can pinpoint the exact location and nature of the problem in your code.

### Example

Consider the following test failure output:

```
E       AssertionError: assert 4 == 16
```

This output indicates that a test expected the value `16`, but the actual value was `4`. This discrepancy needs to be investigated and corrected in the code.

### Your Task

The code in this Bite runs, but it is not doing what we expect it to do, hence the tests are failing. The code is supposed to create a dictionary where the keys are the numbers 0 through 20, and the values are those keys squared.

### Steps to Complete

1. **Run the Tests**: Execute the provided tests to see the failures.
2. **Read the Output**: Carefully read through the pytest output to understand why the tests are failing.
3. **Identify the Issue**: Determine what is wrong with the current implementation based on the test output.
4. **Fix the Code**: Correct the logic in the `perfect_squares_to_20` function so that the tests pass again.

Here is the initial function definition you need to work with:

```
def perfect_squares_to_20():
    perfect_squares = {}
    for number in range(20):
        perfect_squares[number] = number * 2
    return perfect_squares
```

### Example Usage

```
print(perfect_squares_to_20())
# Output should be:
# {
#     0: 0,
#     1: 1,
#     2: 4,
#     3: 9,
#     ...
#     20: 400
# }
```

### Tests

Here are the provided tests:

```
import pytest

from failing_tests import perfect_squares_to_20

def test_proper_length():
    assert len(perfect_squares_to_20()) == 21

@pytest.mark.parametrize("key, value", [(16, 256), (3, 9), (19, 361), (21, None)])
def test_perfect_squares(key, value):
    actual = perfect_squares_to_20()
    assert actual.get(key) == value
```

### Correcting the Code

After running the tests and reading the failure output, correct the logic in the `perfect_squares_to_20` function. Ensure that the function creates a dictionary with keys from 0 to 20 and values as the squares of the keys.

By completing this task, you'll gain a better understanding of how to read and interpret test failures, and how to use this information to debug and fix your code.

### Wrapping Up

Good luck, and congratulations on completing our Newbie Bites! We hope you've enjoyed them and learned a lot. 🎉 🔥

Now onto the regular Bites, keep calm and code in Python, good luck! 🐍 💪
