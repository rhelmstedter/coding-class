---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): conditionals, comparison, elif
Path:
Related Bites: newbie 16, newbie 17
---

# Bite Description

Sometimes there are more than two choices. In this Bite, you'll use `elif` and the less than / greater than operators to pick between three.

### `if`, `elif`, and `else` Statements

```
if conditional:
    # do something if the conditional is True
elif another_conditional:
    # do something if the other conditional is True
else:
    # do something if all the conditionals were False
```

`elif` is short for *else if*. You can have as many `elif` branches as you need. Python checks each conditional from the top down, and runs the **first** branch that is `True`. Once a branch runs, the rest are skipped.

Since the order matters, think carefully about which check goes first.

### Example

> 🔍 **Investigate.** Read the code below line by line. What would print for an age of `16`? `18`? `12`?

```python
def check_age(age):
    if age >= 18:
        print("You can vote.")
    elif age >= 16:
        print("You can drive.")
    else:
        print("You're still a kid!")

check_age(16)
check_age(18)
check_age(12)
```

An 18 year old can drive too, but `check_age(18)` only prints `You can vote.` The first `True` branch wins.

> 🔧 **Modify.** What happens if you swap the `if` and `elif` conditionals? Try `check_age(20)` and see.

Watch out for the edges. `age > 18` and `age >= 18` give different answers when `age` is exactly `18`.

### Your Task

Complete the `speed_check` function. It needs to take one parameter, `speed`. You'll need to add it yourself.

| Speed                       | Print                        |
|-----------------------------|------------------------------|
| less than 80                | `Please speed up.`           |
| 80 up to and including 100  | `Thanks for driving safely!` |
| more than 100               | `Please slow down.`          |

Test your function with the edge cases, like `79`, `80`, `100`, and `101`, before you run the tests.

Good luck, and happy coding! 🐍
