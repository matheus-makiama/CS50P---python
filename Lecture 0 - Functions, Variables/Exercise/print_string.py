# code hello.py(open/create a file called hello.py)

# Ask user for their name. Remove whitespace from str and cap the start of each word.
name = input("What's your name? :").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Say hello to the user.
print("Hello, " + first + "!")
print("Hello," + "" + last + "!")
print("Hello,",name + "!")

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print("Hello, ", end="")
print(name)

print("Hello,", name, sep="???")

print('Hello, "friend"')
print("Hello, \"friend\"")

print(f"Hello, {name}!") 

# python hello.py(run the file)

#"python" - activate interactive mode.
