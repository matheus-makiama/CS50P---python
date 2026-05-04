# CS50P - Lecture 2: Loops / ループ

> Use this after watching the lecture and after trying the examples yourself.  
> This note is meant to help you review, understand, and remember Lecture 2.

---

## 0. Big Picture

Lecture 2 is about **loops**.

A loop lets your program repeat an action without copying and pasting the same code many times.

Tiny mental picture:

```txt
without loop:
print
print
print
print

with loop:
repeat this action 4 times
```

In Lecture 1, your program learned how to choose a path with conditionals.

In Lecture 2, your program learns how to repeat a path.

This is where code stops being a single arrow and starts becoming a little hamster wheel with discipline. 🐹

---

## 1. What Problem Do Loops Solve?

Imagine you want to print this:

```txt
meow
meow
meow
```

You could write:

```python
print("meow")
print("meow")
print("meow")
```

This works.

But what if you wanted 500 meows?

That would be ugly, repetitive, and hard to change.

A loop lets you write the idea once:

```python
for _ in range(3):
    print("meow")
```

This means:

> Repeat this block 3 times.

---

## 2. Loop Vocabulary

| Word | Meaning |
|---|---|
| loop | code that repeats |
| iteration | one cycle through a loop |
| loop body | the indented code inside the loop |
| condition | a True/False expression controlling a `while` loop |
| infinite loop | a loop that never stops |

Example:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

This loop has 3 iterations:

```txt
i = 0
 i = 1
 i = 2
```

When `i` becomes `3`, the condition `i < 3` is false, so the loop stops.

---

## 3. `while` Loops

A `while` loop repeats **while a condition is True**.

Basic structure:

```python
while condition:
    code_to_repeat
```

Example:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

This means:

1. Start with `i = 0`
2. Check if `i < 3`
3. If true, print `meow`
4. Increase `i` by 1
5. Go back and check again
6. Stop when `i < 3` becomes false

Output:

```txt
meow
meow
meow
```

---

## 4. Infinite Loops

An infinite loop is a loop that never ends.

Example:

```python
i = 3
while i != 0:
    print("meow")
```

This loop never stops because `i` stays `3` forever.

The condition:

```python
i != 0
```

is always true.

To fix it, change `i` inside the loop:

```python
i = 3
while i != 0:
    print("meow")
    i -= 1
```

Now `i` becomes:

```txt
3 → 2 → 1 → 0
```

When `i` becomes `0`, the loop stops.

### Emergency button

If you accidentally create an infinite loop in the terminal, you can usually stop it with:

```txt
Ctrl + C
```

Tiny keyboard fire extinguisher. 🧯

---

## 5. Counting From 0

In programming, counting often starts at `0`.

This is common:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

The values of `i` are:

```txt
0
1
2
```

It still runs 3 times.

Why?

Because there are three numbers before 3 when starting from 0:

```txt
0, 1, 2
```

---

## 6. `i += 1`

This:

```python
i += 1
```

means the same as:

```python
i = i + 1
```

It increases `i` by 1.

This is called **incrementing**.

Similarly:

```python
i -= 1
```

means:

```python
i = i - 1
```

It decreases `i` by 1.

---

## 7. `for` Loops

A `for` loop repeats over a sequence.

Example:

```python
for i in [0, 1, 2]:
    print("meow")
```

This means:

1. Put `0` into `i`, then print `meow`
2. Put `1` into `i`, then print `meow`
3. Put `2` into `i`, then print `meow`
4. Stop

Output:

```txt
meow
meow
meow
```

`for` loops are usually cleaner than `while` loops when you already know the sequence or the number of repetitions.

---

## 8. `range()`

Instead of writing this:

```python
for i in [0, 1, 2]:
    print("meow")
```

You can write:

```python
for i in range(3):
    print("meow")
```

`range(3)` produces:

```txt
0, 1, 2
```

Important:

```python
range(3)
```

does **not** include `3`.

It stops before `3`.

More examples:

| Code | Values |
|---|---|
| `range(3)` | `0, 1, 2` |
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(2, 5)` | `2, 3, 4` |

---

## 9. The `_` Variable

Sometimes a loop needs a variable, but you do not actually use it.

Example:

```python
for i in range(3):
    print("meow")
```

The variable `i` exists, but the code does not use it.

So Python programmers often write:

```python
for _ in range(3):
    print("meow")
```

The `_` means:

> I need a loop variable here, but I do not care about its value.

Use `_` when the value is unused.

Do not use `_` when the value matters.

Good:

```python
for _ in range(3):
    print("meow")
```

Not good:

```python
students = ["Hermione", "Harry", "Ron"]

for _ in students:
    print(_)
```

This works, but `student` is clearer:

```python
for student in students:
    print(student)
```

---

## 10. String Multiplication

Python can multiply strings.

```python
print("meow" * 3)
```

Output:

```txt
meowmeowmeow
```

No spaces or new lines are added automatically.

To print each `meow` on its own line:

```python
print("meow\n" * 3, end="")
```

Why `end=""`?

`print()` normally adds a newline at the end. Since the string already contains `\n`, `end=""` prevents an extra blank line.

---

## 11. Input Validation With Loops

Loops are useful when you want to keep asking until the user gives valid input.

Example:

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
```

This means:

1. Ask for `n`
2. If `n > 0`, leave the loop
3. Otherwise, keep asking
4. After a valid number is given, print `meow` `n` times

`while True` creates an intentional infinite loop.

It becomes safe because we use `break` to leave it.

---

## 12. `break`

`break` exits the nearest loop immediately.

Example:

```python
while True:
    command = input("Command: ")

    if command == "stop":
        break

    print("Still running")
```

If the user types `stop`, the loop ends.

`break` is like opening the trapdoor under the loop. 🕳️

---

## 13. `continue`

`continue` skips the rest of the current iteration and jumps to the next one.

Example:

```python
while True:
    n = int(input("What's n? "))

    if n < 0:
        continue
    else:
        break
```

If `n < 0`, Python goes back to the top and asks again.

But in this simple case, `continue` is not really needed.

This is cleaner:

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
```

---

## 14. `return` Inside a Loop

Inside a function, `return` exits the whole function.

Example:

```python
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
```

When the user enters a positive number, Python returns `n` and leaves the function.

This is often cleaner than using `break` and then returning later.

### `break` vs `return`

| Keyword | What it exits |
|---|---|
| `break` | the nearest loop |
| `return` | the whole function |
| `continue` | only the current iteration |

---

## 15. Functions and Loops Together

A cleaner version of the meow program:

```python
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
```

Why this is better:

- `main()` controls the program
- `get_number()` handles input validation
- `meow(n)` handles repetition

Each function has one clear job.

That is good design.

---

## 16. Lists

A list stores multiple values in one ordered collection.

Example:

```python
students = ["Hermione", "Harry", "Ron"]
```

You can access items by index:

```python
print(students[0])  # Hermione
print(students[1])  # Harry
print(students[2])  # Ron
```

Python lists start at index `0`.

| Index | Value |
|---:|---|
| `0` | `Hermione` |
| `1` | `Harry` |
| `2` | `Ron` |

---

## 17. Looping Over a List

Instead of this:

```python
print(students[0])
print(students[1])
print(students[2])
```

You can do this:

```python
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
```

Output:

```txt
Hermione
Harry
Ron
```

Use a meaningful variable name:

```python
for student in students:
```

This reads almost like English:

> For each student in students, print the student.

---

## 18. `len()`

`len()` gives the number of items.

```python
students = ["Hermione", "Harry", "Ron"]
print(len(students))
```

Output:

```txt
3
```

This is useful because your code can adapt if the list grows.

---

## 19. `range(len(...))`

Sometimes you need both the index and the value.

Example:

```python
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
```

Output:

```txt
1 Hermione
2 Harry
3 Ron
```

Why `i + 1`?

Because humans usually count from 1, but Python indexes from 0.

| `i` | `i + 1` | `students[i]` |
|---:|---:|---|
| `0` | `1` | `Hermione` |
| `1` | `2` | `Harry` |
| `2` | `3` | `Ron` |

---

## 20. Dictionaries

A dictionary stores key-value pairs.

Example:

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
```

Here:

- key = student name
- value = house

You can look up a value by key:

```python
print(students["Hermione"])
```

Output:

```txt
Gryffindor
```

Mental model:

```txt
dictionary = label → value
```

A list uses number positions.

A dictionary uses meaningful keys.

---

## 21. Looping Over a Dictionary

When you loop over a dictionary, Python gives you the keys by default.

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student)
```

Output:

```txt
Hermione
Harry
Ron
Draco
```

To print both the key and value:

```python
for student in students:
    print(student, students[student], sep=", ")
```

Output:

```txt
Hermione, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin
```

This part is important:

```python
students[student]
```

The variable `student` contains the key.

So `students[student]` looks up the value for that key.

---

## 22. List of Dictionaries

Sometimes each item needs more than one piece of information.

Example:

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
```

This is a **list of dictionaries**.

Each dictionary represents one student.

You can loop over the list:

```python
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```

Output:

```txt
Hermione, Gryffindor, Otter
Harry, Gryffindor, Stag
Ron, Gryffindor, Jack Russell terrier
Draco, Slytherin, None
```

---

## 23. `None`

`None` means there is no value.

It is different from:

```python
""
```

which is an empty string.

It is also different from:

```python
0
```

which is a number.

Example:

```python
{"name": "Draco", "house": "Slytherin", "patronus": None}
```

This means the `patronus` key exists, but there is no actual patronus value.

Mental model:

```txt
None = no value here
```

---

## 24. Mario: Columns

To print a vertical column:

```python
def print_column(height):
    for _ in range(height):
        print("#")


print_column(3)
```

Output:

```txt
#
#
#
```

The loop controls the height.

---

## 25. Mario: Rows

To print a horizontal row:

```python
def print_row(width):
    print("#" * width)


print_row(4)
```

Output:

```txt
####
```

String multiplication controls the width.

---

## 26. Mario: Squares

To print a square:

```python
def print_square(size):
    for _ in range(size):
        print("#" * size)


print_square(3)
```

Output:

```txt
###
###
###
```

The loop controls the number of rows.

The string multiplication controls the number of columns.

---

## 27. Nested Loops

A nested loop is a loop inside another loop.

Example:

```python
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
```

The outer loop controls rows.

The inner loop controls columns.

For `size = 3`:

```txt
row 1 → ###
row 2 → ###
row 3 → ###
```

This works, but this version is simpler:

```python
def print_square(size):
    for _ in range(size):
        print("#" * size)
```

Good programmers do not worship complexity.

They tame it.

---

## 28. Common Beginner Mistakes

### Mistake 1: Forgetting to update the counter

Wrong:

```python
i = 0
while i < 3:
    print("meow")
```

This never stops.

Correct:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

### Mistake 2: Thinking `range(3)` includes 3

Wrong idea:

```txt
range(3) → 0, 1, 2, 3
```

Correct:

```txt
range(3) → 0, 1, 2
```

### Mistake 3: Using `_` when the value matters

Not ideal:

```python
for _ in students:
    print(_)
```

Better:

```python
for student in students:
    print(student)
```

### Mistake 4: List index out of range

Wrong:

```python
students = ["Hermione", "Harry", "Ron"]
print(students[3])
```

Valid indexes are:

```txt
0, 1, 2
```

Correct:

```python
print(students[2])
```

### Mistake 5: Treating a dictionary like a list

Wrong:

```python
students = {"Hermione": "Gryffindor"}
print(students[0])
```

Correct:

```python
print(students["Hermione"])
```

### Mistake 6: Using `break` when you needed `return`

Incomplete:

```python
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
```

This exits the loop, but the function does not return `n`.

Better:

```python
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
```

---

## 29. When Should I Use Each Tool?

| Situation | Tool |
|---|---|
| repeat while condition is true | `while` |
| repeat a known number of times | `for` + `range()` |
| repeat over names/items | `for` + list |
| keep asking until valid input | `while True` + `break` or `return` |
| store many ordered values | list |
| store key-value relationships | dictionary |
| no real value exists | `None` |
| need rows and columns | nested loop or string multiplication |

---

## 30. Mini Projects for This Lecture

### 1. Simple command menu

Use `while True` to keep asking for a command.

Commands:

- `start`
- `help`
- `stop`

Stop the program only when the user types `stop`.

### 2. Mood bot

Ask the user for a mood number from 1 to 10.

Keep asking until the number is valid.

Then print a different message depending on the mood.

### 3. Factory inspection counter

Ask how many parts were checked.

Print numbered labels:

```txt
1 Checked
2 Checked
3 Checked
```

### 4. Student house report

Use a dictionary to store names and houses.

Print:

```txt
Hermione, Gryffindor
Harry, Gryffindor
Draco, Slytherin
```

### 5. Mario square

Ask for a positive size.

Print a square made of `#`.

---

## Final Mental Model

Lecture 2 teaches repetition.

But the deeper lesson is not only:

> “How do I repeat code?”

The deeper lesson is:

> “How do I avoid repeating myself?”

Loops are not just a syntax trick.

They are a way to make code shorter, clearer, and easier to change.

You are learning to turn copy-paste into structure.

That is a big step.
