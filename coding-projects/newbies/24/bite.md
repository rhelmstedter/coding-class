---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): tuples, data structures, lists
Path:
Related Bites: newbie 9, newbie 11
---

# Bite Description

In this Bite, you'll meet the **tuple**, the list's stubborn cousin.

### Tuples

A tuple holds a sequence of items, just like a list. You write it with parentheses `()` instead of square brackets.

```python
coordinates = (34.2, -119.2)
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
```

You can index a tuple exactly the way you index a list:

```python
print(weekdays[0])
```

### Lists vs Tuples

The big difference is that a list can be changed after you create it, and a tuple **cannot**. We say lists are **mutable** and tuples are **immutable**.

> 🔮 **Predict first.** What do you think will happen when you run this? Then run it.

```python
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
weekdays.append("Sat")
```

Tuples don't have `.append()` or `.remove()`. Once the box is packed, it's taped shut. That sounds like a limitation, but it is the entire point. If you have data that should never change, like the days of the week, a tuple protects it from being changed by accident.

Here's where some common data types land:

| Immutable | Mutable      |
|-----------|--------------|
| strings   | lists        |
| integers  | dictionaries |
| floats    | sets         |
| tuples    |              |

So why have both? **Mutable** objects are easy to change as your program runs. **Immutable** objects stay put, so Python lets you use them in places where a list isn't allowed, like as the keys of a dictionary.

### Converting Between Types

You've already seen `int()` and `str()` turn one data type into another. Python has a function like that for most data types, and they all work the same way: put the object you want to convert inside the parentheses, and you get back a new object of that type.

```python
digits = "123"
number = int(digits)

print(type(digits))
print(type(number))
```

### Your Task

Complete the `convert_to_tuple` function. It takes **one** parameter: a list. Add the parameter yourself, and pick a name for it.

Convert the list to a tuple and **return** it.

The tests will call your function with a few different lists. If you are having trouble, you can try calling it with a list of your own and printing what comes back.

Good luck, and happy coding! 🐍
