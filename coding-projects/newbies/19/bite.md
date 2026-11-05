---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): booleans, truthiness, conditionals
Path:
Related Bites: newbie 16, newbie 18
---

# Bite Description

In the last Bite, the `if` statement checked a comparison like `date == "payday"`. But you don't always need a comparison. In this Bite, we'll look at how Python decides whether *any* object counts as `True` or `False`.

### Truthy and Falsy

When you put an object right after `if`, Python asks: *does this count as true?* Objects that count as true are called **truthy**. Objects that count as false are called **falsy**.

In Python, these values are all treated as `False` when used in a conditional:

- `False`
- `None`
- Zero of any numeric type (`0`, `0.0`)
- Any empty sequence (`""`, `[]`, `()`)
- Any empty mapping (`{}`)

Pretty much everything else is truthy. For truthy values, just existing is enough.

If you're ever not sure, the `bool()` function will tell you whether an object is truthy or falsy.

```python
print(bool("pizza"))
print(bool([]))
```

### Example

> 🔮 **Predict first.** Which of these lines will print? Then run it.

```python
if "pizza":
    print("one")

if "":
    print("two")

if [1, 2, 3]:
    print("three")

if []:
    print("four")
```

An empty string and an empty list are falsy, so their `print()` lines never run.

This is really handy for checking whether something is there at all. Instead of checking whether a list has a length of zero, you can just put the list after `if`.

```python
movies = []

if movies:
    print(f"There are {len(movies)} movies to choose from.")
else:
    print("So sad, there is nothing to watch.")
```

> 🔧 **Modify.** Put a few movies in the list and run it again.

### Your Task

The template has two functions for you to complete.

1. `get_username` should ask the user to enter their username and **return** what they type.
2. `print_username` takes one parameter, `username`. Use truthiness to check it:
   - If it is truthy, print `Your username is: USERNAME.` with the actual username in place of `USERNAME`.
   - If it is falsy, print `Sorry, no username was defined.`

Don't forget the period at the end of each sentence.

Good luck, and happy coding! 🐍
