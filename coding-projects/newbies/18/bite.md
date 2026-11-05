---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): conditionals, if/else
Path:
Related Bites: newbie 17
---

# Bite Description

In the last Bite, you saw that a comparison gives you back `True` or `False`. In this Bite, you'll use that answer to make your program choose what to do.

### `if` and `else` Statements

```
if conditional:
    # do something if the conditional is True
else:
    # do something if the conditional is False
```

A few things to notice:

- Both the `if` line and the `else` line end with a colon `:`.
- The code that belongs to each branch is indented 4 spaces underneath it.
- `else` doesn't get a conditional. It catches everything the `if` didn't.

Only **one** branch ever runs. If the conditional is `True`, Python runs the `if` branch and skips the `else`. If it is `False`, it skips the `if` and runs the `else`.

### Example

```python
def check_weather(weather):
    if weather == "rainy":
        print("Bring an umbrella.")
    else:
        print("Leave the umbrella at home.")

check_weather("rainy")
check_weather("sunny")
```

> 🔧 **Modify.** Change the first call to `check_weather("Rainy")` and run it again. What prints? Why?

### Your Task

Complete the `check_battery` function. It takes one parameter, `percent`, the amount of charge left on a phone.

- If `percent` is less than `20`, print `Plug in your phone.`
- Otherwise, print `You're good to go.`

The template already has the function line for you. Your code goes inside it, so don't forget your indents!

Before you run the tests, call your function with a few values of your own. What should happen at exactly `20`?

Good luck, and happy coding! 🐍
