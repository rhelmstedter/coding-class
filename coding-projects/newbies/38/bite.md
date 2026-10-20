---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): classes, dunder methods
Path:
Related Bites: make_a_class, make_dataclass
---

# Bite Description

This Bite continues where the previous class Bite left off. You are presented with a `Rectangle` class, and you will add the special `__str__` method to give it a string representation.

### Understanding the `__str__` Method

You may have noticed in the previous bite, we never printed the `Circle` objects directly. Let's see what that looks like.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius


my_circle = Circle(5)
print(my_circle)
```

Output:
```
<__main__.Circle object at 0x102ee7dc0>

```

Now you see why we didn't print it. So let's break it down. By default, when you print a custom object you will see a message that tells you the type of object you printed and the location in memory. Here the object is `__main__.Circle object`. `__main__` is just a label that represents the Python file that I am running to print out the code. That number, `0x102ee7dc0`, is just the location in memory where Python is storing the `Circle` object and will likely change each time you run the code. Generally, we don't care about the number. 

For our `Circle` object, having a sentence that tells us how big the circle is would be nice. That way when we print it we get something like "A circle with a radius of 5." instead of that output we saw above. 

To print something more friendly, we can write a `__str__` method. Like `__init__`, `__str__` is a "dunder" (double underscore) method. We are defining a function inside the class, but instead of choosing a name, we have to call it `__str__` so that Python knows we want to use it for the string representation of an object. When you print an object or use `str()` on it, the `__str__` method is called.

For example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"A circle with a radius of {self.radius}."

circle = Circle(5)
print(circle)
```

Output:
```
A circle with a radius of 5.
```

Notice, for the `__str__` method, we also pass in `self` and inside the f-string, we use `self.radius` to get the radius of the `Circle` object. The final class would look like this:


```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
	   
    def calc_area(self):
        return 3.14159 * self.radius**2

    def calc_circumference(self):
        return 2 * 3.14159 * self.radius

    def __str__(self):
        return f"A circle with a radius of {self.radius}."
```

We could put the `__str__` method about the `calc_area` and `calc_circumference` methods or even the `__init__` method if we wanted to. Generally, programmers write the `__init__` first.

## Your Task

Add the `__str__` method to the existing `Rectangle` class. Given a `Rectangle` object with a base of 3 and a height of 4, he `__str__` method should return a string that describes the rectangle in the following format: `"A rectangle with a base of 3 and a height of 4."`.

### Steps to Complete

1. **Define the `__str__` Method**: Add the `__str__` method to the `Rectangle` class. This method should return an f-string with the format shown below.

```python
rectangle = Rectangle(3, 4)
print(rectangle)
```

Output:

```
A rectangle with a base of 3 and a height of 4.
```

Good luck, and happy coding!
