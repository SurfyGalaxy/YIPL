# YIPL

YIPL <small> pronounced `Yip-el` </small> is a turing-complete interpreted language using YAML as it's syntax, 
made for Hackclub Horizons.

## Quick start

1. In your terminal of choice type `pip install yipl`
2. Create a YAML file with your code (example code below)
```yaml
print:
  - Hello World!
```
3. Run `yipl <file.yaml>` 

## AI Disclaimer <small> for hackclub </small>
No AI was used :)

### Maybe Helpful Links
- [GitHub](https://github.com/SurfyGalaxy/YIPL)
- [PyPI](https://pypi.org/project/yipl)

# Syntax

## General rules

### Key names

Because of YAML's inherent structure, every key must be unique. YIPL allows any keyword to be appended by text with a leading space. Examples include:
- `print 1:`
- `set main variable`
- `if a and b are equal`


### Truthiness
YIPL uses the same truthiness values as Python when using logical operators.

**Falsy values:** `False`, `None`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict)

**Truthy values:** Everything else

### Function nesting
YIPL allows the nesting of functions to allow for more complex functions than the basic keywords. Some examples include:

#### Greater than or equal
```yaml
or:
  - greater:
    - $a
    - $b
  - equality:
    - $a
    - $b
```  
#### Modulo ($a mod $b)
```yaml
minus:
  - $a
  - multiply:
    - $b
    - cast:
      - int
      - divide:
        - $a
        - $b
```

#### Increment by $b
```yaml
set:
  - $a
  - plus:
    - $a
    - $b
```

## Keywords
YIPL posesses 17 unique keywords, all listed below.

## Comparisons

### Equality
```python
a == b
```

Takes two variables, outputs bool if exactly the same
```yaml
equality:
  - a
  - b
```

### Greater than
```python
a > b
```

Takes two int or floats, outputs bool if `a` is greater than `b` (not equal to)
```yaml
greater:
  - a
  - b
```

### Less than
```python
a < b
```

Takes two int or floats, outputs bool if `a` is less than `b` (not equal to)
```yaml
less:
  - a
  - b
```

### Or
```python
a or b
```

Takes two bools or comparisons, outputs bool if `a` or `b` is `True`
```yaml
or:
   - a
   - b
```

### And
```python
a and b
```

Takes two bools or comparisons, outputs bool if `a` and `b` is `True`
```yaml
and:
  - a
  - b
```

### Not
```python
not a
```

Takes one bool or comparisons, outputs the opposite boolean literal
```yaml
not:
  - a
```


## Conditionals

```python
if a == True:
    print("Yes")
elif a == False:
    print("No")
else:
    print("something else")
```

#### If / Goto:
Takes one bool or comparison, jumps to the **name** of the second entry if true, the third entry if false (think ASM). Every term is required.

Both branching functions require tags to jump to, they will not jump to a function.


```yaml
if_1:
  - equality:
    - a
    - True
  - print_1
  - if_2
print_1:
  - Yes
goto_1:
  - <code>
if_2:
  - equality:
    - a
    - False
  - print_2
  - print_3
print_2:
  - No
goto_2:
  - <code>
print_3:
  - something else
goto_3:
  - <code>
```


## Arithmetic
All of YIPL's arithmetic only works on two values at a time; `a + b + c` in one function is not possible in YIPL

```python
a + b

a - b

a * b

a / b
```

#### Addition:
Returns the sum of two ints or floats as an int or float

#### Subtraction:
Returns the difference of two ints or floats as an int or float

#### Multiplication:
Returns the product of two ints or floats as an int or float

#### Division:
Returns the Quotient of two ints or floats as an int or float

```yaml
plus:
  - a
  - b

minus:
  - a
  - b

multiply:
  - a
  - b

divide:
  - a
  - b
```


## Variables

variables are made by prepending a string with `$`. They do not need to be put in quotes
When using `set:`, the `$` is optional

```python
filler_word = "Foobar"
```

```yaml
set:
  - $filler word
  - Foobar
```

## I/O

### Print:

```python
print(a)
```

Prints the given data to the terminal
```yaml
print:
  - a
```

### Set:

```python
input(a)
```

Returns the typed value as a `str`. `a` is the prompt displayed in the terminal/
```yaml
input:
  - a
```

## Cast:

```python
int(a)
str(b)
float(c)
```

Returns argument `b` as the type `a`

Supported types:
- int
- str
- float

```yaml
cast:
  - int
  - $a

cast:
  - str
  - $b

cast:
  - float
  - $c
```

## List operations

YIPL posesses multiple operations to be done on a list object.
To make a list, use `[]` like python in the second field of `set:`

```yaml
set:
  - $a
  - [a, b, c]
```

<sub> makes a variable `$a` with the contents `[a, b, c]` </sub>

All operations on lists are done in the `list:` function, with the first argument being which one to use.
Currently implemented functions are:

- length
- read
- delete
- append
- replace

```yaml
list:
  - length
  - $a
```
Returns the length of the list `$a` as an `int`. Equivialent to `len(a)` in python

```yaml
list:
  - read
  - $a
  - $b
```

Returns the item at index `$b` of list `$a`. Equivialent to `a[b]`

```yaml
list:
  - delete
  - $a
  - $b
```

Removes the item at index `$b` of list `$a`. Equivialent to `del a[b]`

```yaml
list:
  - append
  - $a
  - $b
```

Appends `$b` to list `$a`. Equivialent to `a.append(b)`

```yaml
list:
  - replace
  - $a
  - $b
  - $c
```

Replaces the item at index `$b` of list `$a` with `$c`. Equivialent to `a[b] = c`