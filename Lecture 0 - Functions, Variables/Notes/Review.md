# CS50P — Lecture 0: Functions, Variables

> Lecture note only.  
> Use this after watching the lecture and after doing your own recall.

---

## 0. Big Picture

Lecture 0 is your first doorway into Python.

The main idea is:

> A program is a set of instructions you write so the computer can do something for you.

In this lecture, you learn how to:

- create and run a Python file
- use built-in functions like `print()` and `input()`
- store information in variables
- work with text using strings
- work with numbers using `int` and `float`
- improve code readability
- write your own functions with `def`
- return values from functions

Think of this lecture as learning the basic “grammar” of Python.

Not the whole language yet.  
Just enough to say your first few sentences.

---

## 1. Creating Code with Python

### 1.1 What is VS Code?

VS Code is a text editor.

You use it to:

- create files
- write code
- organize project files
- use the terminal

In CS50P, you often use a browser-based VS Code environment called a **codespace**.

### 1.2 Creating a Python file

To create or open a file named `hello.py`, you can type this in the terminal:

```bash
code hello.py
```

This means:

> Open a file called `hello.py` in the editor.

Important:

- `code hello.py` does **not** run the program.
- It opens the file so you can write code inside it.

### 1.3 Running a Python file

Inside `hello.py`, you can write:

```python
print("hello, world")
```

Then in the terminal, run:

```bash
python hello.py
```

This means:

> Use Python to execute the code inside `hello.py`.

### 1.4 `code hello.py` vs `python hello.py`

| Command | Meaning |
|---|---|
| `code hello.py` | Open/create the file so you can edit it |
| `python hello.py` | Run/execute the file |

Simple memory trick:

- `code` = open the notebook
- `python` = make the notebook come alive 🧪

---

## 2. Functions

### 2.1 What is a function?

A **function** is an action that Python already knows how to do, or an action you define yourself.

Examples:

```python
print("hello, world")
input("What's your name? ")
round(3.14159, 2)
```

The function name usually looks like a verb:

- `print()` prints something
- `input()` asks the user for input
- `round()` rounds a number

### 2.2 Function structure

Most functions look like this:

```python
function_name(argument)
```

Example:

```python
print("hello, world")
```

Here:

- `print` is the function name
- `"hello, world"` is the argument
- the parentheses `()` are where the argument goes

### 2.3 Arguments

An **argument** is information you pass into a function.

Example:

```python
print("hello")
```

The argument is:

```python
"hello"
```

You are telling `print()`:

> Print this text.

Some functions can take multiple arguments:

```python
print("hello,", "David")
```

Here, `print()` receives two arguments:

```python
"hello,"
"David"
```

Python automatically adds a space between them.

Output:

```text
hello, David
```

---

## 3. Bugs

### 3.1 What is a bug?

A **bug** is a mistake in your code.

Example:

```python
print("hello, world"
```

This is missing the closing `)`.

Python will complain with an error message.

### 3.2 Error messages are clues

At first, error messages look like an angry robot wrote a poem during a fever.

But they usually give you clues:

- what kind of error happened
- what line might be wrong
- sometimes what Python expected

Do not panic when you see an error.  
Debugging is part of programming, not a sign that you are bad at it.

### 3.3 Beginner mindset

When your code breaks, ask:

1. What line is Python pointing to?
2. Did I forget a quote?
3. Did I forget a parenthesis?
4. Did I spell the function or variable correctly?
5. Did I put text inside quotation marks?

---

## 4. Input

### 4.1 The `input()` function

`input()` asks the user to type something.

Example:

```python
input("What's your name? ")
```

This shows the prompt:

```text
What's your name?
```

But if you write only this:

```python
input("What's your name? ")
print("hello, world")
```

The program asks for your name, but does nothing with it.

The input disappears like a snack in a factory break room.

To keep the user’s answer, you need a variable.

---

## 5. Variables

### 5.1 What is a variable?

A **variable** is a container for a value.

Example:

```python
name = input("What's your name? ")
```

This means:

> Ask the user for their name, then store the answer inside `name`.

### 5.2 The `=` sign

In Python, `=` means **assignment**.

It does not mean “equal” in the math sense here.

```python
name = input("What's your name? ")
```

Read it from right to left:

1. Run `input("What's your name? ")`
2. Take the value the user typed
3. Store it in `name`

So if the user types:

```text
David
```

Then Python stores:

```python
name = "David"
```

### 5.3 Using a variable

```python
name = input("What's your name? ")
print("hello,")
print(name)
```

Output:

```text
What's your name? David
hello,
David
```

This works, but it prints on two lines.

### 5.4 Common mistake: putting variable names inside quotes

Wrong:

```python
name = input("What's your name? ")
print("hello, name")
```

Output:

```text
hello, name
```

Why?

Because `"name"` inside quotes is literal text.

Python sees it as the word `name`, not the variable.

Correct:

```python
name = input("What's your name? ")
print("hello,", name)
```

Output:

```text
hello, David
```

### 5.5 Variable naming

Good variable names describe what they store.

Good:

```python
name = "David"
age = 30
price = 100
```

Bad:

```python
x = "David"
a = 30
thing = 100
```

Short names like `x` can be okay in math or tiny examples, but clear names are usually better.

---

## 6. Comments

### 6.1 What is a comment?

A **comment** is a note in your code that Python ignores.

You write comments with `#`.

Example:

```python
# Ask the user for their name
name = input("What's your name? ")

# Say hello to the user
print("hello,", name)
```

Python does not execute comments.

Comments are for:

- yourself
- other programmers
- explaining intention
- leaving reminders

### 6.2 Good comments vs useless comments

Useless comment:

```python
# Print hello
print("hello")
```

This comment does not add much because the code is already obvious.

Better comment:

```python
# Ask for the user's name before greeting them
name = input("What's your name? ")
```

Even better: make the code itself readable.

---

## 7. Pseudocode

### 7.1 What is pseudocode?

**Pseudocode** is writing the logic of your program in plain language before writing real code.

Example:

```python
# Ask the user for their name
# Remove extra spaces
# Capitalize the name nicely
# Say hello to the user
```

Then you convert each step into Python.

### 7.2 Why pseudocode helps

Pseudocode helps when your brain feels like ten browser tabs arguing.

It lets you separate:

- thinking about the problem
- writing the exact syntax

This is important because beginners often try to do both at once and get overwhelmed.

---

## 8. Strings

### 8.1 What is a string?

A **string**, or `str`, is text.

Examples:

```python
"hello"
"David"
"What's your name?"
"123"
```

Important:

```python
"123"
```

is a string, not a number.

It looks like a number, but Python treats it as text because it is inside quotes.

### 8.2 Quotes

You can use double quotes:

```python
print("hello")
```

Or single quotes:

```python
print('hello')
```

Both are okay.

### 8.3 Quotation problem

This can be a problem:

```python
print("Hello, "friend"")
```

Python gets confused because it thinks the string ends before `friend`.

Correct ways:

Use single quotes outside:

```python
print('Hello, "friend"')
```

Or escape the inner quotes:

```python
print("Hello, \"friend\"")
```

Output:

```text
Hello, "friend"
```

### 8.4 Your earlier confusion: typing `"friend"` literally

If you want the output to include the quotation marks around friend, write:

```python
print('Hello, "friend"')
```

This is the cleanest beginner-friendly way.

---

## 9. Printing Strings in Different Ways

### 9.1 Concatenation with `+`

You can combine strings with `+`.

```python
name = input("What's your name? ")
print("hello, " + name)
```

Output:

```text
hello, David
```

But this can get clunky.

### 9.2 Multiple arguments with comma

```python
name = input("What's your name? ")
print("hello,", name)
```

Output:

```text
hello, David
```

This is easier.

`print()` automatically adds a space between arguments.

### 9.3 `sep`

`sep` controls what goes **between** multiple arguments.

Default:

```python
print("hello,", "David")
```

Output:

```text
hello, David
```

Python secretly uses:

```python
sep=" "
```

Example with no separator:

```python
print("hello,", "David", sep="")
```

Output:

```text
hello,David
```

Example with three dots:

```python
print("hello", "David", sep="...")
```

Output:

```text
hello...David
```

### 9.4 `end`

`end` controls what goes at the **end** of a `print()` call.

Default:

```python
end="\n"
```

`\n` means newline.

Example:

```python
print("hello,")
print("David")
```

Output:

```text
hello,
David
```

Because the first `print()` ends with a newline.

You can change that:

```python
print("hello, ", end="")
print("David")
```

Output:

```text
hello, David
```

### 9.5 `sep` vs `end`

| Parameter | Controls | Default |
|---|---|---|
| `sep` | What goes between multiple arguments | `" "` |
| `end` | What goes after the printed output | `"\n"` |

Memory trick:

- `sep` = separator between things
- `end` = ending after everything

---

## 10. f-strings

### 10.1 What is an f-string?

An **f-string** lets you insert variables directly inside a string.

Example:

```python
name = input("What's your name? ")
print(f"hello, {name}")
```

If `name` is `"David"`, output:

```text
hello, David
```

### 10.2 Why f-strings are useful

Instead of writing:

```python
print("hello, " + name)
```

or:

```python
print("hello,", name)
```

You can write:

```python
print(f"hello, {name}")
```

This becomes especially useful when strings get more complex.

Example:

```python
name = "David"
age = 30

print(f"{name} is {age} years old.")
```

Output:

```text
David is 30 years old.
```

### 10.3 Important syntax

You need:

- `f` before the string
- `{}` around the variable

Correct:

```python
print(f"hello, {name}")
```

Wrong:

```python
print("hello, {name}")
```

Output:

```text
hello, {name}
```

Without the `f`, Python treats `{name}` as normal text.

---

## 11. String Methods

### 11.1 What is a method?

A **method** is like a function attached to a value.

Example:

```python
name = name.strip()
```

`strip()` is a method that belongs to strings.

### 11.2 `strip()`

`strip()` removes extra spaces from the beginning and end of a string.

Example:

```python
name = "   David   "
name = name.strip()
print(name)
```

Output:

```text
David
```

This is useful because users often type extra spaces.

### 11.3 `capitalize()`

`capitalize()` capitalizes the first character of the string.

```python
name = "david"
name = name.capitalize()
print(name)
```

Output:

```text
David
```

But for full names, it is limited.

Example:

```python
name = "david malan"
print(name.capitalize())
```

Output:

```text
David malan
```

Only the first word becomes capitalized.

### 11.4 `title()`

`title()` capitalizes the first letter of each word.

```python
name = "david malan"
name = name.title()
print(name)
```

Output:

```text
David Malan
```

### 11.5 Chaining methods

You can combine methods.

Long version:

```python
name = input("What's your name? ")
name = name.strip()
name = name.title()
print(f"hello, {name}")
```

Shorter version:

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

This means:

1. Ask for input
2. Remove extra spaces
3. Convert to title case
4. Store result in `name`

### 11.6 Readability warning

This is powerful:

```python
name = input("What's your name? ").strip().title()
```

But if a line gets too magical, split it into steps.

Readable code beats “I wrote this like a wizard and now even I fear it.”

---

## 12. Integers: `int`

### 12.1 What is an integer?

An **integer**, or `int`, is a whole number.

Examples:

```python
1
2
3
100
-5
```

No decimal point.

### 12.2 Operators

Python can do math.

| Operator | Meaning | Example | Result |
|---|---|---:|---:|
| `+` | addition | `2 + 3` | `5` |
| `-` | subtraction | `5 - 2` | `3` |
| `*` | multiplication | `4 * 3` | `12` |
| `/` | division | `10 / 2` | `5.0` |
| `%` | modulo / remainder | `10 % 3` | `1` |

### 12.3 Interactive mode

You can type `python` in the terminal to enter interactive mode.

Then you can test small things:

```python
>>> 1 + 1
2
```

This is useful for quick experiments.

### 12.4 `input()` returns a string

Important:

```python
x = input("x: ")
y = input("y: ")
print(x + y)
```

If the user types:

```text
x: 1
y: 2
```

Output:

```text
12
```

Why?

Because `input()` gives you strings.

So Python sees:

```python
"1" + "2"
```

That combines text into:

```python
"12"
```

### 12.5 Converting string to int

Use `int()`:

```python
x = input("x: ")
y = input("y: ")

z = int(x) + int(y)

print(z)
```

Output:

```text
3
```

### 12.6 Cleaner version

You can convert immediately:

```python
x = int(input("x: "))
y = int(input("y: "))

print(x + y)
```

This means:

1. Ask for input
2. Convert it to an integer
3. Store it in the variable

---

## 13. Readability Wins

CS50P emphasizes that code should be readable.

Programming is not only about making the computer understand.

It is also about making future-you understand.

And future-you has probably slept badly, eaten too much convenience-store food, and forgotten why you wrote that line.

### 13.1 Readable version

```python
x = int(input("x: "))
y = int(input("y: "))

z = x + y

print(z)
```

### 13.2 Shorter version

```python
print(int(input("x: ")) + int(input("y: ")))
```

This works, but it is harder to read.

### 13.3 Rule of thumb

Prefer code that is:

- correct
- readable
- easy to debug
- easy to change later

Clever code is not always good code.

---

## 14. Floats: `float`

### 14.1 What is a float?

A **float** is a number with a decimal point.

Examples:

```python
1.5
3.14
0.25
```

### 14.2 Converting input to float

```python
x = float(input("x: "))
y = float(input("y: "))

z = x + y

print(z)
```

### 14.3 Floating-point weirdness

Computers can sometimes show decimal numbers in slightly strange ways.

This happens because computers represent numbers using binary, and not all decimal values fit perfectly.

Do not panic if decimals sometimes look odd.

This is normal in many programming languages.

---

## 15. Rounding Numbers

### 15.1 `round()`

You can round a number:

```python
z = round(x + y)
```

Example:

```python
x = float(input("x: "))
y = float(input("y: "))

z = round(x + y)

print(z)
```

### 15.2 Rounding to decimal places

```python
z = round(x / y, 2)
```

This rounds to 2 decimal places.

Example:

```python
x = float(input("x: "))
y = float(input("y: "))

z = round(x / y, 2)

print(z)
```

### 15.3 Formatting with commas

You can use an f-string to format large numbers with commas:

```python
z = 1000
print(f"{z:,}")
```

Output:

```text
1,000
```

### 15.4 Formatting decimal places

```python
z = 2 / 3
print(f"{z:.2f}")
```

Output:

```text
0.67
```

This means:

> Format `z` with 2 digits after the decimal point.

---

## 16. Defining Your Own Functions with `def`

### 16.1 Why define your own function?

So far, you used built-in functions:

```python
print()
input()
int()
float()
round()
```

But you can create your own.

This helps you:

- organize your code
- avoid repeating yourself
- give names to actions
- make programs easier to read

### 16.2 Basic function definition

```python
def hello():
    print("hello")
```

This defines a function called `hello`.

But defining a function does not automatically run it.

You need to call it:

```python
hello()
```

Full example:

```python
def hello():
    print("hello")


hello()
```

Output:

```text
hello
```

### 16.3 Functions with parameters

A **parameter** is a variable that a function receives.

```python
def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)
```

Here:

- `to` is the parameter
- `name` is the argument passed into the function

### 16.4 Parameter vs argument

These two words are easy to mix up.

| Word | Meaning |
|---|---|
| Parameter | The variable in the function definition |
| Argument | The actual value you pass when calling the function |

Example:

```python
def hello(to):
    print("hello,", to)


hello("David")
```

- `to` is the parameter
- `"David"` is the argument

Tiny distinction, but important. A little vocabulary gremlin.

### 16.5 Default parameter values

You can give a parameter a default value.

```python
def hello(to="world"):
    print("hello,", to)


hello()
hello("David")
```

Output:

```text
hello, world
hello, David
```

When no argument is passed, Python uses the default value.

---

## 17. `main()` and Program Organization

### 17.1 Why use `main()`?

As programs grow, you need structure.

A common pattern is:

```python
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
```

This helps organize the program.

### 17.2 Important: order matters for calling

Python reads the file from top to bottom.

This is okay:

```python
def main():
    hello()


def hello():
    print("hello")


main()
```

Why?

Because by the time `main()` is called at the bottom, Python has already seen both function definitions.

This can be a problem:

```python
main()


def main():
    hello()


def hello():
    print("hello")
```

Python tries to call `main()` before it knows what `main()` is.

So put the function call after the function definitions.

---

## 18. Scope

### 18.1 What is scope?

**Scope** means where a variable exists and can be used.

Example:

```python
def main():
    name = input("What's your name? ")
    hello()


def hello():
    print(name)


main()
```

This does not work properly because `name` was created inside `main()`.

`hello()` does not automatically know about it.

### 18.2 Fix with parameters

```python
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to):
    print("hello,", to)


main()
```

Now `main()` passes the value of `name` into `hello()`.

---

## 19. Return Values

### 19.1 Side effect vs return value

Some functions do something visible.

Example:

```python
print("hello")
```

This prints to the screen.

That visible action is a **side effect**.

Other functions give back a value.

Example:

```python
name = input("What's your name? ")
```

`input()` returns what the user typed.

### 19.2 `return`

You can make your own function give back a value with `return`.

Example:

```python
def square(n):
    return n * n


x = int(input("x: "))
print(square(x))
```

If the user types `4`, output:

```text
16
```

### 19.3 Why not just print inside the function?

You could write:

```python
def square(n):
    print(n * n)
```

But this only displays the result.

Using `return` is more flexible:

```python
def square(n):
    return n * n
```

Now you can:

```python
result = square(4)
print(result)
```

Or:

```python
print(square(4) + square(5))
```

A returned value can be reused.

A printed value is just shown on the screen.

### 19.4 `return` ends the function

When Python reaches `return`, the function gives back the value and stops.

---

## 20. Important Vocabulary

| Term | Meaning |
|---|---|
| Program | A set of instructions for the computer |
| Terminal | Place where you type commands |
| Function | Reusable action |
| Argument | Value passed into a function |
| Parameter | Variable inside a function definition |
| Variable | Container for a value |
| Assignment | Storing a value using `=` |
| String / `str` | Text |
| Integer / `int` | Whole number |
| Float | Decimal number |
| Comment | Note ignored by Python |
| Pseudocode | Plain-language plan for code |
| Bug | Mistake in code |
| Debugging | Finding and fixing mistakes |
| Side effect | Visible action caused by a function, like printing |
| Return value | Value a function gives back |
| Scope | Where a variable exists and can be used |

---

## 21. Best Beginner Patterns from This Lecture

### 21.1 Greeting program

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

### 21.2 Add two integers

```python
x = int(input("x: "))
y = int(input("y: "))

print(x + y)
```

### 21.3 Divide two floats and format result

```python
x = float(input("x: "))
y = float(input("y: "))

z = x / y

print(f"{z:.2f}")
```

### 21.4 Function with parameter

```python
def hello(to="world"):
    print("hello,", to)


name = input("What's your name? ")
hello(name)
```

### 21.5 Function with return

```python
def square(n):
    return n * n


x = int(input("x: "))
print(square(x))
```

### 21.6 Organized with `main()`

```python
def main():
    x = int(input("x: "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```

---

## 22. Common Beginner Mistakes

### Mistake 1: Thinking `code hello.py` runs the file

Wrong idea:

```bash
code hello.py
```

This only opens the file.

To run it:

```bash
python hello.py
```

---

### Mistake 2: Putting variable names inside quotes

Wrong:

```python
print("hello, name")
```

Correct:

```python
print("hello,", name)
```

or:

```python
print(f"hello, {name}")
```

---

### Mistake 3: Forgetting that `input()` returns a string

This:

```python
x = input("x: ")
y = input("y: ")
print(x + y)
```

does text joining, not math.

Use:

```python
x = int(input("x: "))
y = int(input("y: "))
print(x + y)
```

---

### Mistake 4: Forgetting parentheses

Wrong:

```python
print("hello"
```

Correct:

```python
print("hello")
```

---

### Mistake 5: Forgetting the `f` in f-strings

Wrong:

```python
print("hello, {name}")
```

Correct:

```python
print(f"hello, {name}")
```

---

### Mistake 6: Writing too much code on one line

This works:

```python
print(int(input("x: ")) + int(input("y: ")))
```

But this is easier to understand:

```python
x = int(input("x: "))
y = int(input("y: "))

print(x + y)
```

---

---

# Final Mental Model

Lecture 0 teaches you this basic flow:

```text
Input → Store → Process → Output
```

Example:

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

- `input()` gets data
- `name =` stores it
- `.strip().title()` processes it
- `print()` outputs it

That pattern appears everywhere in programming.

Tiny program, big skeleton.