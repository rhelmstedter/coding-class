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
## Boolean Values and Conditionals

Coding 2021-2022

Mr. Helmstedter

---

## Boolean Values

Python uses capital letters for `True` and `False`

---

### Conditionals 

| Operator | Definition               |
|:--------:|:-------------------------|
|    ==    | equal                    |
|    !=    | not equal                |
|     >    | greater than             |
|     <    | less than                |
|    >=    | greater than or equal to |
|    <=    | less than or equal to    |
|    is    | object identity          |

---

### if, elif, andelse statements

```python
if <conditional>:
	"do something if conditional is" True
elif <another-conditional>:
	"do something if the other conditional is" True
else:
	"do something if all the conditionals were" False
```

---

### building complex statements

Python offers keywords for working with booleans and conditionals

```python
and
or
not
```

---

### False Values

- False
- None
- Zero of any numeric type
- Any empty squence
- Any empty mapping

---
