---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): print, f-strings, strings
Path:
Related Bites: newbie 3
---

# Bite Description

In this Bite, you'll print a sentence that mixes plain text with the values stored in objects.

### String Concatenation

One way to combine text and objects is with the `+` sign. This is called **string concatenation**. A number has to be wrapped in `str()` before it can be joined with text.

```
name = "Mr. Helmstedter"
age = 35

print("My name is " + name + " and I am " + str(age) + " years old.")
# Output: My name is Mr. Helmstedter and I am 35 years old.
```

It works, but look at all those quotes, plus signs, and spaces you have to keep track of.

### f-strings

**f-string** stands for *formatted string*. Put an `f` right before the opening quote, and you can drop objects straight into `{ }` placeholders. No `+` or `str()` needed.

```
name = "Mr. Helmstedter"
age = 35

print(f"My name is {name} and I am {age} years old.")
# Output: My name is Mr. Helmstedter and I am 35 years old.
```

> 🔍 **Investigate.** Compare the two `print()` lines above. What is the same? What is different? Which is easier to read?

When Python sees `{name}` inside an f-string, it finds the box labeled `name` and puts whatever is inside it into the sentence.

### Your Task

The template gives you three objects: `year`, `month`, and `name`. Use **one** `print()` with an f-string to display:

```
PyBites was founded in December 2016.
```

Don't type the words `PyBites`, `December`, or `2016` yourself. Use the objects to fill them in. If someone changed the value of `year`, your sentence should change too.

Good luck, and happy coding! 🐍
