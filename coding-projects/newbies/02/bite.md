---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): data types, integers, floats, strings
Path:
Related Bites: newbie 1
---

# Bite Description

In the last Bite you put a value in a box. In this Bite we are going to look at the different *kinds* of values you can put in the box. These are called **data types**.

### Data Types

| Data Type | Common Name             | Python Name              |
|-----------|-------------------------|--------------------------|
| Text      | string                  | `str`                    |
| Numeric   | integer, float, complex | `int`, `float`, `complex`|
| Sequence  | list, tuple, range      | `list`, `tuple`, `range` |
| Mapping   | dictionary              | `dict`                   |
| Set       | set, frozenset          | `set`, `frozenset`       |
| Boolean   | boolean                 | `bool`                   |

For now we only care about three of them:

- **Integers** (`int`) are whole numbers, like `7`, `-12`, or `2024`.
- **Floats** (`float`) are numbers with a decimal point, like `3.14` or `9.99`.
- **Strings** (`str`) store text. Strings always go inside quotation marks, like `"hello"`.

Strings store text. Numbers store, you guessed it, numbers.

You can check the type of any object with the `type()` function.

### Example

> 🔮 **Predict first.** Read the code below and guess what each line will print. Then check the output.

```
price = 9.99
players = 11
team = "Galaxy"
jersey = "11"

print(type(price))
print(type(players))
print(type(team))
print(type(jersey))
```

Output:

```
<class 'float'>
<class 'int'>
<class 'str'>
<class 'str'>
```

Look closely at `players` and `jersey`. They look like the same number, but the quotation marks turn `"11"` into a string. To Python, `11` and `"11"` are two different things.

### Your Task

Create three objects:

1. `my_integer` that holds the integer `29`.
2. `my_float` that holds the float `400.68`.
3. `my_lie` that holds the string `"I love data types!"`.

Good luck, and happy coding! 🐍
