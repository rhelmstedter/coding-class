---
transition: slide
highlight: atom-one-dark
backgroundTransition: slide
progress: true
controls: true
hideAddressBar: true

# Editor settings
editor:
    fontSize: 14
    theme: gruvbox
    keybinding: vim
    
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,400;0,700;0,900;1,400;1,700;1,900&display=swap');
.slide { color:#116466; background: #282c34;}
.slide h1 { color: #c678dd; font-family: 'Source Code Pro'; }
.slide h2 { color: #a9a1e1; font-family: 'Source Code Pro'; }
.slide h3 { color: #c678dd; font-family: 'Source Code Pro'; }
.reveal p { color: #98be65; font-family: 'Source Code Pro';}
.reveal li { color: #51afef; font-family: 'Source Code Pro';}
.reveal a { color: #89b08c; font-family: 'Source Code Pro';}
.reveal th { color: #ECBE7B; font-family: 'Source Code Pro';}
.reveal tr { color: #51afef; font-family: 'Source Code Pro'; font-size: 90%; }
.reveal .controls { color: #0a97b0; }
.reveal .progress { color: #1b6ca8; }
.reveal strong, .reveal b { font-weight: bold; }
.reveal em { font-style: italic; }
</style>

# Python
## Loops

Coding 2021-2022

Mr. Helmstedter

---

### `while` loops

```python
while conditional:
	indent body of loop
```

---

### Infinite `while` loops

```python
while True:
	print("hello world")
```

---

![nooooo gif](https://c.tenor.com/_vtSpIWnb3kAAAAC/no-nooo.gif)

---

### Working with infinite loops

Python offers two keywords: 

- **break**: if you reach this keyword exit the loop
- **continue**: if you reach this keyword return to the top of the loop

---

### Demo

[How to keep an idiot busy for hours](https://replit.com/@MrHelmstedter/idiot)

---

### Vocabulary

**Iterable:** anything you can loop over (e.g., a list or string)

**Iteration:** one execution (think step) of the loop

**Index:** a variable that tracks which iteration you're currently on

---

### Basic Structure of `for` loops

```python
for variable in interable:
    indent body of loop body
    second line of loop body
    third line of loop body

rest of program outside of loop
```

---

### Example `for` loop

```python
for number in [1, 2, 3]:
    print(number, end='')
```

---

### Break down of the `for` loop

First time through:
```python
for number in [*1*, 2, 3]:
    print(number, end=" ")
```
current output -> 1

---

### Break down of the `for` loop

Second time though:
```python
for number in [1, *2*, 3]:
    print(number, end=" ")
```
current output -> 1 2


---

### Break down of the `for` loop

Third time through:
```python
for number in [1, *2*, 3]:
    print(number, end=" ")
```
current output -> 1 2 3

---

### Using `range()`

If you are trying to loop over numbers only, use the `range()` function. 

The `range()` function takes three arguments.
```
range(start=0, stop, step=1)
```

---

### Replicate the `for` loop with `range()`

```python
for num in range(1,4):
    print(num)
```

---

### These loops do the same thing

```python
for num in range(1,11):
    print(num)
```

```python
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)
```


