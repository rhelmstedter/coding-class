---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): variables, assignment
Path:
Related Bites:
---

# Bite Description

Welcome to the Newbie Bites! Each Bite is a small exercise that focuses on one idea. Read the description, write a little code, and then run the tests to see if it passes.

In this Bite, you'll create your very first variable.

### Variables

A variable is a container for storing a value. In Python the equal sign `=` is called the **assignment operator**. When you use `=` in your code, you are assigning a value to a label. Whatever is on the left hand side is the name. Whatever is on the right hand side is the value.

```
name = value
```

We refer to this thing as an **object**.

A useful analogy comes from Stephen Gruppetta's [Monty and the White Room](https://thepythoncodingbook.com/2021/08/12/learn-python-coding-with-monty-and-the-white-room/). Picture your program as a White Room, with Monty inside following your instructions. Every object is a box. Monty writes the name on a label on the outside of the box, puts the value inside, and sets the box on a shelf. Whenever you write the name later on, Monty finds the box with that label and hands you back whatever is inside.

### Example

```python
food = "Pizza"
score = 35

print(food)
print(score)
```

After the first two lines run, there are two boxes on the shelf. One is labeled `food` and holds `"Pizza"`. The other is labeled `score` and holds `35`.

Notice that the name never has quotes around it.

### Keep In Mind

Object names...

- only contain letters, numbers, and underscores (A-Z, a-z, 0-9, and `_`). No spaces! If you need more than one word, connect the words with an underscore, like `high_score`.
- cannot start with a number.
- are case-sensitive. `age`, `Age`, and `AGE` are three different objects.
- cannot be one of Python's reserved words (keywords), like `if`, `for`, or `def`.

### Your Task

Bob is 86 years old. Create an object named `bobs_age` and assign it the integer `86`.

Good luck, and happy coding! 🐍
