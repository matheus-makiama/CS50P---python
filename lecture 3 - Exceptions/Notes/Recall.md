# CS50P Lecture 3 — Exceptions: Recall

> Matheus's own recall. Written without looking at notes.

---

In this lecture I learned about `try` / `except` blocks, and how to handle unexpected errors or inputs using `ValueError`, `pass`, and related tools.

What interested me most was connecting it to real life. When I use websites — especially Japanese ones — there are forms that reject your input with a vague error, or they only accept names in Japanese format, or they have character limits that don't adapt to foreign names. I always assumed that was a design choice, but now I realize it's probably the base structure of the code — whoever built it only handled the cases they expected, and everything else just crashes or throws a generic error.

That made me think: when I build something, I need to make the input handling flexible from the start, because it's impossible to predict every error a user will produce. The lesson is not to handle every single case — it's to handle the unexpected gracefully instead of crashing.

I also noticed how intuitive indentation is in Python. The structure visually shows you what belongs to what. But when you have a lot of `if` statements or `while` loops nested together, the code starts drifting to the right and becomes hard to follow. I think this is exactly why the professor likes to break code into small functions — it resets the indentation level, keeps each block clean, and lets you reuse the function anywhere. At first, jumping between functions felt harder to read than one big block, but now I can see why it's better. Even something as simple as a function that validates whether the input is an integer and shows the user a message — that's already more practical and reusable than writing the same check inline every time.

## Something I Wondered

Security. If exception handling is what stands between a program and a crash, and a crash can expose information about the system — then how do developers handle that in a world where AI can probe for those gaps much faster than a human? A defensive or pentesting AI that systematically tests all input edge cases to find vulnerabilities seems both inevitable and already happening. The base structure of how you handle errors is not just a user experience problem — it's a security surface.

---

*Source: CS50P Lecture 3 — Exceptions*
