---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): list comprehensions, string module, string manipulation
Path:
Related Bites:
---

# Bite Description

In this exercise, you'll practice writing another list comprehension (a robust tool for creating lists from other iterables and one of our favorite Python features!)

But we'll add another concept to the mix: the `string` module, which provides a series of string constants that can be useful in various string manipulation tasks.


### The `string` Module

There maybe times when you need to get all of the letters of the alphabet or perhaps all of the possible punctuation symbols. One option would be to type them all out and assign the string to a constant. Here is an example of that.
 
```python
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
```

That works, but as programmers we want to work smarter not harder. The `string` module in Python includes various sets of characters so you don't have to type them out each time you want them. Below is an example.

```python
import string

print(string.ascii_lowercase)
```

Output:
```
abcdefghijklmnopqrstuvwxyz
```

Just as we have seen before, we import the module, and then access the object using dot notation. In this case, we used `string.ascii_lowercase`.

Now, you might be wondering what the heck `ascii` is. It is an acronym for American Standard Code for Information Interchange ([ASCII](https://en.wikipedia.org/wiki/ASCII#:~:text=ASCII%20(%2Fˈæsk,telecommunications%20equipment%2C%20and%20other%20devices.)). ASCII codes are how text characters are stored by computers. We won't go into all the details here in the newbies bites, but you should know that ASCII codes represent the [English alphabet](https://en.wikipedia.org/wiki/English_alphabet) letters A through Z (uppercase and lowercase), the digits 0 through 9, and some punctuation characters. Sometimes people refer to this as plain text, but there is a lot more to it. (Check out this excellent talk on [Plain Text](https://youtu.be/4mRxIgu9R70?si=t4aA05k5Sz2ZME2L) by Dylan Beattie for more information.)

Let's see a couple more examples of objects available in the `string` module.

```python
import string

print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.punctuation)
```

Output:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

In the snippet above, we see all the uppercase letters, both the lowercase and uppercase letters combined, and a set of punctuation characters. If you want to see all of the available string constants, the are available in the [Python Docs](https://docs.python.org/3/library/string.html#string-constants).


### The `.join` Method

`.join` is another string method. You can think of `.join` almost like the opposite of `.split`. Where `.split` takes a string and splits it into items in a list, `.join` takes strings in an iterable and joins them together with a given string. Let's see an example.
 
```python
words = ["These", "are", "words"]
joined_words = " ".join(words)
print(joined_words)
```

Output:

```
These are words
```

`.join` works by calling it on the string that will be used to concatenate the items together. Then the iterable is passed in the parenthesis. So in the code snippet above, we used a space character (`" "`) to join together the words from the list `words`. You can use whatever character you want though. Here is the same snippet, but this time the words are joined with a pipe character (`"|"`).


```python
words = ["These", "are", "words"]
joined_words = "|".join(words)
print(joined_words)
```

Output:

```
These|are|words
```

In the examples above, the strings inside the `words` list are the individual items that will be joined together. Remember though, strings are also iterable in Python. If you pass in a string directly to `.join` the individual characters are the items that will be joined together.


```python
import string


letters_joined_by_commas = ",".join(string.ascii_letters)
print(string.ascii_letters)
print(letters_joined_by_commas)
```

Output:

```
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
```

### Your Task

You're tasked with completing the `get_letters_from_string` function. This function should:

1. Iterate over the `text` parameter and filter out any character that is not a letter.
2. Return a string of just the letters separated by a hyphen (`-`).



### Example Usage

```python
print(get_letters_from_string("123abcABC!"))
print(get_letters_from_string("Hello World 2024 "))
print(get_letters_from_string("@#Sky^Is.Blue@"))
```

Output:

```
a-b-c-A-B-C
H-e-l-l-o-W-o-r-l-d
S-k-y-I-s-B-l-u-e
```


By completing this task, you'll gain a better understanding of `.join` and how to use the `string` module to manipulate strings efficiently in Python.

Good luck, hope you're having fun!
