---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): lists, data structures
Path:
Related Bites: newbie 2
---

# Bite Description

So far every box has held a single value. In this Bite, you'll make a box that holds a whole collection of values.

### Lists

A **list** holds more than one value in a single object. Write it with square brackets `[]` and commas between the items.

```
label = [first_item, second_item, third_item, ...]
```

A list is still just one box on the shelf, with one label on the outside. Inside, the items sit in a row, one per slot. The order you type them in is the order they stay in.

### Example

```
scores = [88, 94, 71, 100, 65]
names = ["Ada", "Grace", "Alan"]

print(names)
# Output: ['Ada', 'Grace', 'Alan']

print(type(names))
# Output: <class 'list'>
```

A list can hold any data type, and it doesn't have to hold just one kind:

```
mixed = ["Ada", 36, True, 3.14]
empty = []
```

### Your Task

The people who created these Bites handed out ninja belts as you completed them. The belts, in order, were:

**white, yellow, orange, green, blue, brown, black**

Create a list called `ninjabelts` that holds each belt color as a lowercase string, in that order.

Good luck, and happy coding! 🐍
