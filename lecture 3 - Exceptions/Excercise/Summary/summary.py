"""
CS50P - Lecture 3 - Exceptions
summary.py

Purpose:
    Runnable study summary for CS50P Lecture 3.
    Read the comments, run the examples, and edit the code to practice.

Main concepts:
    - Exceptions
    - SyntaxError
    - Runtime errors
    - ValueError
    - NameError
    - try / except / else
    - pass
    - raise
    - defensive programming
    - helper functions like get_int()

How to use:
    python summary.py

Important idea:
    Errors are not just failure.
    Errors are Python sending you smoke signals.
    The skill is learning how to read the smoke.
"""


# ============================================================
# 1. What is an exception?
# ============================================================

"""
An exception is a problem that happens while your program is running.

Example:
    You ask the user for a number.
    They type "cat".
    Python tries to convert "cat" into an integer.
    Python cannot do that.
    So Python raises a ValueError.

Exceptions let us handle expected problems instead of letting the
program crash like a dropped plate.
"""


# ============================================================
# 2. SyntaxError
# ============================================================

"""
A SyntaxError happens when Python cannot even understand your code.

Bad example:
    print("hello, world)

The quotation mark is not closed.

Important:
    You usually cannot fix SyntaxError with try/except because Python
    cannot run the program until the syntax is corrected.
"""


def syntax_error_explanation():
    print("SyntaxError means Python cannot understand the code structure.")
    print("Fix the typing/grammar of the code before trying to handle errors.")


# ============================================================
# 3. Runtime errors
# ============================================================

"""
A runtime error happens while the program is already running.

Example:
    x = int(input("What's x? "))

The code is syntactically valid.
But if the user types "hello", int("hello") raises ValueError.
"""


# ============================================================
# 4. ValueError
# ============================================================

"""
ValueError means the value is invalid for the operation.

Examples:
    int("123")      works
    int("hello")    raises ValueError
    int("")         raises ValueError
    int("3.14")     raises ValueError

"3.14" looks like a number to us, but int() expects an integer string.
"""


def value_error_demo():
    examples = ["123", "0", "-5", "hello", "3.14", ""]

    print("\n--- ValueError demo ---")

    for text in examples:
        try:
            number = int(text)
        except ValueError:
            print(f"int({text!r}) failed: this value cannot become an integer.")
        else:
            print(f"int({text!r}) worked: {number}")


# ============================================================
# 5. NameError
# ============================================================

"""
NameError means Python sees a variable or name it does not know.

Example:
    print(x)

If x was never created, Python raises NameError.

Common beginner trap:

    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")

    print(f"x is {x}")

If int(input(...)) fails, x is never assigned.
Then the final print may cause NameError.
"""


def name_error_explanation():
    print("\n--- NameError explanation ---")
    print("If a variable is created only inside try, and try fails, the variable may not exist.")


# ============================================================
# 6. try / except
# ============================================================

"""
Basic pattern:

    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")

try:
    Put risky code here.

except ValueError:
    This runs only if ValueError happens inside the try block.

Prefer specific exceptions instead of bare except.
"""


def get_int_basic():
    try:
        x = int(input("Basic demo - What's x? "))
    except ValueError:
        print("x is not an integer.")
    else:
        print(f"x is {x}")


# ============================================================
# 7. else with try/except
# ============================================================

"""
else runs only if the try block does NOT raise an exception.

Pattern:

    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")

Why use else?
    It keeps the risky code inside try small.
    It avoids accidentally catching errors from code that should run only after success.
"""


def else_demo():
    print("\n--- else demo ---")

    try:
        x = int(input("Else demo - What's x? "))
    except ValueError:
        print("x is not an integer.")
    else:
        print(f"x is {x}")


# ============================================================
# 8. while True + break
# ============================================================

"""
A core CS50P pattern:

    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break

This keeps asking until input is valid.

while True:
    Repeat forever.

break:
    Escape the loop after successful input.
"""


def get_int_with_loop():
    while True:
        try:
            x = int(input("Loop demo - What's x? "))
        except ValueError:
            print("x is not an integer. Try again.")
        else:
            break

    return x


# ============================================================
# 9. Cleaner get_int() function
# ============================================================

"""
A helper function makes your program cleaner.
Instead of rewriting try/except every time, create get_int().
"""


def get_int(prompt):
    """Ask until the user gives a valid integer, then return it."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type a valid integer.")



def get_positive_int(prompt):
    """
    Ask until the user gives an integer greater than 0.

    This shows that exceptions do not replace if statements:
        - try/except handles invalid conversion, like "cat"
        - if handles invalid logic, like -5
    """
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Please type a valid integer.")
        else:
            if number > 0:
                return number
            print("Please type a number greater than 0.")


# ============================================================
# 10. pass
# ============================================================

"""
pass means do nothing.

Example:

    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

This silently ignores the error and asks again.

Good:
    Short and clean.

Bad:
    The user may not know what went wrong.
"""


def get_int_silent(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


# ============================================================
# 11. raise
# ============================================================

"""
raise creates an exception manually.

Use raise when your function detects something invalid.
"""


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age



def raise_demo():
    print("\n--- raise demo ---")

    test_ages = [10, 0, -3]

    for age in test_ages:
        try:
            valid_age = validate_age(age)
        except ValueError as error:
            print(f"{age} failed validation: {error}")
        else:
            print(f"{valid_age} is valid.")


# ============================================================
# 12. Bare except warning
# ============================================================

"""
Avoid this when possible:

    try:
        ...
    except:
        ...

Why?
    It catches almost everything, including errors you did not expect.
    That can hide bugs.

Better:

    except ValueError:
        ...
"""


# ============================================================
# 13. Practice examples
# ============================================================


def practice_division():
    """
    Ask for two integers and divide them.

    Possible exceptions:
        ValueError       -> input could not become int
        ZeroDivisionError -> denominator is 0
    """
    print("\n--- Division practice ---")

    try:
        x = int(input("x: "))
        y = int(input("y: "))
        result = x / y
    except ValueError:
        print("Both x and y must be integers.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print(f"{x} / {y} = {result}")



def practice_menu_choice():
    """
    Ask the user to choose a menu item.

    try/except handles bad conversion.
    if/elif/else handles numbers outside the allowed range.
    """
    print("\n--- Menu choice practice ---")
    print("1. Coffee")
    print("2. Tea")
    print("3. Water")

    try:
        choice = int(input("Choose 1, 2, or 3: "))
    except ValueError:
        print("Please type a number.")
    else:
        if choice == 1:
            print("You chose coffee.")
        elif choice == 2:
            print("You chose tea.")
        elif choice == 3:
            print("You chose water.")
        else:
            print("That number is not on the menu.")


# ============================================================
# 14. Mini quiz inside Python
# ============================================================


def mini_quiz():
    print("\n--- Mini quiz ---")

    questions = [
        {"q": "Which error happens when int('cat') runs?", "answer": "valueerror"},
        {"q": "Which keyword starts code that might fail?", "answer": "try"},
        {"q": "Which keyword runs only if try succeeds?", "answer": "else"},
        {"q": "Which keyword means do nothing?", "answer": "pass"},
        {"q": "Which keyword creates an exception manually?", "answer": "raise"},
    ]

    score = 0

    for item in questions:
        user_answer = input(item["q"] + " ").strip().lower()
        if user_answer == item["answer"]:
            print("Correct.")
            score += 1
        else:
            print(f"Not quite. Answer: {item['answer']}")

    print(f"Score: {score}/{len(questions)}")


# ============================================================
# 15. Main menu
# ============================================================


def main():
    print("CS50P Lecture 3 - Exceptions Summary")
    print("------------------------------------")
    print("Choose a demo:")
    print("1. SyntaxError explanation")
    print("2. ValueError demo")
    print("3. NameError explanation")
    print("4. Basic try/except input")
    print("5. try/except/else input")
    print("6. get_int with loop")
    print("7. get_positive_int")
    print("8. raise demo")
    print("9. division practice")
    print("10. menu choice practice")
    print("11. mini quiz")
    print("0. exit")

    while True:
        choice = input("\nChoose: ").strip()

        if choice == "1":
            syntax_error_explanation()
        elif choice == "2":
            value_error_demo()
        elif choice == "3":
            name_error_explanation()
        elif choice == "4":
            get_int_basic()
        elif choice == "5":
            else_demo()
        elif choice == "6":
            x = get_int_with_loop()
            print(f"Valid x: {x}")
        elif choice == "7":
            x = get_positive_int("Positive integer: ")
            print(f"Valid positive integer: {x}")
        elif choice == "8":
            raise_demo()
        elif choice == "9":
            practice_division()
        elif choice == "10":
            practice_menu_choice()
        elif choice == "11":
            mini_quiz()
        elif choice == "0":
            print("Done. Review the mistakes, not just the correct answers.")
            break
        else:
            print("Please choose one of the menu numbers.")


if __name__ == "__main__":
    main()
