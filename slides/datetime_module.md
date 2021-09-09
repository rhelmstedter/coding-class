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
## Datetime Module

Coding 2021-2022

Mr. Helmstedter

---

# What is a module?

Modules are libraries of code that other people have written so you can write less code.

---

## [The Python Standard Library](https://docs.python.org/3/library/)

---

### Some Common Examples

- datetime
- time
- collections
- random
- math
- os
- turtle

---

### Datetime Objects

```python
>>> from datetime import date, time, datetime

>>> date(year=2021, month=9, day=3)
datetime.date(2021, 9, 3)

>>> time(hour=13, minute=14, second=31)
datetime.time(13, 14, 31)

>>> datetime(year=2021, month=9, day=3, hour=13, minute=14, second=31)
datetime.datetime(2021, 9, 3, 13, 14, 31)
```

---

### Datetime Methods

1. date.today() creates a datetime.date instance with the current local date.
2. datetime.now() creates a datetime.datetime instance with the current local date and time.
3. datetime.combine() combines instances of datetime.date and datetime.time into a single datetime.datetime instance.

---
