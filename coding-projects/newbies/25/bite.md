---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): functions, return, dictionaries
Path:
Related Bites: newbie 15, newbie 23
---

# Bite Description

You've written plenty of functions by now. In this Bite, you'll write a function that **calls another function**.

### Functions Calling Functions

You've been doing this all along. Every time you used `print()` or `input()` inside one of your functions, your function was calling another function. Your own functions work exactly the same way.

When Monty is inside a function room, he leaves the door **open** behind him. That means he can still see the main room, and he can walk over to any other function room he needs. When that room hands something back with `return`, he carries it back with him and keeps going.

### Example

> 🔍 **Investigate.** Read the code below line by line. Which function decides how the weather feels? Which one does the printing?

```python
def describe_temperature(degrees):
    if degrees >= 85:
        return "hot"
    elif degrees >= 60:
        return "nice"
    else:
        return "cold"


def print_forecast(day, temperature):
    feeling = describe_temperature(temperature)
    print(f"{day} will be {feeling}.")


print_forecast("Monday", 91)
print_forecast("Tuesday", 72)
```

Notice that `describe_temperature` doesn't print anything. Working out the answer is that function's job. Deciding what to *do* with the answer belongs to whoever called it.

Also notice the names. Inside `print_forecast`, the number lives in a box labeled `temperature`. When it calls `describe_temperature(temperature)`, Monty carries that value into the other room and drops it in a box labeled `degrees`. The labels don't have to match. A parameter is just the name a function uses for whatever value gets handed to it.

> 🔧 **Modify.** Add a call to `print_forecast` for Wednesday that comes out `cold`.

Splitting a program into small functions like this means you only write the temperature logic once. Any other function that needs it can just call `describe_temperature()`.

### Your Task

The template gives you a finished `get_letter_grade` function. It takes a score and returns a letter grade. Don't change it.

Complete the `print_report_card` function. It takes **one** parameter: a dictionary where each key is a student's name and each value is their score. Add the parameter yourself, and pick a name for it.

For each student, `print_report_card` should **call** `get_letter_grade` to get their letter grade, then print the name and grade on its own line, like this:

```
Ada: A
Grace: C
```

The tests will call your function with a few different dictionaries.

### Wrapping Up

That's the end of the first half of the Newbie Bites! 🎉 You can now store data, make decisions, repeat yourself with loops, and organize your code into functions. In the second half, we'll start reading errors and tests, so you can figure out what went wrong on your own.

Good luck, and happy coding! 🐍
