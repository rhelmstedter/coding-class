---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): imports, modules
Path:
Related Bites:
---

# Bite Description

In this Bite, we are going to continue working with dates in Python, focusing on using the `date` class from the `datetime` module.

This time though, we will focus on the difference between importing the entire module and importing a specific object from the module.

### Importing Modules

There are two common ways to import in Python:

1. **Importing the Entire Module**:

```
import datetime

# Using the datetime.date class
my_date = datetime.date(2023, 5, 24)
```
This is what we have already seen.

2. **Importing a Specific Object from a Module**:

```
from datetime import date

# Using the datetime.date class
my_date = date(2023, 5, 24)
```
This is new. Notice that when we want to create a `datetime.date` object, we don't write the `datetime.` prefix.

### When to Use Each Import Method

#### Importing the Entire Module

This is useful when you need to use multiple objects from the module. It helps to avoid potential naming conflicts in your code. Imagine you have an object `date = "May 24, 2023"` in you code already. Well, if you import the entire module you can still use the `datetime.date` object no problem.

For example:

```python
import datetime

date = "May 24, 2023"
my_date = datetime.date(2023, 5, 24)
print(date)
print(my_date)
```

Output:
```
May 24, 2023
2023-05-24
```

Because we imported the entire module, in order to get to the `date` object we have to use `datetime.date`. That lets us use the label `date` as the name for another object. This approach is called keeps your namespace clean. Here's what it looks like if you just import the `date` object.

```python
from datetime import date

date = "May 24, 2023"
my_date = date(2023, 5, 24)
print(date)
print(my_date)
```

Output:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
```

Using the `from module import object` style of importing lets us access `datetime.date` object using just the label `date`. So then two lines latter when we have `date = "May 24, 2024"`, the label `date` no longer refers to the `datetime.date` object, it is just a string so we get a TypeError.

#### Importing a Specific Object
This is useful when you only need one or a few objects from the module. It can make your code more readable. It can also mean less typing overall since you don't have to write the name of the moudle every time. However, you must ensure that the names of the imported objects do not conflict with existing names in your code.

### A refresher from last exercise: `datetime.date` and `.weekday()`

The `date` class inside the `datetime` module represents a date (year, month, and day). The `.weekday()` method of a `date` object returns the day of the week as an integer, where Monday is 0 and Sunday is 6. When you use the new import style we just learned, you no longer have to include the `datetime` prefix.

For example:
```python
from datetime import date
my_date = date(2023, 5, 24)
print(my_date.weekday())
```
 
Output: 
```
2
```
 
# Your Task
This bite should produce the same exact result as the previous. The goal here is to change the code to use the `from module import object` styling of imports.

1. Import only the `date` class from `datetime`.
2. Create a `date` object for December 19, 2016, the day Pybites was founded. 🎉 Assign this object to a variable called `start_date`.
3. Use the `.weekday()` method on `start_date` to get the day of the week (integer) and store it in a new variable called `day_of_the_week`.
4. Lastly use the `weekdays` dictionary, the we defined for you at the top of the module, to look up the `day_of_the_week` integer variable you just defined and retrieve its corresponding value. Return this retrieved value from the function.

Good luck, and happy coding!
