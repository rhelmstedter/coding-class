---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): constants, math
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll learn about assigning and using constants in Python. Constants are values that do not change throughout the execution of a program. They are used to make your code more readable and maintainable.

### Understanding Constants

Imagine that you are writing a program that involves a [standard 52-card deck](https://en.wikipedia.org/wiki/Standard_52-card_deck). You will probably use the number `52` throughout the program. This would be a good candidate for a constant. Instead of using the number `52` directly, you would assign it to a descriptive label. That way when you read your code you know exactly what that number `52` represents. Here is an example:
  
```python
DECK_LENGTH = 52
```
Constants can be any data type, but numbers are the most common. Numerical objects that do not change and have not been assigned labels are sometimes referred to as "magic numbers". There is nothing magic about them, it's just a name that some people give them.

In Python, constants are conventionally defined underneath the imports at the top of a module, and are written in uppercase letters with underscores separating words (see the [PEP 8 style guide](https://peps.python.org/pep-0008/#constants) for more information). If you choose to define constants later in the module or not use all capital letters, your program will still work. That being said, it's a good idea to stick to the convention.

### Why Use Constants?

1. **Readability**: Constants make your code easier to read and understand. Instead of having numbers sprinkled throughout your code, you can use descriptive names.
2. **Maintainability**: If a value needs to be updated, you only need to change it in one place, which reduces the chance of errors.
3. **Avoid Hard-coding**: Constants prevent hard-coding values directly in your logic, which can lead to bugs and inconsistencies.

### Example

Let's pretend you are working a job where you get paid hourly. For the first `40` hours, you get paid a certain rate. For any time over the `40` hours, your rate is increased. Read through the following code and see if you can make sense of it.

```python
def calc_weekly_pay(hours: float) -> float:
    if hours > 40:
        overtime = hours - 40
        hours = 40
    else:
        overtime = 0
    pay = 15 * hours + 15 * 1.5 * overtime
    return pay
```

This code works as follows:

1. If the hours you worked is more than 40, calculate the `overtime` hours and reassign `hours` to `40`.
2. Otherwise, assign the label `overtime` the value `0` and leave `hours` alone. 
3. Calculate the pay and return it.

Let's refactor this code to use constants. 

```python
FULL_TIME_HOURS = 40
HOURLY_RATE = 15
OVERTIME_RATE = 1.5 * HOURLY_RATE

def calc_weekly_pay(hours: float) -> float:
    if hours > FULL_TIME_HOURS:
        overtime = hours - FULL_TIME_HOURS
        hours = FULL_TIME_HOURS
    else:
        overtime = 0
    pay = HOURLY_RATE * hours + OVERTIME_RATE * overtime
    return pay
```

At first glance, this may just seem like more work. We have added three lines of code and made many of the individual lines longer. However, there are still some advantages to this extra initial work.

First, every numerical value (that does not change) now has a label. Just by reading the code we know that the number `40` is the number of hours considered full time. We also know that the `15` represents a dollar amount because it is an hourly rate.

Next, in the first version the pay calculation was `15 * hours + 15 * 1.5 * overtime`. Could you tell what each of those numbers meant immediately? In the second version, the pay calculation becomes `HOURLY_RATE * hours + OVERTIME_RATE * overtime`. It is now clear we are multiplying the hours worked by the hourly rate and multiplying the overtime hours by the overtime rate.

Finally, imagine in the future, you get a raise and your hourly rate changes. In the first version, you would have to scan through your code and change every line where there is a `15`. In the second version, you only have to change it in one place right at the top of your module.

### Your Task

Remember the `Circle` class we first created back in Newbie Bite 37? This is a perfect example of where we can use constants. Instead of using `3.14159` directly in the class, define it as a constant.

#### Steps to Complete

1. **Assign a Constant**: Update the class to assign a constant called `PI` with a value of `3.14159`.
2. **Refactor the class to use the constant**: Anywhere the class has 3.14159 replace it with the `PI` constant.

By completing this task, you'll gain a better understanding of how to define and use constants in Python to make your code more readable and maintainable.

Good luck, and happy coding!
