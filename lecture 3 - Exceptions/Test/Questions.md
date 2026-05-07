---
type: questions
course: CS50P
lecture: 3
topic: exceptions
status: active
tags:
  - python
  - cs50p
  - exceptions
  - questions
---

# CS50P - Lecture 3 - Exceptions - Questions

Use these questions after reviewing `summary.py` and `Review.md`.

Try to answer without looking first.

---

# Part 1 - Basic Understanding

## Q1

What is an exception in Python?

## Q2

What is the difference between a `SyntaxError` and a runtime error?

## Q3

Can `try/except` usually fix a `SyntaxError`?

Why or why not?

## Q4

What does `ValueError` mean?

Give one example.

## Q5

What does `NameError` mean?

Give one example.

---

# Part 2 - Code Reading

## Q6

What happens if the user types `cat`?

```python
x = int(input("What's x? "))
print(f"x is {x}")
```

## Q7

What does this code do if the user types `hello`?

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
```

## Q8

Why is this code dangerous?

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```

## Q9

What is the purpose of `else` here?

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

## Q10

What does `break` do in this code?

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
```

---

# Part 3 - Writing Code

## Q11

Write a function called `get_int(prompt)`.

It should:

- ask the user for input
- convert the input to an integer
- keep asking if the input is invalid
- return the valid integer

## Q12

Write a function called `get_positive_int(prompt)`.

It should only return an integer greater than 0.

## Q13

Write code that asks for two integers and divides them.

Handle:

- invalid number input
- division by zero

## Q14

Write a function called `validate_age(age)`.

If age is negative, raise a `ValueError`.

## Q15

Write a program that asks the user to choose from this menu:

```text
1. Coffee
2. Tea
3. Water
```

Handle:

- non-number input
- numbers outside 1 to 3

---

# Part 4 - Debugging

## Q16

What is wrong with this code?

```python
try:
    number = int(input("Number: "))
except:
    print("Invalid")
```

How would you improve it?

## Q17

What is wrong with this code?

```python
try:
    x = int(input("x: "))
    print(y)
except ValueError:
    print("Invalid number")
```

## Q18

What will happen here if the user types `0`?

```python
try:
    x = int(input("x: "))
    result = 10 / x
except ValueError:
    print("Invalid number")
else:
    print(result)
```

What exception is not being handled?

## Q19

Why might this code be unfriendly?

```python
while True:
    try:
        x = int(input("x: "))
        break
    except ValueError:
        pass
```

## Q20

Why is this better for beginners?

```python
while True:
    try:
        x = int(input("x: "))
        break
    except ValueError:
        print("Please type an integer.")
```

---

# Part 5 - Explain in Your Own Words

## Q21

Explain `try`, `except`, and `else` using a real-life example.

## Q22

Explain why exceptions are useful.

## Q23

Explain why catching every error with bare `except` can be dangerous.

## Q24

Explain the difference between:

```python
break
```

and

```python
return
```

inside an input-validation loop.

## Q25

Explain this pattern in simple language:

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type an integer.")
```

---

# Answer Key

Open this only after you answer.

<details>
<summary>Click to show suggested answers</summary>

## A1

An exception is a problem that happens while a program is running.

## A2

A `SyntaxError` means Python cannot understand the code structure. A runtime error happens while valid code is already running.

## A3

Usually no. Python must understand the file before it can run any `try/except` code.

## A4

`ValueError` means a value is invalid for an operation. Example: `int("cat")`.

## A5

`NameError` means Python sees a variable/name that does not exist. Example: `print(x)` before assigning `x`.

## A6

The program raises `ValueError` because `"cat"` cannot become an integer.

## A7

It prints `x is not an integer`.

## A8

If input is invalid, `x` is never assigned. Then `print(f"x is {x}")` can cause `NameError`.

## A9

`else` runs only when the `try` block succeeds.

## A10

`break` exits the `while True` loop.

## A11

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type an integer.")
```

## A12

```python
def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            print("Please type an integer.")
        else:
            if n > 0:
                return n
            print("Number must be greater than 0.")
```

## A13

```python
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except ValueError:
    print("Please type integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## A14

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age
```

## A15

```python
try:
    choice = int(input("Choose 1, 2, or 3: "))
except ValueError:
    print("Please type a number.")
else:
    if choice == 1:
        print("Coffee")
    elif choice == 2:
        print("Tea")
    elif choice == 3:
        print("Water")
    else:
        print("Invalid menu choice.")
```

## A16

It uses bare `except`, which catches too much. Better: `except ValueError:`.

## A17

`print(y)` can raise `NameError`, but only `ValueError` is handled.

## A18

It raises `ZeroDivisionError`. The code does not handle division by zero.

## A19

It silently ignores bad input. The user does not know what went wrong.

## A20

It tells the user what to fix.

## A21

Example: `try` is the risky attempt, `except` is the backup plan, and `else` is what happens if everything works.

## A22

They let programs handle expected problems instead of crashing.

## A23

Bare `except` can hide unexpected bugs and make debugging harder.

## A24

`break` exits a loop. `return` exits the function and gives back a value.

## A25

It asks forever until the input can become an integer, then returns that integer.

</details>
