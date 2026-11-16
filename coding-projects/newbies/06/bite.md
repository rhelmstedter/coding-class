---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): math, operators
Path:
Related Bites: newbie 5
---

# Bite Description

In the last Bite you added two objects together. In this Bite we'll use the rest of the basic math operators.

### Math Operators

| Operator | Operation      | Example  | Result |
|:--------:|:---------------|:---------|:------:|
| `+`      | addition       | `8 + 2`  | `10`   |
| `-`      | subtraction    | `8 - 2`  | `6`    |
| `*`      | multiplication | `8 * 2`  | `16`   |
| `/`      | division       | `8 / 2`  | `4.0`  |

Multiplication uses an asterisk `*`, not an `x`. Division uses a forward slash `/`.

> 🔍 **Investigate.** Look at the result of `8 / 2` in the table. Why does it have a decimal point when the others don't? (Hint: think back to data types in Newbie Bite 2.)

Python has a few more operators you'll run into later:

| Operator | Operation      | Example   | Result |
|:--------:|:---------------|:----------|:------:|
| `**`     | exponentiation | `2 ** 3`  | `8`    |
| `//`     | floor division | `7 // 2`  | `3`    |
| `%`      | modulus        | `7 % 2`   | `1`    |

Floor division divides and then chops off the decimal. Modulus gives you the remainder.

> 🔮 **Predict first.** Python follows the same order of operations you learned in math class. What do you think this gives you? Then run it.

```python
3*2 + 8/4 - 2**2
```

### Example

```python
width = 12
height = 3

perimeter = 2 * width + 2 * height
area = width * height

print(perimeter)
print(area)
```

### Your Task

The template gives you two objects, `a` and `b`. Using `a` and `b` (not the numbers they hold), create three new objects:

1. `subtraction` that holds `a` minus `b`.
2. `multiplication` that holds `a` times `b`.
3. `division` that holds `a` divided by `b`.

Keep `a` first and `b` second in each one.

Good luck, and happy coding! 🐍
