# CS50P - Lecture 2: Loops Questions Workbook

> Purpose: active recall and practice only.  
> Do your separate free-memory writing in `Recall.md`.  
> This file is only for checking understanding, code reading, and code writing.

---

# A. Core Concepts

## 1. What problem do loops solve in programming?

**Your answer:**


---

## 2. What is one iteration of a loop?

**Your answer:**


---

## 3. What is the loop body?

**Your answer:**


---

## 4. What is an infinite loop?

**Your answer:**


---

## 5. Why is copy-pasting the same line many times usually bad code?

**Your answer:**


---

# B. while Loops

## 6. What does a `while` loop do?

**Your answer:**


---

## 7. What has to eventually change in a `while` loop so it does not run forever?

**Your answer:**


---

## 8. What does this print?

```python
i = 3
while i != 0:
    print("meow")
    i -= 1
```

**Your answer:**


---

## 9. What is wrong with this code?

```python
i = 3
while i != 0:
    print("meow")
```

**Your answer:**


---

## 10. What keyboard shortcut can usually stop an accidental infinite loop in the terminal?

**Your answer:**


---

## 11. What does `i += 1` mean?

**Your answer:**


---

## 12. What does `i -= 1` mean?

**Your answer:**


---

## 13. What values does `i` have here?

```python
i = 0
while i < 3:
    print(i)
    i += 1
```

**Your answer:**


---

## 14. Why does `while i < 3` stop before `i` becomes useful as a printed `3`?

**Your answer:**


---

# C. for Loops and range

## 15. When is a `for` loop usually better than a `while` loop?

**Your answer:**


---

## 16. What values does `range(3)` produce?

**Your answer:**


---

## 17. Does `range(5)` include `5`? Explain.

**Your answer:**


---

## 18. What does this print?

```python
for i in range(3):
    print("meow")
```

**Your answer:**


---

## 19. What does this print?

```python
for i in range(4):
    print(i)
```

**Your answer:**


---

## 20. What values does `range(2, 5)` produce?

**Your answer:**


---

## 21. Why might we write `for _ in range(3)` instead of `for i in range(3)`?

**Your answer:**


---

## 22. Should you use `_` if you need the loop value inside the loop? Why?

**Your answer:**


---

# D. String Multiplication

## 23. What does this print?

```python
print("meow" * 3)
```

**Your answer:**


---

## 24. How can you print `meow` three times on separate lines using string multiplication?

**Your answer:**


---

## 25. What does `\n` mean inside a string?

**Your answer:**


---

## 26. Why might we use `end=""` with `print("meow\n" * 3, end="")`?

**Your answer:**


---

# E. Input Validation, break, continue, return

## 27. Why is `while True` useful for input validation?

**Your answer:**


---

## 28. What does `break` do?

**Your answer:**


---

## 29. What does `continue` do?

**Your answer:**


---

## 30. What does `return` do inside a function?

**Your answer:**


---

## 31. What is the difference between `break` and `return` inside a function?

**Your answer:**


---

## 32. Why is `continue` unnecessary in this version?

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
```

**Your answer:**


---

## 33. Write a loop that keeps asking for `n` until `n > 0`.

**Your answer:**


---

## 34. Write a function `get_number()` that keeps asking until the user gives a positive number, then returns it.

**Your answer:**


---

# F. Functions With Loops

## 35. Why put repeated behavior inside a function like `meow(n)`?

**Your answer:**


---

## 36. What should `meow(3)` do?

**Your answer:**


---

## 37. Write a function `meow(n)` that prints `meow` `n` times.

**Your answer:**


---

## 38. In this structure, what is the job of `main()`?

```python
def main():
    number = get_number()
    meow(number)
```

**Your answer:**


---

# G. Lists

## 39. What is a list in Python?

**Your answer:**


---

## 40. In `students = ["Hermione", "Harry", "Ron"]`, what is `students[0]`?

**Your answer:**


---

## 41. In `students = ["Hermione", "Harry", "Ron"]`, what is `students[2]`?

**Your answer:**


---

## 42. Why does `students[3]` cause a problem in a list of three students?

**Your answer:**


---

## 43. What does this do?

```python
for student in students:
    print(student)
```

**Your answer:**


---

## 44. Why is `student` a better variable name than `_` in the loop above?

**Your answer:**


---

# H. len and Indexes

## 45. What does `len(students)` give?

**Your answer:**


---

## 46. Why might we use `range(len(students))`?

**Your answer:**


---

## 47. What does this print?

```python
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])
```

**Your answer:**


---

## 48. Why do we use `i + 1` when printing a human-friendly position number?

**Your answer:**


---

# I. Dictionaries

## 49. What is a dictionary in Python?

**Your answer:**


---

## 50. What is the difference between a list and a dictionary?

**Your answer:**


---

## 51. In `students = {"Hermione": "Gryffindor"}`, what is the key and what is the value?

**Your answer:**


---

## 52. What does `students["Hermione"]` do?

**Your answer:**


---

## 53. When you loop over a dictionary using `for student in students`, what do you get by default?

**Your answer:**


---

## 54. How do you print both the key and value in this dictionary?

```python
students = {"Hermione": "Gryffindor"}
```

**Your answer:**


---

## 55. What does `sep=", "` do in `print(student, students[student], sep=", ")`?

**Your answer:**


---

# J. List of Dictionaries and None

## 56. Why use a list of dictionaries for students with name, house, and patronus?

**Your answer:**


---

## 57. What does `None` mean?

**Your answer:**


---

## 58. Is `None` the same as an empty string `""`? Explain.

**Your answer:**


---

## 59. What does this print?

```python
student = {"name": "Draco", "patronus": None}
print(student["patronus"])
```

**Your answer:**


---

## 60. How do you print each student's name, house, and patronus from a list of dictionaries?

**Your answer:**


---

# K. Mario and Nested Loops

## 61. Write a function `print_column(height)` that prints a vertical column of `#` symbols.

**Your answer:**


---

## 62. Write a function `print_row(width)` that prints one horizontal row of `#` symbols.

**Your answer:**


---

## 63. What does this print?

```python
for _ in range(3):
    print("#" * 3)
```

**Your answer:**


---

## 64. What is a nested loop?

**Your answer:**


---

## 65. In a nested loop for a square, what does the outer loop usually control?

**Your answer:**


---

## 66. In a nested loop for a square, what does the inner loop usually control?

**Your answer:**


---

## 67. Why can `print("#" * size)` sometimes replace an inner loop?

**Your answer:**


---

# L. Code Writing Practice

## 68. Write a program that asks the user for a positive number and prints `meow` that many times.

**Your answer:**


---

## 69. Write a program that asks for a command until the user types `stop`.

**Your answer:**


---

## 70. Write a program that stores three names in a list and prints them one per line.

**Your answer:**


---

## 71. Write a program that stores students and houses in a dictionary and prints `Name, House` for each one.

**Your answer:**


---

## 72. Write a program that asks for a square size and prints a square made of `#` symbols.

**Your answer:**


---

## 73. Write one tiny mini-project idea using loops in one sentence.

**Your answer:**


---

# Final Self-Check

Before moving to Lecture 3, make sure you can do these without looking:

- [ ] Explain what a loop is
- [ ] Explain what one iteration means
- [ ] Write a `while` loop without making an infinite loop
- [ ] Use `for` with `range()`
- [ ] Explain why `range(3)` gives `0, 1, 2`
- [ ] Use `_` when the loop variable is not needed
- [ ] Explain `break`, `continue`, and `return`
- [ ] Use a loop to validate input
- [ ] Loop over a list
- [ ] Use `len()` with a list
- [ ] Loop over a dictionary and print keys/values
- [ ] Explain what `None` means
- [ ] Print a Mario-style column, row, and square