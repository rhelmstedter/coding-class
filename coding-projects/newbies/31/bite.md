---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): strings, methods
Path:
Related Bites:
---

# Bite Description

In this bite, we are going to explore two useful string methods in Python: `.split()` and `.splitlines()`. These methods are powerful tools for working with and manipulating text data.

**Understanding `.split()`**

The `.split()` method is used to split a string into a list of words. By default, it splits the string at every whitespace character (spaces, tabs, and newlines). If you provide a specific separator, it will split the string based on that separator.

For example:

```python
text = "Hello, world!"
words = text.split()
print(words)  # Output: ['Hello,', 'world!']
```

In this example, the string is split into words using spaces as the separator.

**Understanding `.splitlines()`**

The `.splitlines()` method is used to split a string into a list of lines. This method splits the string at newline characters (`\n`). It's useful when you want to work with text that spans multiple lines.

For example:

```python
text = "Line one.\nLine two.\nLine three."
lines = text.splitlines()
print(lines)  # Output: ['Line one.', 'Line two.', 'Line three.']
```

In this example, the string is split into individual lines.

Now, let's apply these methods to some text processing tasks.

### Your Task

You are provided with a string `prince_of_py` and two functions: `word_count` and `line_count`.

1. Implement `word_count`: This function takes a string as input and returns the number of words in the string.

Use the `.split()` method on the string passed into the function to split it into a list of _words_. Then, use the `len()` built-in on this list to get the length and return this integer from the function. _Built-in_ means here that it's readily available, you don't have to import it into the script to use it.

2. Implement `line_count`: This function takes a string as input and returns the number of lines in the string.

The same as above but instead of `split()` you use the `.splitlines()` method on the string passed into the function to split it into a list of _lines_. Also here use the `len()` built-in on this list to get the length and return this integer from the function.

Optionally, you can add type hints to specify that the input is a string and the return value is an integer.

Here are the initial function definitions you need to modify.

_Note: don't modify the `prince_of_py` string nor the function argument: `string = prince_of_py` (this is another example of a default argument we covered in the previous Bite), only write code in the body of each function._

```
prince_of_py = """This is a story all about how,
My code got flipped-turned upside down.
And I'd like to take a minute, so just stand by,
I'll tell you how I became the prince of these bites of py.
"""

def word_count(string=prince_of_py):
    # Your code here

def line_count(string=prince_of_py):
    # Your code here
```

Modify these functions to use `.split()` and `.splitlines()` respectively to count the words and lines in the provided string.

_Note we used default arguments from the last Bite, so you can call the functions without arguments._

Good luck and have fun!
