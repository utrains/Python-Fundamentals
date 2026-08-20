"""Modules 5 to 8: control flow, collections, errors, functions."""

from nbcore import header, md, code, todo, turn, lab, practice

# ---------------------------------------------------------------- Module 5

M5 = [
    header(
        5,
        "Control Flow",
        [
            "Make decisions with if, elif and else",
            "Repeat work with a for loop over range() and over a string",
            "Repeat while a condition holds, without writing an endless loop",
            "Interrupt a loop with break, continue and pass",
        ],
        "Part 3 of the course: Control Flow and Collections.",
    ),
    md(
        """
Control flow statements let a program make decisions and repeat work. This
module covers conditionals, loops, and the statements that interrupt a loop.

## if, elif and else

Python uses **indentation**, not curly braces, to mark what belongs inside a
block. Four spaces is the standard.
"""
    ),
    code(
        """
# In a script this would be: severity = int(input("Enter severity (1-3): "))
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
        """
Change `severity` to `1` and then to `3`, re-running the cell each time, so you
see all three branches fire.

## The for loop

A `for` loop steps through a sequence one item at a time. The most common
sequence to start with is `range()`, which generates a run of numbers. It takes
up to three arguments: `range(start, stop, step)`. `start` defaults to 0,
`stop` is required and is **not** included, and `step` defaults to 1.
"""
    ),
    code(
        """
for attempt in range(1, 4):
    print(f"Deployment attempt {attempt}...")
"""
    ),
    md("A string is also a sequence, so you can loop through it character by character."),
    code(
        """
error_code = "ERR404"

for char in error_code:
    print(char)
"""
    ),
    turn(
        1,
        "Print a countdown from 5 down to 1 using range(). You need all three "
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
    md(
        """
## The while loop

A `while` loop repeats as long as its condition stays `True`. Remember to
update the condition inside the loop, or it will run forever.
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
    md(
        """
## break, continue and pass

- `break` stops the loop immediately
- `continue` skips the rest of this iteration and moves to the next one
- `pass` does nothing, and is a placeholder for where you are not ready to
  write code yet
"""
    ),
    code(
        """
# break: stop at 5
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print()

# continue: skip vowels
for char in "education":
    if char in "aeiou":
        continue
    print(char, end="")
print()

# pass: placeholder
for i in range(5):
    pass

print("loop finished without doing anything")
"""
    ),
    turn(
        2,
        "Poll a resource until it reports ready, but give up after five "
        "attempts. Stop the loop the moment it is ready.",
    ),
    todo(
        """
statuses = ["pending", "pending", "creating", "ready", "ready"]
attempt = 0

# TODO: loop up to 5 times, and leave the loop early once status is ready.
while attempt < ____:
    status = statuses[attempt]
    attempt += 1
    print(f"attempt {attempt}: {status}")
    if status == "ready":
        print("resource is ready")
        ____

if status != "ready":
    print("gave up after", attempt, "attempts")
""",
        """
statuses = ["pending", "pending", "creating", "ready", "ready"]
attempt = 0

while attempt < 5:
    status = statuses[attempt]
    attempt += 1
    print(f"attempt {attempt}: {status}")
    if status == "ready":
        print("resource is ready")
        break

if status != "ready":
    print("gave up after", attempt, "attempts")
""",
    ),
    lab(
        "Classify a batch of incidents",
        """
You are given a list of incident severities. Loop through them and, for each
one, print a line saying what happens: severity 1 pages the on-call engineer,
severity 2 logs a warning, anything else needs no action.

Then count how many of each kind you saw and print a summary at the end.

Finally, add a rule: if you ever hit a severity of `0`, that is a data error.
Print a message and stop processing the rest of the list immediately.
""",
        [
            "One if / elif / else chain handles all three cases",
            "A counter for each severity is updated inside the loop",
            "A summary prints once, after the loop, not inside it",
            "A severity of 0 stops the loop with break",
        ],
    ),
    code(
        """
severities = [3, 2, 1, 3, 2, 0, 1, 3]

# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Write a for loop that prints the status of each server in a list of server names, using a placeholder status.",
            "Write a while loop that checks up to 5 times whether a cloud resource is ready, printing an attempt count each time.",
            "Write an if/elif/else chain that classifies an incident by severity level (1, 2, or 3) and prints the right response.",
            "Write a for loop that prints each character of a string one at a time, the way a streamed response might appear.",
        ]
    ),
]

# ---------------------------------------------------------------- Module 6

M6 = [
    header(
        6,
        "Lists, Tuples, Dictionaries and Sets",
        [
            "Choose between the four collection types on order, mutability and duplicates",
            "Add, remove and slice list items, and build a list in one line with a comprehension",
            "Look values up safely in a dictionary, including nested ones",
            "Use a set to answer 'does this exist' and to remove duplicates",
        ],
        "Part 3 of the course: Control Flow and Collections.",
    ),
    md(
        """
Python gives you four built in ways to hold a group of values. Picking the
right one comes down to three questions: do you need **order**, should the
values be **changeable**, and do **duplicates** matter?

| Type | Ordered | Changeable | Duplicates |
|---|---|---|---|
| list `[]` | yes | yes | yes |
| tuple `()` | yes | no | yes |
| dict `{k: v}` | yes | yes | keys must be unique |
| set `{}` | no | yes | no |

## Lists: ordered and changeable
"""
    ),
    code(
        """
empty_list = []
services = ["api-gateway", "auth-service", "worker-node"]
cluster_map = [["us-east-1", 10], ["eu-west-1", 8]]

print(services)
print(cluster_map)
print("how many services:", len(services))
"""
    ),
    code(
        """
nodes = ["node-01", "node-02", "node-03", "node-04", "node-05"]

print(nodes[0])
print(nodes[-1])
print(nodes[1:4])
print(nodes[::2])
"""
    ),
    md(
        """
### Common list methods

`append(x)` adds one item to the end &middot; `extend(iterable)` adds several
&middot; `insert(i, x)` inserts at a position &middot; `remove(x)` deletes the
first match &middot; `pop(i)` removes and returns by position &middot; `sort()`
sorts in place &middot; `reverse()` flips the order in place
"""
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
    md(
        """
### List comprehensions

A list comprehension builds a new list in one line, combining a loop and an
optional condition. Read it as: *the value I want, for each item, if a test
passes.*
"""
    ),
    code(
        """
latencies = [12.4, 45.1, 8.9, 102.3, 15.6]

critical = [l for l in latencies if l > 50]
print(critical)

# The same thing written out the long way, for comparison.
critical_long = []
for l in latencies:
    if l > 50:
        critical_long.append(l)
print(critical_long)
"""
    ),
    turn(
        1,
        "Keep only the pipeline stages whose name contains 'test', using a "
        "list comprehension.",
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
    md(
        """
### Truthiness when looping

A list can hold gaps or missing pieces. Checking a value inside an `if`, called
**truthiness**, lets you skip anything empty or missing. `None`, an empty
string and an empty list are all treated as `False`.
"""
    ),
    code(
        """
pieces = ["Hello", None, " ", "", "world"]
full = ""

for piece in pieces:
    if piece:              # skips None and ""
        full += piece

print(repr(full))
"""
    ),
    md(
        """
## Tuples: ordered and unchangeable

Use a tuple when the data should not change, such as coordinates or a fixed
record. The trailing comma in a one item tuple matters.
"""
    ),
    code(
        """
mixed_tuple = (10, "Python", 3.14, True)
single_element = (5,)

numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[1:4])
print(type(single_element))

# Unpacking assigns each item to its own variable in one line.
person = ("John", 25, "Engineer")
name, age, job = person
print(name, age, job)

# This would raise a TypeError, which is the whole point of a tuple:
# person[1] = 26
"""
    ),
    md(
        """
## Dictionaries: key and value pairs

A dictionary stores data as key/value pairs. Keys must be unique and are used
to look values up quickly. `get()` is the safe way to read: it returns a
fallback instead of raising `KeyError` when the key is missing.
"""
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

for key, value in student.items():
    print(f"{key} -> {value}")
"""
    ),
    md(
        """
An AI API response is usually a **nested** dictionary. Reading it is the same
skill as reading `student["subjects"]`, just one or two levels deeper.
"""
    ),
    code(
        """
response = {
    "model": "llama3.2:1b",
    "message": {
        "role": "assistant",
        "content": "Hello Serge! Nice to meet you.",
    },
    "done": True,
}

print(response["message"]["content"])
"""
    ),
    code(
        """
squares = {x: x**2 for x in range(1, 6)}
print(squares)
"""
    ),
    md(
        """
### Lists of dictionaries

A list can hold dictionaries as its items. Chat APIs represent conversation
history exactly this way: a list where each entry is a dictionary with a role
and content.
"""
    ),
    code(
        """
messages = [
    {"role": "user", "content": "Hi, I am Serge."},
    {"role": "assistant", "content": "Hello Serge! Nice to meet you."},
    {"role": "user", "content": "What is my name?"},
]

print(messages[0]["role"])
print(messages[-1]["content"])

for m in messages:
    print(f"[{m['role']:>9}] {m['content']}")
"""
    ),
    md(
        """
## Sets: unordered and unique

A set drops duplicates automatically and does not preserve order. Reach for one
when you only care **whether** something exists, not how many times.
"""
    ),
    code(
        """
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)

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
        "Build a dictionary of region to instance count, print the total "
        "across all regions, then find the unique error codes from a list "
        "that contains duplicates.",
    ),
    todo(
        """
counts = {"us-east-1": 10, "eu-west-1": 8, "ap-south-1": 4}

# TODO: which dict method gives you just the numbers?
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

1. Only the assistant's replies, each on its own line
2. How many turns each role took, using a dictionary you build as you loop
3. The set of unique roles that appear
4. The longest message, and which role sent it

Use a list comprehension for at least one of these.
""",
        [
            "The history is a list of dictionaries with role and content keys",
            "The assistant replies are filtered out, not hand-copied",
            "A dictionary holds the per-role counts",
            "A set is used for the unique roles",
            "The longest message is found by comparing lengths, not by eye",
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
        ]
    ),
]

# ---------------------------------------------------------------- Module 7

M7 = [
    header(
        7,
        "Handling Errors",
        [
            "Catch a failure with try and except instead of crashing",
            "Use else and finally for success-only and always-run code",
            "Retry a flaky call instead of giving up on the first failure",
            "Raise your own errors when your code detects a problem",
        ],
        "Part 4 of the course: Writing Reliable Code.",
    ),
    md(
        """
When something goes wrong, for example a value cannot be converted or a network
call times out, Python stops the program and raises an error. `try` and
`except` catch that error so the program can respond instead of crashing.

## try and except
"""
    ),
    code(
        """
import json

api_response = '{"id": "msg_01", "content": "Success"}'

try:
    data = json.loads(api_response)
    print("parsed fine:", data["content"])
except json.JSONDecodeError:
    print("Failed to parse API response.")
"""
    ),
    code(
        """
broken_response = '{"id": "msg_01", "content": '   # truncated on the wire

try:
    data = json.loads(broken_response)
    print("parsed fine:", data["content"])
except json.JSONDecodeError:
    print("Failed to parse API response.")
"""
    ),
    md(
        """
You can catch more than one kind of error, and use `else` for code that should
only run on success and `finally` for code that must always run.
"""
    ),
    code(
        """
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("That was not a valid value.")
else:
    print("Success:", result)      # only if no exception happened
finally:
    print("Done trying.")          # always runs, error or not
"""
    ),
    md(
        """
> `finally` is for cleanup work, such as closing a connection, that has to
> happen whether or not something went wrong.
"""
    ),
    turn(
        1,
        "An incident ticket must always end up marked closed, even when the "
        "update step blows up. Pick the right two keywords.",
    ),
    todo(
        """
def update_ticket(ticket_id):
    raise ConnectionError("ticketing system unreachable")

ticket = {"id": "INC-4412", "status": "open"}

# TODO: catch the failure, and guarantee the closing step always runs.
try:
    update_ticket(ticket["id"])
    print("ticket updated")
____ ConnectionError as e:
    print("could not update:", e)
____:
    ticket["status"] = "closed"

print(ticket)
""",
        """
def update_ticket(ticket_id):
    raise ConnectionError("ticketing system unreachable")

ticket = {"id": "INC-4412", "status": "open"}

try:
    update_ticket(ticket["id"])
    print("ticket updated")
except ConnectionError as e:
    print("could not update:", e)
finally:
    ticket["status"] = "closed"

print(ticket)
""",
    ),
    md(
        """
## Retrying instead of giving up

Calling an AI model is a network call, and network calls fail sometimes: the
connection drops, the server is slow, or you hit a rate limit. Wrapping the
call lets your program recover instead of stopping.

`time.sleep()` pauses between attempts. Module 10 covers `import` in full.
"""
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

try:
    call_with_retry("")
except RuntimeError as e:
    print("gave up:", e)
"""
    ),
    md(
        """
## Raising your own errors

You are not limited to errors Python raises on its own. `raise` lets you signal
that something in your own code has gone wrong, with a message explaining why.
"""
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
        "Write a guard that rejects an invalid model temperature. Anything "
        "outside 0.0 to 2.0 should raise, with a clear message.",
    ),
    todo(
        """
def set_temperature(value):
    if value < 0.0 or value > 2.0:
        # TODO: signal the problem yourself, with the right error type.
        ____ ____(f"temperature {value} is outside 0.0 to 2.0")
    return value


print("valid:", set_temperature(0.7))

try:
    set_temperature(3.5)
except ValueError as e:
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
        "A deployment step that refuses to crash",
        """
Write a function `deploy(stage)` that raises a `RuntimeError` when the stage
name is `"migrate"`, and otherwise returns a success message.

Then write a loop over the stages `build`, `test`, `migrate`, `release` that
calls `deploy()` for each one. A failing stage must not stop the others.

For every stage, record the outcome in a results dictionary. Use `finally` so
that a line is always printed for each stage, whether it succeeded or not. At
the end, print how many stages succeeded and how many failed.

For extra credit, wrap the `migrate` stage in the retry pattern from earlier in
this notebook and give it three attempts before recording it as failed.
""",
        [
            "deploy() raises for one specific stage",
            "One failing stage does not stop the loop",
            "finally guarantees a line per stage",
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
        ]
    ),
]

# ---------------------------------------------------------------- Module 8

M8 = [
    header(
        8,
        "Functions",
        [
            "Define a function and call it, and know why return ends it",
            "Use the four kinds of argument, including *args and **kwargs",
            "Write a generator with yield and see why streaming needs it",
            "Pass a function itself as a value into another function",
        ],
        "Part 4 of the course: Writing Reliable Code.",
    ),
    md(
        """
A function is a reusable block of code. You define it once with `def` and call
it as many times as you need, which keeps programs organised and stops you
repeating yourself.

## Defining and calling
"""
    ),
    code(
        """
def greet():
    print("Hello! Welcome to Python.")


greet()
greet()
"""
    ),
    md(
        """
## Parameters, arguments and return values

A **parameter** is the name in the definition. An **argument** is the value you
pass when calling. `return` sends a value back to the caller.

> Once `return` runs, the function stops immediately. Any code after it inside
> that function never executes.
"""
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


def early_exit():
    return "first"
    print("this line never runs")


print(early_exit())
"""
    ),
    md(
        """
## The four kinds of argument

- **Positional**, passed in the same order as the parameters: `func(1, 2)`
- **Default**, supplying a fallback when none is given: `def func(a=5)`
- **Keyword**, passed by name so order does not matter: `func(b=10, a=5)`
- **Variable length**, collecting extras with `*args` or `**kwargs`
"""
    ),
    code(
        """
def add(a, b):
    return a + b


print(add(3, 5))


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
    md(
        """
> The keyword argument style is exactly how you call real AI SDKs, for example
> `ollama.chat(model=..., messages=..., options=...)`.
"""
    ),
    turn(
        1,
        "Write a deployment message builder that takes the service positionally "
        "and the environment as a keyword argument with a sensible default.",
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
    md(
        """
### *args and **kwargs

`*args` collects any number of extra positional values into a **tuple**.
`**kwargs` collects any number of extra named values into a **dictionary**.
"""
    ),
    code(
        """
def add_numbers(*args):
    print("received a", type(args).__name__, ":", args)
    return sum(args)


print(add_numbers(1, 2, 3, 4))


def describe_person(**kwargs):
    print("received a", type(kwargs).__name__)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


describe_person(name="Alice", age=25, city="New York")
"""
    ),
    md(
        """
## Generators: yield instead of return

`return` sends back one value and ends the function. `yield` sends back a value
and **pauses**, letting the function continue later from exactly where it left
off. This is how streaming AI responses are built up piece by piece on screen.
"""
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
    md(
        """
## Passing a function as a value

A function name **without parentheses** is just a value, like any variable. You
can pass it into another function and call it later. Tools such as Gradio use
this pattern constantly.
"""
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
        "and a callback runner that applies any function to a message.",
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
Write three functions that work together.

`monthly_cost(*resources)` takes any number of per-resource monthly costs and
returns the total.

`format_bill(total, currency="USD", warn_above=500)` returns a formatted string
with the total to two decimal places, and appends `" OVER BUDGET"` when the
total is above the threshold. Both extra parameters must have defaults.

`report(builder, *resources)` takes a **function** as its first argument, calls
`monthly_cost` on the resources, then passes the total to `builder` and returns
the result.

Prove all three work by calling `report(format_bill, 120.0, 340.5, 88.25)`.
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
        ]
    ),
]
