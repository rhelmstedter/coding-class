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
    theme: github
    keybinding: vim

---

# Python

## Functions

Coding 2021-2022

Mr. Helmstedter

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

---

## Example Function

```python
def function_name(arguments):
    body of the function
    return values
```

---

code:
<pre>
  <code data-line-numbers="1|2|5" class='language-python'>def say_hello(name):
      print(f"Hello, {name}! Have a great day.")

  # now need to call the function
  say_hello("Mr. Helmstedter")
  </code>
</pre>

output:

```md
Hello, Mr. Helmstedter! Have a great day.
```

---

![black box](https://marvel-b1-cdn.bc0a.com/f00000000225793/blog-c7ff.kxcdn.com/blog/wp-content/uploads/2016/10/blog-01.jpg)

---

### Familiar Functions

```python
print()
input()
```

---

## Methods

Methods are functions that you can use on objects using dot notation.

---

### Familiar Methods

```python
import random
random.randint()
```

---

### String Methods

- [All String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [replit example](https://replit.com/@MrHelmstedter/string-methods)
