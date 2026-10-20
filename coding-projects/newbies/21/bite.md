---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): comments, indentation
Path:
Related Bites: newbie 17
---

# Bite Description

Code is read by computers, but it is also read by people, including you a week from now. In this Bite, you'll learn how to leave notes in your code that Python ignores.

### Comments

Anything after a `#` on a line is a **comment**. Python skips right over it.

A comment can take up a whole line:

```
# Calculate the area of the rectangle
area = width * height
```

Or it can come at the end of a line of code. This is called an **inline comment**:

```
area = width * height  # square units
```

Everything to the **left** of the `#` still runs. Everything to the **right** is ignored.

### Commenting Out Code

Comments aren't just for notes. Putting a `#` in front of a line of code is called **commenting it out**. The line stays in your file, but Python won't run it. It's a great way to see what your program does without that line, and you don't have to delete it.

```python
print("This line runs.")
# print("This line doesn't.")
```

Most editors have a shortcut that comments or uncomments every line you have highlighted:

| Editor  | Shortcut   |
|---------|------------|
| Replit  | `Ctrl + /` |
| Colab   | `Ctrl + /` |
| VS Code | `Ctrl + /` |
| PyCharm | `Ctrl + /` |
| Mu      | `Ctrl + K` |

### Triple Quotes (Sort Of)

You'll sometimes see text wrapped in triple quotes used like a comment:

```
"""This
is a
multi-line
comment (sort of)"""
```

Technically that's a string that never gets used, not a comment. It's mostly used to describe what a function does. For commenting out code, stick with `#`.

### Indentation Matters

Remember that Python uses indentation to figure out which lines belong to a function, an `if`, or a loop. A line of junk that isn't indented properly will break the whole block, and you'll get an `IndentationError` or a `SyntaxError`. Once that junk is turned into a comment, Python ignores it, and the code around it can run again.

### Your Task

The `time_printer` function in the template has been filled with garbage. Some of it is on its own line, and some of it is on the same line as real code.

Use comments to get the function running again. **Don't delete the garbage.** The tests check that it is still in your code, just commented out. And don't change the real code, either.

When you're done, `time_printer("12:11")` should print `The time is 12:11.`

Good luck, and happy coding! 🐍
