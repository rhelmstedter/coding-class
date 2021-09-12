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
.reveal .progress { color: #ff6c6b; }
.reveal strong, .reveal b { font-weight: bold; }
.reveal em { font-style: italic; }
</style>

# Python
## Expressions, Data Types, & Variables

Coding 2021

Mr. Helmstedter

---

# Expressions

Expressions contain terms and operations

---

# Data Types

| Data Type | Python Representation        |
|-----------|------------------------------|
| Text      | string                       |
| Numeric   | integer, float, complex      |
| Sequence  | list, tuple, range           |
| Mapping   | dictionary                   |
| Set       | set, frozenset               |
| Boolean   | boolean                      |
| Binary    | bytes, bytearray, memoryview |

---

## Strings vs Numerics

Strings store text. 

Numbers store, you guessed it, numbers.

---

<!-- .slide: data-background="https://img0.etsystatic.com/105/1/10162971/il_fullxfull.922903208_9vmq.jpg" -->

---

### Quiz Time

What is the output of this code?

```python
>>>5 + 3
```

---

### Quiz Time

What is the output of this code?

```python
>>>5 + 3
8
```

What is the output of this code?

```python
>>>2 * 3
```
---

### Quiz Time

What is the output of this code?

```python
>>>5 + 3
8
```

What is the output of this code?

```python
>>>2 * 3
6
```
---

### Quiz Time

What is the output of this code?

```python
>>>"5" + "3"
```
---

### Quiz Time

What is the output of this code?

```python
>>>"5" + "3"
'53'
```
What is the output of this code?

```python
>>>"2" * "3"
```
---

### Quiz Time

What is the output of this code?

```python
>>>"5" + "3"
'53'
```
What is the output of this code?

```python
>>>"2" * "3"
TypeError: can only concatentate str (not "int") to str
```
What is the output of this code?

```python
>>>"2" * 3
```
---

### Quiz Time

What is the output of this code?

```python
>>>"5" + "3"
'53'
```
What is the output of this code?

```python
>>>"2" * "3"
TypeError: can only concatentate str (not "int") to str
```
What is the output of this code?

```python
>>>"2" * 3
'222'
```
---
# Variables

Variables are containers for storing data values.

---
## Variables

Use the assignment operator `=` to store data in a variable.

```python
name = "Bob"
winner = "True"
score = 35
```
---

![variables](https://microbit-challenges.readthedocs.io/en/latest/_images/variable.jpg)

---

# See It In Action
