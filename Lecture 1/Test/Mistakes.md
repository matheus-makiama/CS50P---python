# CS50P Lecture 1 — Corrections Workbook

> This file only includes answers that were **wrong, incomplete, or worth correcting**.  
> The questions you answered correctly are intentionally not included.  
> Use this as a repair sheet, not a full answer key.

---

## Quick Summary

You understood a lot of the lecture well, especially basic comparisons, grade logic, modulo outputs, and reading simple `if / elif / else` programs.

The main things to fix are:

- `!=` means **not equal to**, not just “not”
- `and` requires **both** sides to be true
- `or` must compare the variable each time, unless you use `in`
- non-empty strings like `"Ron"` are automatically truthy in Python
- chained comparisons must point in the correct direction: `90 <= score <= 100`
- `return n % 2 == 0` already returns both `True` and `False`
- `n % n == 0` is not an even check
- `case _:` means “anything else,” not “empty”
- `=` assigns a value, while `==` compares values
- some `else` blocks were unnecessary because all possible cases were already covered
- small typos like `pirnt` break the whole spellbook

Your biggest pattern mistake was not the big idea of conditionals.  
It was **Boolean logic syntax**, especially `or`, `and`, and chained comparisons.

---

# Corrections

## Question 4 — What is control flow?

### Your answer

> Not sure but if i was to guess, I'd say it's controling the flow onf the programm to work smoothly

### What needs fixing

Your instinct is close, but “work smoothly” is too vague.

**Control flow** means the order in which Python runs your code.

Normally, Python reads code from top to bottom.  
But conditionals, loops, and functions can change that path.

### Correct idea

Control flow is the path the program follows while running.

For example:

```python
if age >= 18:
    print("Adult")
else:
    print("Not adult")
```

Depending on the value of `age`, Python follows a different branch.

### Mental model

Control flow is the program’s road system.

`if`, `elif`, and `else` are the traffic signs.

---

## Question 10 — What does `!=` mean?

### Your answer

> not

### What needs fixing

`!=` does not mean just “not.”

It means **not equal to**.

### Correct idea

```python
10 != 5
```

means:

```text
10 is not equal to 5
```

So this is `True`:

```python
print(10 != 5)
```

Output:

```text
True
```

### Mental model

`==` asks:

> Are these the same?

`!=` asks:

> Are these different?

---

## Question 16 — What does an `if` statement do?

### Your answer

> If is always checked and you can set a condition with if and if it matches it excecute.

### What needs fixing

The idea is mostly right, but the wording should be clearer.

An `if` statement checks a condition.  
If the condition is `True`, Python runs the indented code below it.

### Correct idea

```python
if x < y:
    print("x is less than y")
```

Python checks:

```python
x < y
```

If that expression is `True`, it prints the message.

If it is `False`, Python skips that indented block.

---

## Question 19 — Why does indentation matter in Python?

### Your answer

> to define the scope of what works how

### What needs fixing

You are close, but for conditionals, the better word is **block**, not only scope.

Indentation tells Python which lines belong inside an `if`, `elif`, `else`, function, loop, etc.

### Correct idea

```python
if x < y:
    print("less")
```

The indented line belongs to the `if` block.

This is wrong:

```python
if x < y:
print("less")
```

because Python cannot tell what code belongs inside the `if`.

### Mental model

Indentation is Python’s way of saying:

> “This line lives inside that block.”

No indentation, no house. 🏚️

---

## Question 27 — Why does Python not need to check later branches after one condition is true?

### Your answer

> because it is considered a set elif and else comes with the if before so if one of them is true it goes to the next code. you could actually make the if inside a if if you use the indentation but I suppose he didint talk about this yet.

### What needs fixing

You got the general idea, but it needs to be sharper.

In an `if / elif / else` chain, Python chooses **only the first true branch**.

After one branch runs, Python skips the rest of that chain.

### Correct idea

```python
score = 95

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
```

Python checks:

```python
score >= 90
```

That is `True`, so it prints:

```text
A
```

Then it skips `elif score >= 80`, even though that condition is also technically true.

### Mental model

An `if / elif / else` chain is not a buffet.

Python does not take every true dish.  
It takes the first one and leaves the restaurant.

---

## Question 32 — What is the output?

### Code

```python
print(True and False)
```

### Your answer

> True

### What needs fixing

This should be `False`.

With `and`, **both sides must be true**.

### Correct output

```text
False
```

### Why

```python
True and False
```

means:

> Is the left side true AND is the right side true?

The right side is `False`, so the whole expression becomes `False`.

### Mini truth table

```python
True and True    # True
True and False   # False
False and True   # False
False and False  # False
```

### Mental model

`and` is strict.

One false ingredient poisons the soup.

---

## Questions 34–35 — What is wrong with this `or` code?

### Code

```python
name = "Harry"

if name == "Harry" or "Hermione" or "Ron":
    print("Gryffindor")
```

### Your answer

> too long? kinda confusing perhaps  
> Id use the match

and:

```python
not sure how to change it useing "or" tho, looks fine to me
```

### What needs fixing

This code looks natural in English, but Python does not read it the way humans do.

Python sees it like this:

```python
if (name == "Harry") or ("Hermione") or ("Ron"):
```

The problem is:

```python
"Hermione"
```

and:

```python
"Ron"
```

are non-empty strings.

In Python, non-empty strings are considered **truthy**.

So the condition is basically always true.

### Correct version using `or`

```python
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
```

### Cleaner version using `in`

```python
if name in ["Harry", "Hermione", "Ron"]:
    print("Gryffindor")
```

### Correct version using `match`

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
```

### Mental model

Python does not understand this shortcut:

```python
name == "Harry" or "Ron"
```

You must say the full thought:

```python
name == "Harry" or name == "Ron"
```

Unless you use `in`, which is the clean little shortcut key.

---

## Question 36 — Check if `score` is at least 90 and at most 100

### Your answer

```python
if 90 <= score >= 100:
    return
```

### What needs fixing

The comparison signs are pointing the wrong way for the second part.

This:

```python
90 <= score >= 100
```

means:

```python
score >= 90 and score >= 100
```

So it really means:

> score is at least 100

That is not what the question asked.

### Correct version

```python
if 90 <= score <= 100:
    print("A")
```

### Same idea using `and`

```python
if score >= 90 and score <= 100:
    print("A")
```

### Mental model

For a range, trap the number between two walls:

```python
90 <= score <= 100
```

`score` is inside the cage. 🧃

---

## Questions 53–54 — How do you check if a number is even or odd?

### Your answers

```python
if x % 2 == 0:
    return
```

and:

```python
if x % 2 != 0:
    return
```

### What needs fixing

The condition is right, but the answer is incomplete.

`return` by itself does not explain what you are returning or printing.

### Correct idea: checking even

```python
x % 2 == 0
```

This expression gives `True` if `x` is even.

### Correct idea: checking odd

```python
x % 2 != 0
```

This expression gives `True` if `x` is odd.

### In an `if` statement

```python
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### In a function

```python
def is_even(x):
    return x % 2 == 0
```

---

## Question 55 — Print `Even` or `Odd`

### Your answer

```python
number = int(input("Choose a number :"))

if number % 2 == 0:
    print("Even")
elif number % 2 != 0:
    print("Even")
else:
    print("Invalid input, please try again.")
```

### What needs fixing

The odd branch prints the wrong word.

This part:

```python
elif number % 2 != 0:
    print("Even")
```

should print:

```python
print("Odd")
```

Also, after converting with `int()`, every integer is either even or odd.  
So the final `else` is not needed here.

### Correct version

```python
number = int(input("Choose a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Why `else` is enough

If a number is not even, it must be odd.

So this:

```python
elif number % 2 != 0:
```

is not wrong, but it is unnecessary.

---

## Question 57 — What does `is_even(4)` return?

### Code

```python
def is_even(n):
    return n % 2 == 0
```

### Your answer

You left it blank.

### Correct answer

```python
True
```

### Why

```python
4 % 2
```

gives:

```python
0
```

So:

```python
4 % 2 == 0
```

is:

```python
True
```

---

## Question 58 — What does `is_even(5)` return?

### Code

```python
def is_even(n):
    return n % 2 == 0
```

### Your answer

> True

### What needs fixing

The correct answer is `False`.

### Why

```python
5 % 2
```

gives:

```python
1
```

So:

```python
5 % 2 == 0
```

becomes:

```python
1 == 0
```

That is:

```python
False
```

---

## Question 59 — Why does `return n % 2 == 0` work?

### Your answer

> because if the condition in the right is True it returns a True

### What needs fixing

This is half-right.

It does not only return `True`.  
It returns the result of the comparison, which can be either `True` or `False`.

### Correct idea

```python
n % 2 == 0
```

is a Boolean expression.

So this:

```python
return n % 2 == 0
```

means:

> Return `True` if `n` is divisible by 2. Otherwise, return `False`.

### Example

```python
is_even(4)  # True
is_even(5)  # False
```

---

## Question 61 — Why is the Pythonic version cleaner?

### Your answer

> I mean no need to specify the False because what matter is returning the True

### What needs fixing

The reason is not only that you do not need to specify `False`.

The deeper reason is that the comparison already creates a Boolean value.

### Less clean version

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

### Cleaner version

```python
def is_even(n):
    return n % 2 == 0
```

### Why it is cleaner

This expression:

```python
n % 2 == 0
```

already evaluates to either `True` or `False`.

So wrapping it in `if / else` is extra packaging.

### Mental model

Do not put a box inside another box if the first box already holds the answer.

---

## Question 65 — What does `case` mean in a `match` statement?

### Your answer

> Its like if its case "Harry" like in the case that its --- i think

### What needs fixing

You are circling the right idea, but it needs a clean definition.

### Correct idea

A `case` is one possible pattern that Python compares against the value in `match`.

```python
match name:
    case "Harry":
        print("Gryffindor")
```

This means:

> If `name` matches the pattern `"Harry"`, run this block.

### Mental model

`match` says:

> “Here is the value.”

`case` says:

> “Does it look like this?”

---

## Question 66 — What does `case _:` mean?

### Your answer

> if its empty

### What needs fixing

`case _:` does **not** mean empty.

It means:

> anything else that did not match before

It is the default case.

### Correct idea

```python
match name:
    case "Harry":
        print("Gryffindor")
    case _:
        print("Who?")
```

If `name` is not `"Harry"`, Python runs:

```python
case _:
```

### Example

If:

```python
name = "Matheus"
```

Output:

```text
Who?
```

### Mental model

`case _:` is the “everything else drawer.”

Not empty.  
Everything that survived the earlier filters.

---

## Question 70 — Exact output matters

### Code

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

### Your answer

> Who

### What needs fixing

The idea is right, but the exact output includes the question mark.

### Correct output

```text
Who?
```

### Why this matters

When reading code, the exact printed text matters.

Python prints exactly what is inside the quotes.

---

# Practice Task Corrections

## Question 81 — Compare two numbers

### Your code

```python
x = int(input("What's \"x\"? :"))
y = int(input("What's \"y\"? :"))

if x > y:
    print("Greater!")
elif x < y:
    print("Less,,,")
elif x == y:
    print("Equal")
else:
    print("Invalid input, please try again.")
```

### What needs fixing

This works, but the last `else` is unnecessary.

For two numbers, there are only three possibilities:

1. `x > y`
2. `x < y`
3. `x == y`

So the final branch can simply be `else`.

### Cleaner version

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
```

### Mental model

If every possible road is already covered, you do not need an extra emergency tunnel.

---

## Question 82 — Grade calculator

### Your code

```python
score = int(input("What's your score? :"))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif 0 <= score > 60:
    print("Grade: F")
else:
    print("Invalid input, please try again!")
```

### What needs fixing

This line is wrong:

```python
elif 0 <= score > 60:
```

It means:

```python
score >= 0 and score > 60
```

But if `score > 60`, one of the earlier branches probably already caught it.

So a score like `50` will not print `F`.  
It goes to `else` and says invalid, even though `50` is a valid failing score.

### Simple correct version

```python
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Version with validation

```python
score = int(input("Score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Mental model

For grades, either:

- validate first, then grade
- or keep it simple and let `else` mean F

Do not twist the comparison signs into a pretzel.

---

## Question 83 — Write `is_even(n)`

### Your code

```python
def is_even(n):
    return n % n == 0
```

### What needs fixing

This does not check whether a number is even.

For most non-zero numbers:

```python
n % n
```

is always:

```python
0
```

Examples:

```python
5 % 5 == 0   # True
7 % 7 == 0   # True
9 % 9 == 0   # True
```

So your function would say almost every number is even.

Also, if `n` is `0`, this crashes:

```python
0 % 0
```

because division by zero is not allowed.

### Correct version

```python
def is_even(n):
    return n % 2 == 0
```

### Why

Even numbers are divisible by `2` with no remainder.

```python
4 % 2 == 0  # True
5 % 2 == 0  # False
```

### Mental model

To check even, compare the number against `2`, not against itself.

`n % n` is a mirror.  
`n % 2` is the evenness test.

---

## Question 84 — Use `is_even(n)` to print `Even` or `Odd`

### Your code

```python
def main():
    number = int(input("Type a number :"))
    if is_even(number) == True:
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % n == 0

main()
```

### What needs fixing

There are two issues.

### Issue 1 — The even check is wrong

Same issue as Question 83:

```python
return n % n == 0
```

should be:

```python
return n % 2 == 0
```

### Issue 2 — `== True` is unnecessary

This works:

```python
if is_even(number) == True:
```

But it is not the cleanest style.

Since `is_even(number)` already returns `True` or `False`, you can write:

```python
if is_even(number):
```

### Correct version

```python
def main():
    number = int(input("Type a number: "))

    if is_even(number):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
```

### Mental model

If a function already answers yes/no, do not ask:

> “Is yes/no equal to yes?”

Just use the answer directly.

---

## Question 85 — Hogwarts house using `if / elif / else`

### Your code

```python
name = input("What's your name? :")

if name == "Harry" or "Ron" or "Harmiony":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin") 
else:
    print("Who are you?")
```

### What needs fixing

This has the same `or` problem from Questions 34–35.

Python reads this:

```python
if name == "Harry" or "Ron" or "Harmiony":
```

as:

```python
if (name == "Harry") or ("Ron") or ("Harmiony"):
```

Since `"Ron"` is a non-empty string, it is truthy.  
So this condition is basically always true.

Also, `Hermione` is misspelled.

### Correct version using `or`

```python
name = input("What's your name? ").strip().title()

if name == "Harry" or name == "Ron" or name == "Hermione":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who are you?")
```

### Cleaner version using `in`

```python
name = input("What's your name? ").strip().title()

if name in ["Harry", "Ron", "Hermione"]:
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who are you?")
```

### Mental model

Never write:

```python
if name == "Harry" or "Ron":
```

Write either:

```python
if name == "Harry" or name == "Ron":
```

or:

```python
if name in ["Harry", "Ron"]:
```

---

## Question 86 — Hogwarts house using `match`

### Your code

```python
 name == input("What's your name? :")

 match name:
    case "Harry" | "Ron" | "Harmiony":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who are you?")
```

### What needs fixing

There are three issues.

### Issue 1 — You used `==` instead of `=`

This is wrong:

```python
name == input("What's your name? :")
```

`==` compares values.  
It does not assign the input to `name`.

You need:

```python
name = input("What's your name? ")
```

### Issue 2 — Extra indentation at the beginning

This line should not start with a random space:

```python
 match name:
```

At the top level, it should start at the left edge:

```python
match name:
```

### Issue 3 — `Hermione` is misspelled

You wrote:

```python
"Harmiony"
```

Correct spelling:

```python
"Hermione"
```

### Correct version

```python
name = input("What's your name? ").strip().title()

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who are you?")
```

### Mental model

`=` stores.  
`==` asks.

```python
name = input(...)
```

means:

> Store the input in `name`.

```python
name == input(...)
```

means:

> Compare `name` with the input.

Different spell. Different creature.

---

## Question 87 — Age category program

### Your code

```python
age = int(input("What's your age? :"))

if age >= 20:
    print("Adult")
elif age >= 13:
    print("Teen")
elif age < 13:
    pirnt("Child")
else:
    print("Please try again!")
```

### What needs fixing

The logic is mostly good, but there is a typo:

```python
pirnt("Child")
```

should be:

```python
print("Child")
```

Also, the final `else` is unnecessary because every integer age is either:

- 20 or older
- 13 to 19
- under 13

### Correct version

```python
age = int(input("What's your age? "))

if age >= 20:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

### Version with validation

```python
age = int(input("What's your age? "))

if age < 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
else:
    print("Adult")
```

### Mental model

Typos are tiny landmines.

`print` is a function.  
`pirnt` is just Python staring at you like: “Who invited this?”

---

## Question 88 — Discount program

### Your code

```python
order_total = int(input("What's the total of your order? :"))

if order_total >= 100:
    print("Discount applied!")
elif order_total < 100:
    print("No discount")
else:
    print("Please try again!")
```

### What needs fixing

This works, but the final `else` is unnecessary.

A number is either:

- `>= 100`
- `< 100`

There is no third possibility after `int()` succeeds.

### Cleaner version

```python
order_total = int(input("What's the total of your order? "))

if order_total >= 100:
    print("Discount applied")
else:
    print("No discount")
```

### Mental model

When there are only two doors, use `if / else`.

No need to build a third door into a wall.

---

## Question 89 — Command program using `match`

### Your code

```python
command = input("Choose your command - [\"start\", \"stop\",\"help\"] \n:")

match command:
    case "start":
        print("Initiating the programm")
    case "stop":
        print("Stopping the programm")
    case "help":
        print("Here's the link to the help page.")
```

### What needs fixing

This is mostly correct, but you should add a default case.

Without `case _:`, nothing happens if the user types something unexpected.

### Better version

```python
command = input("Choose a command: start, stop, or help: ").strip().lower()

match command:
    case "start":
        print("Starting the program")
    case "stop":
        print("Stopping the program")
    case "help":
        print("Here is the help page")
    case _:
        print("Unknown command")
```

### Why `.strip().lower()` helps

```python
.strip()
```

removes extra spaces.

```python
.lower()
```

makes the input lowercase.

So:

```text
 Start 
```

becomes:

```text
start
```

### Mental model

`case _:` is the safety net.

Without it, weird input falls into the void.

---

# Extra Mini Review

## The mistakes to remember

### 1. `and` needs both sides to be true

```python
True and False
```

is:

```python
False
```

### 2. Repeat the comparison when using `or`

Wrong:

```python
if name == "Harry" or "Ron":
```

Correct:

```python
if name == "Harry" or name == "Ron":
```

Cleaner:

```python
if name in ["Harry", "Ron"]:
```

### 3. Use the correct chained comparison for ranges

Wrong:

```python
90 <= score >= 100
```

Correct:

```python
90 <= score <= 100
```

### 4. Even numbers use `% 2`, not `% n`

Wrong:

```python
return n % n == 0
```

Correct:

```python
return n % 2 == 0
```

### 5. `case _:` means anything else

Wrong idea:

```text
case _ means empty
```

Correct idea:

```text
case _ means default / anything else
```

### 6. `=` and `==` are different

```python
name = input("Name: ")
```

stores a value.

```python
name == "Harry"
```

compares a value.

### 7. Exact output matters

If the code says:

```python
print("Who?")
```

The output is:

```text
Who?
```

not:

```text
Who
```

---

# Tiny Practice to Fix the Weak Spots

Try these again without looking.

## Practice 1 — Fix the `or` condition

Wrong:

```python
if name == "Harry" or "Ron" or "Hermione":
    print("Gryffindor")
```

**Your corrected code:**

```python

```

---

## Practice 2 — Fix the range check

Wrong:

```python
if 90 <= score >= 100:
    print("A")
```

**Your corrected code:**

```python

```

---

## Practice 3 — Fix the even function

Wrong:

```python
def is_even(n):
    return n % n == 0
```

**Your corrected code:**

```python

```

---

## Practice 4 — What does this print?

```python
print(True and False)
```

**Your answer:**



---

## Practice 5 — What does `case _:` mean?

**Your answer:**



---

## Practice 6 — Fix this `match` input line

Wrong:

```python
name == input("What's your name? ")
```

**Your corrected code:**

```python

```

---

# Final Mental Model

You are understanding the concepts.  
The weak spots are mostly syntax traps and Boolean logic.

The four dragons to defeat before Lecture 2 are:

```python
or
```

```python
and
```

```python
% 2
```

```python
case _
```

If you fix those, your Lecture 1 foundation becomes much stronger.

Right now, the biggest villain is this pattern:

```python
if name == "Harry" or "Ron":
```

Burn it from memory.

Replace it with:

```python
if name == "Harry" or name == "Ron":
```

or better:

```python
if name in ["Harry", "Ron"]:
```

That one correction alone removes a lot of future bugs.
