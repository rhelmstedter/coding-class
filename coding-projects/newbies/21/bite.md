---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): loops, while, input
Path:
Related Bites: newbie 7, newbie 18
---

# Bite Description

What if you need to keep asking the user something until they get it right? You can't know ahead of time how many tries it will take. In this Bite, you'll use a `while` loop.

### `while` Loops

A `while` loop repeats the indented body underneath it for as long as its conditional is `True`.

```
while conditional:
    indented body of loop
```

Every time the body finishes, Python jumps back up to the `while` line and checks the conditional again. As soon as it is `False`, the loop is over and the program moves on.

### Example

> 🔍 **Investigate.** Read the code below line by line. What makes this loop stop?

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Pay close attention to the last line: `count = count + 1`. This is called **incrementing** a variable. The right hand side of the `=` is evaluated first, so the current value of `count` has one added to it and then gets put back in the `count` box. Read it as "count becomes count plus 1."

### Infinite Loops

If the conditional never becomes `False`, the loop never stops.

```
while True:
    print("hello world")
```

Sometimes that's on purpose. Python gives you two keywords for working with loops like this:

- **`break`**: if you reach this keyword, exit the loop.
- **`continue`**: if you reach this keyword, go back to the top of the loop.

> 🔮 **Predict first.** Which numbers will print? Is `3` one of them? Then run it.

```python
count = 0

while True:
    count = count + 1
    if count == 3:
        break
    print(count)

print("Out of the loop!")
```

### Your Task

Complete the `get_username` function so that it:

1. Asks the user to enter a username with this prompt: `Please type in the name PyBites: `
2. If they type exactly `PyBites`, the loop stops. Nothing else is printed.
3. If they type anything else, print `Invalid username.` and ask again.

The user might get it wrong once, five times, or not at all. Your function has to handle all of those.

Good luck, and happy coding! 🐍
