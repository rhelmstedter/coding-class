---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): error handling, debugging, syntax errors
Path:
Related Bites:
---

# Bite Description

Welcome to the second half of the Newbie Bites! This half builds on everything from the first 25 and covers some more advanced topics that will help you write better code and understand more complex concepts.

In this Bite, you'll practice reading and understanding error messages in Python. Error messages provide valuable information about what went wrong in your code.

### Understanding Errors

When Python encounters an error, it generates an error message that includes:
- The type of error (e.g., `SyntaxError`, `TypeError`, `NameError`).
- A description of what went wrong.
- The line number where the error occurred.

By carefully reading error messages, you can pinpoint the exact location and nature of the problem in your code.

### Examples

Here are some common types of errors and what they mean:

1. **SyntaxError**: This error occurs when the code is not syntactically correct. Syntax is the set of rules that python follows in order for your code to run correctly. For example, anytime you have quotations `""`, parentheses `()`, brackets `[]`, or braces `{}` they must come in pairs. Another example would be that you need a colon at the end of each function definition, if/else statement, or for/while loops. If you are missing these things, you will get a `SyntaxError`.

```
print("Hello, world!)
# Output: SyntaxError: unterminated string literal
```

Here the quotation marks are never closed. Python reached the end of the line before it found a second quotation mark, so it raised an error.

2. **TypeError**: This error occurs when an operation or function is applied to an object of an inappropriate type.

```
print(5 + "five")
# Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Here the `TypeError` is saying that we can't add integers and strings. If we put quotations around the 5 then we would be able to add (concatenate) the two strings together.

3. **NameError**: This error occurs when a local or global name is not found.

```
print(welcome)
# Output: NameError: name 'welcome' is not defined
```

Here the `NameError` is telling us we never created an object named `welcome`. If we wanted to use the object `welcome` we would need to assign a value to it using the assignment operator. For example, `welcome = "Welcome to the newbie bites part 2."`.

4. **IndexError**: This error occurs when you try to access an index that is out of range for a list.

```
nums = [1, 2, 3]
print(nums[5])
# Output: IndexError: list index out of range
```

Here the `IndexError` is saying that the index `5` is out of range for the list `nums`, which only has indices `0`, `1`, and `2`. To avoid this error, you can ensure that the index is within the valid range of the list, or use a condition to check the length of the list before accessing an index.

5. **KeyError**: This error occurs when you try to access a key that is not present in a dictionary.

```
person = {"name": "Alice"}
print(person["age"])
# Output: KeyError: 'age'
```

Here the `KeyError` is telling us that the key 'age' does not exist in the dictionary `person`. To avoid this error, you can check if the key exists using the `in` keyword, like `if 'age' in person:`, before trying to access it.

### Your Task

Read the code below. The function is designed to loop through the `ninjabelt_scores` dictionary and return a new dictionary called `filtered`. The `filtered` dictionary should only contain belts with scores above the `cutoff`. However, the code does not work at the moment. It contains multiple errors that prevent it from running correctly. Your task is to:

1. **Understand the Code**: Read through the code to understand what each line is supposed to do.
2. **Run the Code**: Save your code, then run the **Run your code** cell to see the error messages.
3. **Fix the Errors**: Use the information from the error messages to fix all the errors.
4. **Pass the Tests**: Run the **Run Tests** cell and see if the code passes all the tests.

#### Example Usage
Here is what the function should return when you call it with a `cutoff` of 50.

```
print(get_belts_above(50))
# Output: {'brown': 60, 'black': 70}
```

Good luck, and happy coding! 🐍
