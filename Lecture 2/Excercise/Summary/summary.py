#!/usr/bin/env python3
"""
CS50P Lecture 2 - Loops / ループ
summary.py

How to use this file:
1. Run: python summary.py
2. Read the printed output and comments.
3. Change small values, run again, and observe what changes.
4. Use this as a memory map for Lecture 2.

This file is intentionally a little verbose.
It is not only code that works. It is code that teaches.

Main topics:
- why loops exist
- while loops
- infinite loops
- counters and i += 1
- for loops
- range()
- underscore _ as a throwaway loop variable
- string multiplication
- validating user input with while True
- continue, break, and return
- lists
- indexes
- len()
- dictionaries
- lists of dictionaries
- None
- Mario-style rows, columns, and squares
"""


def section(number, title):
    """Print a clean section header."""
    print("\n" + "=" * 72)
    print(f"{number}. {title}")
    print("=" * 72)


# ---------------------------------------------------------------------------
# 1. WHY LOOPS EXIST
# ---------------------------------------------------------------------------

def demo_why_loops_exist():
    section(1, "Why loops exist")

    print("Without a loop, repeated code looks like this:")
    print("meow")
    print("meow")
    print("meow")

    print("\nThis works, but it is not good design if we need 50 or 500 meows.")
    print("A loop lets us say: do this action again and again.")


# ---------------------------------------------------------------------------
# 2. WHILE LOOPS
# ---------------------------------------------------------------------------

def demo_while_countdown():
    section(2, "while loop - counting down")

    print("A while loop keeps running while its condition is True.")
    print("Here, i starts at 3 and moves toward 0.")

    i = 3
    while i != 0:
        print(f"meow  | i is currently {i}")
        i = i - 1

    print("The loop stopped because i became 0.")


# Dangerous example kept as a comment on purpose.
# If you run this, it never stops because i never changes.
# Press Ctrl + C in the terminal to interrupt an accidental infinite loop.
#
# i = 3
# while i != 0:
#     print("meow")


def demo_while_countup():
    section(3, "while loop - counting up from 0")

    print("Programmers usually count from 0.")
    print("range-like thinking: start at 0, stop before 3.")

    i = 0
    while i < 3:
        print(f"meow  | i is currently {i}")
        i += 1  # same as i = i + 1

    print("The loop ran for i = 0, 1, 2. It stopped before 3.")


# ---------------------------------------------------------------------------
# 3. FOR LOOPS AND RANGE
# ---------------------------------------------------------------------------

def demo_for_range():
    section(4, "for loop with range()")

    print("A for loop is cleaner when you already know how many times to repeat.")
    print("range(3) gives the values 0, 1, 2.")

    for i in range(3):
        print(f"meow  | i is {i}")

    print("\nImportant: range(3) does not include 3.")


def demo_underscore_variable():
    section(5, "Using _ when you do not care about the loop variable")

    print("If the loop variable is not used, _ is a common Python convention.")

    for _ in range(3):
        print("meow")

    print("The _ says: Python needs a variable here, but I do not care about its value.")


# ---------------------------------------------------------------------------
# 4. STRING MULTIPLICATION
# ---------------------------------------------------------------------------

def demo_string_multiplication():
    section(6, "String multiplication")

    print("Python can multiply strings.")
    print('"meow" * 3 gives:')
    print("meow" * 3)

    print("\nTo put each meow on a new line, use \\n inside the string:")
    print("meow\n" * 3, end="")

    print("\nThe end=\"\" prevents print() from adding one extra blank line at the end.")


# ---------------------------------------------------------------------------
# 5. INPUT VALIDATION WITH WHILE TRUE
# ---------------------------------------------------------------------------

def get_positive_number():
    """
    Ask the user for a positive integer and return it.

    This function is not called automatically in this summary file because
    interactive input can be annoying during review. You can call it manually.
    """
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        print("Please type a number greater than 0.")



def demo_input_validation_pattern():
    section(7, "Input validation pattern with while True")

    print("Common pattern:")
    print("1. Start an intentional infinite loop with while True")
    print("2. Ask for input")
    print("3. If the input is good, return or break")
    print("4. If the input is bad, loop again")

    print("\nExample function:")
    print("""
def get_positive_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
""")

    print("Notice: return exits both the loop and the function.")


# ---------------------------------------------------------------------------
# 6. BREAK, CONTINUE, AND RETURN
# ---------------------------------------------------------------------------

def demo_break_continue_return():
    section(8, "break, continue, and return")

    print("continue = skip the rest of this loop cycle and go to the next cycle")
    print("break    = exit the nearest loop")
    print("return   = exit the function and optionally hand back a value")

    print("\nExample with continue and break:")

    for number in range(1, 8):
        if number == 2:
            print("number is 2, continue skips this cycle")
            continue
        if number == 6:
            print("number is 6, break exits the loop")
            break
        print(f"number: {number}")


# ---------------------------------------------------------------------------
# 7. FUNCTIONS WITH LOOPS
# ---------------------------------------------------------------------------

def meow(n):
    """Print meow n times."""
    for _ in range(n):
        print("meow")



def demo_functions_with_loops():
    section(9, "Functions with loops")

    print("Functions let us hide a loop behind a meaningful name.")
    print("Calling meow(3):")
    meow(3)

    print("\nThe caller does not need to know exactly how meow() works inside.")
    print("That is abstraction: a simple name hiding reusable logic.")


# ---------------------------------------------------------------------------
# 8. LISTS
# ---------------------------------------------------------------------------

def demo_lists_and_indexes():
    section(10, "Lists and indexes")

    students = ["Hermione", "Harry", "Ron"]

    print("A list stores multiple values in one variable.")
    print(f"students = {students}")

    print("\nLists are zero-indexed:")
    print(f"students[0] = {students[0]}")
    print(f"students[1] = {students[1]}")
    print(f"students[2] = {students[2]}")

    print("\nZero-indexed means the first item is at position 0, not 1.")



def demo_for_over_list():
    section(11, "Looping over a list directly")

    students = ["Hermione", "Harry", "Ron"]

    print("Instead of manually printing students[0], students[1], students[2], use a loop:")

    for student in students:
        print(student)

    print("\nUse a meaningful loop variable name when you actually use it.")



def demo_range_len():
    section(12, "Using range(len(...)) when you need the index")

    students = ["Hermione", "Harry", "Ron"]

    print("If you need both a number and the value, you can use range(len(students)).")

    for i in range(len(students)):
        print(i + 1, students[i])

    print("\nlen(students) gives the length of the list.")
    print("i + 1 is used only for human-friendly numbering.")


# ---------------------------------------------------------------------------
# 9. DICTIONARIES
# ---------------------------------------------------------------------------

def demo_dictionaries_basic():
    section(13, "Dictionaries: keys and values")

    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
    }

    print("A dictionary associates keys with values.")
    print("Here, student names are keys and houses are values.")

    print(f"Hermione's house: {students['Hermione']}")
    print(f"Draco's house: {students['Draco']}")

    print("\nLooping over a dictionary gives the keys by default:")

    for student in students:
        print(student, students[student], sep=", ")



def demo_list_of_dictionaries():
    section(14, "List of dictionaries and None")

    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    print("A list can contain dictionaries.")
    print("Each dictionary can describe one student with multiple pieces of data.")
    print("None means there is no value here.")

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")


# ---------------------------------------------------------------------------
# 10. MARIO STYLE OUTPUT
# ---------------------------------------------------------------------------

def print_column(height):
    """Print a vertical column of bricks."""
    for _ in range(height):
        print("#")



def print_row(width):
    """Print a horizontal row of bricks."""
    print("#" * width)



def print_square(size):
    """Print a square of bricks using nested loops."""
    for _ in range(size):
        print_row(size)



def demo_mario_patterns():
    section(15, "Mario-style columns, rows, and squares")

    print("Column height 3:")
    print_column(3)

    print("\nRow width 4:")
    print_row(4)

    print("\nSquare size 3:")
    print_square(3)

    print("\nNested loop idea: for each row, print a row of blocks.")


# ---------------------------------------------------------------------------
# 11. COMMON BEGINNER MISTAKES
# ---------------------------------------------------------------------------

def demo_common_mistakes():
    section(16, "Common beginner mistakes")

    print("Mistake 1: forgetting to update the while-loop variable")
    print("Result: accidental infinite loop")

    print("\nMistake 2: off-by-one errors")
    print("range(3) gives 0, 1, 2, not 1, 2, 3 and not 0, 1, 2, 3")

    print("\nMistake 3: using _ when you actually need the value")
    print("Use _ only when the loop variable is not used.")

    print("\nMistake 4: confusing list indexes")
    print("students[0] is the first item, not the zeroth item in normal human language.")

    print("\nMistake 5: using many parallel lists when a dictionary or list of dictionaries is clearer")


# ---------------------------------------------------------------------------
# 12. MINI PRACTICE FUNCTIONS
# ---------------------------------------------------------------------------

def repeat_word(word, times):
    """Return word repeated times times with spaces between each copy."""
    result = []
    for _ in range(times):
        result.append(word)
    return " ".join(result)



def count_students(students):
    """Return the number of students in a list."""
    return len(students)



def houses_report(students):
    """Return a readable report from a dictionary of student -> house."""
    lines = []
    for student in students:
        lines.append(f"{student}: {students[student]}")
    return "\n".join(lines)



def demo_mini_practice_functions():
    section(17, "Mini practice functions")

    print(repeat_word("loop", 3))

    names = ["Hermione", "Harry", "Ron"]
    print(f"Number of students: {count_students(names)}")

    houses = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Draco": "Slytherin",
    }
    print(houses_report(houses))


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    demo_why_loops_exist()
    demo_while_countdown()
    demo_while_countup()
    demo_for_range()
    demo_underscore_variable()
    demo_string_multiplication()
    demo_input_validation_pattern()
    demo_break_continue_return()
    demo_functions_with_loops()
    demo_lists_and_indexes()
    demo_for_over_list()
    demo_range_len()
    demo_dictionaries_basic()
    demo_list_of_dictionaries()
    demo_mario_patterns()
    demo_common_mistakes()
    demo_mini_practice_functions()

    section("Final", "What to remember")
    print("Loops are for repetition.")
    print("while is best when you repeat until a condition changes.")
    print("for is best when you repeat over a known sequence, like range() or a list.")
    print("Lists store ordered values. Dictionaries associate keys with values.")
    print("Functions make loop logic reusable and easier to understand.")


if __name__ == "__main__":
    main()
