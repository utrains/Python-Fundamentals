"""Modules 1 to 4: foundations, variables, strings, operators."""

from nbcore import header, md, code, todo, turn, lab, practice

# ---------------------------------------------------------------- Module 1

M1 = [
    header(
        1,
        "Getting Started with Python",
        [
            "Show output on screen with print()",
            "Keep several print() calls on one line with end and flush",
            "Read input from the person running the script",
            "Use Python as a calculator with the arithmetic operators",
        ],
        "Part 1 of the course: Foundations.",
    ),
    md(
        """
## Python in one paragraph

Python is a high level, interpreted language created by Guido van Rossum in
1991. *High level* means you write code close to plain English rather than
close to the machine. *Interpreted* means Python reads and runs your code line
by line, so there is no separate compile step before you see results.

First, confirm which version is running this notebook.
"""
    ),
    code(
        """
import sys

print("Python version:", sys.version.split()[0])
print("Running from:", sys.executable)
"""
    ),
    md(
        """
## The print() function

`print()` is how a Python program shows something on the screen. You call it
with the value you want displayed inside the parentheses.
"""
    ),
    code(
        """
print("Initializing deployment pipeline...")
print("Service: payment-gateway | Version: 2.1.0")
"""
    ),
    md(
        """
`print()` can also take several items separated by commas. Python inserts a
space between them automatically.
"""
    ),
    code(
        """
total_requests = 5000
failed_requests = 12

print("Current Error Rate:", (failed_requests / total_requests) * 100, "%")
print("The sum of 5 and 3 is:", 5 + 3)
"""
    ),
    md(
        """
### Printing without a new line

By default `print()` adds a new line after every call. When you want several
calls to stay on the same line, for example to show tokens streaming in from an
AI model one after another, pass `end` and `flush`.
"""
    ),
    code(
        """
print("Token 1 ", end="", flush=True)
print("Token 2 ", end="", flush=True)
print("Token 3")
"""
    ),
    turn(
        1,
        "Print a deployment banner on a single line, built from three separate "
        "`print()` calls. The first two must not break onto a new line.",
    ),
    todo(
        """
# TODO: fill in the blanks so all three pieces land on ONE line.
print("Deploying ", end=____, flush=True)
print("payment-gateway ", ____="", flush=True)
print("to us-east-1")
""",
        """
print("Deploying ", end="", flush=True)
print("payment-gateway ", end="", flush=True)
print("to us-east-1")
""",
    ),
    md(
        """
## The input() function

`input()` pauses your program and waits for the person running it to type
something and press Enter. Whatever they type is handed back to you as a
string.

```python
name = input("Enter your name: ")
print(name)
```

A notebook cell that calls `input()` sits there waiting, which makes a notebook
awkward to run top to bottom. So from here on we simulate the typed answer by
assigning the variable directly. The rest of the code is identical to what you
would write in a real script.
"""
    ),
    code(
        """
# In a script this line would be:  name = input("Enter your name: ")
name = "Serge"

print("Hello,", name)
"""
    ),
    md(
        """
> **Watch out:** `input()` always hands you back a string, even if the person
> typed digits. You have to convert it before doing maths with it. Module 2
> covers how.

## A first look at arithmetic

Python can act as a calculator. Operators such as `+` and `-` work the way you
would expect. A few, like `//` and `%`, are Python specific. Module 4 covers
every operator in depth.
"""
    ),
    code(
        """
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)
"""
    ),
    md(
        """
## Putting it together

This short program combines everything from the module: two values collected
from the user, the `+` operator to join them, and `print()` to show the result.
"""
    ),
    code(
        """
# In a script these two lines would be input() calls.
environment = "prod"
region = "us-east-1"

deploy_tag = region + "-" + environment
print("Pushing to artifact registry:", deploy_tag)
"""
    ),
    turn(
        2,
        "Build the same deploy tag, but put a colon between the region and the "
        "environment instead of a hyphen, and print it with a label.",
    ),
    todo(
        """
# TODO: join the two pieces with a colon, then print with a label.
environment = "stage"
region = "eu-west-1"

deploy_tag = region ____ ":" ____ environment
____("Artifact tag:", deploy_tag)
""",
        """
environment = "stage"
region = "eu-west-1"

deploy_tag = region + ":" + environment
print("Artifact tag:", deploy_tag)
""",
    ),
    lab(
        "Your first health check script",
        """
Write a few lines that print a service health banner.

Start by storing the service name, the latency in milliseconds and the status
in three variables. Then print a banner line, and on a second line print the
service, latency and status together in one `print()` call using commas.

Finish by printing three fake response tokens on the same line using `end` and
`flush`, followed by a final line break.
""",
        [
            "Three variables hold the service name, latency and status",
            "The banner prints on its own line",
            "The detail line uses one print() call with commas",
            "Three tokens appear on a single line, then the output ends cleanly",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Write a script that prints a deployment banner with your service name and version number using variables and print().",
            "Use input() to ask for a cloud region name, then print a one-line confirmation message using that region.",
            "Use the arithmetic operators from this module to calculate the percentage of failed requests, given a total request count and a failed count.",
            "Use end and flush to print three fake response tokens on the same line, then a final newline, the way a model's reply might stream in.",
        ]
    ),
]

# ---------------------------------------------------------------- Module 2

M2 = [
    header(
        2,
        "Variables, Data Types, and Type Casting",
        [
            "Name a variable so that Python accepts it and a human understands it",
            "Recognise the six core types: int, float, complex, str, bool and None",
            "Check a type with type() and test one with isinstance()",
            "Convert between types, and avoid the classic input() bug",
        ],
        "Part 1 of the course: Foundations.",
    ),
    md(
        """
## What a variable is

A variable is a name that points to a value stored in memory. You do not have
to declare a type in Python. The type is decided automatically from the value
you assign.

### Naming rules

- Must start with a letter or an underscore
- Can contain letters, numbers and underscores after that
- Is case sensitive, so `name` and `Name` are two different variables
- Cannot be a reserved keyword such as `if`, `while` or `import`
"""
    ),
    code(
        """
# Valid names
my_variable = 10
_myVar = "Python"
age_2024 = 30

print(my_variable, _myVar, age_2024)

# Invalid names, left commented out on purpose:
# 2name = "John"        cannot start with a number
# my-variable = 50      hyphens are not allowed
# if = 25               "if" is a reserved keyword
"""
    ),
    md(
        """
A constant is just a variable written in all uppercase by convention, as a
signal to other readers that it should not change. Python does not enforce it.
"""
    ),
    code(
        """
PI = 3.14159
MAX_USERS = 100

print(PI, MAX_USERS)
"""
    ),
    md(
        """
## The core data types

- `int` for whole numbers such as `10` or `-5`
- `float` for decimal numbers such as `3.14`
- `complex` for numbers with a real and an imaginary part, such as `3 + 4j`
- `str` for text such as `"Hello"`
- `bool` for `True` or `False`
- `NoneType` for the absence of a value, written as `None`
"""
    ),
    code(
        """
replica_count = 3          # int
uptime_pct = 99.98         # float
model_id = "gpt-4o"        # str
is_healthy = True          # bool
error_log = None           # NoneType

print(type(replica_count))
print(type(uptime_pct))
print(type(model_id))
print(type(is_healthy))
print(type(error_log))
"""
    ),
    code(
        """
c = 3 + 4j

print(c)
print(type(c))
print("real part:", c.real, "| imaginary part:", c.imag)
"""
    ),
    md(
        """
## Checking a type

Use `type()` to see a value's type, and `isinstance()` to test it against one
or more expected types. `isinstance()` is the one you reach for inside an `if`.
"""
    ),
    code(
        """
status_code = 200
latency_ms = 45.5
error_msg = "Gateway Timeout"

print(isinstance(status_code, int))
print(isinstance(latency_ms, float))
print(isinstance(error_msg, str))
print(isinstance(3.14, (int, float)))
"""
    ),
    turn(
        1,
        "Check whether an alert severity is a whole number before comparing it "
        "to a threshold. Fill in the function name and the type being tested.",
    ),
    todo(
        """
severity = 2

# TODO: use the safe type test, checking for a whole number type.
if ____(severity, ____):
    print("severity is numeric, comparing to threshold")
    print("page on call:", severity <= 2)
else:
    print("severity is not a number, cannot compare")
""",
        """
severity = 2

if isinstance(severity, int):
    print("severity is numeric, comparing to threshold")
    print("page on call:", severity <= 2)
else:
    print("severity is not a number, cannot compare")
""",
    ),
    md(
        """
## Type casting

Casting converts a value from one type to another using a small set of built in
functions.

- `int(x)` converts to a whole number, so `int(3.9)` becomes `3`
- `float(x)` converts to a decimal, so `float("10")` becomes `10.0`
- `str(x)` converts to text, so `str(123)` becomes `"123"`
- `bool(x)` converts to True or False, so `bool(0)` is `False`
"""
    ),
    code(
        """
cpu_limit = "4"
cpu_int = int(cpu_limit)

memory_gb = 16.5
mem_str = str(memory_gb) + "GB"

is_prod = 1
active_status = bool(is_prod)

print(cpu_int, type(cpu_int))
print(mem_str, type(mem_str))
print("Is Production:", active_status)
print("int(3.9) ->", int(3.9), "  (it truncates, it does not round)")
"""
    ),
    md(
        """
### Why this matters with input()

`input()` always returns a string. Adding two strings does not add numbers, it
glues the text together. This is one of the most common early bugs, and it is
silent: nothing crashes, the answer is just wrong.
"""
    ),
    code(
        """
# Simulating two typed values, as if the person entered 50 and 30.
latency1 = "50"
latency2 = "30"

print("Wrong  ->", latency1 + latency2)              # 5030, glued together
print("Right  ->", int(latency1) + int(latency2))    # 80, actually added
"""
    ),
    turn(
        2,
        "A cloud bill arrives as a string. Convert it to a decimal number and "
        "print what a 10 percent increase would cost.",
    ),
    todo(
        """
bill = "248.50"

# TODO: cast the text to a decimal number, then apply the increase.
bill_value = ____(bill)
increased = bill_value ____ 1.10

print(f"Current: {bill_value:.2f}")
print(f"After 10 percent: {increased:.2f}")
""",
        """
bill = "248.50"

bill_value = float(bill)
increased = bill_value * 1.10

print(f"Current: {bill_value:.2f}")
print(f"After 10 percent: {increased:.2f}")
""",
    ),
    lab(
        "Describe a server safely",
        """
Store a server's CPU count as an `int`, its memory in GB as a `float`, its
hostname as a `str` and whether it is in production as a `bool`.

Print a one line summary using all four. Then take the string `"0.9"`,
representing a model temperature setting typed by a user, cast it to a float,
and print the result along with proof of its type.

Before you print the temperature, use `isinstance()` to confirm the cast
actually produced a float.
""",
        [
            "Four variables, each a different type",
            "One summary line that includes all four values",
            "The string \"0.9\" is cast to a float, not left as text",
            "isinstance() confirms the type before printing",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Store a server's CPU count as an int and its memory in GB as a float, then print a one-line summary using both.",
            "Take a cloud bill amount as a string, cast it to a float, and print what a 10 percent increase would look like.",
            "Use isinstance() to check whether an incoming alert's severity level is an int before comparing it to a threshold.",
            "Store a model's temperature setting as a float, then cast a string like \"0.9\" into a float to update it safely.",
        ]
    ),
]

# ---------------------------------------------------------------- Module 3

M3 = [
    header(
        3,
        "Strings",
        [
            "Create strings with single, double and triple quotes",
            "Pull pieces out of a string with indexing and slicing",
            "Clean and reshape text with the common string methods",
            "Build strings from variables with f-strings",
        ],
        "Part 2 of the course: Text and Logic.",
    ),
    md(
        """
## What a string is

A string is a sequence of characters wrapped in single quotes, double quotes or
triple quotes. Strings are **immutable**, meaning once created they cannot be
changed in place. They are also indexed and iterable, so you can grab
individual characters or loop through them.
"""
    ),
    code(
        """
str1 = 'Hello'
str2 = "World"
str3 = '''Multiline
string using triple quotes.'''

print(str1, str2)
print(str3)
"""
    ),
    md(
        """
A system prompt for an AI assistant is really just a multi-line string. This is
exactly the pattern behind a `SYSTEM_PROMPT` variable.
"""
    ),
    code(
        """
SYSTEM_PROMPT = '''You are a senior AI consultant.
Give exactly 5 ideas. No intro. No explanation.'''

print(SYSTEM_PROMPT)

# Joining string literals with parentheses, handy for long structured prompts.
SYSTEM_CONTRACT = (
    "You are a senior SRE assistant.\\n"
    "LINE1: <one short diagnostic step>\\n"
    "LINE2: <one short follow-up check>\\n"
)

print(SYSTEM_CONTRACT)
"""
    ),
    md(
        """
## Indexing and slicing

Each character has a position, starting at `0` from the left or `-1` from the
right. A slice `[start:stop]` includes `start` and excludes `stop`.
"""
    ),
    code(
        """
instance_id = "i-0a1b2c3d4e5f"

print(instance_id[0])       # i, the prefix
print(instance_id[-4:])     # last four characters

log_entry = "2024-08-19 [ERROR] Database Connection Failed"

print(log_entry[:10])       # the date
print(log_entry[11:18])     # the severity
print(log_entry[19:])       # the message

word = "Programming"
print(word[::2])            # every second character
print(word[::-1])           # reversed
"""
    ),
    md(
        """
## Common string methods

These are the ones you will reach for constantly:

`upper()`, `lower()`, `title()`, `capitalize()` change case &middot;
`strip()`, `lstrip()`, `rstrip()` remove whitespace &middot;
`find()`, `count()` search inside a string &middot;
`replace(old, new)` substitutes text &middot;
`split(sep)` breaks a string into a list &middot;
`join(iterable)` glues a list back into a string &middot;
`startswith()`, `endswith()` check the edges
"""
    ),
    code(
        """
trace_id = "  req_001_auth_service  "
clean_id = trace_id.strip().upper()
print(repr(clean_id))

service_log = "INFO: User login success"
print(service_log.replace("INFO", "DEBUG"))

tags = "env:prod,service:orders,region:us-east-1"
tag_list = tags.split(",")
print(tag_list)
print(";".join(tag_list))
"""
    ),
    turn(
        1,
        "Take a messy log line, strip the whitespace, split it on the pipe "
        "character, and print the number of fields you got back.",
    ),
    todo(
        """
raw = "  api-gateway | 200 | 45ms  "

# TODO: remove the surrounding whitespace, then split on the pipe.
fields = raw.____().____("|")

print(fields)
print("field count:", len(fields))
""",
        """
raw = "  api-gateway | 200 | 45ms  "

fields = raw.strip().split("|")

print(fields)
print("field count:", len(fields))
""",
    ),
    md(
        """
## String formatting with f-strings

f-strings are the modern way to build strings with variables inside them. Put
an `f` before the opening quote and wrap any variable in curly braces. You can
add a format spec after a colon, such as `:.1f` for one decimal place.
"""
    ),
    code(
        """
service = "api-gateway"
latency = 22.4

print(f"Metrics: service={service} avg_latency={latency}ms")

temperature = 0.7
waited = 2.3

print(f"--- temperature={temperature} ---")
print(f"Waited {waited:.1f}s in silence.")
"""
    ),
    md(
        """
## Escape sequences and raw strings

A backslash sequence inserts a character that is hard to type directly, such as
a newline `\\n` or a tab `\\t`. A raw string, written with an `r` before the
quote, tells Python to ignore those sequences entirely, which is what you want
for Windows file paths.
"""
    ),
    code(
        """
print("Hello\\nWorld")
print("Name:\\tAlice")
print(r"C:\\newfolder\\test")
"""
    ),
    turn(
        2,
        "Build a status line with an f-string. Show the uptime to two decimal "
        "places and put the service name in upper case.",
    ),
    todo(
        """
service = "auth-service"
uptime = 99.9812

# TODO: mark this as an f-string, upper case the name, and round to 2 places.
line = ____"{service.____()} uptime={uptime:____}%"

print(line)
""",
        """
service = "auth-service"
uptime = 99.9812

line = f"{service.upper()} uptime={uptime:.2f}%"

print(line)
""",
    ),
    lab(
        "Parse a log line",
        """
You are given this log line:

```
2024-08-19 [ERROR] payment-service | Database Connection Failed | retry=3
```

Pull it apart and print each piece on its own labelled line: the date, the
severity without its square brackets, the service name, the message, and the
retry count as an **integer** rather than as text.

Use slicing for the date, `split()` for the fields, and `strip()` to clean up
the spaces that splitting leaves behind. Finish with an f-string that
reassembles a one line summary.
""",
        [
            "The date is extracted by slicing",
            "The severity prints without its brackets",
            "The retry count is an int, proven with type() or isinstance()",
            "A final f-string summarises the whole line",
        ],
    ),
    code(
        """
line = "2024-08-19 [ERROR] payment-service | Database Connection Failed | retry=3"

# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Use a triple-quoted string to write a short multi-line deployment changelog entry.",
            "Use string slicing to pull the region code out of an instance id like \"i-0123456789-us-east-1\".",
            "Use split() and join() to reformat a log line so the timestamp and message are separated by a single dash.",
            "Build a SYSTEM_PROMPT string with an f-string that inserts a variable holding the assistant's persona name.",
        ]
    ),
]

# ---------------------------------------------------------------- Module 4

M4 = [
    header(
        4,
        "Operators and Expressions",
        [
            "Use the arithmetic operators, including // and %",
            "Compare values and combine conditions with and, or and not",
            "Update a variable in place with += and friends",
            "Tell the difference between is and ==, and test membership with in",
        ],
        "Part 2 of the course: Text and Logic.",
    ),
    md(
        """
An **operator** performs an operation on values. An **expression** is any
combination of values, variables and operators that produces a result.

## Arithmetic operators
"""
    ),
    code(
        """
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
"""
    ),
    md(
        """
## Comparison operators

These always return `True` or `False`. The main ones are `==` (equal to),
`!=` (not equal to), `>`, `<`, `>=` and `<=`.
"""
    ),
    code(
        """
x = 10
y = 5

print(x > y)
print(x < y)
print(x == 10)
print(y != 5)
"""
    ),
    md(
        """
## Logical operators

`and`, `or` and `not` combine or invert conditions.
"""
    ),
    code(
        """
a = True
b = False

print(a and b)
print(a or b)
print(not a)

# A realistic combination: page someone only if it is severe AND in hours.
severity = 1
business_hours = False

print("page on call:", severity == 1 and business_hours)
print("send email:", severity == 1 or not business_hours)
"""
    ),
    turn(
        1,
        "Decide whether a build number should go to the canary group. Even "
        "build numbers go to canary. Use the remainder operator.",
    ),
    todo(
        """
build_number = 4118

# TODO: use the remainder operator to test for an even number.
is_even = build_number ____ 2 ____ 0

print("build:", build_number)
print("route to canary:", is_even)
""",
        """
build_number = 4118

is_even = build_number % 2 == 0

print("build:", build_number)
print("route to canary:", is_even)
""",
    ),
    md(
        """
## Assignment operators

These update a variable in place. `x += 5` is shorthand for `x = x + 5`.
"""
    ),
    code(
        """
x = 10
x += 5
print(x)

x *= 2
print(x)

x -= 10
x //= 2
print(x)
"""
    ),
    md(
        """
## Identity and membership operators

`is` checks whether two names point to the **exact same object in memory**,
which is a stricter test than `==`. Two lists can hold equal values while being
two separate objects.

`in` and `not in` check whether a value exists inside a collection. Module 6
covers lists fully; for now read `[1, 2, 3]` as an ordered group of values.
"""
    ),
    code(
        """
primary_db = ["10.0.1.5", "10.0.1.6"]
alias_db = primary_db                       # same object, new name
replica_db = ["10.0.1.5", "10.0.1.6"]       # different object, same values

print("primary is alias  :", primary_db is alias_db)
print("primary is replica:", primary_db is replica_db)
print("primary == replica:", primary_db == replica_db)
"""
    ),
    code(
        """
allowed_ips = ["192.168.1.1", "10.0.0.5"]
incoming_ip = "10.0.0.5"

print(incoming_ip in allowed_ips)
print("1.1.1.1" not in allowed_ips)
"""
    ),
    turn(
        2,
        "Check a user prompt against a list of banned terms, and separately "
        "confirm two config objects are equal in value but not the same object.",
    ),
    todo(
        """
banned = ["password", "api key", "ssn"]
prompt = "what is my api key"

# TODO: first blank tests membership, second tests identity, third tests value.
contains_banned = "api key" ____ banned

config_a = {"model": "gpt-4o"}
config_b = {"model": "gpt-4o"}

print("blocked:", contains_banned)
print("same object:", config_a ____ config_b)
print("same value :", config_a ____ config_b)
""",
        """
banned = ["password", "api key", "ssn"]
prompt = "what is my api key"

contains_banned = "api key" in banned

config_a = {"model": "gpt-4o"}
config_b = {"model": "gpt-4o"}

print("blocked:", contains_banned)
print("same object:", config_a is config_b)
print("same value :", config_a == config_b)
""",
    ),
    lab(
        "A budget and paging check",
        """
You are given a monthly cloud budget of 500 dollars and a running spend of
612.40 dollars, plus an incident with severity 2 that arrived outside business
hours.

Work out and print four things:

1. Whether the spend has gone over budget
2. By what percentage it is over, to one decimal place
3. Whether the incident should page someone, where paging requires severity 1
   **or** any severity during business hours
4. Whether the region `"eu-west-1"` appears in the list of regions you are
   responsible for
""",
        [
            "A comparison operator decides the over-budget question",
            "The percentage uses arithmetic and prints to one decimal place",
            "The paging decision combines conditions with and / or / not",
            "The region check uses the in operator",
        ],
    ),
    code(
        """
budget = 500.0
spend = 612.40
severity = 2
business_hours = False
my_regions = ["us-east-1", "us-west-2", "eu-west-1"]

# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Use the modulus operator to decide whether a build number is even or odd, to route it to a canary group.",
            "Use a comparison operator to check whether a monthly cloud bill has gone over a set budget threshold.",
            "Use and/or to decide whether an alert should page someone, based on high severity and it being business hours.",
            "Use the in operator to check whether a keyword appears in a list of banned prompt terms.",
        ]
    ),
]
