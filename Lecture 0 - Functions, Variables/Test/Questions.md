# CS50P — Lecture 0: Questions Workbook

> Answer these separately from the lecture note.  
> Try to answer from memory first, then check the lecture note after.

---

## Questions to Check Your Understanding

## A. Basic Concepts

1. What is the difference between `code hello.py` and `python hello.py`?

**Your answer:**
code hello.py - open the hello.py
python hello.py - run the hello.py(python file)


---
2. What is a function?

**Your answer:**
It is a block of code that can be set - def hello(): - and called - hello(). 
Basically a reusable block of code that you can use, intead of writing the same code many times.


---
3. What is an argument?

**Your answer:**
Argument is a vallue you can hand to a function, which effect the output.
print("Hello") - in this case "Hello" is the argument.



---
4. What does `print("hello, world")` do?

**Your answer:**
It will print - hello, world - in the screen.



---
5. What is a bug?

**Your answer:**
Bug is where the code is working in an unintended way.



---
6. Why are error messages useful even when they look scary?

**Your answer:**
It helps you find the problem/bug.



---
7. What does `input()` do?

**Your answer:**

It receives the user input.


---
8. Why do we need a variable after using `input()`?

**Your answer:**

To store the input from the user or it will be gonne.


---
9. What does the `=` sign mean in Python?

**Your answer:**

It assign the vallue in the right to the variable in the left.



---
10. What is a string?

**Your answer:**
Basically a letter. String indicates a string of letter. A data type.



---
## B. Variables and Strings

11. What is the output of this code?

```python
name = "David"
print("hello, name")
```

**Your answer:**

hello, name


---
12. Why does the code above not print `hello, David`?

**Your answer:**

Because the name is a string in that case.


---
13. Fix the code above using a comma.

**Your answer:**

name = "David"
print("Hello,",name)


---
14. Fix the code above using an f-string.

**Your answer:**

name = "David"
print(f"Hello, {name}")


---
15. What is the difference between these two?

```python
print("hello,", name)
print(f"hello, {name}")
```

**Your answer:**

I believe it does the same thing but fstring is easier to read later perhaps.


---
16. How do you print this exact output?

```text
Hello, "friend"
```

**Your answer:**

print("Hello, \"friend\"")


---
17. What does `strip()` do?

**Your answer:**

It takes out the empty space before the first letter.


---
18. What does `title()` do?

**Your answer:**

Title will captalize the first letter of each word.


---
19. Why might this be useful?

```python
name = input("What's your name? ").strip().title()
```

**Your answer:**

It adjust the user input in a way that was intended like the user perhaps put a lot of space before the name or didint captalize etc.


---
20. What happens if you forget the `f` here?

```python
print("hello, {name}")
```

**Your answer:**

It's gonna output an error i suppose?


---
## C. `print()` Parameters

21. What does `sep` control?

**Your answer:**

separation, which is what will be shown in space. if its noamally its gonna be like hello, Matt. but if you do sep = !!! its gonna be hello,!!!Matt I think.




---
22. What does `end` control?

**Your answer:**

it controls what happens after the print on defalt it goes to the next line.


---
23. What is the default value of `sep`?

**Your answer:**

" "


---
24. What is the default value of `end`?

**Your answer:**

\n


---
25. What is the output?

```python
print("hello", "David", sep="...")
```

**Your answer:**

hello...David 




---
26. What is the output?

```python
print("hello, ", end="")
print("David")
```

**Your answer:**

hello, David


---
27. Why does `print()` usually move to a new line after printing?

**Your answer:**

becuase the defalt for end = \n which move to the next line.


---
## D. Numbers

28. What is an `int`?

**Your answer:**

integer a number whithout the number after the "."


---
29. What is a `float`?

**Your answer:**

a number with floating number like 10.5557



---
30. What is the result of this?

```python
print(1 + 2)
```

**Your answer:**

3


---
31. What is the result of this?

```python
print("1" + "2")
```

**Your answer:**

12


---
32. Why does this code print `12` instead of `3`?

```python
x = input("x: ")
y = input("y: ")
print(x + y)
```

**Your answer:**

becuse the dafalt output for a input is string and it expects a string.

---
33. Fix the code above so it prints `3` when the user enters `1` and `2`.

**Your answer:**

x = int(input("x: "))
y = int(input("y: "))
print(x + y)



---
34. What does `int()` do?

**Your answer:**

changes the data type of the vallue inside to a integer.


---
35. What does `float()` do?

**Your answer:**

changers the data type of the vallue inside to a float


---
36. What does `round()` do?

**Your answer:**

it rounds up a float number to an int.


---
37. What does this mean?

```python
print(f"{z:.2f}")
```

**Your answer:**

it will print a float number to the 2number after the "."


---
38. What does this mean?

```python
print(f"{z:,}")
```

**Your answer:**

, for each 3 digit. like 1,000


---
## E. Functions, Parameters, and Return Values

39. How do you define your own function?

**Your answer:**

def hello():
    print("hello")


---
40. Does defining a function automatically run it?

**Your answer:**

no, you have to call it.


---
41. What is the difference between a parameter and an argument?

**Your answer:**

parameter is the def hello(to): - to is the parameter which you can hand to the function and by giving it a name(just to show how you gonna use the value ahnded to the function / argument)


---
42. In this code, what is the parameter and what is the argument?

```python
def hello(to):
    print("hello,", to)


hello("David")
```

**Your answer:**
hello(to)   the to is the parameter_

argument is the hello("David") - "David"



---
43. What does a default parameter value do?

**Your answer:**

nothing if not set specifically.


---
44. What is the output?

```python
def hello(to="world"):
    print("hello,", to)


hello()
hello("David")
```

**Your answer:**

hello, world
hello, David


---
45. Why do many Python programs use a `main()` function?

**Your answer:**

it is more related to readability which allow you to understand that thats the main part of the programm


---
46. Why is this pattern useful?

```python
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to):
    print("hello,", to)


main()
```

**Your answer:**

It is easy to read and the handshake/the data passing between the functions is clear.


---
47. What is scope?

**Your answer:**

To waht extent can that function reach to get or give or even read something perhaps.


---
48. Why can a variable created inside one function sometimes not be used inside another function?

**Your answer:**

because its out of scope that variable only exist inside that function.


---
49. What does `return` do?

**Your answer:**

to make sure that well if its a function it return a vallue.


---
50. What is the difference between printing a value and returning a value?

**Your answer:**

printing will show, return will give back that vallue to something.


---
## F. Code Reading Practice

### Question 51

What does this program print if the user types `  david malan  `?

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

**Your answer:**

hello, David Malan



---
### Question 52

What does this program print?

```python
def square(n):
    return n * n


print(square(5))
```

**Your answer:**

25


---
### Question 53

What does this program print?

```python
def hello(to="world"):
    print("hello,", to)


hello()
```

**Your answer:**

hello, world


---
### Question 54

What does this program print?

```python
x = "1"
y = "2"

print(x + y)
```

**Your answer:**

12


---
### Question 55

What does this program print?

```python
x = int("1")
y = int("2")

print(x + y)
```

**Your answer:**

3


---
## G. Small Practice Tasks

Try writing these without looking at the answers.

1. Write a program that asks for your name and prints:

```text
hello, YOUR_NAME
```

**Your code / answer:**

```python

name = input("What's your name? :").strip.title
print(f"hello, {name}")

```

---
2. Improve it so extra spaces are removed and the name is title-cased.

**Your code / answer:**

```python

name = input("What's your name? :").strip.title
print(f"hello, {name}")
```

---
3. Write a program that asks for two numbers and prints their sum.

**Your code / answer:**

```python
x = int(input("What's the vallue of \"x\"? :"))
x = int(input("What's the vallue of \"y\"? :"))

print(x + y)

```

---
4. Write a program that asks for two numbers and prints the result rounded to 2 decimal places.

**Your code / answer:**

```python

x = int(input("What's the vallue of \"x\"? :"))
x = int(input("What's the vallue of \"y\"? :"))

z = x + y

print(f"{z:.f2}")

```

---
5. Write a function called `square` that returns the square of a number.

**Your code / answer:**

```python

def square(n):
    return n * n

```

---
6. Write a program with a `main()` function and another function called `hello()`.

**Your code / answer:**

```python
def main():
    name = input("What's your name? :").strip.title
    hello(name)

def hello(to):
    print("Hello,", to)


main()


```

---
