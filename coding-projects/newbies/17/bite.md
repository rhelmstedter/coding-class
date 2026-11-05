---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): comparison, booleans, operators
Path:
Related Bites: newbie 1
---

# Bite Description

In this Bite, we are going to look at the difference between `=` and `==`. They look almost the same, but they do very different things.

### Assigning vs Comparing

- `=` is the **assignment operator** from Newbie Bite 1. It puts a value in a box.
- `==` is the **equality operator**. It asks a question: *are these two things equal?*

The answer to a question like that is always a **boolean**: `True` or `False`. Python uses capital letters for `True` and `False`.

### Comparison Operators

| Operator | Definition               |
|:--------:|:-------------------------|
| `==`     | equal                    |
| `!=`     | not equal                |
| `>`      | greater than             |
| `<`      | less than                |
| `>=`     | greater than or equal to |
| `<=`     | less than or equal to    |

### Example

> 🔮 **Predict first.** Guess whether each line prints `True` or `False`. Then run it.

```python
age = 18

print(age == 16)
print(age != 16)
print(age >= 18)
print("Ada" == "ada")
```

Look closely at the last one. Strings are compared letter by letter, and to Python an uppercase `A` and a lowercase `a` are different characters.

### Your Task

Create two objects, `pybites1` and `pybites2`, that both hold the string `"PyBites"`.

The tests will check `pybites1 == pybites2`, so think about what could make that comparison come out `False`.

Good luck, and happy coding! 🐍
