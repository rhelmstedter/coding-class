---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): comments
Path:
Related Bites: newbie 4
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

### Writing Good Comments

> 🔍 **Investigate.** Both comments below are about the same line. Which one tells you something the code doesn't already say?

```
tip = total * 0.2  # multiply total by 0.2
tip = total * 0.2  # 20% tip
```

The first comment just reads the code out loud. The second one explains *why* the number is there. A good comment answers a question a reader might have.

### Commenting Out Code

Comments aren't just for notes. Putting a `#` in front of a line of code is called **commenting it out**. The line stays in your file, but Python won't run it. It's a great way to see what your program does without that line, and you don't have to delete it.

```python
print("This line runs.")
# print("This line doesn't.")
```

> 🔧 **Modify.** Comment out the first line and uncomment the second. Run it again.

Most editors have a shortcut that comments or uncomments every line you have highlighted. In Colab, it's `Ctrl + /` (`Cmd + /` on a Mac).

### Triple Quotes (Sort Of)

You'll sometimes see text wrapped in triple quotes used like a comment:

```
"""This
is a
multi-line
comment (sort of)"""
```

Technically that's a string that never gets used, not a comment. You'll see these later, describing what a piece of code does. For commenting out code, stick with `#`.

### Your Task

The code in the template has been filled with garbage. Some of it is on its own line, and some of it is at the end of a line of real code. Right now, the code won't run at all.

1. Use comments to get the code running again. **Don't delete the garbage.** The tests check that it is still in your code, just commented out. And don't change the real code, either.
2. Write at least **one** comment of your own that explains a line of the real code.

When you're done, running your code should print:

```
I ate 4 tacos for $12.
['tacos', 'burritos', 'horchata']
```

Good luck, and happy coding! 🐍
