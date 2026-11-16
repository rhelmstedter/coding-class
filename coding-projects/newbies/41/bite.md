---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): strings, string manipulation, strip, slicing, split, lowercase, lists
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll learn more about manipulating strings in Python. String manipulation is a fundamental skill in programming, allowing you to process and transform text data effectively.

## String Manipulations

We have talked about string methods before, but in this bite we are taking it to the next level. Let's break down some common manipulations programmers perform, the string methods required to do so, and explain why and when you would want to do so.

Before we jump into examples, it is important to know that strings in Python are immutable. In this context, "immutable" means that once an object has been made and stored in memory by Python, you cannot change it programmatically. As a result, every time you call a string method, a new string is created.

### Converting to lowercase

We have talked about the `.lower` method before, so let's use it to explore the idea of immutability.

```python
text = "Learning Python is fun and engaging!"
lowercase_text = text.lower()
print(text) 
print(lowercase_text)
```

Output:

```
Learning Python is fun and engaging!
learning python is fun and engaging!
```

We first created an object labeled `text` that has the value `"Learning Python is fun and engaging!"`. Then, we called the `.lower` method. This returns a new copy of `text` with all lowercase letters, and assigns the lowercased version to the label `lowercase_text`. We still have access to the original `text` object.

If we don't need the original string, we can reuse the label `text`. That code would look like this:

```python
text = "Learning Python is fun and engaging!"
text = text.lower()
print(text) 
```

Output:

```
learning python is fun and engaging!
```

The original string `"Learning Python is fun and engaging!"` still exists in memory. However, there is no label associated with it anymore because we reassigned the label `text` to the lowercased version.

#### Why?

Now, the question is, why would you want a string with only lowercase letters? Well, consider the following code:

```python
confirm = input("Do you want to continue?")
if confirm == "yes":
    print("Let's move on")
else:
    print("OK, quitting now.")
```

This code asks the user to enter some text and stores it with the label `confirm`. If the value of `confirm` is equal to `"yes"`, the program moves on. Otherwise, the program quits. 

What happens if the user types in `Yes`? In Python, the string `"yes"` and the string `"Yes"` are not equivalent, so the code will display `OK, quitting now.` even though the user wanted to continue.

One way to address this issue is to use the `.lower` method to convert the value of `confirm` to all lowercase no matter what the user types in.

You have two options on where to call `.lower`. Read through the two examples below: What is the same? What is different?

**Option 1**
```python
confirm = input("Do you want to continue?")
if confirm.lower() == "yes":
    print("Let's move on")
else:
    print("OK, quitting now.")
```

**Option 2**
```python
confirm = input("Do you want to continue?").lower()
if confirm == "yes":
    print("Let's move on")
else:
    print("OK, quitting now.")
```

In the first option, `.lower` is called during the `if` statement. In the second option, `.lower` is called on the return value from `input`. Since `input` always returns a string, you can call string methods directly. Generally, I prefer option 2, but it is up to you.

### Removing punctuation

Let's move on to a new method: `.strip`. Can you guess what `.strip` does just by its name? It strips off characters from the beginning and end of strings. To use it, call `.strip` and place the characters you want to remove inside the parentheses. In the following example, we want to strip off the `"x"` characters from the beginning and end of the string.

```python
text = "xxxxhelloxxxx"
stripped_text = text.strip("x")
print(stripped_text)
```

Output:

```
hello
```

It doesn't matter how many of them there are. But, it does matter that they are at the beginning and end of the string. Look closely at the following example.

```python
text = "xxxxhelloxxxx!"
stripped_text = text.strip("x")
print(stripped_text)
```

Output:

```
helloxxxx!
```

That `"!"` at the end of the string caused only the `"x"` characters at the beginning to be stripped. If you want, you can add multiple characters inside the parentheses to remove both. 

```python
text = "xxxxhelloxxxx!"
stripped_text = text.strip("!x")
print(stripped_text)
```

Output:

```
hello
```

In addition to `.strip`, there are two other similar methods: `.lstrip` and `.rstrip`. Look at the examples below. Can you figure out what is happening?

**`.lstrip` Example**

```python
text = "xxxxhelloxxxx"
stripped_text = text.lstrip("x")
print(stripped_text)
```

Output:

```
helloxxxx
```
**`.rstrip` Example**

```python
text = "xxxxhelloxxxx"
stripped_text = text.rstrip("x")
print(stripped_text)
```

Output:

```
xxxxhello
```

`.lstrip` is short for "left strip". So, it only strips characters from the left side, or the beginning, of the string. `.rstrip` is short for "right strip". So, it only strips characters from the right side, or the end, of the string.

#### Why?

Now, why would you want to use this? Remember our confirmation example from above? We already addressed the issue when a user types capitals, but what if you have a really excited user who types `"YES!"`. Even after converting to lowercase, the strings "yes" and "yes!" will not be equal. So let's add a line to deal with possible punctuation.

```python
confirm = input("Do you want to continue?").lower()
confirm = confirm.strip(".?!")
if confirm == "yes":
    print("Let's move on")
else:
    print("OK, quitting now.")
```

Very nice! Now our code can handle variability in both casing and punctuation.

### Chaining

Since each string method returns a new copy of the string you can chain together multiple methods. Using our confirmation example still, read through this version.

```python
confirm = input("Do you want to continue?").lower().strip(".?!")
if confirm == "yes":
    print("Let's move on")
else:
    print("OK, quitting now.")
```

We call this chaining because methods are called directly after each other like links in a chain. Chaining methods together is like reading a recipe from left to right. Step 1: Get the input from the user. Step 2: Lowercase it. Step 3: Strip away punctuation characters. The final result is what gets stored with the label `confirm`.

Whenever you are working with methods that return a new copy of an object, you can use this type of chaining.

### Extracting Specific Words

We learned about the `.split` method back in Newbie Bite 31. Let's take it up a notch. This time, instead of splitting right away, let's strip off some punctuation first, and then get the individual words. 

```python
text = "Learning Python is fun and engaging!"
words = text.rstrip("!").split()
print(words)
```

Output:

```
['Learning', 'Python', 'is', 'fun', 'and', 'engaging']
```

This is another example of chaining methods together. Did you notice that we used `.rstrip` since the only punctuation was at the end of the sentence. We could have also used `.strip` here. Now, we have all the words without any of the punctuation on that final word.

### Why?

Why would you want to do this? Perhaps you are interested in the length of the individual words. Using list indexing we learned about in Newbie Bite 10 and the `len` function we learned in Newbie Bite 31 we can extract individual words and calculate their lengths.

```python
text = "Learning Python is fun and engaging!"
words = text.rstrip("!").split()

second_word = words[1]
last_word = words[-1]
print(f"{second_word} has {len(second_word)} letters.")
print(f"{last_word} has {len(last_word)} letters.")
```

Output:

```
Python has 6 letters.
engaging has 8 letters.
```

### Your Task

Your task is to create a function `extract_words` that performs string manipulations and returns a formatted string.

### Steps to Complete

1. **Convert to Lowercase**: Use the `.lower` method to convert the text to lowercase.
2. **Remove Trailing Punctuation**: Use the `.rstrip` method to remove any trailing ".", "!", or "?" from the text.
3. **Split into Words**: Use the `.split` method to split the text into individual words.
4. **Extract and Concatenate Words**: Extract the first and last words from the list and concatenate them with a hyphen.

### Example Usage

```
text = "Today it's a sunny day in LA!"
print(extract_words(text))
```

Output: 

```
today-la
```

By completing this task, you'll gain a better understanding of basic string manipulations in Python.

Good luck, and happy coding!
