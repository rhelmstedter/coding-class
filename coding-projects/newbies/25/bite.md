---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): functions, return
Path:
Related Bites: newbie 14, newbie 24
---

# Bite Description

You've written plenty of functions by now. In this Bite, you'll write a function that **calls another function** you already wrote.

### Functions Calling Functions

You've been doing this all along. Every time you used `print()` or `input()` inside one of your functions, your function was calling another function. Your own functions work exactly the same way.

When Monty is inside a function room, he leaves the door **open** behind him. That means he can still see the main room, and he can walk over to any other function room he needs. When that room hands something back with `return`, he carries it back with him and keeps going.

### Example

> 🔍 **Investigate.** Read the code below line by line. Which function does the math? Which one does the printing?

```
def convert_to_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


def print_report(name, score):
    grade = convert_to_letter_grade(score)
    print(f"{name}'s grade is {grade}.")


print_report("Ada", 95)
# Output: Ada's grade is A.
```

Notice that `convert_to_letter_grade` doesn't print anything. Working out the answer is that function's job. Deciding what to *do* with the answer belongs to whoever called it.

Splitting a program into small functions like this means you only have to write the grade logic once. Any other function that needs a letter grade can just call `convert_to_letter_grade()`.

### Your Task

The template gives you the `convert_to_tuple` function from the last Bite. It's already finished, so don't change it.

Complete the `print_tuples` function so it **calls** `convert_to_tuple` with the `car_brands` list and prints what comes back.

Your output should look like this:

```
('Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda')
```

### Wrapping Up

That's the end of the first half of the Newbie Bites! 🎉 You can now store data, make decisions, repeat yourself with loops, and organize your code into functions. In the second half, we'll start reading errors and tests, so you can figure out what went wrong on your own.

Good luck, and happy coding! 🐍
