---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): datetime, imports, modules
Path:
Related Bites:
---

# Bite Description

In this bite, we are going to explore the `datetime` module in Python. Inside of `datetime` is a class called `date`. We will talk about classes in Python in later bites, but for now, just think of the `datetime.date` class as a special type of object for dealing with dates. The `datetime` module is essential for working with dates (and times) and can help you do cool things such as determining the day of the week you were born. 

### Understanding `datetime.date`

The `datetime.date` class represents a date (year, month, and day) based on the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar). You can create a `date` object by importing `datetime`, calling `datetime.date` and passing in the year, month, and day as arguments.

For example:

```python
import datetime

my_date = datetime.date(2023, 5, 24)
print(my_date)
```

Output: 
```
2023-05-24
```

When you print a `datetime.date` object, it gives you the year, the month, and the day each separated by dashes.

Sometimes it is useful to just get certain parts of the `datetime.date` object. For example, maybe in one part of your project you are only interested in the year of the object not the month or day. You can access that information using the `.year` attribute.

For example,

```python
import datetime

my_date = datetime.date(2023, 5, 24)
print(my_date.year)
```

Output: 

```
2023
```

You can think of an attribute like a character trait for an object. Each `datetime.date` object has attributes of `year`, `month`, and `day`. You access them by writing the name of the object, followed by a dot and then the attribute you are interested in. It looks the same as calling a method, but without the trailing parenthesis.

### Understanding the `.weekday()` Method

There are methods for `datetime.date` objects too. The `.weekday()` method of a date object returns the day of the week as an integer, where Monday is 0 and Sunday is 6. This is useful for quickly finding out which day of the week a specific date falls on.

For example:

```python
import datetime

my_date = datetime.date(2023, 5, 24)
print(my_date.weekday())
```

Output:

```
2
```


### Using these Tools

Now, let's use these tools to determine the day of the week for a specific date. We will create a function that returns the name of the day that Pybites was founded: December 19, 2016.

# Your Task

1. Import the `datetime` module at the top of the module (imports should almost always go at the top of the module).
2. Create a `datetime.date` object for December 19, 2016, the day Pybites was founded. 🎉 Assign this object to a variable called `start_date`.
3. Use the `.weekday()` method on `start_date` to get the day of the week (integer) and store it in a new variable called `day_of_the_week`.
4. Lastly use the `weekdays` dictionary, the we defined for you at the top of the module, to look up the `day_of_the_week` integer variable you just defined and retrieve its corresponding value (we've covered this in Newbie Bite 29). Return this retrieved value from the function.

Good luck, and happy coding!
