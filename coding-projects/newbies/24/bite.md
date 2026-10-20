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

```
coordinates = (34.2, -119.2)
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
```

You can index a tuple exactly the way you index a list:

```
print(weekdays[0])
# Output: Mon
```

### Lists vs Tuples

The big difference is that a list can be changed after you create it, and a tuple **cannot**. We say lists are **mutable** and tuples are **immutable**.

> 🔮 **Predict first.** What do you think will happen when you run this?

```
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
weekdays.append("Sat")
```

Output:

```
AttributeError: 'tuple' object has no attribute 'append'
```

Tuples don't have `.append()` or `.remove()`. Once the box is packed, it's taped shut. That sounds like a limitation, but it is the entire point. If you have data that should never change, like the days of the week, a tuple protects it from being changed by accident.

Here's where the data types you've seen so far land:

| Immutable | Mutable      |
|-----------|--------------|
| strings   | lists        |
| integers  | dictionaries |
| floats    | sets         |
| tuples    |              |

So why have both? **Immutable** objects are faster for Python to access. **Mutable** objects are easy to change.

### Converting Between Types

You've already used `int()` and `str()` to turn one data type into another. Python has a function like that for most data types, and they all work the same way: put the object you want to convert inside the parentheses, and you get back a new object of that type.

```
digits = "123"
number = int(digits)

print(type(number))
# Output: <class 'int'>
```

### Your Task

Complete the `convert_to_tuple` function. It takes the `car_brands` list as a parameter. Convert the list to a tuple and **return** it.

Good luck, and happy coding! 🐍
