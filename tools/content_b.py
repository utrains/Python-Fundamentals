"""Modules 5 to 8, following the slide decks section by section."""

from nbcore import header, md, only_nb, slide, code, todo, turn, lab, practice, heads_up

# ---------------------------------------------------------------- Module 5

M5 = [
    header(
        5,
        "Control Flow",
        "Make decisions with if, repeat work with for and while, and steer loops with break, continue, and pass.",
        [
            "Choose a path with if, elif and else",
            "Repeat work with a for loop over range() and over a string",
            "Repeat while a condition holds, without writing an endless loop",
            "Steer a loop with break, continue and pass",
        ],
        "It follows the Module 5 slide deck, slide by slide.",
        "Modules 1 to 4. Lists arrive in Module 6, so nothing in this notebook "
        "loops over a list. The deck loops over `range()` and over a string, and "
        "so does everything here, including the exercises and the lab.",
    ),
    slide(
        2,
        "What Is Control Flow?",
        """
Control flow statements let a program make decisions and repeat work, instead
of running the same fixed lines every time.

- **Conditionals**: `if`, `elif`, `else` choose a path
- **Loops**: `for`, `while` repeat work
- **Loop control**: `break`, `continue`, `pass` steer a loop
""",
    ),
    code(
        """
temperature = 15

if temperature < 0:
    print("Freezing")
elif temperature < 20:
    print("Cool")
else:
    print("Warm")

# this is control flow: the path taken depends on the value
"""
    ),
    slide(
        3,
        "if, elif, and else",
        """
`if` runs a block only when its condition is `True`. `elif` checks another
condition if the first was `False`. `else` catches everything left over.

**Indentation matters.** Python uses indentation, not curly braces, to mark
what belongs inside a block. Four spaces is the standard.
""",
    ),
    code(
        """
# In a script this would be:  num = int(input("Enter a number: "))
num = -7

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
"""
    ),
    code(
        """
severity = 2

if severity == 1:
    print("Alerting On-Call SRE...")
elif severity == 2:
    print("Log warning; monitor throughput.")
else:
    print("No action required.")
"""
    ),
    md(
        "Change `severity` to `1` and then to `3`, re-running the cell each "
        "time, so you see all three branches fire."
    ),
    slide(
        4,
        "The for Loop",
        """
A `for` loop steps through a sequence, one item at a time. `range()` is the
most common starting point, a built in function that generates a run of
numbers.

`range(start, stop, step)`: `start` defaults to 0, `stop` is required and is
**not** included, `step` defaults to 1.
""",
    ),
    code(
        """
for i in range(1, 6):
    print(i)
"""
    ),
    code(
        """
for attempt in range(1, 4):
    print(f"Deployment attempt {attempt}...")
"""
    ),
    turn(
        1,
        "Print a countdown from 5 down to 1 using `range()`. You need all three "
        "arguments, because you are counting backwards.",
    ),
    todo(
        """
# TODO: count down 5, 4, 3, 2, 1 using range(start, stop, step).
for n in range(____, ____, ____):
    print(f"restarting in {n}...")

print("restarting now")
""",
        """
for n in range(5, 0, -1):
    print(f"restarting in {n}...")

print("restarting now")
""",
    ),
    slide(
        5,
        "Looping Over a String",
        """
A string is also a sequence, so a `for` loop can step through it character by
character.

**Coming up.** Module 6 introduces lists and tuples, which are also sequences
you can loop through the same way. Once you have that module, come back and try
looping over a list here.
""",
    ),
    code(
        """
word = "Python"

for char in word:
    print(char)
"""
    ),
    code(
        """
# The same idea, used to imitate a reply streaming in one character at a time.
for char in "ERR404":
    print(char, end=" ", flush=True)

print()
"""
    ),
    slide(
        6,
        "The while Loop",
        """
A `while` loop repeats as long as its condition stays `True`. Remember to
update the condition inside the loop, or it will run forever.

**The three parts of a while loop.** A starting value, a condition to check,
and a step that moves toward ending the loop.
""",
    ),
    code(
        """
i = 1

while i <= 5:
    print(i)
    i += 1
"""
    ),
    code(
        """
health_score = 100

while health_score > 95:
    print(f"System Healthy: {health_score}%")
    health_score -= 1

print("dropped below threshold at", health_score)
"""
    ),
    slide(
        7,
        "break and continue",
        """
`break` stops the loop immediately. `continue` skips the rest of the current
pass and moves to the next one.
""",
    ),
    code(
        """
# break: stop at 5
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

print()
"""
    ),
    code(
        """
# continue: skip vowels
for char in "education":
    if char in "aeiou":
        continue
    print(char, end="")

print()
"""
    ),
    turn(
        2,
        "Poll a resource up to five times, waiting for it to become ready. It "
        "becomes ready on the third attempt. Stop the loop the moment it is "
        "ready, rather than running the remaining attempts.",
    ),
    todo(
        """
attempt = 0
ready_on = 3

# TODO: allow at most 5 attempts, and leave the loop early once ready.
while attempt < ____:
    attempt += 1
    print("attempt", attempt, "checking resource...")

    if attempt == ready_on:
        print("resource is ready")
        ____

print("finished after", attempt, "attempts")
""",
        """
attempt = 0
ready_on = 3

while attempt < 5:
    attempt += 1
    print("attempt", attempt, "checking resource...")

    if attempt == ready_on:
        print("resource is ready")
        break

print("finished after", attempt, "attempts")
""",
    ),
    slide(
        8,
        "pass: the Placeholder",
        """
`pass` does nothing. It exists so Python has a valid statement to run when you
are not ready to write the real logic yet.
""",
    ),
    code(
        """
for i in range(5):
    pass          # to be filled in later

print("loop finished without doing anything")
"""
    ),
    lab(
        "A triage simulation",
        """
Work only with `range()`, strings, and the loop statements from this module.

First, loop over the severity levels 1, 2 and 3 with `range()`. For each one,
use an `if` / `elif` / `else` chain to print what happens: severity 1 pages the
on-call engineer, severity 2 logs a warning, anything else needs no action.

Second, count how many of those levels were page-level, using a counter you
update inside the loop, and print the total once the loop has finished.

Third, write a `while` loop that simulates up to six deployment attempts and
stops early with `break` on the fourth, printing the attempt number each time.

Fourth, loop over the string `"ERR404"` and use `continue` to skip the digits,
printing only the letters.
""",
        [
            "One if / elif / else chain covers all three severities",
            "A counter is updated inside the loop and printed once after it",
            "A while loop stops early with break",
            "continue skips part of a pass over a string",
            "No lists anywhere, since they arrive in Module 6",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Write a for loop that prints the status of each server in a list of server names, using a placeholder status.",
            "Write a while loop that checks up to 5 times whether a cloud resource is ready, printing an attempt count each time.",
            "Write an if/elif/else chain that classifies an incident by severity level (1, 2, or 3) and prints the right response.",
            "Write a for loop that prints each character of a string one at a time, the way a streamed response might appear.",
        ],
        "You can now make decisions, repeat work, and steer a loop with break, continue and pass. "
        "Exercise 1 needs a list, so come back to it after Module 6.",
    ),
]

# ---------------------------------------------------------------- Module 6

M6 = [
    header(
        6,
        "Lists, Tuples, Dictionaries, and Sets",
        "Four ways to hold a group of values, and how to pick the right one.",
        [
            "Pick the right collection on order, changeability and duplicates",
            "Create, access, grow and reorder a list, and build one in a single line",
            "Unpack a tuple, and know why a one item tuple needs a trailing comma",
            "Look values up safely in a dictionary, including nested ones",
            "Use a set to drop duplicates and to answer 'does this exist'",
        ],
        "It follows the Module 6 slide deck, slide by slide.",
        "Modules 1 to 5. Loops and `if` are used freely here, since Module 5 "
        "covered them, and this is where the list you were promised in Module 5 "
        "finally arrives.",
    ),
    slide(
        2,
        "What Are Collections?",
        """
Python has four built in ways to hold a group of values. Picking the right one
comes down to order, whether it can change, and whether duplicates matter.

| Written as | Type | Ordered | Changeable | Duplicates |
|---|---|---|---|---|
| `[ ]` | List | yes | yes | yes |
| `( )` | Tuple | yes | no | yes |
| `{ k: v }` | Dictionary | yes | yes | keys are unique |
| `{ }` | Set | no | yes | no |
""",
    ),
    slide(
        3,
        "Lists: Creating and Accessing",
        """
A list holds items in order and lets you add, remove or change them after
creation. Indexing and slicing work exactly as they did for strings in
Module 3.
""",
    ),
    code(
        """
empty_list = []
mixed_list = [10, "Python", 3.14, True]
nested_list = [
    [1, 2, 3],
    ["a", "b", "c"],
]

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print("how many:", len(numbers))
print(nested_list[1][0])
"""
    ),
    slide(
        4,
        "Common List Methods",
        """
These are the methods you will use to grow, shrink and reorder a list.

| Method | What it does |
|---|---|
| `append(x)` | Add one item to the end |
| `extend(list)` | Add several items |
| `insert(i, x)` | Insert at a position |
| `remove(x)` | Delete the first match |
| `pop(i)` | Remove and return by index |
| `sort()` / `reverse()` | Reorder in place |
""",
    ),
    code(
        """
regions = ["us-east-1", "us-west-2"]
regions.append("eu-central-1")
print(regions)

error_codes = [404, 500]
error_codes.extend([502, 504])
print(error_codes)

error_codes.sort()
print("sorted:", error_codes)
print("popped:", error_codes.pop(), "-> remaining:", error_codes)
"""
    ),
    slide(
        5,
        "List Comprehensions",
        """
A list comprehension builds a new list in one line, combining a loop and a
condition.

**Reading the pattern.** `[expression for item in sequence if condition]`, and
the condition part is optional.
""",
    ),
    code(
        """
squares = [x**2 for x in range(1, 6)]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)
"""
    ),
    code(
        """
latencies = [12.4, 45.1, 8.9, 102.3, 15.6]

critical = [l for l in latencies if l > 50]
print(critical)

# The same thing written the long way, for comparison.
critical_long = []
for l in latencies:
    if l > 50:
        critical_long.append(l)

print(critical_long)
"""
    ),
    turn(
        1,
        "Keep only the pipeline stages whose name contains `\"test\"`, using a "
        "list comprehension rather than a loop with append.",
    ),
    todo(
        """
stages = ["build", "unit-test", "lint", "integration-test", "deploy"]

# TODO: complete the comprehension so only stages containing "test" survive.
test_stages = [s ____ s ____ stages ____ "test" ____ s]

print(test_stages)
""",
        """
stages = ["build", "unit-test", "lint", "integration-test", "deploy"]

test_stages = [s for s in stages if "test" in s]

print(test_stages)
""",
    ),
    slide(
        6,
        "Looping Over a List",
        """
Now that lists exist, the `for` loop from Module 5 can step through one
directly. This is the exercise Module 5 told you to come back for.

**Skipping empty values.** A list can hold gaps. Checking a value inside an
`if`, called **truthiness**, skips anything empty or missing: `None`, `""` and
`[]` all count as `False`.
""",
    ),
    code(
        """
scores = [88, 92, 79, 95]

for score in scores:
    print(f"Score: {score}")
"""
    ),
    code(
        """
pieces = ["Hello", None, " ", "", "world"]
full = ""

for piece in pieces:
    if piece:                 # skips None and ""
        full += piece

print(repr(full))
"""
    ),
    slide(
        7,
        "Tuples: Ordered and Unchangeable",
        """
A tuple looks like a list but cannot be modified after creation. Use one when
the data should not change, such as coordinates or a fixed record.

**The trailing comma matters.** `(5)` is just the number 5 in parentheses.
`(5,)` with a comma is a one item tuple.
""",
    ),
    code(
        """
mixed_tuple = (10, "Python", 3.14, True)
single_element = (5,)

numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[1:4])
print(type(single_element), type((5)))

# fruits = ("apple", "banana")
# fruits[1] = "blueberry"     -> this raises an error
"""
    ),
    slide(
        8,
        "Unpacking Tuples",
        """
Unpacking lets you assign each item in a tuple to its own variable in one line.
""",
    ),
    code(
        """
person = ("John", 25, "Engineer")
name, age, job = person

print(name, age, job)
"""
    ),
    slide(
        9,
        "Dictionaries: Key and Value Pairs",
        """
A dictionary stores data as key value pairs. Keys must be unique and are used
to look up values quickly.

**Safe access with `get()`.** `student.get("email", "N/A")` returns `"N/A"`
instead of raising an error when the key does not exist.
""",
    ),
    code(
        """
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "Physics"],
}

print(student["name"])
print(student.get("email", "N/A"))

student["city"] = "New York"
student["grade"] = "A+"
del student["age"]

print(student)
"""
    ),
    slide(
        10,
        "Useful Dictionary Methods",
        """
These make reading, combining and looping through a dictionary straightforward.

| Method | What it does |
|---|---|
| `get(key)` | Read a value safely |
| `keys()` / `values()` / `items()` | Loop over keys, values or pairs |
| `update(other)` | Merge another dictionary in |
| `pop(key)` | Remove and return a value |
""",
    ),
    code(
        """
for key, value in student.items():
    print(f"{key} -> {value}")

print()
print("keys  :", list(student.keys()))
print("values:", list(student.values()))
"""
    ),
    slide(
        11,
        "Nested Dictionaries",
        """
A dictionary value can be another dictionary. This nesting shows up constantly
in real data.

**AI framing.** An AI API response is usually a nested dictionary. Reading it
is the same skill as reading `student["subjects"]`, just one or two levels
deeper.
""",
    ),
    code(
        """
response = {
    "model": "llama3.2:1b",
    "message": {
        "role": "assistant",
        "content": "Hello Serge!",
    },
    "done": True,
}

print(response["message"]["content"])
"""
    ),
    slide(
        12,
        "Dictionary Comprehension",
        """
The same one-line pattern from list comprehensions works for dictionaries too.
""",
    ),
    code(
        """
squares = {x: x**2 for x in range(1, 6)}
print(squares)
"""
    ),
    slide(
        13,
        "Lists of Dictionaries",
        """
A list can hold dictionaries as its items. Chat APIs represent conversation
history exactly this way: each item is a dictionary with a role and content,
which is the list and dictionary skills you already have, combined.
""",
    ),
    code(
        """
messages = [
    {"role": "user", "content": "Hi, I am Serge."},
    {"role": "assistant", "content": "Hello Serge!"},
    {"role": "user", "content": "What is my name?"},
]

print(messages[0]["role"])
print(messages[-1]["content"])

for m in messages:
    print(f"[{m['role']:>9}] {m['content']}")
"""
    ),
    slide(
        14,
        "Sets: Unordered and Unique",
        """
A set automatically drops duplicates and does not preserve order. Reach for one
when you only care whether something exists.

**No indexing.** Since a set has no order, there is no `fruits[0]`. You can
only check membership or loop through it.
""",
    ),
    code(
        """
fruits = {"apple", "banana", "apple", "cherry"}

print(fruits)
print("banana" in fruits)
print("how many unique:", len(fruits))
"""
    ),
    slide(
        15,
        "Set Operations",
        """
Sets support the same operations as maths sets, using `A = {1, 2, 3}` and
`B = {3, 4, 5}`.

| Operation | Call | Result |
|---|---|---|
| union | `A.union(B)` | `{1,2,3,4,5}` |
| intersection | `A.intersection(B)` | `{3}` |
| difference | `A.difference(B)` | `{1,2}` |
| symmetric difference | `A.symmetric_difference(B)` | `{1,2,4,5}` |
""",
    ),
    code(
        """
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
"""
    ),
    turn(
        2,
        "Total the instances across every region in a dictionary, then reduce a "
        "list of log codes to just the unique ones.",
    ),
    todo(
        """
counts = {"us-east-1": 10, "eu-west-1": 8, "ap-south-1": 4}

# TODO: which dictionary method hands you just the numbers?
total = sum(counts.____())
print("total instances:", total)

log_codes = [500, 404, 500, 502, 404, 500]

# TODO: which collection type removes duplicates for you?
unique_codes = ____(log_codes)
print("unique codes:", sorted(unique_codes))
""",
        """
counts = {"us-east-1": 10, "eu-west-1": 8, "ap-south-1": 4}

total = sum(counts.values())
print("total instances:", total)

log_codes = [500, 404, 500, 502, 404, 500]

unique_codes = set(log_codes)
print("unique codes:", sorted(unique_codes))
""",
    ),
    lab(
        "Summarise a chat history",
        """
Build a list of dictionaries representing a short conversation, with at least
five turns alternating between `user` and `assistant`.

Then produce a summary that prints:

1. Only the assistant's replies, each on its own line, using a list
   comprehension rather than a loop with an `if` inside it
2. How many turns each role took, using a dictionary you build as you loop
3. The set of unique roles that appear
4. The longest message and which role sent it, found by comparing lengths as
   you loop rather than by eye
""",
        [
            "The history is a list of dictionaries with role and content keys",
            "The assistant replies are filtered with a list comprehension",
            "A dictionary holds the per-role counts",
            "A set gives the unique roles",
            "The longest message is found by comparing lengths in a loop",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Store a list of failed pipeline stage names and use a list comprehension to keep only the ones containing \"test\".",
            "Build a dictionary mapping cloud region names to their instance counts, then print the total across all regions.",
            "Use a set to find the unique error codes out of a list of incident log entries that contains duplicates.",
            "Build a list of dictionaries representing a short chat history, then print only the assistant's replies.",
        ],
        "You can now pick the right collection and work with lists, tuples, dictionaries and sets. "
        "This is also the moment to go back and finish Module 5's first practice exercise.",
    ),
]

# ---------------------------------------------------------------- Module 7

M7 = [
    header(
        7,
        "Handling Errors",
        "Catch problems instead of crashing, retry what's worth retrying, and raise your own errors.",
        [
            "Explain what happens when Python raises an error",
            "Catch a specific error with try and except",
            "Use multiple except blocks, plus else and finally",
            "Retry a flaky call instead of giving up on the first failure",
            "Raise your own error when your code detects a problem",
        ],
        "It follows the Module 7 slide deck, slide by slide.",
        "Modules 1 to 6. The retry slide uses `def` to build a function, exactly "
        "as the deck does. Functions get their full treatment in Module 8; here "
        "you only need to read one, not design one.",
    ),
    slide(
        2,
        "When Something Goes Wrong",
        """
When code fails, Python stops the program immediately and raises an error.
`try` and `except` catch that error so the program can respond instead of
crashing.

**Crashes**

```python
text = "abc"
number = int(text)
# ValueError: invalid literal for int()
# program stops here
```

**Handled**

```python
text = "abc"
try:
    number = int(text)
except ValueError:
    print("That was not a number.")
# program keeps running
```
""",
    ),
    code(
        """
# The crashing version, kept safe inside a demonstration.
text = "abc"

try:
    number = int(text)
except ValueError as e:
    print("Python raised:", type(e).__name__)
    print("with the message:", e)

print("and the program carried on")
"""
    ),
    slide(
        3,
        "try and except",
        """
Code inside `try` runs normally. If it raises the error type named in `except`,
that block runs instead of the program crashing.

**Name the error you expect.** `except ValueError` only catches `ValueError`. A
different error still crashes the program, which is usually what you want:
catching everything hides bugs.
""",
    ),
    code(
        """
text = "abc"

try:
    number = int(text)
except ValueError:
    print("That was not a number.")
"""
    ),
    code(
        """
# The same shape, applied to a truncated API response.
import json

broken_response = '{"id": "msg_01", "content": '

try:
    data = json.loads(broken_response)
    print("parsed fine:", data["content"])
except json.JSONDecodeError:
    print("Failed to parse API response.")
"""
    ),
    heads_up(
        "`import` appears here because JSON parsing needs it. Module 10 explains "
        "`import` in full. The short version: it brings in code someone else "
        "already wrote, used with a dot, like `json.loads()`."
    ),
    slide(
        4,
        "Multiple except, else, and finally",
        """
You can catch more than one kind of error. `else` runs only if nothing went
wrong. `finally` always runs, error or not.

**Why `finally` matters.** It is for cleanup work, like closing a connection,
that needs to happen whether or not something went wrong.
""",
    ),
    code(
        """
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Not a valid value.")
else:
    print("Success:", result)      # only if no exception
finally:
    print("Done trying.")          # always runs
"""
    ),
    md(
        "Change `10 / 0` to `10 / 2` and run the cell again. The `else` branch "
        "fires, and `finally` still runs. That is the whole point of the pair."
    ),
    turn(
        1,
        "An incident ticket must always end up marked closed, even when the "
        "update step fails. Pick the two keywords that catch the failure and "
        "guarantee the closing step.",
    ),
    todo(
        """
ticket = {"id": "INC-4412", "status": "open"}

# TODO: catch the failure, then guarantee the closing step always runs.
try:
    raise ConnectionError("ticketing system unreachable")
____ ConnectionError as e:
    print("could not update:", e)
____:
    ticket["status"] = "closed"

print(ticket)
""",
        """
ticket = {"id": "INC-4412", "status": "open"}

try:
    raise ConnectionError("ticketing system unreachable")
except ConnectionError as e:
    print("could not update:", e)
finally:
    ticket["status"] = "closed"

print(ticket)
""",
    ),
    slide(
        5,
        "Retrying Instead of Giving Up",
        """
Calling an AI model is a network call, and network calls fail sometimes: the
connection drops, the server is slow, or you hit a rate limit. Wrapping the
call lets your program recover instead of stopping.

**Reading the retry loop.** Each failed attempt is caught, logged and tried
again, up to a limit. Only after every attempt fails does the function give up
for good.
""",
    ),
    code(
        """
import time


def call_model(prompt):
    if prompt == "":
        raise TimeoutError("model did not respond in time")
    return f"response to: {prompt}"


def call_with_retry(prompt, attempts=3):
    for attempt in range(1, attempts + 1):
        try:
            return call_model(prompt)
        except TimeoutError:
            print(f"attempt {attempt} timed out, retrying...")
            time.sleep(0.2)
    raise RuntimeError("model call failed after all retries")


print(call_with_retry("Summarize this document."))
"""
    ),
    code(
        """
try:
    call_with_retry("")
except RuntimeError as e:
    print("gave up:", e)
"""
    ),
    slide(
        6,
        "Raising Your Own Errors",
        """
You are not limited to errors Python raises on its own. `raise` lets you signal
that something in your own code has gone wrong, with a message explaining why.

**`as e` captures the message.** `except ValueError as e` lets you read the
error's message with `str(e)`, or just `print(e)`.
""",
    ),
    code(
        """
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age


try:
    set_age(-5)
except ValueError as e:
    print("Invalid input:", e)
"""
    ),
    turn(
        2,
        "Guard a model temperature setting. Anything outside 0.0 to 2.0 should "
        "signal a problem with a clear message, and the caller should catch it "
        "and read that message.",
    ),
    todo(
        """
def set_temperature(value):
    if value < 0.0 or value > 2.0:
        # TODO: signal the problem yourself, with the right error type.
        ____ ____(f"temperature {value} is outside 0.0 to 2.0")
    return value


print("valid:", set_temperature(0.7))

# TODO: catch it, and capture the message so it can be printed.
try:
    set_temperature(3.5)
except ValueError ____ e:
    print("rejected:", e)
""",
        """
def set_temperature(value):
    if value < 0.0 or value > 2.0:
        raise ValueError(f"temperature {value} is outside 0.0 to 2.0")
    return value


print("valid:", set_temperature(0.7))

try:
    set_temperature(3.5)
except ValueError as e:
    print("rejected:", e)
""",
    ),
    lab(
        "A deployment run that refuses to crash",
        """
Write a function `deploy(stage)` that raises a `RuntimeError` when the stage
name is `"migrate"`, and otherwise returns a success message.

Loop over the stages `build`, `test`, `migrate`, `release` and call `deploy()`
for each one. A failing stage must not stop the others.

Record every outcome in a results dictionary. Use `finally` so a line is always
printed for each stage, whether it succeeded or not. At the end, print how many
stages succeeded and how many failed.

For extra credit, wrap the `migrate` stage in the retry pattern from slide 5,
giving it three attempts before recording it as failed.
""",
        [
            "deploy() raises for one specific stage",
            "One failing stage does not stop the loop",
            "finally guarantees a line per stage",
            "A results dictionary records every outcome",
            "A summary counts successes and failures",
        ],
    ),
    code(
        """
stages = ["build", "test", "migrate", "release"]

# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Wrap a deployment step function in try/except to catch a simulated DeploymentError and print a clear message.",
            "Write a retry loop around a function that checks whether a cloud storage bucket exists, catching a simulated exception.",
            "Use try/except/finally so an incident ticket always gets marked as closed, even if updating it raises an error.",
            "Add retry logic around a function that simulates calling a model API which sometimes raises a TimeoutError.",
        ],
        "You can now catch errors, retry what's worth retrying, and raise your own.",
    ),
]

# ---------------------------------------------------------------- Module 8

M8 = [
    header(
        8,
        "Functions",
        "Package reusable logic, pass arguments four different ways, and stream results with yield.",
        [
            "Define a function with def and call it",
            "Tell a parameter from an argument, and know why return ends a function",
            "Use all four kinds of argument, including *args and **kwargs",
            "Write a generator with yield and see why streaming needs it",
            "Pass a function itself as a value into another function",
        ],
        "It follows the Module 8 slide deck, slide by slide.",
        "Modules 1 to 7. You have already read functions in Module 7's retry "
        "example; this is where you write them.",
    ),
    slide(
        2,
        "What Is a Function?",
        """
A function is a reusable block of code. You define it once with `def` and call
it as many times as you need, which keeps your programs organised.

**Order matters.** A function must be defined before it is called, and the code
inside it must be indented consistently.
""",
    ),
    code(
        """
def greet():
    print("Hello! Welcome to Python.")


greet()          # calls the function
greet()
"""
    ),
    slide(
        3,
        "Parameters, Arguments, Return",
        """
A **parameter** is the name listed in the definition. An **argument** is the
value you pass in. `return` sends a value back to whoever called the function.

**`return` stops the function.** Once `return` runs, the function ends
immediately. Any code written after it never executes.
""",
    ),
    code(
        """
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


def square(num):
    return num * num


result = square(4)
print("Square:", result)
"""
    ),
    code(
        """
def early_exit():
    return "first"
    print("this line never runs")


print(early_exit())
"""
    ),
    slide(
        4,
        "Four Kinds of Arguments",
        """
A function can accept arguments in four different ways, and you will mix and
match them.

| Kind | Looks like | Matched by |
|---|---|---|
| Positional | `func(1, 2)` | order |
| Default | `def func(a=5)` | falls back if omitted |
| Keyword | `func(b=10, a=5)` | name |
| Variable length | `*args` / `**kwargs` | collects the extras |
""",
    ),
    code(
        """
def add(a, b):
    return a + b


print(add(3, 5))
"""
    ),
    slide(
        5,
        "Default and Keyword Arguments",
        """
A default value fills in when the caller leaves an argument out. Keyword
arguments let a call stay readable no matter the order.

**This is how AI SDKs read.** Keyword arguments are exactly how you call real
AI SDKs, for example `ollama.chat(model=..., messages=..., options=...)`.
""",
    ),
    code(
        """
def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()
greet("Alice")


def describe_pet(animal, name):
    print(f"{name} is a {animal}.")


describe_pet(animal="dog", name="Buddy")
describe_pet(name="Kitty", animal="cat")
"""
    ),
    turn(
        1,
        "Write a deployment message builder. The service is passed by position, "
        "the environment has a default of `\"dev\"`, and the message is handed "
        "back to the caller rather than printed inside the function.",
    ),
    todo(
        """
# TODO: give environment a default of "dev", and send the message back.
def deployment_message(service, environment____):
    ____ f"Deploying {service} to {environment}"


print(deployment_message("api-gateway"))
print(deployment_message("api-gateway", environment="prod"))
""",
        """
def deployment_message(service, environment="dev"):
    return f"Deploying {service} to {environment}"


print(deployment_message("api-gateway"))
print(deployment_message("api-gateway", environment="prod"))
""",
    ),
    slide(
        6,
        "*args and **kwargs",
        """
`*args` collects any number of extra positional values into a **tuple**.
`**kwargs` collects any number of extra named values into a **dictionary**.
Both are Module 6 types you already know.

**The names are a convention.** `args` and `kwargs` are not keywords. The `*`
and `**` are what matter; you could name them anything.
""",
    ),
    code(
        """
def add_numbers(*args):
    print("received a", type(args).__name__, ":", args)
    return sum(args)


print(add_numbers(1, 2, 3, 4))
"""
    ),
    code(
        """
def describe_person(**kwargs):
    print("received a", type(kwargs).__name__)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


describe_person(name="Alice", age=25, city="New York")
"""
    ),
    slide(
        7,
        "Generators: yield Instead of return",
        """
`return` sends back one value and ends the function. `yield` sends back a value
and **pauses**, continuing later from exactly where it left off.

**AI framing.** This is how streaming AI responses are built up piece by piece
on screen.
""",
    ),
    code(
        """
def stream_reply(tokens):
    full = ""
    for token in tokens:
        full += token
        yield full


for partial in stream_reply(["Hi, ", "I ", "am ", "an ", "AI."]):
    print(partial)
"""
    ),
    slide(
        8,
        "Passing a Function as a Value",
        """
A function name **without parentheses** is just a value, like any variable. You
can pass it into another function and call it later. Tools such as Gradio use
this pattern constantly.
""",
    ),
    code(
        """
def run_chat(fn, user_text):
    return fn(user_text, history=[])


def my_bot(message, history):
    return f"You said: {message}"


print(run_chat(fn=my_bot, user_text="Hello"))
# note: pass my_bot, not my_bot()
"""
    ),
    turn(
        2,
        "Write a generator that yields incident status updates one at a time, "
        "then a runner that takes any function as a value and applies it to a "
        "message.",
    ),
    todo(
        """
updates = ["triage started", "root cause found", "fix deployed", "resolved"]


def status_stream(items):
    for item in items:
        # TODO: hand back one value at a time WITHOUT ending the function.
        ____ f"[update] {item}"


for line in status_stream(updates):
    print(line)


def process(callback, message):
    # TODO: call whatever function was handed in.
    return ____(message)


def shout(text):
    return text.upper()


# TODO: pass the function itself, not its result.
print(process(____, "incident closed"))
""",
        """
updates = ["triage started", "root cause found", "fix deployed", "resolved"]


def status_stream(items):
    for item in items:
        yield f"[update] {item}"


for line in status_stream(updates):
    print(line)


def process(callback, message):
    return callback(message)


def shout(text):
    return text.upper()


print(process(shout, "incident closed"))
""",
    ),
    lab(
        "A small cost calculator toolkit",
        """
Write three functions that work together, one for each of the ideas in this
module.

`monthly_cost(*resources)` takes any number of per-resource monthly costs and
returns the total.

`format_bill(total, currency="USD", warn_above=500)` returns a formatted string
with the total to two decimal places, and appends `" OVER BUDGET"` when the
total is above the threshold. Both extra parameters must have working defaults.

`report(builder, *resources)` takes a **function** as its first argument, calls
`monthly_cost` on the resources, passes the total to `builder`, and returns the
result.

Prove all three work by calling `report(format_bill, 120.0, 340.5, 88.25)`.

For extra credit, add a generator that yields each resource cost as a running
total, the way `stream_reply` did.
""",
        [
            "monthly_cost uses *args and works with any number of values",
            "format_bill has two working default arguments",
            "report accepts a function as a value and calls it",
            "The final call prints a formatted total with the budget warning",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Write a function that takes a service name and environment as keyword arguments and returns a formatted deployment message.",
            "Write a function using *args that sums the estimated monthly costs of any number of cloud resources.",
            "Write a generator function that yields incident status updates one at a time, from a list of updates.",
            "Write a function that accepts another function as a callback and uses it to process a chat message, the way the Gradio example does.",
        ],
        "You can now write functions, handle arguments four ways, and stream results with yield.",
    ),
]
