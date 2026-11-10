---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): dictionaries
Path:
Related Bites: newbie 13
---

# Bite Description

In this bite, we are going to revisit dictionaries. The point of a dictionary is that you have two pieces of information for each item, the `key` and the `value`.

In a Python dictionary, if you look up the key, it will return the value. You do this by typing the name of the dictionary followed by square brackets `[]`. Inside the square brackets you type the `key`. Below is a `cars` dictionary.

Let's see how a look up works:

```
>>> cars = {'Mazda': 2019, 'Nissan': 1997, 'Holden': 2005, 'McLaren': 2011}
>>> cars['Mazda']
2019
```

This would be the case for all items in the dictionary. For example, if you typed `cars["Nissan"]` you would get back `1997`. Remember, you always look up the `key` and get back the `value`.

Now, what if you try to look up a `key` that doesn't exist? Well, the default behavior of a dictionary lookup using `[]` raises a `KeyError`.

Let's see what that looks like:

```
>>> cars = {'Mazda': 2019, 'Nissan': 1997, 'Holden': 2005, 'McLaren': 2011}
>>> cars['mazda']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'mazda'
```

If you look carefully, you'll notice the "m" in "mazda" wasn't capitalized. So to python the `key` "mazda" doesn't exist. This will raise an error and cause your program to crash.

### Your Task

In this Bite you're going to use a key to retrieve a value from a dictionary and embed both this key + value in an f-string. We covered f-strings back in Newbie Bite 4.

First look up the score for the `belt_key` key. This variable gets passed into the function. The dictionary is defined at the top of the module and is called `ninjabelt_scores`.

Store the value you retrieve from this dictionary to a variable called `score`.

Next make an f-string that embeds both the `belt_key` and `score` variables like this: `Your BELT belt has a score of SCORE.` (don't forget the period at the end). Assign this f-string to a variable called `message`.

So if the `belt_key` is "white" and `score` = 10, the `message` variable would hold "Your white belt has a score of 10."

Lastly return this `message` variable from the function.
