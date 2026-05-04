# CS50P - Lecture 1: Conditionals Questions Workbook

> Purpose: active recall and practice only.  
> Do your separate free-memory writing in `Recall.md`.  
> This file is only for checking understanding, code reading, and code writing.

---

# A. Core Concepts

## 1. What does a conditional allow a program to do?

**Your answer:**

It allows the programm to behave differently based on the conditions set.

---

## 2. What is a Boolean expression?

**Your answer:**

It is a True or False ecpression.

---

## 3. What are the two Boolean values in Python?

**Your answer:**

True and False.

---

## 4. What is control flow?

**Your answer:**

Not sure but if i was to guess, I'd say it's controling the flow onf the programm to work smoothly

---

# B. Comparison Operators

## 5. What does `<` mean?

**Your answer:**

It means smaller than

---

## 6. What does `>` mean?

**Your answer:**

Bigger than

---

## 7. What does `<=` mean?

**Your answer:**

smaller or equal to

---

## 8. What does `>=` mean?

**Your answer:**

bigger or equal to

---

## 9. What does `==` mean?

**Your answer:**

equal

---

## 10. What does `!=` mean?

**Your answer:**

not

---

## 11. What is the difference between `=` and `==`?

**Your answer:**

= is to assigh the right vallue to the left, == is equal

---

## 12. What is the output?

```python
print(3 < 5)
```

**Your answer:**

True

---

## 13. What is the output?

```python
print(10 == 5)
```

**Your answer:**

False

---

## 14. What is the output?

```python
print(10 != 5)
```

**Your answer:**

True

---

## 15. What is the output?

```python
x = 4
y = 4

print(x <= y)
```

**Your answer:**

True

---

# C. `if`, `elif`, and `else`

## 16. What does an `if` statement do?

**Your answer:**

If is always checked and you can set a condition with if and if it matches it excecute.

---

## 17. What does `elif` mean?

**Your answer:**

if the if doesnt match it checks the elif.

---

## 18. What does `else` do?

**Your answer:**

if the if or elif set before it doesnt match it will excecute.

---

## 19. Why does indentation matter in Python?

**Your answer:**

to define the scope of what works how

---

## 20. What is wrong with this code?

```python
if x < y:
print("x is less than y")
```

**Your answer:**

no indentation on the print, it wont work

---

## 21. Fix the code above.

**Your answer:**

```python

if x < y:
    print("x is less than y")

```

---

## 22. What is wrong with this code?

```python
if x < y
    print("x is less than y")
```

**Your answer:**

forgot the : at the end of the if

---

## 23. Fix the code above.

**Your answer:**

```python

if x < y:
    print("x is less than y")

```

---

## 24. What does this code print if `x = 3` and `y = 5`?

```python
if x < y:
    print("less")
elif x > y:
    print("greater")
else:
    print("equal")
```

**Your answer:**

less

---

## 25. What does this code print if `x = 10` and `y = 5`?

```python
if x < y:
    print("less")
elif x > y:
    print("greater")
else:
    print("equal")
```

**Your answer:**

greater

---

## 26. What does this code print if `x = 7` and `y = 7`?

```python
if x < y:
    print("less")
elif x > y:
    print("greater")
else:
    print("equal")
```

**Your answer:**

equal

---

## 27. In an `if/elif/else` chain, why does Python not need to check the later branches after one condition is true?

**Your answer:**

because it is considered a set elif and else comes with the if before so if one of them is true it goes to the next code. you could actually make the if inside a if if you use the indentation but I suppose he didint talk about this yet.

---

# D. `or` and `and`

## 28. What does `or` mean?

**Your answer:**

literary if there "or" if one of the condition is met it works

---

## 29. What does `and` mean?

**Your answer:**

both condition have to be met

---

## 30. What is the output?

```python
print(True or False)
```

**Your answer:**

True

---

## 31. What is the output?

```python
print(False or False)
```

**Your answer:**

False

---

## 32. What is the output?

```python
print(True and False)
```

**Your answer:**

True

---

## 33. What is the output?

```python
print(True and True)
```

**Your answer:**

True

---

## 34. What is wrong with this code?

```python
name = "Harry"

if name == "Harry" or "Hermione" or "Ron":
    print("Gryffindor")
```

**Your answer:**

too long? kinda confusing perhaps
Id use the match

---

## 35. Fix the code above using `or`.

**Your answer:**

```python
not sure how to change it useing "or" tho, looks fine to me

```

---

## 36. Write a condition that checks if `score` is at least 90 and at most 100.

**Your answer:**

```python
if 90 <= score >= 100:
    return

```

---

## 37. What is the output?

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Denied")
```

**Your answer:**

Allowed

---

## 38. What is the output?

```python
age = 16
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Denied")
```

**Your answer:**

Denied

---

# E. Chained Comparisons and Grades

## 39. What does this condition mean?

```python
90 <= score <= 100
```

**Your answer:**

bigger or equal to 90 and smaller or equal to 100

---

## 40. Why can this be easier to read?

```python
if 90 <= score <= 100:
```

Compared to this:

```python
if score >= 90 and score <= 100:
```

**Your answer:**

less word simpler to understand and read in flow

---

## 41. What grade does this code print if `score = 95`?

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Your answer:**

A

---

## 42. What grade does this code print if `score = 85`?

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Your answer:**

B

---

## 43. What grade does this code print if `score = 72`?

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Your answer:**

C

---

## 44. What grade does this code print if `score = 50`?

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Your answer:**

F

---

## 45. Why does this code not need `score < 90` in the `elif score >= 80` line?

**Your answer:**

because the code go from top to bottom and if it not equal to or bgger than 90 it will automatically go to the 80 line swhich means there are no need to specify it.

---

## 46. What is wrong with this grade order?

```python
if score >= 60:
    print("D")
elif score >= 70:
    print("C")
elif score >= 80:
    print("B")
elif score >= 90:
    print("A")
else:
    print("F")
```

**Your answer:**

even if its 95 it will get the D, it should be the reverse.

---

## 47. If `score = 95`, what does the wrong code above print?

**Your answer:**

D

---

## 48. Fix the wrong grade code.

**Your answer:**

```python

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

```

---

# F. Modulo and Parity

## 49. What does the modulo operator `%` do?

**Your answer:**

it devides the number with the number in the right and shows the remaining.

---

## 50. What is the output?

```python
print(4 % 2)
```

**Your answer:**

0

---

## 51. What is the output?

```python
print(5 % 2)
```

**Your answer:**

1

---

## 52. What is the output?

```python
print(10 % 3)
```

**Your answer:**

1

---

## 53. How do you check if a number `x` is even?

**Your answer:**

```python

if x % 2 == 0:
    return

```

---

## 54. How do you check if a number `x` is odd?

**Your answer:**

```python
if x % 2 != 0:
    return

```

---

## 55. Write code that asks the user for a number and prints `Even` or `Odd`.

**Your answer:**

```python

number = int(input("Choose a number :"))

if number % 2 == 0:
    print("Even")
elif number % 2 != 0:
    print("Even")
else:
    print("Invalid input, please try again.")

```

---

# G. Boolean Functions

## 56. What should a function named `is_even(n)` return?

**Your answer:**

True or False

---

## 57. What does this function return if `n = 4`?

```python
def is_even(n):
    return n % 2 == 0
```

**Your answer:**



---

## 58. What does this function return if `n = 5`?

```python
def is_even(n):
    return n % 2 == 0
```

**Your answer:**

True

---

## 59. Why does this work?

```python
return n % 2 == 0
```

**Your answer:**

because if the condition in the right is True it returns a True

---

## 60. Which version is more Pythonic?

Version A:

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

Version B:

```python
def is_even(n):
    return n % 2 == 0
```

**Your answer:**

B shorter cleaner

---

## 61. Why is the Pythonic version cleaner?

**Your answer:**

I mean no need to specify the False because what matter is returning the True

---

## 62. What is the output?

```python
def is_even(n):
    return n % 2 == 0


if is_even(20):
    print("Even")
else:
    print("Odd")
```

**Your answer:**

Even

---

## 63. What is the output?

```python
def is_even(n):
    return n % 2 == 0


if is_even(21):
    print("Even")
else:
    print("Odd")
```

**Your answer:**

Odd

---

# H. `match`

## 64. What does `match` do?

**Your answer:**

it checkes if the variable in the right side of match match the cases

---

## 65. What does `case` mean in a `match` statement?

**Your answer:**

Its like if its case "Harry"   like in the case that its --- i think

---

## 66. What does `case _:` mean?

**Your answer:**

if its empty

---

## 67. What does `|` mean inside a `case` pattern?

**Your answer:**

or

---

## 68. What does this code print if `name = "Harry"`?

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

**Your answer:**

Gryffindor

---

## 69. What does this code print if `name = "Draco"`?

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

**Your answer:**

Slytherin

---

## 70. What does this code print if `name = "Matheus"`?

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

**Your answer:**

Who

---

## 71. When is `match` useful?

**Your answer:**

When the input is determined in some patterns

---

## 72. When is `if` better than `match`?

**Your answer:**

when the input is not really determined by patterns

---

# I. Code Reading Practice

## 73. What does this program print?

```python
x = 2
y = 8

if x < y:
    print("small")
else:
    print("big")
```

**Your answer:**

small

---

## 74. What does this program print?

```python
x = 8
y = 2

if x < y:
    print("small")
else:
    print("big")
```

**Your answer:**

big

---

## 75. What does this program print?

```python
x = 5
y = 5

if x < y:
    print("less")
elif x > y:
    print("greater")
else:
    print("same")
```

**Your answer:**

same

---

## 76. What does this program print?

```python
score = 72

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Your answer:**

C

---

## 77. What does this program print?

```python
number = 14

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Your answer:**

Even

---

## 78. What does this program print?

```python
number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Your answer:**

Odd

---

## 79. What does this program print?

```python
x = 10
y = 20

if x > y:
    print("A")
elif x < y:
    print("B")
else:
    print("C")
```

**Your answer:**

B

---

## 80. What does this program print?

```python
command = "help"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case "help":
        print("Help menu")
    case _:
        print("Unknown")
```

**Your answer:**

Help menu

---

# J. Code Writing Practice

## 81. Write a program that asks for two numbers and prints whether `x` is less than, greater than, or equal to `y`.

**Your answer:**

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

---

## 82. Write a program that asks for a score and prints a letter grade.

**Your answer:**

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

---

## 83. Write a function called `is_even(n)` that returns `True` if `n` is even and `False` otherwise.

**Your answer:**

```python

def is_even(n):
    return n % n == 0

```

---

## 84. Write a program that asks for a number and uses your `is_even(n)` function to print `Even` or `Odd`.

**Your answer:**

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

---

## 85. Write a program that asks for a name and prints a Hogwarts house using `if/elif/else`.

**Your answer:**

```python

name = input("What's your name? :")

if name == "Harry" or "Ron" or "Harmiony":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin") 
else:
    print("Who are you?")


```

---

## 86. Write the same Hogwarts house program using `match`.

**Your answer:**

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

---

## 87. Write a program that asks for an age and prints:
- `Child` if age is under 13
- `Teen` if age is from 13 to 19
- `Adult` if age is 20 or older

**Your answer:**

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

---

## 88. Write a program that asks for an order total and prints:
- `Discount applied` if total is 100 or more
- `No discount` otherwise

**Your answer:**

```python

order_total = int(input("What's the total of your order? :"))

if order_total >= 100:
    print("Discount applied!")
elif order_total < 100:
    print("No discount")
else:
    print("Please try again!")

```

---

## 89. Write a program that asks for a command: `start`, `stop`, or `help`. Use `match` to print the correct message.

**Your answer:**

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

---

## 90. Write one tiny Lecture 1 mini-project idea in one sentence.

**Your answer:**
I could make a simple chat bot that asks people to put into number theyre current mood or feeling from 1 to 10.
and depending on the answer he will say different things out of a random list perhaps to make the person feel good or to push the person etc.
it may even crack a joke.
the only work will be ion creating the list of output for each number and also, using the random function that i dont think i lerned here yet

---

# Final Self-Check

Before moving to Lecture 2, make sure you can do these without looking:

- [ ] Explain `if`, `elif`, and `else`
- [ ] Explain `or` and `and`
- [ ] Explain `=` vs `==`
- [ ] Fix indentation errors
- [ ] Use `%` to check even/odd
- [ ] Write a Boolean-returning function
- [ ] Explain why `return n % 2 == 0` works
- [ ] Use `match` with `case _`
- [ ] Write a small grade calculator
