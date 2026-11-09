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
print("5" == 5)
```

Look closely at the last two. Strings are compared letter by letter, and to Python an uppercase `A` and a lowercase `a` are different characters. And remember data types from Newbie Bite 2: `"5"` is a string and `5` is an integer, so they are never equal.

### Returning a Comparison

A comparison gives back a value, so a function can `return` it. Python works out the comparison first, then Monty carries the `True` or `False` out of the room.

```python
def is_sold_out(tickets_left):
    return tickets_left == 0

print(is_sold_out(0))
print(is_sold_out(12))
```

### Your Task

The template has three empty functions. Each one takes parameters (add them yourself) and **returns** `True` or `False`.

1. `can_vote` takes a person's age. Return whether they are old enough to vote. You can vote at 18 or older.
2. `is_too_cold` takes a temperature. Return whether it is below 50.
3. `is_same_name` takes two names. Return whether they are the same name. Capitalization shouldn't matter, so `"Ada"` and `"ada"` count as the same name.

Return the actual boolean, not the string `"True"`. And check your edges: what should `can_vote(18)` give back? What about `is_too_cold(50)`?

Good luck, and happy coding! 🐍
