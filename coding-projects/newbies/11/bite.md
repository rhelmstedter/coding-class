---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): lists, methods
Path:
Related Bites: newbie 8, newbie 10
---

# Bite Description

Lists can change after you create them. In this Bite, you'll add an item to a list and take one away.

### Mutability

**Mutable:** the object can be changed after it is created.

**Immutable:** the object cannot be changed after it is created.

Lists are mutable. That's what makes the methods below possible.

### List Methods

Back in Newbie Bite 8 we used string methods like `.upper()`. Lists have their own methods, and you use them with the same dot notation.

- `.append(item)` adds an item to the **end** of the list.
- `.remove(item)` removes the first item that matches.
- `.pop()` removes the last item and hands it back to you.

Unlike string methods, list methods change the list **in place**. You don't need to assign the result back to a name; the box itself gets changed.

### Example

> 🔍 **Investigate.** Read the code below line by line. What changed between each `print()`?

```python
movies = ["star wars", "the batman", "shaft"]
print(movies)

movies.remove("the batman")
print(movies)

movies.append("batman")
print(movies)
```

### Your Task

The `ninjabelts` list from the last Bite is missing a belt, and it has one we don't want anymore.

1. Add `'bronze'` to the end of `ninjabelts`.
2. Remove `'blue'` from `ninjabelts`.

Use list methods to do it. Don't rewrite the list by hand.

Good luck, and happy coding! 🐍
