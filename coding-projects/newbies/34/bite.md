---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): imports, modules, random
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll write a simple number guessing game using Python. An essential part of this exercise involves using the `random` module, which brings us to an important concept in Python: modules.

What is a Module?

A module in Python is essentially a file containing Python code. It may include functions, variables, and classes which are designed to be used in other Python programs. By using modules, Python allows you to leverage pre-written code so you don't have to write everything from scratch, making your coding more efficient and your programs more powerful.

Why Do We Need Imports?

To use the code from a module in your program, you need to import it. Importing is like bringing tools into your workspace. Without importing the necessary modules, you wouldn't have access to the functions and variables defined in them. This not only helps in organizing your code better but also in reusing code efficiently. Think of imports as a way to borrow and use helpful tools created by others (or yourself) without having to recreate them.

How to Use a Module

To use a module, you must first import it into your Python script. This is done at the beginning of your file with the `import` statement. For example, to use the `randint` function from the `random` module, which generates a random integer between two specified values, you would start by importing the module:

```python
import random
```

Once imported, you can call the `randint` function using dot notation (`.`) which accesses `randint` from within the `random` module:

```
random.randint(a, b)  # Returns a random integer where `a` is the minimum and `b` is the maximum.
```

This setup is critical for our guessing game, as you will use the `randint` function to generate the secret number the player tries to guess.

### Your Task

Follow these steps:

- Use `random.randint` to get a random number between 1 and 100 and assign this integer to a variable called `secret_number`.

- Use the `input()` built-in to get the user to guess a number, make sure you _cast_ (convert) the entered user input into an integer (use `int()`). Store this number into a variable called `user_guess`.

- Return the following strings:

  - If `user_guess` and `secret_number` are the same, return "You got it!"
  - If `user_guess` is greater than `secret_number` return "Your guess is too high."
  - Else return "Your guess is too low."

That's it, good luck!
