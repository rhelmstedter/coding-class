---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): input, strings
Path:
Related Bites: newbie 3, newbie 4
---

# Bite Description

Up to now, you have been the one deciding what goes in every box. In this Bite, you'll let the user decide.

### The `input()` Function

`input()` is a function that allows the user to input data for your program to process. Every function works in three steps:

1. You **call** the function.
2. It does all the things.
3. It **returns** something.

For `input()`, that looks like:

1. You call `input()`.
2. The things:
   - it prints the prompt (whatever you put inside the parentheses)
   - it collects whatever the user types
   - it stops collecting when the user presses Enter
3. It returns what the user typed as a **string**.

You usually want to save that string in a box so you can use it later.

### Example

```python
user_name = input("What is your name? ")
print(f"Hello, {user_name}!")
```

Notice the space after the question mark in the prompt. Without it, whatever the user types would be squished right up against the `?`.

Since `input()` always returns a string, if you want to use the answer as a number you need to convert it with `int()` or `float()`. We don't need that for this Bite, but keep it in your back pocket.

### Your Task

Ask the user this question:

```
What's the name of the 12th month of the calendar year?
```

Store their answer in an object called `month`.

Watch out for the apostrophe in *What's*. Think about which kind of quotation marks you need around the prompt so Python doesn't think the string ends early.

Good luck, and happy coding! 🐍
