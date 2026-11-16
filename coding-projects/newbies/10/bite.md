---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): lists, indexing
Path:
Related Bites: newbie 9
---

# Bite Description

Now that you can make a list, let's pull single items back out of it.

### Indexing

Each item in a list has a position called its **index**. Put the index in square brackets after the list name to pull out one item.

**Python starts counting at 0.**

```python
movies = ["Rush Hour", "Blues Brothers", "Ocean's Eleven", "Shaft", "Back to the Future"]
```

| Index | Item                   |
|:-----:|:-----------------------|
| `0`   | `"Rush Hour"`          |
| `1`   | `"Blues Brothers"`     |
| `2`   | `"Ocean's Eleven"`     |
| `3`   | `"Shaft"`              |
| `4`   | `"Back to the Future"` |

A list of 5 items has indexes 0 through 4. There is no index 5. If you ask for it, you'll get `IndexError: list index out of range`. That's Python telling you that you counted past the end of the list. It is one of the most common errors you will see.

```python
movies[1]
```

### Counting From the End

> 🔮 **Predict first.** Based on the error above, what do you think will happen here?

```python
movies[-1]
```

If you guessed `IndexError`, you are not alone. That is a great guess. However, the creators of Python decided that negative indexes should make sense. A negative index counts backwards from the end of the list. `-1` is the last item, so this gives back `'Back to the Future'`.

### Your Task

The template gives you the `ninjabelts` list. Using indexing, get:

1. The **last** belt, by counting from the end.
2. The **fifth** belt. (Careful! What index is the fifth item?)
3. The **first** belt.

Put each one on its own line, by itself. You don't need to `print()` them or store them in a variable. The tests are looking for the indexing expressions themselves.

Good luck, and happy coding! 🐍
