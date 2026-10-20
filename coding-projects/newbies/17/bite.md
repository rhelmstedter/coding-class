---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): conditionals, if/else
Path:
Related Bites: newbie 16
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

```
def check_weather(weather):
    if weather == "rainy":
        print("Bring an umbrella.")
    else:
        print("Leave the umbrella at home.")

check_weather("rainy")
# Output: Bring an umbrella.

check_weather("sunny")
# Output: Leave the umbrella at home.
```

> 🔧 **Modify.** What would `check_weather("Rainy")` print? Why?

### Your Task

Complete the `check_payday` function. It takes one parameter, `date`.

- If `date` is equal to the string `"payday"`, print `Time to pay the rent.`
- Otherwise, print `Keep calm and eat two minute noodles.`

The template already has the function line for you. Your code goes inside it, so don't forget your indents!

Good luck, and happy coding! 🐍
