---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): dictionaries, methods
Path:
Related Bites: newbie 12
---

# Bite Description

Just like strings and lists, dictionaries have methods too. In this Bite, you'll try out the three methods that hand back what is inside the box.

### Dictionary Methods

| Method      | Gives back              |
|-------------|-------------------------|
| `.keys()`   | every key               |
| `.values()` | every value             |
| `.items()`  | every key-value pair    |

### Example

> 🔍 **Investigate.** Read the code below line by line. How does `.items()` show each pair?

```
prices = {"taco": 3, "burrito": 9, "quesadilla": 7, "horchata": 4}

print(prices.keys())
# Output: dict_keys(['taco', 'burrito', 'quesadilla', 'horchata'])

print(prices.values())
# Output: dict_values([3, 9, 7, 4])

print(prices.items())
# Output: dict_items([('taco', 3), ('burrito', 9), ('quesadilla', 7), ('horchata', 4)])
```

`.items()` hands back each pair wrapped in parentheses: the key first, then the value. Hang on to that idea. It will come back when we start looping over dictionaries.

### Your Task

The template gives you the `ninjabelt_scores` dictionary from the last Bite. Call each of the three methods above on `ninjabelt_scores`.

Put each one on its own line, by itself. You don't need to `print()` them or store them in a variable. The tests are looking for the method calls themselves.

Good luck, and happy coding! 🐍
