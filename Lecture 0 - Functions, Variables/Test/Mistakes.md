# CS50P Lecture 0 — Corrections Workbook

> This file only includes answers that were **wrong, incomplete, or worth correcting**.  
> The questions you answered correctly are intentionally not included.  
> Use this as a repair sheet, not a full answer key.

---

## Quick Summary

You understood most of the lecture well.

The main things to fix are:

- strings are **sequences of characters**, not just “a letter”
- text inside quotes is **literal text**, not a variable
- `strip()` needs parentheses and removes spaces from **both sides**
- forgetting `f` in an f-string does **not** cause an error
- `round()` does **not** always round up
- default parameters are used when no argument is provided
- method calls need `()`, like `.strip().title()`
- some practice code reused `x` when it needed `y`
- f-string formatting should be `{z:.2f}`, not `{z:.f2}`

---

# Corrections

## Question 10 — What is a string?

### Your answer

> Basically a letter. String indicates a string of letter. A data type.

### What needs fixing

A string is not just one letter.

A **string** is text, or more precisely, a sequence of characters.

A string can be:

```python
"hello"
```

or:

```python
"a"
```

or:

```python
"123"
```

Important:

```python
"123"
```

looks like a number, but it is a string because it is inside quotes.

### Correct idea

A string, or `str`, is a data type used for text.  
It can contain letters, numbers, spaces, symbols, or even be empty.

```python
name = "David"
message = "hello, world"
number_as_text = "123"
```

### Mental model

A string is not “a letter.”  
A string is a **line of text characters tied together**.

Tiny text train. 🚃

---

## Question 12 — Why does the code not print `hello, David`?

### Code

```python
name = "David"
print("hello, name")
```

### Your answer

> Because the name is a string in that case.

### What needs fixing

The real problem is not that `name` is a string.

The problem is that `"name"` is inside quotation marks.

Anything inside quotes becomes literal text.

So Python does not look for the variable `name`.  
It just prints the word `name`.

### Correct idea

```python
print("hello, name")
```

means:

> Print the exact text `hello, name`.

To use the variable, keep it outside the quotes:

```python
print("hello,", name)
```

or use an f-string:

```python
print(f"hello, {name}")
```

### Mental model

Quotes tell Python:

> “Do not think. Just print these characters.”

---

## Question 17 — What does `strip()` do?

### Your answer

> It takes out the empty space before the first letter.

### What needs fixing

This is half-right.

`strip()` removes extra whitespace from **both the beginning and the end** of a string.

It does not remove spaces in the middle.

### Correct idea

```python
name = "   David   "
name = name.strip()
print(name)
```

Output:

```text
David
```

But:

```python
text = "David   Malan"
print(text.strip())
```

Output:

```text
David   Malan
```

The spaces in the middle stay.

### Mental model

`strip()` cleans the outside edges of the string, not the inside rooms.

---

## Question 20 — What happens if you forget the `f`?

### Code

```python
print("hello, {name}")
```

### Your answer

> It's gonna output an error i suppose?

### What needs fixing

This does **not** cause an error.

Python will just print `{name}` literally because the string is not an f-string.

### Correct output

```text
hello, {name}
```

### Correct version

```python
print(f"hello, {name}")
```

### Why

The `f` tells Python:

> “Look inside `{}` and replace it with the variable value.”

Without `f`, Python treats `{name}` as normal text.

### Mental model

`f` is the “wake up and replace this” switch.

---

## Question 21 — What does `sep` control?

### Your answer

> separation, which is what will be shown in space. if its noamally its gonna be like hello, Matt. but if you do sep = !!! its gonna be hello,!!!Matt I think.

### What needs fixing

Your idea is mostly right, but the wording should be clearer.

`sep` means **separator**.

It controls what appears **between multiple arguments** passed to `print()`.

### Correct idea

```python
print("hello", "Matt")
```

Output:

```text
hello Matt
```

Python uses the default separator:

```python
sep=" "
```

If you change it:

```python
print("hello", "Matt", sep="!!!")
```

Output:

```text
hello!!!Matt
```

### Important detail

`sep` only matters when `print()` receives multiple arguments.

This has multiple arguments:

```python
print("hello", "Matt")
```

This has one argument:

```python
print("hello Matt")
```

So `sep` would not change anything useful in the second one.

---

## Question 32 — Why does this code print `12` instead of `3`?

### Code

```python
x = input("x: ")
y = input("y: ")
print(x + y)
```

### Your answer

> becuse the dafalt output for a input is string and it expects a string.

### What needs fixing

You got the important idea, but the wording should be corrected.

`input()` does not have a “default output.”  
It **returns a string**.

So if the user types:

```text
1
2
```

Python stores them as:

```python
x = "1"
y = "2"
```

Then:

```python
"1" + "2"
```

means string concatenation, so the result is:

```text
12
```

### Correct idea

`input()` always returns text.  
If you want math, convert the input:

```python
x = int(input("x: "))
y = int(input("y: "))
print(x + y)
```

---

## Question 36 — What does `round()` do?

### Your answer

> it rounds up a float number to an int.

### What needs fixing

`round()` does **not** always round up.

It rounds to the nearest value.

Also, it does not only work with floats, and it does not always return an integer.

### Correct idea

```python
round(3.2)
```

Output:

```python
3
```

```python
round(3.8)
```

Output:

```python
4
```

With a second argument, you can choose decimal places:

```python
round(3.14159, 2)
```

Output:

```python
3.14
```

### Important distinction

This means “round to 2 decimal places”:

```python
round(x / y, 2)
```

This means “display with 2 decimal places”:

```python
print(f"{z:.2f}")
```

They are related, but not exactly the same.

### Mental model

`round()` is not an elevator that always goes up.  
It goes to the nearest floor.

---

## Question 41 — Parameter vs argument

### Your answer

> parameter is the def hello(to): - to is the parameter which you can hand to the function and by giving it a name(just to show how you gonna use the value ahnded to the function / argument)

### What needs fixing

You are close, but the explanation got tangled.

A **parameter** is the variable name inside the function definition.

An **argument** is the actual value you pass when calling the function.

### Correct idea

```python
def hello(to):
    print("hello,", to)


hello("David")
```

In this code:

```python
to
```

is the parameter.

```python
"David"
```

is the argument.

### Mental model

The parameter is the empty labeled box.

The argument is the thing you put into the box.

```text
parameter = box label
argument = actual value
```

---

## Question 43 — What does a default parameter value do?

### Your answer

> nothing if not set specifically.

### What needs fixing

A default parameter value is used **when no argument is provided**.

### Correct idea

```python
def hello(to="world"):
    print("hello,", to)
```

If you call:

```python
hello()
```

Python uses the default value:

```text
hello, world
```

If you call:

```python
hello("David")
```

Python uses your argument instead:

```text
hello, David
```

### Mental model

A default parameter is the backup value.

If nobody brings an argument to the party, Python uses the backup snack.

---

## Question 47 — What is scope?

### Your answer

> To waht extent can that function reach to get or give or even read something perhaps.

### What needs fixing

Your instinct is in the right direction, but make it more precise.

**Scope** means where a variable exists and where it can be used.

### Correct idea

```python
def main():
    name = "David"


print(name)
```

This will cause an error because `name` was created inside `main()`.

The variable belongs to that function’s local scope.

### Correct pattern

Pass the value into another function:

```python
def main():
    name = "David"
    hello(name)


def hello(to):
    print("hello,", to)


main()
```

### Mental model

Scope is the room where a variable lives.  
If another function is in a different room, it cannot automatically grab that variable.

---

# Practice Task Corrections

## Practice Task 1 — Ask for your name and print `hello, YOUR_NAME`

### Your code

```python
name = input("What's your name? :").strip.title
print(f"hello, {name}")
```

### What is wrong

`.strip.title` is not calling the methods.

You need parentheses:

```python
.strip().title()
```

Without parentheses, Python sees the method itself instead of running it.

### Correct version

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

### Why

This line does three things:

```python
name = input("What's your name? ").strip().title()
```

1. `input()` asks for the name
2. `.strip()` removes extra spaces
3. `.title()` capitalizes each word

---

## Practice Task 2 — Remove spaces and title-case the name

### Your code

```python
name = input("What's your name? :").strip.title
print(f"hello, {name}")
```

### What is wrong

Same issue:

```python
.strip.title
```

should be:

```python
.strip().title()
```

### Correct version

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

### Mental model

Methods need `()` to actually run.

```python
name.strip
```

means:

> Here is the method.

```python
name.strip()
```

means:

> Run the method.

Tiny parentheses, big difference.

---

## Practice Task 3 — Ask for two numbers and print their sum

### Your code

```python
x = int(input("What's the vallue of \"x\"? :"))
x = int(input("What's the vallue of \"y\"? :"))

print(x + y)
```

### What is wrong

You used `x` twice.

This line overwrites the first value:

```python
x = int(input("What's the value of y? "))
```

Also, `y` was never created, so:

```python
print(x + y)
```

will cause an error.

### Correct version

```python
x = int(input("What's the value of x? "))
y = int(input("What's the value of y? "))

print(x + y)
```

### Why

You need one variable for each input:

```python
x = first number
y = second number
```

Then you can add them:

```python
x + y
```

---

## Practice Task 4 — Ask for two numbers and print the result rounded to 2 decimal places

### Your code

```python
x = int(input("What's the vallue of \"x\"? :"))
x = int(input("What's the vallue of \"y\"? :"))

z = x + y

print(f"{z:.f2}")
```

### What is wrong

There are several issues.

### Issue 1 — You used `x` twice

You need `y` for the second input.

Wrong:

```python
x = int(input("What's the value of y? "))
```

Correct:

```python
y = int(input("What's the value of y? "))
```

### Issue 2 — `y` is never created

Because you did not create `y`, this line will break:

```python
z = x + y
```

### Issue 3 — Format syntax is wrong

Wrong:

```python
print(f"{z:.f2}")
```

Correct:

```python
print(f"{z:.2f}")
```

The `2` goes before the `f`.

### Issue 4 — Use `float()` if decimals are possible

If the lecture topic is floats, use:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))
```

### Correct version: sum shown with 2 decimals

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x + y

print(f"{z:.2f}")
```

### Correct version: division shown with 2 decimals

This matches the lecture example better:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")
```

### Mental model

```python
:.2f
```

means:

> show this number with 2 digits after the decimal point

---

## Practice Task 6 — Program with `main()` and `hello()`

### Your code

```python
def main():
    name = input("What's your name? :").strip.title
    hello(name)

def hello(to):
    print("Hello,", to)


main()
```

### What is wrong

Again:

```python
.strip.title
```

should be:

```python
.strip().title()
```

### Correct version

```python
def main():
    name = input("What's your name? ").strip().title()
    hello(name)


def hello(to):
    print("Hello,", to)


main()
```

### Why this is good

`main()` controls the main flow:

```python
def main():
    name = input("What's your name? ").strip().title()
    hello(name)
```

`hello()` handles the greeting:

```python
def hello(to):
    print("Hello,", to)
```

Then this starts the program:

```python
main()
```

This makes the program easier to read.

---

# Extra Mini Review

## The mistakes to remember

### 1. Methods need parentheses

Wrong:

```python
name.strip.title
```

Correct:

```python
name.strip().title()
```

### 2. Do not reuse the wrong variable name

Wrong:

```python
x = int(input("x: "))
x = int(input("y: "))
```

Correct:

```python
x = int(input("x: "))
y = int(input("y: "))
```

### 3. F-string decimal format

Wrong:

```python
print(f"{z:.f2}")
```

Correct:

```python
print(f"{z:.2f}")
```

### 4. Forgetting `f` does not cause an error

```python
print("hello, {name}")
```

prints:

```text
hello, {name}
```

Correct:

```python
print(f"hello, {name}")
```

### 5. `round()` does not always round up

```python
round(3.2)
```

gives:

```python
3
```

```python
round(3.8)
```

gives:

```python
4
```

---

# Tiny Practice to Fix the Weak Spots

Try these again without looking.

## Practice 1

Fix this:

```python
name = input("Name: ").strip.title
print(f"hello, {name}")
```

**Your corrected code:**

```python

```

---

## Practice 2

Fix this:

```python
x = int(input("x: "))
x = int(input("y: "))
print(x + y)
```

**Your corrected code:**

```python

```

---

## Practice 3

Fix this:

```python
z = 2 / 3
print(f"{z:.f2}")
```

**Your corrected code:**

```python

```

---

## Practice 4

What does this print?

```python
name = "David"
print("hello, {name}")
```

**Your answer:**




---

## Practice 5

Explain the difference:

```python
def hello(to):
    print("hello,", to)


hello("David")
```

**Parameter:**




**Argument:**




---

# Final Mental Model

Your biggest issue was not the big concepts.

It was the small Python syntax traps:

```python
()
```

for calling methods,

```python
f""
```

for f-strings,

```python
:.2f
```

for decimal formatting,

and using the right variable names.

This is normal beginner territory.

You are not missing the map.  
You mostly stepped on a few syntax banana peels.
