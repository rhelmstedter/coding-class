---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): functions, arguments
Path:
Related Bites:
---

# Bite Description

In this Bite, we are going to explore the concept of default arguments in Python functions.

Default arguments allow you to define functions that use default values if no arguments are provided, making your functions more flexible and easier to use.

Default arguments are specified by assigning a value to the parameter in the function definition. If the caller does not provide a value for that parameter, the default value is used.

This can be particularly useful for functions that have parameters with common default values, allowing you to simplify function calls and avoid repetitive code.

Here is a basic example:

```
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())       # Output: Hello, World!
print(greet("Bob"))  # Output: Hello, Bob!
```

In this example, the `greet` function has a default argument `name` set to "World". If no argument is provided when calling the function, it uses the default value. We assign the default argument using the `=` (equal) sign. This is the assignment operator we learned back in Newbie Bite 1.

Now, let's apply this concept to a couple of functions that calculate the area and perimeter of a rectangle. You will add default arguments to these functions, allowing them to work even if no arguments are provided.

### Your Task

You are given two functions: `calc_rectangle_area` and `calc_rectangle_perimeter`.

1. _Define default values_: Both functions should have default values for their parameters `base` and `height`. Set these defaults to `1`.
2. _Type hints (optional)_: Optionally, add type hints to specify that both `base` and `height` are of type `float`, and the return value is also a `float`. Where does the type hint go here? Glad you asked! It goes after the variable but BEFORE the equal sign + default argument. For example: `base: float = 1`.

Here are the initial function definitions you need to modify:

```
def calc_rectangle_area(base, height):  # <-- Add default values here
    # multiply base by height to calculate the area of a rectangle, and return the result

def calc_rectangle_perimeter(base, height):  # <-- Add default values here
    # calculate and return the perimeter of a rectangle (2 * base + 2 * height)
```

By doing this, you ensure that both functions can compute the area and perimeter of a rectangle with default values if no arguments are passed.

Good luck, and happy coding!
