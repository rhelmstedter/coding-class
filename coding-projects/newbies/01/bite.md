---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): variables, assignment
Path:
Related Bites:
---

# Bite Description

Welcome to the Newbie Bites! Each Bite is a small exercise that focuses on one idea. Read the description, write a little code, and then submit it to see if it passes the tests.

In this Bite, you'll create your very first variable.

### Variables

A variable is a container for storing a value. In Python the equal sign `=` is called the **assignment operator**. When you use `=` in your code, you are assigning a value to a label. Whatever is on the left hand side is the name. Whatever is on the right hand side is the value.

```
name = value
```

We refer to this thing as an **object**.

A useful analogy (borrowed from Stephen Gruppetta's [Monty and the White Room](https://thepythoncodingbook.com/2021/08/12/learn-python-coding-with-monty-and-the-white-room/)) is to think of a box. The name of the object is written on a label on the outside of the box, and the value is stored inside the box. Once the box is made, Python puts it on a shelf somewhere in memory. Whenever you write the name later on, Python finds the box with that label and hands you back whatever is inside.

### Example

```
food = "Pizza"
score = 35

print(food)
# Output: Pizza

print(score)
# Output: 35
```

After these two lines run, there are two boxes on the shelf. One is labeled `food` and holds `"Pizza"`. The other is labeled `score` and holds `35`.

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
