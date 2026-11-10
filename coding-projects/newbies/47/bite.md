---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): collections, in operator, lists
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll learn how to use the `in` operator to check for the presence of multiple items in a collection. The `in` operator is a powerful tool in Python for checking membership within iterables.

### Understanding the `in` Operator

`in` is a Python keyword.  We have already been using the `in` keyword in `for` loops, but we can use it as a stand alone operator as well. The `in` operator is used to check if an item exists within an object. The `in` operator works on all iterables such as lists, tuples, and strings. (It also works on a few other objects that we haven't learned about yet.)

The general syntax for using the `in` operator is `item in iterable`. It returns `True` if the item is found, and `False` otherwise. Below is list of strings. We can check if a given string is in the list.

```python
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)
```
Output:

```
True
```

In this example, `'apple' in fruits` returns `True` because `'apple'` is in the `fruits` list. What do you think will happen if we try `"a" in fruits`? Take a moment and guess before reading the code.

```python
fruits = ['apple', 'banana', 'cherry']
print('a' in fruits)
```

Output:

```
False
```

Did that surprise you? Let's think about what's happening here. There are three items in the list `fruits`: `"apple"`, `"banana"`, and `"cherry"`. In the second code snippet, we are essentially asking if the string `"a"` is an item in the list. Even though the character `"a"` exists in one of the items, it is not its own item in the list. So, the `in` operator returns `False`.

If you want to check if certain characters are in a string, then you would need to use the string with the `in` operator.
 
```python
print("a" in "apple")
```

Output:
```
True
```

We can also check other types of items such as numbers.

```python
scores = [75, 99, 60, 82, 79, 84, 87, 74, 71, 60]
print(99 in scores)
print(15 in scores)
```
Output:
```
True
False
```

Here, `99` is an item in the `scores` list so the `in` operator returns `True`. In the second check, `15` is not in the `scores` list so it returns `False`. 

Depending on your needs, you might want to know if an item is **not** in an iterable. You can use the `in` operator with the `not` keyword. Let's say a score of `100` represents a perfect score. It's possible to do something like this:

```python
scores = [75, 99, 60, 82, 79, 84, 87, 74, 71, 60]
if 100 not in scores:
    print("Did not find a perfect score.")
```

Output:

```
Did not find a perfect score.
```

In this code snippet, the item `100` is not in the list. If we had written `100 in scores`, it would return `False`. So, the Python expression `100 not in scores` evaluates to `True`. The fancy name for this is logical negation. But, all that is happening is the `not` keyword returns the opposite boolean.

### Your Task

Your task is to complete the `count_matching_items` function. This function takes two parameters:
- `collection`: A list of unique items.
- `items`: A list of items to check for membership in the `collection`.

The goal is to count how many items from the `items` list are present in the `collection` list.

### Steps to Complete

1. Use a variable to store the count of matching items.
2. Use a `for` loop to iterate over each item in the `items` list passed into the function.
3. In the loop check if the `item` is in the `collection` (also passed into the function) using the `in` operator. In that case, increment the count.
4. Return the count of matching items.

Although there are other, more efficient, methods to solve this problem, we want you to practice using the `in` operator to check for membership in this Bite.


### Example Usage

```
collection = [1, 2, 3, 4, 5]
items = [3, 4]
print(count_matching_items(collection, items))
```

Output:

```
2
```

```
collection = ['apple', 'banana', 'cherry']
items = ['banana', 'cherry']
print(count_matching_items(collection, items))
```

Output:

```
2
```

```
collection = ['apple', 'banana', 'cherry']
items = ['date', 'fig']
print(count_matching_items(collection, items))
```

Output:

```
0
```

By completing this task, you'll gain a better understanding of how to use the `in` operator for checking membership and counting matches in a collection.

Good luck, and happy coding!
