---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): string interpolation, .format(), strings
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll learn about string interpolation using the `.format()` method in Python. String interpolation allows you to insert variables into strings dynamically, making it a powerful tool for creating flexible and informative text.

### Understanding String Interpolation with `.format()`

We first learned about f-strings all the way back in [Newbie 4](https://codechalleng.es/bites/258/newbie). f-strings allow us to use place objects inside curly braces `{}`. The value of the object inside the curly braces then becomes part of that string. The formal phrase for this is, string interpolation. Since f-strings have been introduced in Python 3.6, they have become the most common method for string interpolation.

However, you will find scenarios where f-strings don't quite work. For these situations, you can use the `.format` method. Let's see how this works, and then we'll explain when to use it. Read through the code below. Think about what this would look like using an f-string. What is same? What is different?


```python
template = "Hello, {}! You have {} new messages."
message = template.format("Alice", 5)
print(message)
```
Output:

```
Hello, Alice! You have 5 new messages.
```

Let's start with the fact that there is no `f` in front of the opening quotation marks. Just like in f-strings, the placeholders are curly braces `{}`. But unlike f-strings, you don't have to pass in any objects. The placeholders in the `template` string are replaced by the arguments passed to the `.format()` method. These must be passed into the `.format` method in the same order as they appear in the original string.
 
One downside to this, is the programmer has to keep track of the order placeholders. The solution to this is to use labels inside the `{}`, and then pass them in as keyword arguments in the `.format` method. Keyword arguments just mean that when you pass in arguments to a function, you include the label with the equal sign. Let's see what that looks like.

```
template = "Hello, {name}! You have {count} new messages."
message = template.format(name="Alice", count=5)
print(message)
```

Output:

```
Hello, Alice! You have 5 new messages.
```

Notice the labels `name` and `count` are not assigned to an object **before** the `template` string is created. The objects don't exist until the `.format` method call. They are passed in as keyword arguments with the form `label=value` for both. So inside of the `.format` function call we type `name="Alice"` and `count=5`. This means, the programmer no longer has to remember the order they appear in the original string, just the placeholder labels.

Even though f-strings is newer and currently the more popular method for string interpolation, the `.format()` method remains an essential tool. It is particularly valuable in scenarios where string templates are defined in advance and values need to be dynamically inserted later, as is the case in this exercise.

### Your Task

You are given a string constant `GREETING` and your task is to complete the `create_greeting` function that takes `name` and `age` as input parameters.

1. Use the `.format()` method to insert the `name` and `age` into the `GREETING` string.
2. The function should return the dynamically created greeting.

### Example Usage

```
print(create_greeting('Alice', 30))
print(create_greeting('Bob', 22))
```

Output:

```
Hello, Alice! You are 30 years old.
Hello, Bob! You are 22 years old.
```

By completing this task, you'll gain a better understanding of string interpolation in Python using the `.format()` method.

Good luck, and happy coding! Only 3 Newbie Bites left to do! 🐍
