---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): loops, for, lists
Path:
Related Bites: newbie 9, newbie 20
---

# Bite Description

A `while` loop keeps going until something changes. But a lot of the time, you just want to do something once for every item in a list. In this Bite, you'll use a `for` loop.

### Vocabulary

**Iterable:** anything you can loop over (e.g., a list or a string)

**Iteration:** one execution (think step) of the loop

### `for` Loops

A `for` loop walks through an iterable one item at a time.

```
for variable in iterable:
    indented body of loop
    second line of loop body

rest of program outside of loop
```

Each time through the loop, the next item gets put in the box named on the `for` line. You get to pick that name. Pick one that describes a single item.

### Example

```
foods = ["tacos", "pizza", "hamburgers"]

for food in foods:
    print(f"I like to eat {food}.")
```

Let's break it down.

First time through, `food` holds `"tacos"`:

```
I like to eat tacos.
```

Second time through, `food` holds `"pizza"`:

```
I like to eat tacos.
I like to eat pizza.
```

Third time through, `food` holds `"hamburgers"`:

```
I like to eat tacos.
I like to eat pizza.
I like to eat hamburgers.
```

There are no more items, so the loop is over.

Notice that we never had to count, check a conditional, or increment anything. The `for` loop handles all of that for you.

### Your Task

Complete the `list_cars` function. It takes the `car_brands` list as a parameter. Use a `for` loop to print each car brand on its own line.

Good luck, and happy coding! 🐍
