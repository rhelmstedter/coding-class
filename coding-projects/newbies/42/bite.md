---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): list comprehensions, numbers, integer, isdigit
Path:
Related Bites:
---

# Bite Description

In this Bite, you will learn how to write list comprehensions. List comprehensions are a concise way to create lists in Python. They are more readable and often more efficient than traditional loops.

### Understanding Iterables

Let's start with some formal definitions for things you are already familiar with. In Python, an object is considered an **iterable** if it is able to return individual components one at a time. Any object that is iterable can be used in a for loop. Some examples of iterables are lists, tuples, strings, and dictionaries. If you loop over lists and tuples, you get each individual item. If you loop over a string, you get back each individual character. And if you loop over a dictionary, you can get the keys, the values, or both depending on which method you call (see: [Newbie 13](https://codechalleng.es/bites/274/newbie)).

Read through the code below.

```python
friends = ["Bob", "Julian", "Sherri", "Eric", "AJ", "Heather"]
for friend in friends:
    print(f"{friend} is my friend")
```
Output:
```
Bob is my friend.
Julian is my friend.
Sherri is my friend.
Eric is my friend.
AJ is my friend.
Heather is my friend.
```

Whenever you read a `for` loop in Python, you should think to yourself "for each item in the iterable". In this case, we use the label `friend` to represent each individual item. In the example above, we are looping over the `friends` list (the iterable), and printing out the name of each friend followed by `"is my friend"`. 

Sometimes, instead of printing each item, you might want to create a new list based on items in an existing list. In the following example, we are going to create a new list of friends, but for each friend, we want to save their name lower cased. We can do that using tools we have already covered. Read through the code below.

```python
friends = ["Bob", "Julian", "Sherri", "Eric", "AJ", "Heather"]
lowercased_friends = []
for friend in friends:
    lowercased_friends.append(friend.lower())
print(lowercased_friends)
```
Output:
```
["bob", "julian", "sherri", "eric", "aj", "heather"]
```

We have to create a new empty list so there is something to append to. (Sometimes people use the word initialize instead of create.) Then, we loop over the original `friends` list. For each item in the list, we called the `.lower` method and appended the modified item to the new `lowercased_friends` list. When we print out `lowercased_friends` we can see that all the names are the same, they have just been lowercased.

Let's add a conditional statement! That is a fancy way of saying we will be using an `if` statement. In this example, we will only keep the names that are longer than three letters.

```python
friends = ["Bob", "Julian", "Sherri", "Eric", "AJ", "Heather"]
lowercased_friends = []
for friend in friends:
    if len(friend) > 3:
        lowercased_friends.append(friend.lower())
print(lowercased_friends)
```

Output:
```
["julian", "sherri", "eric", "heather"]
```

See how now there are only 4 items in the list, but they are still lowercased? Any name that was not at least four letters was filtered out with the conditional `if len(friend) > 3`. (Sorry Bob and AJ!)

You can think of this as a recipe with the following steps:

1. **Initialize**: Create a new list.
2. **Loop**: Use a `for` loop with the original list.
3. **Condition (Optional)**: Use an `if` statement to filter out unwanted items.
4. **Manipulate**: Write an expression that modifies the original item 
5. **Append**: Now that you have the modified item you want, add it to the new list.

Depending on how you are modifying the items, or what your conditional is, you might want to switch steps 3 and 4. Or, you might not have a conditional statement at all.

### Enter List Comprehensions

Every thing we just learned works great. However, there is another way, list comprehensions. List comprehensions offer a special syntax that do all the steps above more efficiently and generally in less lines of code. When you write a list comprehension, you end up with a new list based on the modified items of an original iterable.

Let's go back to our friends example and see what it looks like. Read through the original code, and the list comprehension code. Both examples produce the same new list. What do the examples have in common? What is different about them?

**Original**

```python
friends = ["Bob", "Julian", "Sherri", "Eric", "AJ", "Heather"]
lowercased_friends = []
for friend in friends:
    lowercased_friends.append(friend.lower())
```

**List Comprehension Version**

```python
friends = ["Bob", "Julian", "Sherri", "Eric", "AJ", "Heather"]
lowercased_friends = [friend.lower() for friend in friends]
```

Both versions have the same `for` loop and the same expression `friend.lower()` to modify each item. In the list comprehension, you no longer have to use the `.append` method. You just build the comprehension directly inside of square brackets and python understands that you want to add that item to the new list.

We can also add conditional statements to list comprehensions, they just go at the end, but still inside the square brackets.

```python
friends = ["Bob", "Julian", "Sherri", "Eric", "AJ", "Heather"]
lowercased_friends = [friend.lower() for friend in friends if len(friend) > 3]
print(lowercased_friends)
```
Output:
```
["julian", "sherri", "eric", "heather"]
```

### General Syntax

List comprehensions can be broken down into the following components:

1. **Expression**: This is the modified item that you want. It is automatically added to the new list.
2. **Item Variable**: This variable represents each item in the original list as it is processed and should be used in the expression.
3. **Iterable**: This is the original iterable from which items are taken.
4. **Condition (Optional)**: An `if` statement that determines whether each item should be included in the new list.


The general syntax for a list comprehension is:

```python
[expression for item in iterable if condition]
```
When I write list comprehensions I like to use the sentence frame, "I want _____ for each _____ in _____ if _____." With the friends example, the sentence frame I think about when is, "**I want** the friend lower cased **for each** friend **in** the friends list **if** the friend has at least 4 letters."

#### Using List Comprehensions Only as a Filter

In certain cases, you don't want to modify the original items, you just want to filter some of them out. Let's say we don't want to lower case our friends names, we only want to filter out names shorter than four letters. My sentence frame now is, "**I want** the friend **for each** friend **in** the friends list **if** the friend has at lest four letters." That sentence becomes this Python code:

```python
friends = ["Bob", "Julian", "Sherri", "Eric", "AJ", "Heather"]
filtered_friends = [friend for friend in friends if len(friend) > 3]
print(filtered_friends)
```

Output:

```
["Julian", "Sherri", "Eric", "Heather"]
```

#### Another Example

Here is an example in which each number in the original list gets squared.

```python
numbers = [1, 2, 3, 4]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)
```
Output:

```
[1, 4, 9, 16]
```

Let's try it as a list comprehension. My sentence frame is, "**I want** the number squared **for each** number **in** the numbers list." That sentence becomes the Python code: 

```python
numbers = [1, 2, 3, 4]
squares = [number ** 2 for number in numbers]
print(squares)
```
Output:

```
[1, 4, 9, 16]
```

The expression on the left (`number ** 2`) is applied to each item in `numbers` and the result is added to `squares`. Did you notice that this list comprehension didn't have an `if`? Remember, the conditional statement is optional.

#### Another Example With A Condition

You can also add a filter condition to include only certain items. For example, to include only even numbers:

```python
numbers = [1, 2, 3, 4]
squares = [number ** 2 for number in numbers if number % 2 == 0]
print(squares)
```
Output:

```
[4, 16]
```

In Python, the `%` symbol is the modulo operator. The modulo operator does division, but instead of returning the answer, it returns the remainder. So if we take the number, divide by 2 and get a remainder of 0, we know the number is even.

### Your Task

Complete the function `filter_out_negative_numbers` to filter out numbers that are 0 or less using a list comprehension.

### Example Usage

```
numbers = [-1, 2, 3, -4, 0, 5]
print(filter_out_negative_numbers(numbers))
```

Output:
```
[2, 3, 5]
```
By completing this task, you'll gain a better understanding of how to use list comprehensions for filtering and transforming lists in Python.

Good luck, and happy coding!
