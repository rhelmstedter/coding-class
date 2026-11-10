---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): classes
Path:
Related Bites: class_with_str, make_dataclass
---

# Bite Description

In this Bite, you'll learn about writing Python classes. Classes are like blueprints for creating custom objects. 

We have seen classes already. In the `datetime` module, the `date` object is a class. The `date` class has attributes and methods that are great for working with dates. Today, we are going to look at creating a `Circle` object, which will have attributes and methods that are great for working with circles.

### Building a Class

When creating a class, you type the `class` keyword followed by the name of the class and end the line with a colon. For example, `class ClassName:`. Since this line ends in a colon, the body of the class will be indented. It is a very strong convention to use [CapWords](https://peps.python.org/pep-0008/#class-names) (also called Pascal case) when naming your class, where every word starts with a capital letter, like `ClassName`. If you don't use CapWords, your program will still work, but it is a good idea to stick with this practice.

Before you start writing the body of the class, you should think about all the attributes your object will have. In our class, every `Circle` object will have a radius. When building your own classes, you can have as many attributes as you would like.

After you figure out your desired attributes, you define the `__init__` method. The first parameter will always be `self`, and you will pass in the remaining attributes you want as parameters for the function. Then, you have to assign the parameters as attributes within the function. Below is what that looks like.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
```
This can be overwhelming the first time you see it, but let's break it down. All you are doing is defining a function, but instead of creating your own name for it, you have to use `__init__`. It starts and ends with double underscores, so many people refer to this as "dunder init". `init` is short for "initialize", which in computer science means to give something a starting value. It is also known as the constructor method, because you use it to construct, or build, the class.

The first parameter of the `__init__` method, always refers to the object you are constructing. That means you need a label for the object that is created when you call the class later in your program. In python, we like to use the word `self`. While in other languages, they use the word `this`. Just like using CapWords to name a class, using the label `self` to refer to the object created when you call the `Circle` class is a convention. While you can use any label you want, it is a good idea to stick with the label `self`.

So we are saying, when we use the `Circle` class later in the program to create a `Circle` object, initialize the `radius` attribute to the value we pass in. Let's see what that looks like: 

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius


# Here we are calling the class to create a Circle object
my_circle = Circle(3)

print(my_circle.radius)
```

Output:
```
3
```

Woohoo! We just created a circle with a radius of 3! 

### Adding More Methods

OK, we have a basic class that creates a `Circle` and gives it a radius. But that is a little boring, let's add some more functionality. If we were given a circle, what else might we want to know? Perhaps, we would want to be able to calculate the area and the circumference. For your convenience, the formulas for the area and the circumference are below.

- Area: πr²
- Circumference: 2πr.

We will use these formulas to create class methods. Remember, methods are just functions that are associated with a certain object. So we will define two functions inside the `Circle` class, one for the area, the other for the circumference. 

Starting with the area, before we write the entire function, let's convert the formula from math to something that python will understand. We will use 3.14159 for π, and the operation for exponents in python is `**`. Translating the formula from math to python we would get: Area = `3.14159 * radius ** 2`. However, which radius are we talking about? Well, we want to use the radius that will be passed in when we call the `Circle` class, so we need to add `self`. The area becomes `3.14159 * self.radius ** 2`. That means we will also need to pass `self` in as a parameter for the function itself. Adding the entire method to the class looks like this:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14159 * self.radius ** 2
```

Doing the same for circumference, the full class looks like this:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14159 * self.radius ** 2

    def calc_circumference(self):
        return 2 * 3.14159 * self.radius
```

An overview of the `Circle` class:

- The `__init__` method is also called the constructor. It initializes a new circle instance with a specific radius.
- The `calc_area` method calculates the area of the circle using the formula πr².
- The `calc_circumference` method calculates the circumference using the formula 2πr.

### The Circle Class in Action

Here is how you would use this class. Use the dot notation to access the attributes and the methods.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14159 * self.radius**2  # Area calculation for the circle.

    def calc_circumference(self):
        return 2 * 3.14159 * self.radius  # Circumference calculation for the circle.


my_circle = Circle(3)


print(f"My circle has a radius of {my_circle.radius}.")
print(f"My circle has an area of {my_circle.calc_area()}.")
print(f"My circle has a circumference of {my_circle.calc_circumference()}.")
```

Output:
```
My circle has a radius of 3.
My circle has an area of 28.27431.
My circle has a circumference of 18.849539999999998.
```

### Type Hints

This section is optional. If we want to add some more information, we can add type hints! We know that the radius should be a number. Does it have to be limited to only integers? Probably not, so we should go with `float`. If we do pass in an integer for the radius that will be OK, because type checkers accept an integer anywhere a float is expected. Since `self.radius` can be a float and in each of the methods we are multiplying by a float, the return value will always be a float. The final class with type hints looks like this: 

```python
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calc_area(self) -> float:
        return 3.14159 * self.radius ** 2

    def calc_circumference(self) -> float:
        return 2 * 3.14159 * self.radius
```

### Your Task

Create a `Rectangle` class and add the following methods:

1. **Constructor (`__init__`)**: every `Rectangle` should have a `base` and `height`. 

2. **`calc_area` method**: This method should calculate and return the area of the rectangle. Area Formula: base * height.

3. **`calc_perimeter` method**: This method should calculate and return the perimeter of the rectangle. Perimeter formula: 2 * base + 2 * height.

Good luck!
