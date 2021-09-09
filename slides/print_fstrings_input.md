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
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');
.slide { color:#116466; background: #282c34;}
.slide h1{ color: #c678dd; font-family: 'Source Code Pro'; }
.slide h2{ color: #a9a1e1; font-family: 'Source Code Pro'; }
.slide h3{ color: #c678dd; font-family: 'Source Code Pro'; }
.reveal p { color: #98be65; font-family: 'Source Code Pro';}
.reveal li{ color: #51afef; font-family: 'Source Code Pro';}
.reveal a { color: #89b08c; font-family: 'Source Code Pro';}
.reveal th { color: #ECBE7B; font-family: 'Source Code Pro';}
.reveal tr { color: #51afef; font-family: 'Source Code Pro'; font-size: 90%; }
.reveal .controls { color: #0a97b0; }
.reveal .progress { color: #ff6c6b; }
</style>

# Python
## print(), f-strings, input()

Coding 2021-2022

Mr. Helmstedter

---

# print()

`print()` is a function that allows you to display text on a screen

---

```python
name = "Mr. Helmstedter"
age = 35

print(name)
print(age)
```
Output: 

Mr. Helmstedter

35

---

```python
name = "Mr. Helmstedter"
age = 35

print("My name is " + name + " and I am " + age + " years old.")
```

Output:

My name is Mr. Helmstedter and I am 35 years old.

---

# f-string

f-string stands for formatted strings.

---

```python
name = "Mr. Helmstedter"
age = 35

print(f"My name is {name} and I am {age} years old.")
```

Output:

My name is Mr. Helmstedter and I am 35 years old.

---

### Which is easier?

string concatenation
```python
print("My name is " + name + " and I am " + age + " years old.")
```

<br> 

f-strings
```python
print(f"My name is {name} and I am {age} years old.")
```

---

# input()

`input()` is a function that allows the user to input data for your program to process
