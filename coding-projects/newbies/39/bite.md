---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): classes, dataclasses
Path:
Related Bites: make_a_class, class_with_str
---

# Bite Description

In this Bite, you'll explore Python dataclasses, introduced in Python 3.7 to simplify class definitions for storing data. 

We have only scratched the surface of what you can do with classes in python. There are lots of other methods and functionality that you can add. There are other dunder methods that let you compare and order objects based on their attributes, for example the equality method (`__eq__`) or the less than method (`__lt__`). There is even a special representation method (`__repr__`) that is designed for programmers to read when they are working on their code.

If you are working with simple objects, dataclasses might be a good option because they automate the creation of initialization (`__init__`), representation (`__repr__`), and equality (`__eq__`) methods among others. This can save time and make your code cleaner and more efficient.

### Why Use Dataclasses?

Dataclasses reduce [boilerplate](https://en.wikipedia.org/wiki/Boilerplate_code) code in class definitions. In computer programming, boilerplate code, or simply boilerplate, are sections of code that are repeated in multiple places with little to no variation. In the context of classes we consider `__init__`, and some other methods that start with double underscore (`__`) boilerplace. When you create a `dataclass`, it automatically generates these methods based on the class attributes you define.

### Revisiting the `Circle` Class

Here is the `Circle` class from last time. At the bottom we have added the `__repr__` method.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14159 * self.radius**2  # Area calculation for the circle.

    def calc_circumference(self):
        return 2 * 3.14159 * self.radius  # Circumference calculation for the circle.
    
    def __str__(self):
        return f"A circle with a radius of {self.radius}."
	   
    def __repr__(self):
        return f"Circle(radius={self.radius})"
	   
my_circle = Circle(3)
print(my_circle.__repr__())
```

Output:

```
Circle(radius=3)
```
When we call the `__repr__` method on an object we get the representation that we coded. It can be different than the `__str__` representation so it provides information for the programmer that isn't always in the string representation.

### Creating a dataclass

When creating a dataclass, you would first import the `dataclasses` module and then use the `dataclass` object. Technically speaking, the `dataclass` object is a decorator. A decorator in Python is a special type of function that can modify the behavior of another function or class. We won't go into detail on how decorators work because that is beyond the scope of the newbies, but just know that you use it by placing at `@` symbol in front of the decorator name. When you see a decorator, such as `@dataclass`, it means that the `dataclass` function is being applied to the class that follows it.

### Converting `Circle` to a dataclass

Just for a moment, let's forget about all of the methods we coded in the previous bites. We are going to refactor the `Cicle` class. Refactoring just means that we are going to change the code, but the output will remain the same. The most simple version of refactoring the `Circle` class to a `dataclass` looks like this:

```python
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float


my_circle = Circle(3)
print(my_circle)
```

Output:

```
Circle(radius=3)
```

Look at that! No more `__init__` and it printed out the object nicely without having to define `__str__` or `__repr__`. The attributes are created using type hints in place of writing the `__init__` method.

We can still add methods to dataclasses just like before. So our final refactoring would like the following:

```python
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float
    
    def calc_area(self):
        return 3.14159 * self.radius**2  # Area calculation for the circle.

    def calc_circumference(self):
        return 2 * 3.14159 * self.radius  # Circumference calculation for the circle.
    
    def __str__(self):
        return f"A circle with a radius of {self.radius}."


my_circle = Circle(3)
print(my_circle)
print(my_circle.__repr__())
```
 
Output:

```
A circle with a radius of 3.
Circle(radius=3)
```
### A New Class

Let's introduce a new class in this Bite called `Point` representing a point in a two-dimensional space:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
	   
my_point = Point(2, 4)
print(my_point)
```

Output:

```
Point(x=2, y=4)
```

In the `Point` class:

- The `__init__` method initializes each new instance with `x` and `y` coordinates.
- The `__repr__` method provides a neat representation of the point for the programmer.

### Point as a Dataclass

Instead of making a class, we can make `Point` a `dataclass`.

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


my_point = Point(2, 4)
print(my_point)
```

Output:

```
Point(x=2, y=4)
```

Much less typing! With this dataclass:

- You no longer need to explicitly define the `__init__` and `__repr__` methods unless you need to customize their behavior beyond the standard functionality.
- The attributes `x` and `y` are defined with type annotations.

### Your Task

In this exercise, you will refactor the previous `Rectangle` class into a dataclass. By refactoring the `Rectangle` class into a dataclass, you reduce the amount of code you need to write and make your class definition cleaner and more maintainable.

Here are the steps you need to take:

1. **Remove the `__init__` and `__str__` Methods**.

2. **Import the `dataclass` Decorator from the `dataclasses` module**

3. **Use the Decorator on the Class**.

4. **Define the Class Attributes**: The `base` and `height` should be floats.

Good luck, and happy coding!
