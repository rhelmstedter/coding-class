---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): loops, for, dictionaries
Path:
Related Bites: newbie 13, newbie 22
---

# Bite Description

In the last Bite, you looped through a list. In this Bite, you'll loop through a dictionary.

### Looping Over a Dictionary

> 🔮 **Predict first.** What do you think this will print?

```
movie_ratings = {
    "star wars": 8.6,
    "the dark knight": 9.0,
    "rush hour": 7.0,
    "back to the future": 8.5,
}

for movie in movie_ratings:
    print(movie)
```

Output:

```
star wars
the dark knight
rush hour
back to the future
```

A `for` loop over a dictionary walks through the **keys** only. Only half the information came out.

### Looping With `.items()`

Back in Newbie Bite 13, you saw that `.items()` hands back each pair wrapped in parentheses: the key first, then the value.

```
dict_items([('star wars', 8.6), ('the dark knight', 9.0), ('rush hour', 7.0), ('back to the future', 8.5)])
```

Since every item holds two pieces of information, a `for` loop over `.items()` can take **two** variable names, separated by a comma. The first one gets the key and the second one gets the value.

```
for key, value in dictionary.items():
    # do something with both the key and the value
```

```
for movie, rating in movie_ratings.items():
    print(f"{movie.title()} has a rating of {rating}.")
```

Output:

```
Star Wars has a rating of 8.6.
The Dark Knight has a rating of 9.0.
Rush Hour has a rating of 7.0.
Back To The Future has a rating of 8.5.
```

> 🔧 **Modify.** What happens if you swap `movie` and `rating` on the `for` line, but leave the f-string alone?

### Your Task

Complete the `print_cars` function. It takes the `my_cars` dictionary as a parameter, where each key is a car brand and each value is the year.

Use a `for` loop with `.items()` to print each car and its year on its own line, in this format:

```
Nissan: 2004
```

Good luck, and happy coding! 🐍
