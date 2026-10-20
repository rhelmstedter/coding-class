---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): functions, parameters, arguments, input
Path:
Related Bites: newbie 7, newbie 14
---

# Bite Description

In the last Bite, your function did the exact same thing every time. In this Bite, you'll write functions that can work with different values each time they are called.

### Parameters

When Monty builds a function room, he can also set a table just inside the door and put an **empty labeled box** on it. That box is a **parameter**. The box stays empty until you put something inside the parentheses when you call the function.

```python
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Ada")
say_hello("Mr. Helmstedter")
```

So there are two words for two different things:

- `name` on the `def` line is the **parameter**: an empty box, labeled, waiting by the door.
- `"Ada"` at the call is the **argument**: what Monty carries in and drops into that box.

### More Than One Parameter

If you need more than one parameter, separate them with commas. Monty sets out one labeled box for each.

> 🔮 **Predict first.** What will the second call print? Then run it.

```python
def introduce(greeting, name):
    print(f"{greeting}, {name}!")

introduce("Hello", "Ada")
introduce("Ada", "Hello")
```

Python doesn't match your arguments up by meaning. Monty fills the boxes **in order** from left to right. **The order of your arguments matters.**

### Functions That Use `input()`

A function doesn't need a parameter to get information. It can ask the user for it.

```python
def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}!")

greet_user()
```

This function prints the greeting on the screen, but the name stays locked inside the function room. When Monty walks out, nothing comes with him. Think back to the last Bite: how do you get Monty to carry something back out?

### Why Write Functions?

- **Reusability.** Write the code once, call it as many times as you like. Programmers call this **DRY**: Don't Repeat Yourself.
- **Organization.** A function lets you name an idea so you can forget about the details. Once `say_hello()` works, you don't need to remember how it works. You just call it.

### Your Task

The template gives you two objects, `a` and `b`, and two empty functions.

1. Complete `multiply_numbers` so it takes **two** parameters (you'll need to add them yourself) and **returns** the result of multiplying them together. It should work for any two numbers, not just `a` and `b`.
2. Complete `enter_name` so it asks the user to enter their name and **returns** whatever they type.

Remember to indent the body of each function 4 spaces.

Good luck, and happy coding! 🐍
