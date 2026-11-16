---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): functions, return
Path:
Related Bites: newbie 3
---

# Bite Description

Every time you write `print()` or `input()`, you are **calling** a function that somebody else wrote. In this Bite, you'll write a function of your own.

### Defining a Function

```
def function_name():
    indented body of function
```

`def` is short for *define*. The line ends with a colon `:`, and everything that belongs to the function is indented 4 spaces underneath it.

> 🔮 **Predict first.** What do you think this code will display? Then run it.

```python
def say_hello():
    print("Hello!")
```

Nothing! And that is correct. Defining a function with `def` does not run it. Remember Monty from Newbie Bite 1? `def` tells him to **build a room**. He puts up a new room next to the White Room (the main room of your program), hangs a door between the two, and writes `say_hello` on the door so he can find it again. The instructions go up on the wall inside. Then he comes back out and carries on.

To make Monty go in and follow the instructions, you **call** the function: write its name, with parentheses.

```python
say_hello()
say_hello()
```

Defining is building the room. Calling is walking in and doing whatever the instructions say. You use `def` once and call it as many times as you like.

### Returning Objects

Printing puts something on the screen, but the rest of your program can't use it. To hand a value **back** to whoever called the function, use `return`. Think of it as Monty carrying something out of the room with him.

```python
def get_favorite_food():
    return "tacos"

food = get_favorite_food()
print(f"My favorite food is {food}.")
```

The moment Monty reaches a `return`, he walks out. Anything after it never runs.

A function *does* something, so a good function name usually starts with a **verb**, like `get_favorite_food()` or `say_hello()`.

### Your Task

Write a function called `functions_rule` that **returns** this string:

```
This is my first function! Woohoo!
```

Make sure you `return` it. If you `print` it instead, the tests won't get anything back.

Good luck, and happy coding! 🐍
