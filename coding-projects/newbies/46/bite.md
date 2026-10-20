---
Level (beginner, intermediate, advanced): newbie
Tags (2-5): loops, control flow, break, continue
Path:
Related Bites:
---

# Bite Description

In this Bite, you'll learn how to control the flow of a `for` loop using the `break` and `continue` statements. These control flow tools allow you to manage how a loop executes, providing a way to skip iterations or exit the loop based on certain conditions.

### Understanding `break` and `continue`

Python offers two keywords to increase control when working with loops: `break` and `continue`. We have already encountered the `break` keyword when working with `while` loops ([Newbie 20](https://codechalleng.es/bites/286/newbie)). Today, we will look at both keywords in the context of a `for` loop. When used in a `for` loop:
 
- **`break`** stops the loop immediately and moves on with the program. I like to think of it as, we are breaking out of the loop completely.
- **`continue`** skips the rest of the code inside the loop for the current iteration and moves to the next item. I like to think of it as, we are skipping a given item and continuing onto the next item in the iterable. 

Generally, these keywords are paired with an `if` statement to see if some condition was met.

### Simple Example

Below is a code snippet that we will use multiple times.

```python
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

for student in students:
    print(f"Processing {student}")
```

Output:

```
Processing Alice
Processing Bob
Processing David
Processing Charlie
Processing Eve
Processing Frank
```
We are looping over a list of students. For each student in the list, we print that we are processing that student. In an actual program, perhaps you would have a function that does something other than just printing.
 
Now, let's modify that code to use the `continue` keyword.

```python
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

for student in students:
    if student == "Charlie":
        continue
    print(f"Processing {student}")
```

Output:

```
Processing Alice
Processing Bob
Processing David
Processing Eve
Processing Frank
```

As Python gets each item, it checks if `student` is equal to `"Charlie"`. If so, Python continues, meaning it skips the `print` function call for `"Charlie"` and moves to the next item in the list. Notice that there is no `Processing Charlie` line in the output. Also, notice the indentation level here.

Here is the same example, but with `break`.

```
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

for student in students:
    if student == "Charlie":
        break
    print(f"Processing {student}")
```

Output:

```
Processing Alice
Processing Bob
```
Here, we have the some conditional. But instead of continuing when `student` is equal to `"Charlie"`, we exit the loop completely. Notice all the students including and after Charlie are not processed.

# A More Realistic Example

In the examples above, we just printed a statement mimicking that we were processing students in some way. The following example is a little more complex, but also more realistic. There will be some functions and methods that we have not covered yet. Don't worry if you don't understand every detail. Instead, focus on the big picture of what is happening, especially in regards to the `continue` keyword.

Let's say you have a bunch of test scores for a student. If we wanted to compute the [average](https://en.wikipedia.org/wiki/Average), we could do something like this.

```python
scores = [75, 99, 60, 82, 79, 84, 87, 74, 71, 60]
average = sum(scores) / len(scores)
print(f"Average: {average}")
```

Output:

```
Average: 77.1
```
`sum` is a built-in function that takes an iterable and as long as the items are numbers, adds them up. (Remember an iterable is anything that can return individual items. Such as a list, tuple, or dictionary.) So we added up all the scores and divided by the number of items in the list.

At some schools in the U.S., it is a common practice for teachers / professors to drop the lowest test score(s) and compute an adjusted average. The example below does just that. Because we will have to skip over the lowest score(s) in the list, we can no longer just use the `sum` function. Read through the code and try to make sense of it. We will break it down after.

```python
scores = [75, 99, 60, 82, 79, 84, 87, 74, 71, 60]
min_score = min(scores)
count_adjusted_scores = len(scores) - scores.count(min_score)

total_score = 0
for score in scores:
    if score == min_score:
        continue
    total_score = total_score + score

adjusted_average = total_score / count_adjusted_scores

print(f"Adjusted Average: {adjusted_average}")
```
Output:

```
Adjusted Average: 81.375
```

The breakdown:

- We started with a list of ten scores.
- We used the built-in `min` function to calculate the lowest, or minimum, score in the list. Turns out in this example, it's `60`. We assign this value to the label `min_score`.
- We figured out how many times the `min_score` occurred using the list method `.count`. Turns out the `min_score` of `60` happened twice. So when we subtract `scores.count(min_score)` from the length of the original `scores` list we get `8`.
- We initialized `total_score` with a value of `0`.
- We used a `for` loop to get each score from the `scores` list.
- Using an `if` statement, we checked if the current `score` was equal to the `min_score`. If so, the `continue` keyword tells Python to skip the rest of the loop and go get the next item.
- If the current `score` is not equal to the `min_score`, we add the current `score` to the existing `total_score` value and reassign it to the label `total_score`. 
- Finally, we computed the `adjusted_average` and print it out.

Again, don't worry if you don't understand every detail. The important takeaway is that we used the `continue` keyword to skip over the lowest scores so they aren't included in the `total_score` calculation.

It is also important to note, the example above is not the only way to compute an adjusted average. Can you think of anything else we have learned that would let you filter the lowest score(s) from the scores list? If you are interested in a challenge, see if you can modify the example on your own to calculate the adjusted average a different way.

### Your Task

In this Bite, you'll complete the `iterate_with_conditions` function to iterate through a list of numbers which is passed in as an argument.

Follow these steps:

1. **Continue Condition**: If the number `5` is encountered, print `"Found five, continue!"` and skip to the next iteration using the `continue` statement.
2. **Break Condition**: If the number `8` is encountered, print `"Found eight, break!"` and exit the loop using the `break` statement.

You don't have to hardcode the numbers; you can use the provided constants:

```
BREAK_NUM = 8
CONTINUE_NUM = 5
```

### Example Usage

```
nums = [1, 3, 5, 8]
iterate_with_conditions(nums)
```

Output:
```
Found five, continue!
Found eight, break!
```

By completing this task, you'll gain a better understanding of how to use `break` and `continue` to control the flow of loops in Python.

Good luck, and one more Newbie done! Keep going!
