---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): exceptions, error handling, functions
Path:
Related Bites:
---

# Bite Description

In this Bite, we introduce you to the essentials of exception handling in Python. Exception handling is a crucial aspect of writing more robust code. By learning how to properly handle exceptions, you can make your programs more resilient and user-friendly.

### Errors and Exceptions

We have worked with errors before in Newbie Bite 26. According to the [Python docs](https://docs.python.org/3/tutorial/errors.html), there are (at least) two types of errors: syntax errors and exceptions. Examples of syntax errors are forgetting to put a closing parenthesis or quotation mark. Or perhaps you wrote a `for` loop, but forgot the colon (`:`) at the end. These types of errors crash your program because you haven't followed the syntax rules. (Crash is a term that people use when your program stops running before you want it to.)

Exceptions are errors that occur when code is syntactically correct. They can be caused by various issues, such as invalid input, trying to divide by zero, or trying to open up files that don't exist. 

Python provides a way to handle these exceptions gracefully using `try`, `except`, `else`, and `finally` blocks. This allows you to manage errors and provide meaningful feedback to users or take corrective actions.

#### Example Without Exception Handling

I created a Python file called `errors_example.py`. The contents of the file are shown below. I ran the code and then pasted the output.
```python
def divide(a, b):
    result = a / b
    return result


print(divide(10, 2))
```
Output:
```
5.0
```
Woohoo, it works as intended!

Now look what happens when I run the code again, but this time try to divide by zero.

```python
def divide(a, b):
    result = a / b
    return result


print(divide(10, 0))
```

Output:
```
Traceback (most recent call last):
  File "errors_example.py", line 6, in <module>
    print(divide(10, 0))
  File "errors_example.py", line 2, in divide
    result = a / b
ZeroDivisionError: division by zero
```
The syntax of the code is still correct. The problem happens when I tried to divide by zero. Python raises an exception called `ZeroDivisionError`. It then displays some more information about the exception such as the file name, and the line(s) where it occurred. Did you notice that there are two line numbers? That is because the error didn't occur when the function was defined. It happened after the function call on line 6. So then Python jumped back up to the function and tried to follow the directions to divide `result = a / b` on line 2. The program crashed and I get this messy error message.

#### Example of Exception Handling

Here’s an example of how to handle the exceptions in Python:

```
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    return result

print(divide(10, 0))
```
Output:
```
Cannot divide by zero
```

You start with the keyword `try` followed by a colon. Then you must indent and include the code that might result in an exception. In our case, `result = a / b`. Then, unindent and use the `except` keyword, followed by the exception and another colon. In our case, the exception was `ZeroDivisionError`. Indent again and write instructions for Python to execute in case the error happens. In this case we tell Python to `return` the string `"Cannot divide by zero"`. Finally we unindent and continue with the body of the function. In this case it is just returning the `result`.

This is sometimes called `catching` the exception. If we don't catch the exception using the try/except blocks, the program will crash and the user sees the traceback message. If we catch the error using try/except blocks, the division by zero still doesn't happen, but the user sees a nicer message.

### Raise Your Own Exceptions

Sometimes it is useful to create custom exceptions. When exceptions happen, it is sometimes called "raising an exception". You can also raise exceptions manually using the `raise` keyword. This allows you to provide more detailed error messages.

Here is an example of raising an exception:

```python
def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid email address")
    return email
```

In this code snippet, if the email address does not contain the "@" symbol, the `validate_email` function raises a `ValueError` with the message `"Invalid email address"`.

This will exit the function and prevent further execution (so return email will not be reached). However unlike a regular return from the function, it will raise an exception which the caller of the function will need to handle (catch), otherwise the program will crash.

### Your Task

In this exercise, you will add exception handling to two functions: `get_number` and `calculate_circle_area`.

#### `get_number`

1. Use a `try` / `except` block to catch any `ValueErrors` that occur when trying to convert the input to a number.
2. If there is an exception, return the string `"You can only enter numbers here."`.

####  `calculate_circle_area`

1. Add a condition to see if the parameter `radius` is less than 0.
2. If that's the case, raise a `ValueError` containing the message "The radius must be positive."

By completing this task, you'll gain a better understanding of how to handle exceptions in Python, making your code more robust and user-friendly.

By the way, there are many built-in exceptions in Python, check out the [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) documentation for more detail, especially at the end of the page where you can see the hierarchy of exceptions.

Good luck, you're getting there! Only five Newbie Bites left!
