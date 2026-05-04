# CS50P - Lecture 1: Conditionals / 条件分岐

> Use this after watching the lecture and after trying the examples yourself.  
> This note is meant to help you review, understand, and remember Lecture 1.

---

## 0. Big Picture

Lecture 1 is about **conditionals**.

A conditional lets your program make a decision.

Instead of always running the same path, your program can ask a question:

> Is this condition true or false?

Then Python chooses what code to run.

Tiny mental picture:

```txt
input
→ question
→ True path or False path
→ output
```

In Lecture 0, your programs mostly moved in a straight line.

In Lecture 1, your programs start to branch.

This is where code stops being a train track and starts becoming a little decision tree. 🌱

---

## 1. What Is a Conditional?

A **conditional** is code that runs only when a condition is true.

Example:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```

This means:

1. Ask the user for `x`
2. Ask the user for `y`
3. Check if `x < y`
4. If that condition is true, print the message

If the condition is false, the indented code under `if` is skipped.

---

## 2. Boolean Expressions

A **Boolean expression** is an expression that becomes either:

```python
True
```

or:

```python
False
```

Example:

```python
x = 3
y = 5

print(x < y)
```

Output:

```txt
True
```

Because `3 < 5` is true.

Another example:

```python
x = 10
y = 2

print(x < y)
```

Output:

```txt
False
```

Because `10 < 2` is false.

Boolean values are the traffic lights of conditionals.

They tell Python:

```txt
True  → go inside this block
False → skip this block
```

---

## 3. Comparison Operators

Python gives us operators to compare values.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `<` | less than | `3 < 5` | `True` |
| `>` | greater than | `10 > 2` | `True` |
| `<=` | less than or equal to | `3 <= 3` | `True` |
| `>=` | greater than or equal to | `5 >= 10` | `False` |
| `==` | equal to | `4 == 4` | `True` |
| `!=` | not equal to | `4 != 5` | `True` |

---

## 4. Important: `=` vs `==`

This is one of the most important beginner distinctions.

### `=` means assignment

```python
x = 10
```

This means:

> Put the value `10` inside the variable `x`.

### `==` means comparison

```python
x == 10
```

This means:

> Is `x` equal to `10`?

Example:

```python
x = 10

if x == 10:
    print("x is ten")
```

### Common mistake

Wrong:

```python
if x = 10:
    print("x is ten")
```

This causes an error because `=` is not used to ask a question.

Use `==` when comparing.

Memory trick:

```txt
=   stores a value
==  asks if two values are equal
```

---

## 5. `if` Statements

An `if` statement asks a question.

Basic structure:

```python
if condition:
    code_to_run_if_true
```

Example:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```

Important details:

- `if` is not a function
- there are no parentheses required around the condition
- the line ends with `:`
- the code inside the `if` must be indented

---

## 6. Indentation Matters

Python uses indentation to know what belongs inside the `if`.

Correct:

```python
if x < y:
    print("x is less than y")
```

Wrong:

```python
if x < y:
print("x is less than y")
```

The second version causes an indentation error.

Python is very picky about indentation because indentation is structure.

Think of indentation like putting code inside a box.

```python
if x < y:
    # this line is inside the if box
    print("x is less than y")
```

---

## 7. Multiple `if` Statements

You can write multiple independent `if` statements.

Example:

```python
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")
```

This works.

But Python checks all three conditions one by one.

That means even after it finds one true condition, it still checks the others.

For small code, this is fine.

But when the conditions are connected, we can write it better with `elif` and `else`.

---

## 8. `elif`

`elif` means:

> else if

It gives Python another condition to check only if the previous condition was false.

Example:

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
```

This is better than three separate `if` statements because once Python finds a true condition, it skips the rest.

### Why this is useful

If `x < y` is true, then `x > y` and `x == y` cannot also be true.

So there is no need to check everything.

This improves:

- readability
- efficiency
- logic clarity

---

## 9. `else`

`else` catches everything that was not caught before.

Example:

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

Why can we use `else` here?

Because if `x` is not less than `y`, and `x` is not greater than `y`, then the only remaining possibility is that they are equal.

So this:

```python
elif x == y:
```

can become:

```python
else:
```

### Mental model

```txt
if      → first question
elif    → another question if the first was false
else    → backup path if nothing above was true
```

---

## 10. Control Flow

**Control flow** means the order in which Python runs your code.

With conditionals, Python does not always run every line.

Example:

```python
if x < y:
    print("less")
elif x > y:
    print("greater")
else:
    print("equal")
```

Only one of these branches runs.

This is control flow:

```txt
Start
→ Check x < y
   → True: print "less" and stop this chain
   → False: check x > y
       → True: print "greater" and stop this chain
       → False: print "equal"
```

---

## 11. `or`

`or` lets you combine conditions.

The whole expression is true if **at least one** condition is true.

Example:

```python
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

This means:

> If the name is Harry, Hermione, or Ron, print Gryffindor.

### Truth table for `or`

| A | B | `A or B` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

### Common mistake

Wrong:

```python
if name == "Harry" or "Hermione" or "Ron":
    print("Gryffindor")
```

This looks natural in English, but it is wrong in Python.

You need to compare the variable each time:

```python
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
```

Better later:

```python
if name in ["Harry", "Hermione", "Ron"]:
    print("Gryffindor")
```

The `in` version is not the main Lecture 1 focus, but it is useful to know.

---

## 12. `and`

`and` lets you require multiple conditions to be true.

The whole expression is true only if **all** conditions are true.

Example:

```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
```

This means:

> If the score is at least 90 and at most 100, print Grade A.

### Truth table for `and`

| A | B | `A and B` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

### Example with grades

```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

This works, but Python can make it cleaner.

---

## 13. Chained Comparisons

Python lets us chain comparisons.

Instead of this:

```python
if score >= 90 and score <= 100:
    print("Grade: A")
```

You can write:

```python
if 90 <= score <= 100:
    print("Grade: A")
```

This reads almost like math:

```txt
90 <= score <= 100
```

Meaning:

> score is between 90 and 100, inclusive.

Another example:

```python
if 0 <= score <= 59:
    print("Grade: F")
```

Chained comparisons are often more readable.

---

## 14. Better Grade Logic

You do not always need both lower and upper limits if you organize conditions carefully.

Example:

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

Why does this work?

Because Python checks from top to bottom.

If `score` is `95`, the first condition is true and Python prints `A`.

If `score` is `85`, the first condition is false, then the second condition is true, so Python prints `B`.

You do not need to write:

```python
score >= 80 and score < 90
```

because if Python reached the `elif score >= 80` line, it already knows `score` was not `>= 90`.

The earlier checks already filtered the score.

---

## 15. Bugs in Conditional Logic

A program can run without syntax errors but still be logically wrong.

Example:

```python
score = int(input("Score: "))

if score >= 60:
    print("Grade: D")
elif score >= 70:
    print("Grade: C")
elif score >= 80:
    print("Grade: B")
elif score >= 90:
    print("Grade: A")
else:
    print("Grade: F")
```

This is wrong.

Why?

If the score is `95`, Python checks:

```python
score >= 60
```

That is true.

So it prints:

```txt
Grade: D
```

and skips the rest.

The order matters.

Correct order:

```python
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

### Lesson

With `if/elif/else`, Python checks from top to bottom.

Put the most specific or highest priority conditions first.

---

## 16. Modulo `%`

The modulo operator `%` gives the remainder after division.

Example:

```python
print(4 % 2)
```

Output:

```txt
0
```

Because 4 divides evenly by 2.

Another example:

```python
print(5 % 2)
```

Output:

```txt
1
```

Because 5 divided by 2 leaves a remainder of 1.

### Why modulo matters

Modulo is useful for checking patterns.

Common examples:

- even or odd numbers
- every second item
- every third row
- repeating cycles
- schedule patterns

---

## 17. Even or Odd

A number is even if it divides by 2 with no remainder.

```python
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

This means:

```txt
x % 2 == 0
```

> Divide `x` by 2 and check if the remainder is 0.

Examples:

| x | x % 2 | Result |
|---:|---:|---|
| 2 | 0 | Even |
| 3 | 1 | Odd |
| 10 | 0 | Even |
| 11 | 1 | Odd |

---

## 18. Creating Your Own Parity Function

Lecture 1 connects conditionals with custom functions from Lecture 0.

Example:

```python
def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
```

Here:

- `main()` controls the program
- `is_even(n)` checks if a number is even
- `return True` sends back a Boolean value
- `return False` sends back a Boolean value

The important part:

```python
if is_even(x):
```

This works because `is_even(x)` returns either `True` or `False`.

---

## 19. Making Boolean Functions Cleaner

This version works:

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

But it can be simplified.

Because this expression already becomes `True` or `False`:

```python
n % 2 == 0
```

We can return it directly:

```python
def is_even(n):
    return n % 2 == 0
```

This is cleaner and more Pythonic.

### Important idea

Do not write extra code when the expression already gives the answer.

This:

```python
return n % 2 == 0
```

is not magic.

It literally means:

> Return the result of the question “is `n % 2` equal to `0`?”

---

## 20. Pythonic Code

**Pythonic** means writing code in a way that feels natural, clean, and readable in Python.

Not just code that works.

Code that works **and** reads nicely.

Example:

Less Pythonic:

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

More Pythonic:

```python
def is_even(n):
    return n % 2 == 0
```

Both work.

The second version is cleaner.

### But warning

Pythonic does not mean “make it short until nobody understands it.”

Good code should be:

```txt
correct
readable
simple
easy to change
```

Clever code that turns your brain into soup is not better.

---

## 21. `match`

`match` is another way to handle multiple exact value cases.

Example with `if/elif/else`:

```python
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

This works, but it repeats `print("Gryffindor")`.

We can improve with `or`:

```python
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

Or use `match`:

```python
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

### Combining cases

You can combine cases with `|`:

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

Here:

```python
case _:
```

means:

> Default case / anything else

It is like `else`.

---

## 22. `match` vs `if`

Use `if` when you are checking conditions like:

```python
score >= 90
x < y
age >= 18 and has_id
```

Use `match` when you are checking exact values like:

```python
name == "Harry"
command == "start"
status == "paid"
```

Simple rule:

```txt
if    → flexible questions
match → exact-value menu
```

---

## 23. Common Beginner Mistakes

## Mistake 1: Using `=` instead of `==`

Wrong:

```python
if x = 5:
```

Correct:

```python
if x == 5:
```

---

## Mistake 2: Forgetting the colon

Wrong:

```python
if x < y
    print("less")
```

Correct:

```python
if x < y:
    print("less")
```

---

## Mistake 3: Forgetting indentation

Wrong:

```python
if x < y:
print("less")
```

Correct:

```python
if x < y:
    print("less")
```

---

## Mistake 4: Writing English-style `or`

Wrong:

```python
if name == "Harry" or "Hermione" or "Ron":
    print("Gryffindor")
```

Correct:

```python
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
```

---

## Mistake 5: Wrong order in grade checks

Wrong:

```python
if score >= 60:
    print("D")
elif score >= 90:
    print("A")
```

Correct:

```python
if score >= 90:
    print("A")
elif score >= 60:
    print("D")
```

---

## Mistake 6: Returning strings instead of Booleans by accident

Less useful:

```python
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

Better for checking:

```python
def is_even(n):
    return n % 2 == 0
```

If the function name starts with `is_`, it usually should return `True` or `False`.

---

## 24. Mini Project Ideas for Lecture 1

Use conditionals to build something small.

Good ideas:

1. **Grade calculator**
   - Input: score
   - Output: A, B, C, D, or F

2. **Even/Odd checker**
   - Input: number
   - Output: Even or Odd

3. **Simple login checker**
   - Input: username
   - Output: allowed / denied

4. **Factory shift classifier**
   - Input: hour
   - Output: morning shift / night shift / outside shift

5. **Discount calculator**
   - Input: order total
   - Output: discount or no discount

6. **Simple command menu**
   - Input: command like `add`, `delete`, `exit`
   - Output: action message

For your future automation goal, conditionals are huge.

Business rules are often just conditionals wearing a suit.

Example:

```python
if stock < minimum_stock:
    print("Order more")
else:
    print("Stock is okay")
```

That is already the baby version of inventory automation.

---

## 25. Lecture 1 Summary

Lecture 1 teaches how to make Python choose between different paths.

Main concepts:

- conditionals let programs make decisions
- Boolean expressions become `True` or `False`
- comparison operators ask questions
- `if` runs code when a condition is true
- `elif` checks another condition if the previous one was false
- `else` catches everything else
- `or` means at least one condition must be true
- `and` means all conditions must be true
- chained comparisons can make code cleaner
- `%` gives the remainder after division
- modulo helps check even/odd numbers
- functions can return Boolean values
- Pythonic code is clean and readable
- `match` can be useful for exact-value cases

The deeper lesson:

> Code becomes powerful when it can react to different situations.

Lecture 0 gave you words.

Lecture 1 gives your program judgment.

Tiny digital brain cell acquired. 🧠

---

## 26. Quick Review Checklist

Before moving to Lecture 2, make sure you can explain:

- [ ] What a conditional is
- [ ] What a Boolean expression is
- [ ] The difference between `=` and `==`
- [ ] How `if`, `elif`, and `else` work
- [ ] Why indentation matters
- [ ] How `or` works
- [ ] How `and` works
- [ ] Why condition order matters
- [ ] What `%` does
- [ ] How to check if a number is even
- [ ] Why `return n % 2 == 0` works
- [ ] What `match` does
- [ ] What `case _` means
- [ ] When to use `if` vs `match`

---

## 27. Suggested Folder Structure

```txt
CS50P_Week_1_Conditionals/
│
├── Review.md
├── Questions.md
├── summary.py
├── compare.py
├── grade.py
├── parity.py
├── house.py
└── mini_project.py
```

Keep it clean.

Your future self should open the folder and instantly know what is happening.

No archaeological digging through code fossils.
