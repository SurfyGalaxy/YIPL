# YIPL

YIPL (YAML Is a Programming Language) is (soon to be) a turing-complete programming language using YAML's file format.
The name is pronounced "Yip - el"

## History

YIPL was made as an entry in Hack Club's Horizons Hackathon.

Why?
Why *not*?


# General rules of YIPL

## Truthiness

For `or`, `and`, and `not`, YIPL follows Python's truthiness rules:

**Falsy values:** `False`, `None`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict)

**Truthy values:** Everything else

## Nesting functions

YIPL allows the nesting of functions to form more complex functions.

#### Example (Greater than or equal):
```yaml
or:
  - greater:
    - a
    - b
  - equality:
    - a
    - b
```  

## Data Types

YIPL supports many types of variables:
- Strings (`"string"` or `'string'` or `string`)
- Ints (`1`)
- Floats (`1.45`)


# Syntax

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

#### If:
Takes one bool or comparison, jumps to the **name** of the second entry if true, the third entry if false (think ASM). Every term is required


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


## variables

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

## Output

```python
print(a)
```

Prints the given data to the terminal
```yaml
print:
  - a
```