---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): dictionaries, data structures
Path:
Related Bites: newbie 9
---

# Bite Description

In this Bite, you'll meet the dictionary, one of the most useful data structures in Python.

### Why Not Just Use Two Lists?

> 🔍 **Investigate.** Read the code below. Whose score is `94`? How do you know?

```
names = ["Ada", "Grace", "Alan"]
scores = [88, 94, 71]
```

Two lists can work, but only if you keep them in the same order. Nothing inside the `scores` box says whose score is whose. If someone adds a name and forgets the score, every score after that lines up with the wrong person.

### Dictionaries

A **dictionary** holds **two** pieces of information per item: a **key** and a **value**. Together they are called a **key-value pair**.

A dictionary is also one box on the shelf with one label on the outside. The difference is inside. Every item in the box has its own small label stuck to it. That small label is the **key**. The thing it is stuck to is the **value**. Python doesn't count slots to find something. It reads the small labels.

Write a dictionary with curly braces `{}`. Put a colon between each key and its value, and a comma between pairs.

```
label = {key: value, key: value, key: value}
```

### Example

```
scores = {"Ada": 88, "Grace": 94, "Alan": 71}

print(scores)
# Output: {'Ada': 88, 'Grace': 94, 'Alan': 71}

print(type(scores))
# Output: <class 'dict'>
```

|                                  | List                  | Dictionary                     |
|:---------------------------------|:----------------------|:-------------------------------|
| Brackets                         | `[ ]`                 | `{ }`                          |
| Pieces of information per item   | one (the item)        | two (the key and the value)    |
| Look up an item by               | its index (position)  | its key                        |

### Your Task

Each ninja belt was worth a score. Create a dictionary called `ninjabelt_scores` where each key is a belt color and each value is its score:

| Belt   | Score |
|--------|:-----:|
| white  | 10    |
| yellow | 20    |
| orange | 30    |
| green  | 40    |
| blue   | 50    |
| brown  | 60    |
| black  | 70    |

The template includes the `ninjabelts` list for reference. Keep the belt names lowercase.

Good luck, and happy coding! 🐍
