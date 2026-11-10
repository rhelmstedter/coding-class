---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): scope
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll learn about variable scope in Python. Understanding variable scope is essential for understanding which objects you have access to and when. Often when you think you have created an object, but you get a `NameError` saying that it doesn't exist, the problem is the scope. Scope can be a difficult concept to wrap your head around, so don't worry if it doesn't make sense at first. If you have the time, I recommend reading the first two articles on [Monty and The White Room](https://www.thepythoncodingstack.com/p/monty-and-the-white-room-python-analogy) by Stephen Gruppetta.

### Understanding Variable Scope

At the most basic level, any time you use the assignment operator directly in your program (in other words, not inside a function) that is called a global variable. Below is a simple program that consists of exactly one line.

```python
message = "Hello from the global scope."
```
`message` is considered a global variable. This means you can use it anywhere in your program. In the following example, we will define a custom function that prints out the `message` object, then call the `message_printer` function. Notice what happens.

```python
message = "Hello from the global scope."


def message_printer():
    print(message)


message_printer()
```

Output:

```
Hello from the global scope.
```

We can print out `message` no problem. Since the `print` function call is happening inside the `message_printer` function, Python first looks for an object labeled message in the `message_printer` function. When Python can't find `message` inside `message_printer`, Python looks in the global scope. It sees `message` in the global scope and prints it out.

If we define `message` inside the function, it is now referred to as a "local variable". Local variables can only be used inside the function where they are assigned. That is called the local scope. So the following will work.
 
```python
def message_printer():
    message = "Hello from the local scope."
    print(message)


message_printer()
```

Output:

```
Hello from the local scope.
```

But if we try to print the local `message` directly from the global scope instead of calling `message_printer`, we get an error. (This example is shown as text, not a code cell, because the `message` you made a few cells up would still exist in this notebook.)

```
def message_printer():
    message = "Hello from the local scope."
    print(message)


print(message)
```

Output:

```
Traceback (most recent call last):
  File "testing.py", line 7, in <module>
    print(message)
NameError: name 'message' is not defined
```

Since `message` is now a local variable, Python can only access it from inside the function. That means the local `message` is only available in the local scope of the `message_printer` function.


### Returning Local Variables into the Global Scope

Sometimes we want to use the local variable later on in our program. But we just learned that local variables can only be used inside the local scope. Clearly we have a problem. What is the solution? The keyword `return`.

We have seen this keyword before, but now we have more context. `return` allows you to pass the local variable back into the main body of your program, or the global scope. There you can do whatever you want with it. So `return` literally returns a value from the local scope to the global scope. Let's see an example.

```python
def message_creator():
    local_message = "This string was assigned to a local variable that will get passed to the global scope."
    return local_message


message = message_creator()
print(message)
```

Output:

```
This string was assigned to a local variable that will get passed to the global scope.
```

Here we defined a function `message_creator`. Inside the function, we assigned a local variable labeled `local_message`. Then we returned the `local_message`. Outside the function, we assigned a global variable `message`. Did you notice that we assigned `message` directly to the function call? Sometimes people refer to this as, "assigning an object the return value of the function". When we print out `message` we see the same value we had for `local_message` because that's what we returned from `message_creator`.

### Shadowing

Shadowing occurs when a local variable in a function has the same name as a global variable, overriding or shadowing the global variable within that function. If you want to be sure you are using the global variable, there exists a `global` keyword. Consider the following example:

```python
message = "Hello from the global scope."

def local_scope_example():
    message = "Hello from the local scope."
    return message

def global_scope_example():
    global message
    return message


print(local_scope_example())
print()
print(global_scope_example())
```

Output:
```
Hello from the local scope.

Hello from the global scope.
```

In this example:

- `message` is a global variable defined outside any function.
- `local_scope_example` defines a local variable named `message` that shadows the global `message` within the function.
- `global_scope_example` uses the `global` keyword to refer to the global `message` within the function. As we saw earlier, in this case the `global` keyword is not strictly necessary. Inside `global_scope_example`, when Python doesn't find `message` it will look for it in the global scope. But it is good to know that the `global` keyword exists.

### Recap

There are mainly three types of variable scopes in Python:

1. **Local Scope**: Variables defined inside a function. These variables are only accessible within the function.
2. **Global Scope**: Variables defined outside any function. These variables are accessible throughout the entire program.
3. **Nonlocal Scope**: Variables defined in the nearest enclosing scope, which is neither local nor global. This is typically used in nested functions, but we won't spend too much time on this in the newbies.

### Your Task

1. **Implement `use_local_object` Function**: This function should return the local `object` string: "This is the local object."
2. **Implement `use_global_object` Function**: This function should return the global `object` string: "This is the global object." Use the `global` keyword inside the function.

By understanding and implementing these functions, you'll gain a better grasp of how variable scope works in Python.

Good luck, and happy coding!
