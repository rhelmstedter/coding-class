---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): dictionaries
Path:
Related Bites:
---

# Bite Description

In this bite, we continue our exploration of Python dictionaries. Dictionaries are powerful data structures that allow you to store key-value pairs.

Normally, you retrieve a value from a dictionary using the key by placing the key inside square brackets `[]` following the dictionary name, as demonstrated in earlier exercises. However, this method has a drawback: if the key does not exist in the dictionary, Python raises a `KeyError`, which can interrupt the flow of your program if not handled properly.

To address this issue, Python dictionaries offer the `.get()` method. This method provides a more forgiving way to retrieve values. When you use `.get()` and the key does not exist, it returns `None` instead of raising an error.

```python
cars = {'Mazda': 2019, 'Nissan': 1997, 'Holden': 2005, 'McLaren': 2011}
print(cars.get('Mazda'))
# Output: 2019

print(cars.get('mazda'))
# Output: None
```

Combining `.get()` with `if` statements lets you handle missing keys with ease. First, check if the return value from `.get()` is None and print out or return a message saying it doesn't exist. Otherwise, print or return your intended message with the information from the dictionary. Below is an example of a function that does just that.

```python
cars = {'Mazda': 2019, 'Nissan': 1997, 'Holden': 2005, 'McLaren': 2011}

def get_car_info(car: str) -> str:
    year = cars.get(car)
    if year is None:
        return f"You don't own a {car}."
    else:
        return f"Your {car} is a {year} model."


print(get_car_info("Mazda"))
# Output: Your Mazda is a 2019 model.

print(get_car_info("Ford"))
# Output: You don't own a Ford.
```

Note, when comparing objects with `None` you should use the `is` keyword instead of `==`. Why you should do this is beyond the scope of the newbies, but if you are interested in learning more a quick google search yields a ton of information.

Or, you can specify a default return value as a second argument, which is returned if the key is not found.

```python
cars = {'Mazda': 2019, 'Nissan': 1997, 'Holden': 2005, 'McLaren': 2011}

print(cars.get("Ford", "Car does not exist."))
#Output: Car does not exist.
```

Using `.get()` makes your dictionary interactions safer and more error-resistant, especially in scenarios where the presence of a key cannot be guaranteed.

This method is particularly useful in data processing and handling user input, where keys might be dynamically specified and may not always be present.

In this exercise, you'll apply what you've learned so far by implementing a function that uses it to safely retrieve scores for ninja belts. You'll handle both cases where the belt exists and where it does not, providing appropriate feedback for each situation.

### Your Task

Complete the `look_up_score_advanced` function that receives a `belt_key` string.

First lookup the `belt_key` in the `ninjabelt_scores` and assign it to the label `score`. Then use an if/else statement.

- If it does not exist return: `"A {belt_key} belt does not exist."`

- If it does exist, return: `"Your {belt_key} belt has a score of {score}."`

This is a form of _string interpolation_.

In computer programming, string interpolation (or variable interpolation, variable substitution, or variable expansion) is the process of evaluating a string literal containing one or more placeholders, yielding a result in which the placeholders are replaced with their corresponding values (source: Wikipedia).

So here you'll "interpolate" or "replace" the belt and score _placeholders_ with the belt and score _variables_ into the given string.

For example, if `belt_key` is "yellow", the retrieved `score` is 20, then `"Your {belt_key} belt has a score of {score}."` will become: `"Your yellow belt has a score of 20."`.
