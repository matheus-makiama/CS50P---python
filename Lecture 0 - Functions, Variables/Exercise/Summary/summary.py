"""
CS50P Lecture 0 Review File
Topic: Functions, Variables

How to use this file:
1. Run it with: python CS50P_L0_review.py
2. Read the comments slowly.
3. Change small things and run again.
4. Use this file as a memory map for Lecture 0.

This file intentionally includes many small examples from the seminar:
- print()
- input()
- variables
- comments
- strings / str methods
- parameters like sep and end
- f-strings
- int
- float
- round()
- functions with def
- default parameter values
- return values
- main()
- scope idea
"""


# ============================================================
# 1. FUNCTIONS: print()
# ============================================================

# print() is a function.
# A function is like an action Python already knows how to do.
# The text inside the parentheses is called an argument.

print("hello, world")


# ============================================================
# 2. VARIABLES + input()
# ============================================================

# input() asks the user a question and waits for an answer.
# IMPORTANT:
# input() always gives back text, also called a string / str.
#
# A variable is a name that stores a value.
# Here, the variable name stores what the user typed.

name = input("What's your name? ")


# ============================================================
# 3. STRING METHODS: strip(), title(), split()
# ============================================================

# A string is text.
# Python strings have methods, which are actions attached to the string.

# strip() removes extra spaces from the left and right.
name = name.strip()

# title() capitalizes the first letter of each word.
name = name.title()

# You can also chain methods in one line:
# name = input("What's your name? ").strip().title()

print(f"Cleaned name: {name}")


# split() separates a string into pieces.
# Example:
# "David Malan".split() becomes ["David", "Malan"]
#
# This gets the first word of the name.
# It is safer than: first, last = name.split(" ")
# because the user might type only one name.

first = name.split()[0]

print(f"First name: {first}")


# ============================================================
# 4. DIFFERENT WAYS TO PRINT STRINGS
# ============================================================

# Old/simple way: use + to join strings.
# You must manually add spaces.
print("Hello, " + first + "!")

# Better beginner way: pass multiple arguments to print().
# By default, print() adds a space between arguments.
print("Hello,", first)

# f-string way:
# Put f before the string, then put variables inside { }.
print(f"Hello, {first}!")


# ============================================================
# 5. print() PARAMETERS: sep and end
# ============================================================

# print() has parameters that change how it behaves.
#
# sep means separator.
# It controls what goes BETWEEN multiple arguments.
print("Hello", first, sep=", ")

# end controls what print adds at the END.
# By default, end is "\n", which means new line.
print("Hello, ", end="")
print(first)

# You can make the separator something unusual for testing.
print("Hello", first, sep="???")

# Useful mental model:
# print(*objects, sep=" ", end="\n")


# ============================================================
# 6. QUOTES INSIDE STRINGS
# ============================================================

# You can use double quotes outside and single quotes inside.
print("It's nice to meet you.")

# You can use single quotes outside and double quotes inside.
print('He said, "hello."')

# You can also escape quotes with a backslash.
print("He said, \"hello.\"")


# ============================================================
# 7. COMMENTS + PSEUDOCODE
# ============================================================

# This is a comment.
# Python ignores comments.
# Comments are for humans.
#
# Pseudocode means writing the plan in human language first.
# Example:
# 1. Ask user for x.
# 2. Ask user for y.
# 3. Add x and y.
# 4. Print the result.


# ============================================================
# 8. INTEGERS: int
# ============================================================

# input() gives text, so this would NOT do math correctly:
# x = input("What's x? ")
# y = input("What's y? ")
# print(x + y)
#
# If user types 1 and 2, that would print 12, not 3.
# Why? Because "1" + "2" joins text.

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y

print(f"{x} + {y} = {z}")


# ============================================================
# 9. INTEGER OPERATORS
# ============================================================

# Common math operators:
# + addition
# - subtraction
# * multiplication
# / division
# % remainder
# ** power

print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} ** 2 = {x ** 2}")


# ============================================================
# 10. FLOATS: float
# ============================================================

# float means a number with a decimal point.
# Example: 1.5, 3.14, 100.0
#
# Again, input() gives text, so we convert with float().

a = float(input("What's a? "))
b = float(input("What's b? Please do not type 0 yet: "))

c = a / b

print(f"{a} / {b} = {c}")


# ============================================================
# 11. ROUNDING AND FORMAT SPECIFIERS
# ============================================================

# round(number, ndigits)
# ndigits is optional.
# The square brackets in documentation often mean optional:
# round(number[, ndigits])

rounded = round(c, 2)
print(f"Rounded with round(c, 2): {rounded}")

# For display, f-string formatting is often cleaner.
# :.2f means show 2 digits after the decimal point.
print(f"Formatted to 2 decimal places: {c:.2f}")

# :, adds commas every 3 digits.
big_number = 1234567
print(f"Comma formatting: {big_number:,}")


# ============================================================
# 12. DEFINING YOUR OWN FUNCTIONS: def
# ============================================================

# def creates your own function.
# This function has one parameter: to
# The default value is "world".
# So if nobody gives a name, it says hello to world.

def hello(to="world"):
    print(f"hello, {to}")


hello()
hello(first)


# ============================================================
# 13. RETURN VALUES
# ============================================================

# Some functions only do something, like print().
# Some functions give a value back.
# return sends a value back to the place where the function was called.

def square(n):
    return n ** 2


number = int(input("Give me a number to square: "))

answer = square(number)

print(f"{number} squared is {answer}")


# These are 3 possible ways to square a number:
# n * n
# n ** 2
# pow(n, 2)


# ============================================================
# 14. main() FUNCTION
# ============================================================

# In bigger files, it is cleaner to put your program inside main().
# This makes the code easier to organize and read.
#
# The lecture shows this style:
#
# def main():
#     name = input("What's your name? ")
#     hello(name)
#
# def hello(to="world"):
#     print("hello,", to)
#
# main()


# ============================================================
# 15. SCOPE IDEA
# ============================================================

# Scope means where a variable exists.
# A variable created inside a function usually belongs to that function.
#
# Example:
#
# def example():
#     message = "I exist inside this function"
#
# print(message)  # This would cause an error.
#
# You do not need to master scope yet.
# For now, remember:
# Variables inside functions are usually local to that function.


# ============================================================
# 16. CLEAN VERSION OF THE SAME IDEAS
# ============================================================

# This is what a clean beginner program can look like:


def main():
    user_name = input("What's your name again? ").strip().title()
    hello(user_name)

    user_number = int(input("Pick one final integer: "))
    print(f"{user_number} squared is {square(user_number)}")


# Calling main() starts the clean program.
main()


# ============================================================
# END OF LECTURE 0 REVIEW
# ============================================================

# Review questions:
# 1. What does input() return?
# 2. Why do we use int(input(...))?
# 3. What is the difference between "1" + "2" and 1 + 2?
# 4. What does strip() do?
# 5. What does title() do?
# 6. What does sep do in print()?
# 7. What does end do in print()?
# 8. What is an f-string?
# 9. What does return do?
# 10. Why can main() make code easier to read?
"""
"""
