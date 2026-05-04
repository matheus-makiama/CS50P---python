"""
CS50P Lecture 1 Review File
Topic: Conditionals / 条件分岐

How to use this file:
1. Run it with: python summary.py
2. Read the comments slowly.
3. Change small values and run again.
4. Use this file as a memory map for Lecture 1.

This file includes:
- Boolean expressions
- comparison operators
- if
- elif
- else
- control flow
- or
- and
- chained comparisons
- modulo %
- even/odd logic
- Boolean-returning functions
- Pythonic expressions
- match / case
- common beginner mistakes
"""


# ============================================================
# 1. BOOLEAN EXPRESSIONS
# ============================================================

# A Boolean expression is an expression that becomes either True or False.

print("1. Boolean expressions")
print(3 < 5)    # True
print(10 < 2)   # False
print(4 == 4)   # True
print(4 != 5)   # True
print()


# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================

# Common comparison operators:
#
# <   less than
# >   greater than
# <=  less than or equal to
# >=  greater than or equal to
# ==  equal to
# !=  not equal to
#
# Important:
# =  means assignment
# == means comparison

print("2. Comparison operators")

x = 10
y = 20

print(f"x = {x}")
print(f"y = {y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print()


# ============================================================
# 3. BASIC IF STATEMENT
# ============================================================

# if asks a question.
# If the answer is True, Python runs the indented block.
# If the answer is False, Python skips it.

print("3. Basic if statement")

x = 3
y = 5

if x < y:
    print("x is less than y")

print()


# ============================================================
# 4. MULTIPLE IF STATEMENTS
# ============================================================

# This works, but Python checks every condition separately.

print("4. Multiple if statements")

x = 5
y = 5

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")

print()


# ============================================================
# 5. IF / ELIF / ELSE
# ============================================================

# elif means "else if".
# Python checks from top to bottom.
# Once one branch is True, the rest of the chain is skipped.

print("5. if / elif / else")

x = 10
y = 3

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

print()


# ============================================================
# 6. CONTROL FLOW
# ============================================================

# Control flow means the order Python runs code.
#
# In an if / elif / else chain, usually only one branch runs.

print("6. Control flow example")

temperature = 28

if temperature >= 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")

# Since 28 >= 25 is True, Python prints "Warm"
# and skips the rest of this chain.

print()


# ============================================================
# 7. OR
# ============================================================

# or means at least one condition must be True.

print("7. or")

name = "Harry"

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# Beginner warning:
# This is wrong:
#
# if name == "Harry" or "Hermione" or "Ron":
#     print("Gryffindor")
#
# It sounds natural in English, but Python does not understand it that way.
# You must compare name each time, or use a cleaner approach like "in".

print()


# ============================================================
# 8. AND
# ============================================================

# and means all conditions must be True.

print("8. and")

score = 95

if score >= 90 and score <= 100:
    print("Grade: A")

print()


# ============================================================
# 9. CHAINED COMPARISONS
# ============================================================

# Python allows chained comparisons.
# This is cleaner than using "and" sometimes.

print("9. Chained comparisons")

score = 85

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

print()


# ============================================================
# 10. BETTER GRADE LOGIC
# ============================================================

# We can make grade logic simpler by ordering from highest to lowest.
# Why?
# Because if Python reaches "elif score >= 80",
# it already knows score was NOT >= 90.

print("10. Better grade logic")

score = 85

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

print()


# ============================================================
# 11. BUG EXAMPLE: WRONG ORDER
# ============================================================

# This is a logic bug.
# The code runs, but the result is wrong.
#
# If score is 95, the first condition score >= 60 is True,
# so Python prints D and skips the rest.
#
# This is why order matters.

print("11. Bug example: wrong order")

score = 95

if score >= 60:
    print("Wrong result: Grade D")
elif score >= 70:
    print("Grade C")
elif score >= 80:
    print("Grade B")
elif score >= 90:
    print("Grade A")
else:
    print("Grade F")

print("Correct version should check >= 90 first.")
print()


# ============================================================
# 12. MODULO %
# ============================================================

# % gives the remainder after division.
#
# 4 % 2 = 0 because 4 divides evenly by 2.
# 5 % 2 = 1 because 5 divided by 2 leaves remainder 1.

print("12. Modulo")

print(f"4 % 2 = {4 % 2}")
print(f"5 % 2 = {5 % 2}")
print(f"10 % 3 = {10 % 3}")
print()


# ============================================================
# 13. EVEN OR ODD
# ============================================================

# A number is even if number % 2 == 0.

print("13. Even or odd")

number = 11

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print()


# ============================================================
# 14. BOOLEAN-RETURNING FUNCTION
# ============================================================

# Function names that start with "is_" often return True or False.
# Example:
# is_even(n) should answer the question:
# "Is n even?"

print("14. Boolean-returning function")


def is_even_verbose(n):
    """Return True if n is even, otherwise return False."""
    if n % 2 == 0:
        return True
    else:
        return False


print(is_even_verbose(10))  # True
print(is_even_verbose(11))  # False
print()


# ============================================================
# 15. PYTHONIC VERSION
# ============================================================

# This expression already becomes True or False:
#
# n % 2 == 0
#
# So we can return that expression directly.

print("15. Pythonic version")


def is_even(n):
    """Return True if n is even, otherwise return False."""
    return n % 2 == 0


print(is_even(10))  # True
print(is_even(11))  # False

# Using the function in an if statement:

x = 12

if is_even(x):
    print(f"{x} is even")
else:
    print(f"{x} is odd")

print()


# ============================================================
# 16. MATCH / CASE
# ============================================================

# match checks a value against different cases.
# It can be useful when you are checking exact values.

print("16. match / case")

student = "Hermione"

match student:
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

print()


# ============================================================
# 17. MATCH WITH COMBINED CASES
# ============================================================

# You can combine cases with |
# case _ means default / anything else.

print("17. match with combined cases")

student = "Ron"

match student:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

print()


# ============================================================
# 18. IF VS MATCH
# ============================================================

# Use if when checking flexible conditions:
# - score >= 90
# - x < y
# - age >= 18 and has_id
#
# Use match when checking exact values:
# - command == "start"
# - name == "Harry"
# - status == "paid"

print("18. if vs match")

command = "start"

match command:
    case "start":
        print("Starting program...")
    case "stop":
        print("Stopping program...")
    case "help":
        print("Showing help...")
    case _:
        print("Unknown command")

print()


# ============================================================
# 19. MINI PRACTICE FUNCTIONS
# ============================================================

def compare_numbers(a, b):
    """Return a message comparing two numbers."""
    if a < b:
        return "a is less than b"
    elif a > b:
        return "a is greater than b"
    else:
        return "a is equal to b"


def get_grade(score):
    """Return a letter grade based on score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_house(name):
    """Return a Hogwarts house or Who? based on name."""
    match name:
        case "Harry" | "Hermione" | "Ron":
            return "Gryffindor"
        case "Draco":
            return "Slytherin"
        case _:
            return "Who?"


print("19. Mini practice functions")

print(compare_numbers(3, 5))
print(compare_numbers(10, 2))
print(compare_numbers(7, 7))

print(f"Score 95: Grade {get_grade(95)}")
print(f"Score 82: Grade {get_grade(82)}")
print(f"Score 50: Grade {get_grade(50)}")

print(f"Harry: {get_house('Harry')}")
print(f"Draco: {get_house('Draco')}")
print(f"Matheus: {get_house('Matheus')}")

print()


# ============================================================
# 20. OPTIONAL INTERACTIVE PRACTICE
# ============================================================

# You can uncomment this function call at the bottom if you want
# the file to ask you questions while running.
#
# Beginner tip:
# Keep the automatic examples above for review.
# Use the interactive part when you want active practice.


def interactive_practice():
    """Small interactive practice for Lecture 1."""

    print("Interactive practice")

    x = int(input("What's x? "))
    y = int(input("What's y? "))

    print(compare_numbers(x, y))

    number = int(input("Give me a number: "))

    if is_even(number):
        print("Even")
    else:
        print("Odd")

    score = int(input("Score: "))
    print(f"Grade: {get_grade(score)}")

    name = input("Name: ").strip().title()
    print(get_house(name))


# Uncomment this line if you want to practice with input:
# interactive_practice()


# ============================================================
# 21. FINAL MEMORY MAP
# ============================================================

print("Final memory map")
print("""
Lecture 1 is about conditionals.

Important ideas:
- Conditions become True or False.
- if runs code when a condition is True.
- elif checks another condition if the previous one was False.
- else catches everything else.
- or means at least one condition is True.
- and means all conditions are True.
- % gives the remainder after division.
- n % 2 == 0 checks if n is even.
- Functions can return Boolean values.
- Pythonic code is clean and readable.
- match is useful for exact-value cases.
""")
