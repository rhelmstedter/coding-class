---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): collections, namedtuples
Path:
Related Bites:
---

# Bite Description

In this bite, you'll learn about the `namedtuple` object. These objects are similar to a regular tuple; However, while elements in a regular tuple are accessed by index, elements in a `namedtuple` can be accessed by an attribute through dot notation, making your code more readable.

### Example: Regular Tuple vs. Namedtuple

Recall from [Newbie 24](https://codechalleng.es/bites/292/newbie) that tuples are similar to lists, but they are immutable. That makes them more efficient because Python knows once you have created a tuple, it will never change programmatically. Just like lists, you can use indexing to get the individual items stored in the tuple. Let's illustrate this with a simple example:

```python
alice = ('Alice', 30)
print(f"{alice[0]} is {alice[1]} years old.")
```

Output:

```
Alice is 30 years old.
```

When your tuple only has two items, and the code is fresh in your mind, it is not so bad. But as the size of the tuple grows, or it has been months since you have looked at it, it is easy to forget what information is at which index.

# Enter The `namedtuple` Object

`namedtuple` objects solve this problem by assigning a label to each item and allowing you to access the information using dot notation. Let's look at an example.

```python
from collections import namedtuple


Person = namedtuple('Person', ['name', 'age'])
alice = Person('Alice', 30)

print(f"{alice.name} is {alice.age} years old.")
```

Output:
```
Alice is 30 years old.
```

We first import the `namedtuple` object from the `collections` module. Then we have to create the general `namedtuple` object. In this case, we are creating a `Person` object. Notice that we have to use the label `Person` twice. We are assigning the `namedtuple` to the label `Person`, and passing in the string `'Person'` as an argument for the `namedtuple`. The second argument is a list of the attributes we want to define. Then, we used the `Person` object we just created to create the `alice` object. Finally, when we print the string, you can see how the name and age are accessible using `.name` and `.age`. This makes it easier to read and understand what each part of the tuple represents.

You can also print out a `namedtuple` directly and it comes will a built-in `__str__` method defined for you.

```python
from collections import namedtuple


Person = namedtuple('Person', ['name', 'age'])
alice = Person('Alice', 30)

print(alice)
```

Output:
```
Person(name='Alice', age=30)
```

Alternatively, instead of passing in a list, you can pass in a string with the attributes separated by white space.

```python
from collections import namedtuple


Person = namedtuple('Person', 'name age')
alice = Person('Alice', 30)
```

If you choose to do it this way, python essentially uses the `.split` method in the background. It will split the string on the white space and create the individual attributes. Personally I prefer to use a list. It requires typing more characters than the string, but it is easier to read. With the list, I can tell at a glance how many attributes there will be. 

### Alternative `NamedTuple` Object

There is also a completely different way to make a named tuple that is located in a different module. Read through the code below. How is it different from the examples we just saw? Is there anything that is the same?

```python
from typing import NamedTuple


class Persion(NamedTuple):
    name: str
    age: int


alice = Person('Alice', 30)
print(f"{alice.name} is {alice.age}")
```

Output:
```
Alice is 30 years old.
```

When we import the `NamedTuple` from the `typing` module, the object is camel-cased. Then we create something that looks very similar to a [dataclass](https://codechalleng.es/bites/536/newbie). But, instead of using a decorator, you pass `NamedTuple` inside of parentheses after the class name. (Technically, this is called sub-classing. Sub-classing is beyond the scope of the newbies, but it's good to know that it exists.) Next, you define the attributes using type hinting just like you would in a `dataclass`.


### Why Not Just Use `dataclass`

You may be wondering, "If it looks like a `dataclass`, why bother making a `namedtuple`?" Great question! We won't go into all the details here in the newbies, but there are some differences between the two. In general, because `NamedTuple` objects are immutable they are more efficient. They are also iterable by default. (Remember, iterable means you access each component using a `for` loop.) `dataclass` objects are more flexible because they are mutable. You can change attributes if you need to. They are also more powerful because you can define dunder methods. If you don't need all the extra power that comes with a `dataclass`, just use a `NamedTuple`.

### Your Task

You can define your named tuple by importing `namedtuple` from the `collections` module, or importing `NamedTuple` from the `typing` module. The function `make_namedtuple` takes in some information about a bite as its parameters. Use these parameters to build up a named tuple object and return it.


### Steps to Complete

1. **Define the Namedtuple**: Define a `Bite` named tuple with the following attributes:
  - `number`: This will always be an integer.
  - `title`: This will always be a string.
  - `is_complex`: This will always be a boolean value.
 
2. **Build the Bite Inside the Function**:
  - Use the `number` parameter for the `number` attribute.
  - Use the `title` parameter for the `title` attribute.
  - Use the `score` parameter to calculate the `is_complex` attribute. `is_complex` should be `True` if `score` is greater than 5, otherwise `False`.

3. **Return the Namedtuple**: Return the instance of the `Bite` named tuple.

### Example Usage

```
bite = make_namedtuple(1, "first bite", 6)
print(bite)
```

Output:

```
Bite(number=1, title='first bite', is_complex=True)
```

By completing this task, you'll gain a better understanding of how to use named tuples to create more readable and maintainable data structures in Python.

Good luck, and keep on coding!
