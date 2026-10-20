---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): math, operators, variables
Path:
Related Bites: newbie 1, newbie 2
---

# Bite Description

Python makes a pretty good calculator. In this Bite, you'll do some math with objects.

### Expressions

**Expressions** contain terms and operations. In Python, an expression is any combination of values, objects, and operators that can be evaluated to produce another value.

When you assign an expression to a name, Python evaluates the right hand side of the `=` **first**, and then puts the result in the box.

### Example

```
apples = 4
oranges = 6
fruit = apples + oranges

print(fruit)
# Output: 10
```

`fruit` doesn't hold the words `apples + oranges`. Python looks inside the `apples` box, looks inside the `oranges` box, adds the values, and puts `10` in the `fruit` box.

Why bother using the names instead of just typing `4 + 6`? Because if `apples` changes later, `fruit` will still be correct.

### A Note on Style

Python doesn't care if you write `x=5` or `x = 5`. People do. The Python style guide says to put one space on each side of `=` and `+`, because it is easier to read. The tests for this Bite expect that style, so give your code some room to breathe.

### Your Task

The template has three objects: `a`, `b`, and `answer`.

1. Assign the integer `7` to `a`.
2. Assign the integer `3` to `b`.
3. Assign `a` plus `b` to `answer`. Use the object names, not the numbers.

Good luck, and happy coding! 🐍
