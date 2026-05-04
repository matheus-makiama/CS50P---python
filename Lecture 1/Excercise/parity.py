# parity.py
# Topic: Functions, return values, and modulo
#
# This program checks if a number is even or odd.
#
# Important idea:
# % is the modulo operator.
# It gives the remainder after division.
#
# Examples:
# 4 % 2 == 0  because 4 divides evenly by 2
# 5 % 2 == 1  because 5 has a remainder of 1
#
# If a number divided by 2 has remainder 0, it is even.

def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()