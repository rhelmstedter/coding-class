---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): strings, methods
Path:
Related Bites: newbie 2
---

# Bite Description

In this Bite, we are going to use our first **methods**.

### Methods

Methods are functions that belong to an object. You use them with **dot notation**: the object's name, a dot, the method's name, and then parentheses.

```
object_name.method_name()
```

Strings come with a lot of methods. Three of the most useful change the casing of the letters:

| Method     | What it does                                   |
|------------|------------------------------------------------|
| `.lower()` | makes every letter lowercase                   |
| `.upper()` | makes every letter uppercase                   |
| `.title()` | makes the first letter of every word uppercase |

### Example

> 🔮 **Predict first.** Read the code below and guess what each line will print before you look at the output.

```
shout = "WHY ARE YOU YELLING"
whisper = "please be quiet"
book = "the lord of the rings"

print(shout.lower())
print(whisper.upper())
print(book.title())
```

Output:

```
why are you yelling
PLEASE BE QUIET
The Lord Of The Rings
```

String methods don't change the original box. `shout` still holds `"WHY ARE YOU YELLING"`. The method gives you back a **new** string. If you want to keep it, you have to put it in a box of its own.

If you want to see everything strings can do, check out the [full list of string methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

### Your Task

The template gives you three objects: `autobot`, `decepticon`, and `transformers`. Use string methods to create three new objects:

1. `lowercase_autobot` that holds `autobot` in all lowercase letters.
2. `uppercase_decepticon` that holds `decepticon` in all uppercase letters.
3. `titlecase_transformers` that holds `transformers` in title case.

Don't retype the strings yourself. Use the methods on the objects you were given.

Good luck, and happy coding! 🐍
