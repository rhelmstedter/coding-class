
---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): type hints
Path: no
Related Bites:
---

# Bite Description

In this bite, we are going to explore type hints in Python. Type hints are a feature introduced in Python 3.5 that allow you to specify the expected data types of function arguments and return values. They help make your code more readable and can also assist with debugging by catching type-related errors before runtime.

Type hints do not change how your code runs but provide additional information that can be used by tools and IDEs to perform static analysis, type checking, and code completion.

Here's a simple example of how to use type hints:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this example, `name` is expected to be a string, and the function returns a string. If you try to pass an integer to `greet`, a type checker (for example `mypy`) would alert you about the mismatch.

### Labels for Type Hints

Each type in python has a special label that you use for its type hints. The labels below work for python >= 3.9. If you are using a python version less than 3.9, you'll have to use these [labels](https://docs.python.org/3.8/library/typing.html) and choose your specific version of python.


| Data Type | Python     | Type Hint Label |
|-----------|------------|-----------------|
| Text      | string     | `str`           |
| Numeric   | integer    | `int`           |
| Numeric   | float      | `float`         |
| Sequence  | list       | `list`          |
| Sequence  | tuple      | `tuple`         |
| Mapping   | dictionary | `dict`          |
| Set       | set        | `set`           |
| Boolean   | boolean    | `bool`          |
| None Type | None       | `None`          |


### Your Task

Add type hints to the `date_formatter` function. The function `date_formatter` takes three arguments: `day`, `month`, and `year`, and returns a formatted date string. We will add type hints to this function to specify the expected types of these arguments and the return type.

1. Add type hints to the `day`, `month`, and `year` parameters; day and year are **integers** and month is a **string**

2. Specify the return type of the function which should be a **string**.

Good luck!
