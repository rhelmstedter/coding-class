---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): counter, documentation, collections, reading docs
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll practice reading and using Python's official documentation. This is an essential skill for any developer, as it allows you to leverage the full power of the language and its libraries.

## Working on Your Own

It is impossible to learn and retain everything that Python can do. Reading the documentation, asking good questions, and learning how to craft search engine prompts are crucial skills for programmers. Both help you understand how to use libraries and functions correctly, troubleshoot issues, and discover new features.

### Reading the Docs

It is important to have good resources where you can look up information. Some of the best information on Python comes are the [Python Docs](https://docs.python.org/3/) from [python.org](https://www.python.org). The only downside is that some of the documentation can be difficult to understand for people who are new to programming in general. Like everything else, the more you engage in [deliberate practice](https://hbr.org/2007/07/the-making-of-an-expert), the better you will get a reading and understanding documentation.

### Asking Good Questions

A great website for asking questions is [StackOverflow](https://stackoverflow.com). In case you are not familiar, Stack Overflow is a website were people ask questions related to programming, and the community answers questions. The answers are voted on by the community. Generally, good and correct answers get upvoted. Often times, people have already asked the same question you have. You can search through the site and utilize the discussions others have already had.

Even if you choose to not use Stack Overflow directly, it is well worth your time to read their article on [How do I ask a good question?](https://stackoverflow.com/help/how-to-ask) or the blog post [Writing The Perfect Question](https://codeblog.jonskeet.uk/2010/08/29/writing-the-perfect-question/) by Jon Skeet.

### Crafting a Good Search Engine Prompt

As you continue your Python journey, search engines like Google become invaluable. Learning how to craft a good search prompt makes it that much easier to find solutions for the problems you are trying to solve.

The first tip is to make sure you are including import words that will narrow down search results. For example, the prompt `format strings` might include formatting strings in other programming languages. The prompt `format strings python` would be a better choice for our purposes.

Second, the top search engines offer various operators that give more control over search results. The first one we will discuss is quotes. If your first attempt didn't provide exactly what you are looking for, you can put parts of your search prompt in quotes. The prompt `python newbies challenges` includes lots of results that include the word *beginner*. While the prompt `python "newbies" challenges` returns results that include the phrase *newbies*.

The second operator we will discuss is the `site` operator. If you want to search a given site, for example Stack Overflow, from your search engine you can try a prompt like `site:stackoverflow.com format strings python`. All of the results will be from stackoverflow.com. If you want to exclude a site, place a hypen (`-`) in front. So, the prompt `-site:stackoverflow.com format strings python` will return results from all sites except stackoverflow.com

Finally, when you are dealing with errors you have never seen before, it can be helpful copy and paste them into a search engine. But copying and pasting the entire error message is not so helpful because it will contain information the only applies to you. Consider this code we first saw back in [Newbie 45](https://codechalleng.es/bites/542/newbie). The name of the file is `errors_example.py` and the contents of the file look like this:

```python
def divide(a, b):
    result = a / b
    return result


print(divide(10, 0))
```

When the file is run, it produces the following error message:

```
Traceback (most recent call last):
  File "/Users/russell/code/pybites-work/tutorials/errors_example.py", line 6, in <mo
dule>
    print(divide(10, 0))
  File "/Users/russell/code/pybites-work/tutorials/errors_example.py", line 2, in div
ide
    result = a / b
ZeroDivisionError: division by zero
```

Some of this information is unique to my situation. I decided to name the file `errors_example.py`. I decided to label the function `divide`. The file path, `"/Users/russell/code/pybites-work/tutorials/errors_example.py"`, is just the location where the file is stored on my computer. Putting all that information into the search engine will not help me figure out how to deal with a `ZeroDivisionError`.

In this case the file name, the path, and label for the function are characteristics that only apply to my program. On the other hand, `ZeroDivisionError` is a general characteristic that anyone trying to divide by zero in Python will encounter. Instead, of copying and pasting everything, work on determining what is unique to your situation, and what information is general. 

### Your Task

You are on your own for this bite. Read the Python documentation on [Counter](https://docs.python.org/3/library/collections.html#collections.Counter), and/or use a search engine to find explanations for how `Counter` objects work in Python. You will use this knowledge to complete two tasks:

**Word Counter**:
1. Split `ZEN_OF_PY` into words.
2. Convert each word to lowercase and strip punctuation.
3. Use `Counter` to count the occurrences of each word.
4. Return the counter.

**Top Three Words**:
1. Use the `word_counter` function to get the word counts.
2. Use `most_common(3)` to get the top three most common words.
3. Return the top three words as a list.

By completing this task, you'll gain experience in reading and utilizing Python documentation, as well as using the `Counter` class for text analysis.

Good luck, and happy coding!
