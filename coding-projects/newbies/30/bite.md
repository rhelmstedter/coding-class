---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): strings, special characters, newline, tab
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll learn about special characters in Python strings. Special characters like `\n` and `\t` are used to format strings in a more readable and structured way.

### Understanding Special Characters

- **`\n` (newline)**: This character is used to insert a new line in a string.
- **`\t` (tab)**: This character is used to insert a tab space in a string.

These special characters help in creating formatted text output, which is particularly useful for creating multi-line strings and aligning text.

### Example

Consider the following example to understand how `\n` and `\t` work:

```python
text = "Hello,\n\tWelcome to Python programming!"
print(text)
```

Output:

```
Hello,
	Welcome to Python programming!
```

In this example, `\n` creates a new line after "Hello," and `\t` adds a tab before "Welcome to Python programming!".

### Your Task

Your task is to create a function `multiline_string_with_tabs` that returns a formatted multi-line string using `\n` and `\t`.

The output should be:
```
    Good morning!
    Today I will code.
    Python :)
```

Here is the initial function definition you need to work with:

```
def multiline_string_with_tabs():
    # Your code here
```

### Steps to Complete

1. **Use `\t` for Tabs**: Insert a tab character (`\t`) at the beginning of each line.
2. **Use `\n` for Newlines**: Insert a newline character (`\n`) at the end of each line, except the last one.

### Example Usage

```
output = multiline_string_with_tabs()
print(output)
```

Output:

```
    Good morning!
    Today I will code.
    Python :)
```

By completing this task, you'll gain a better understanding of how to use special characters to format strings in Python.

Good luck and have fun!
