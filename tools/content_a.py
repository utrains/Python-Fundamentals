"""Modules 1 to 4, following the slide decks section by section."""

from nbcore import header, md, only_nb, slide, code, todo, turn, lab, practice, heads_up

# ---------------------------------------------------------------- Module 1

M1 = [
    header(
        1,
        "Getting Started with Python",
        "Install Python, meet print() and input(), run your first script, and do a little arithmetic.",
        [
            "Say what high level and interpreted mean",
            "Show output on screen with print()",
            "Keep several print() calls on one line with end and flush",
            "Read what someone types with input()",
            "Use Python as a calculator with the arithmetic operators",
        ],
        "It follows the Module 1 slide deck, slide by slide, so you can keep the "
        "deck and this notebook side by side.",
        "Nothing. This is the first module. Everything here uses only `print()`, "
        "simple values and the arithmetic operators. There are no imports, no "
        "`if` statements and no loops, because none of those have been taught yet.",
    ),
    slide(
        2,
        "What Is Python?",
        """
Python is a high level, interpreted language created by Guido van Rossum in
1991.

**High level** means you write code close to plain English, rather than close
to the machine. **Interpreted** means Python reads and runs your code line by
line, so there is no separate compile step.
""",
    ),
    code(
        """
# Python runs top to bottom, line by line
print("Step 1")
print("Step 2")
print("Step 3")

# no compiling, no build step, just run the file
"""
    ),
    slide(
        3,
        "Why People Choose Python",
        """
**A. Simple, readable syntax.** Code reads close to plain English.

**B. Cross platform.** The same code runs on Windows, macOS and Linux.

**C. Huge library ecosystem.** The standard library plus third party packages
for almost anything.

**D. Fits many domains.** Web apps (Django, Flask), data and AI (Pandas, NumPy,
TensorFlow), automation scripts.
""",
    ),
    slide(
        4,
        "Installing Python",
        """
These are terminal commands, not Python, so they are shown here rather than run
in a cell.

**Windows.** Download from python.org and tick the box that adds Python to PATH
during install. Then confirm:

```bash
python --version
```

**Linux / macOS.** Python 3 is usually already there:

```bash
python3 --version
```

If it is missing:

```bash
sudo apt install python3      # Ubuntu / Debian
brew install python           # macOS with Homebrew
```

If this notebook is running at all, Python is already installed and working.
""",
    ),
    slide(
        5,
        "Installing with uv",
        """
`uv` is a modern, much faster alternative to the classic pip and venv
combination. Many teams now reach for it first.

You do not need `uv` yet. Just get it installed now so it is ready later in the
course.

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

uv --version
```
""",
    ),
    slide(
        6,
        "The print() Function",
        """
`print()` is how a Python program shows something on the screen. You call it
with the value you want displayed inside the parentheses.

`print()` can also take several items separated by commas, and Python inserts a
space between them automatically.
""",
    ),
    code(
        """
print("Welcome to Python!")
print("My name is John.")
print("The sum of 5 and 3 is:", 5 + 3)
"""
    ),
    code(
        """
print("Initializing deployment pipeline...")
print("Service: payment-gateway | Version: 2.1.0")
"""
    ),
    slide(
        7,
        "Printing Without a New Line",
        """
By default `print()` adds a new line after every call. When you want several
calls to stay on the same line, for example to show tokens streaming in from an
AI model one after another, pass `end` and `flush`.

`end=""` replaces the default newline with nothing. `flush=True` makes sure the
text appears immediately rather than waiting in a buffer.
""",
    ),
    code(
        """
print("Token 1 ", end="", flush=True)
print("Token 2 ", end="", flush=True)
print("Token 3")          # this one adds the final newline
"""
    ),
    turn(
        1,
        "Print a deployment banner on a single line, built from three separate "
        "`print()` calls. Only the last one may break onto a new line.",
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
    slide(
        8,
        "Your First Script",
        """
**1. Create a file.** Save this single line in a file named `hello.py`:

```python
print("Hello, World!")
```

**2. Run it.** From the terminal, in the same folder as the file:

```bash
python hello.py
# or, on Linux/macOS
python3 hello.py
```

A notebook cell and a `.py` file run the same code. The difference is only how
you start it.
""",
    ),
    code(
        """
print("Hello, World!")
print("Health Check: OK | Latency: 45ms")
"""
    ),
    slide(
        9,
        "The input() Function",
        """
`input()` pauses your program and waits for the person running it to type
something and press Enter. Whatever they type is handed back to you as a
string.

```python
name = input("Enter your name: ")
print(name)
```

**Heads up.** `input()` always hands you back a string, even if the person
typed digits. You will need to convert that string before doing maths with it.
Module 2 covers how.
""",
    ),
    heads_up(
        "A notebook cell that calls `input()` sits there waiting, which makes a "
        "notebook awkward to run top to bottom. So from here on we simulate the "
        "typed answer by assigning the value directly. Everything else is "
        "identical to what you would write in a real script."
    ),
    code(
        """
# In a script this line would be:  name = input("Enter your name: ")
name = "Serge"

print(name)
print("Hello,", name)
"""
    ),
    slide(
        10,
        "A First Look at Arithmetic",
        """
Python can act as a calculator. Module 4 covers every operator in depth. Here
is a quick look using two values, `a = 10` and `b = 5`.

| Operator | Name | Result |
|---|---|---|
| `+` | Addition | `a + b = 15` |
| `-` | Subtraction | `a - b = 5` |
| `*` | Multiplication | `a * b = 50` |
| `/` | Division | `a / b = 2.0` |
| `%` | Modulus | `a % b = 0` |
| `//` | Floor Division | `a // b = 2` |
| `**` | Exponent | `a ** b = 100000` |
""",
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
    code(
        """
total_requests = 5000
failed_requests = 12

print("Current Error Rate:", (failed_requests / total_requests) * 100, "%")
"""
    ),
    slide(
        11,
        "Putting It Together",
        """
This short program combines everything from the module: `input()` to collect
two values, the `+` operator to join them, and `print()` to show the result.

1. Ask for the first name
2. Ask for the last name
3. Join them together
4. Print a greeting
""",
    ),
    code(
        """
# In a script these two lines would be input() calls.
first_name = "Serge"
last_name = "Kamgang"

full_name = first_name + " " + last_name
print("hello,", full_name)
"""
    ),
    turn(
        2,
        "Build a deployment tag the same way, joining a region and an "
        "environment with a hyphen between them, then print it with a label.",
    ),
    todo(
        """
# TODO: join the two pieces with a hyphen, then print with a label.
region = "eu-west-1"
environment = "stage"

deploy_tag = region ____ "-" ____ environment
____("Artifact tag:", deploy_tag)
""",
        """
region = "eu-west-1"
environment = "stage"

deploy_tag = region + "-" + environment
print("Artifact tag:", deploy_tag)
""",
    ),
    lab(
        "Your first health check banner",
        """
Store a service name, a latency in milliseconds and a status in three separate
values.

Print a banner line on its own. Then print the service, latency and status
together in a single `print()` call, using commas to separate them.

Work out the error rate as a percentage from a total request count and a failed
count, and print it.

Finish by printing three fake response tokens on the same line using `end` and
`flush`, followed by a final line break.

Everything you need is `print()`, the arithmetic operators, and joining text
with `+`.
""",
        [
            "Three values hold the service name, latency and status",
            "The banner prints on its own line",
            "One print() call shows all three details, separated by commas",
            "The error rate is calculated, not typed in by hand",
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
        ],
        "You can now install Python, print and read input, and run your first script.",
    ),
]

# ---------------------------------------------------------------- Module 2

M2 = [
    header(
        2,
        "Variables, Data Types, and Type Casting",
        "Store values in variables, meet Python's core data types, and convert safely between them.",
        [
            "Explain why you never declare a type in Python",
            "Name a variable so Python accepts it and a human understands it",
            "Recognise the six core types: int, float, complex, str, bool and NoneType",
            "Check a type with type() and test one with isinstance()",
            "Convert between types, and avoid the classic input() bug",
        ],
        "It follows the Module 2 slide deck, slide by slide.",
        "Module 1 only: `print()` and the arithmetic operators. There are still "
        "no `if` statements, no loops and no f-strings here, so every result is "
        "shown with `print()` and commas.",
    ),
    slide(
        2,
        "What Is a Variable?",
        """
A variable is a name that points to a value stored in memory. You do not have
to declare a type in Python. The type is decided automatically based on the
value you assign.

Unlike some languages, you never write `int score` or `string name`. You just
assign a value, and you can assign a different kind of value to the same name
later.
""",
    ),
    code(
        """
score = 100
print(score)

score = "high score!"
print(score)

# same variable, new type, Python figures it out
"""
    ),
    slide(
        3,
        "Naming Variables",
        """
Rules for a valid variable name:

- Must start with a letter or an underscore
- Can contain letters, numbers and underscores after that
- Is case sensitive, so `name` and `Name` are different variables
- Cannot be a reserved keyword such as `if`, `while` or `import`

**Style tip.** Most Python code uses `snake_case` for variable names, like
`max_users`, rather than `camelCase` or `PascalCase`.
""",
    ),
    code(
        """
# Valid
my_variable = 10
_myVar = "Python"
age_2024 = 30

print(my_variable, _myVar, age_2024)

# Invalid, left commented out on purpose:
# 2name = "John"        -> cannot start with a number
# my-variable = 50      -> hyphens are not allowed
# if = 25               -> "if" is a reserved keyword
"""
    ),
    slide(
        4,
        "Constants",
        """
A constant is just a variable written in all uppercase, by convention. It
signals to other readers that the value should not change. Python does not
actually enforce this. It is a naming habit, not a language rule.
""",
    ),
    code(
        """
PI = 3.14159
MAX_USERS = 100

print(PI, MAX_USERS)
"""
    ),
    slide(
        5,
        "The Core Data Types",
        """
Python has six built in number and value types you will run into constantly.

| Type | Example | `type()` gives |
|---|---|---|
| `int` | `age = 25` | int |
| `float` | `price = 19.99` | float |
| `complex` | `c = 3 + 4j` | complex |
| `str` | `message = "Hi"` | str |
| `bool` | `flag = True` | bool |
| `NoneType` | `x = None` | NoneType |
""",
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
    slide(
        6,
        "Complex Numbers",
        """
A complex number has a real part and an imaginary part. Python writes the
imaginary part with a trailing `j` instead of `i`.

Electrical engineering already uses `i` for current, so Python, and the maths
in that field, uses `j` instead.

You will not need these often, but Python supports them natively with no extra
import required.
""",
    ),
    code(
        """
c = 3 + 4j

print(c)
print(type(c))
print("real part:", c.real, "| imaginary part:", c.imag)
"""
    ),
    slide(
        7,
        "Checking a Type",
        """
Use `type()` to see a value's type, and `isinstance()` to test it against one
or more expected types.

**Why `isinstance()`?** It can check against more than one type at once by
passing a tuple, which is handy when a value could reasonably be an `int` or a
`float`.
""",
    ),
    code(
        """
x = 42
y = "Python"
z = 3.14

print(type(x))
print(isinstance(42, int))
print(isinstance(3.14, (int, float)))
print(isinstance(y, str))
"""
    ),
    turn(
        1,
        "Test three values against the type you expect each one to be, and "
        "print the answers. Use the function that can also accept a tuple of "
        "types, not `type()`.",
    ),
    todo(
        """
severity = 2
uptime = "99.98"
threshold = 1.5

# TODO: name the safe type test, then fill in each expected type.
print("severity is a whole number:", ____(severity, ____))
print("uptime is text            :", isinstance(uptime, ____))
print("threshold is a number     :", isinstance(threshold, (int, ____)))
""",
        """
severity = 2
uptime = "99.98"
threshold = 1.5

print("severity is a whole number:", isinstance(severity, int))
print("uptime is text            :", isinstance(uptime, str))
print("threshold is a number     :", isinstance(threshold, (int, float)))
""",
    ),
    slide(
        8,
        "Type Casting",
        """
Type casting converts a value from one type to another using a small set of
built in functions.

- `int(x)` so `int(3.9)` becomes `3`. Note that it truncates, it does not round.
- `float(x)` so `float("10")` becomes `10.0`
- `str(x)` so `str(123)` becomes `"123"`
- `bool(x)` so `bool(0)` is `False` and `bool(1)` is `True`
""",
    ),
    code(
        """
num = 10
print(type(num))

num_str = str(num)
print(type(num_str))

pi = "3.14"
pi_float = float(pi)
print(type(pi_float))

print("int(3.9) ->", int(3.9))
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

print("CPU:", cpu_int, type(cpu_int))
print("Memory:", mem_str, type(mem_str))
print("Is Production:", active_status)
"""
    ),
    slide(
        9,
        "Why This Matters with input()",
        """
`input()` always returns a string. Adding two strings does not add numbers, it
glues the text together. This is one of the most common early bugs, and it is
silent: nothing crashes, the answer is just wrong.

**Wrong**

```python
num1 = input("Enter first: ")     # user enters 5
num2 = input("Enter second: ")    # user enters 3
print("Sum:", num1 + num2)        # Output: 53
```

**Right**

```python
num1 = int(input("Enter first: "))
num2 = int(input("Enter second: "))
print("Sum:", num1 + num2)        # Output: 8
```
""",
    ),
    code(
        """
# Simulating two typed values, as if the person entered 5 and 3.
num1 = "5"
num2 = "3"

print("Wrong ->", num1 + num2)                 # 53, glued together
print("Right ->", int(num1) + int(num2))       # 8, actually added
"""
    ),
    turn(
        2,
        "A cloud bill arrives as text. Convert it to a decimal number and print "
        "what a 10 percent increase would come to. `round(value, 2)` tidies the "
        "result to two decimal places.",
    ),
    todo(
        """
bill = "248.50"

# TODO: cast the text to a decimal number, then apply the increase.
bill_value = ____(bill)
increased = bill_value ____ 1.10

print("Current         :", bill_value)
print("After 10 percent:", round(increased, 2))
print("Type after cast :", type(bill_value))
""",
        """
bill = "248.50"

bill_value = float(bill)
increased = bill_value * 1.10

print("Current         :", bill_value)
print("After 10 percent:", round(increased, 2))
print("Type after cast :", type(bill_value))
""",
    ),
    lab(
        "Describe a server safely",
        """
Store a server's CPU count as an `int`, its memory in GB as a `float`, its
hostname as a `str` and whether it is in production as a `bool`.

Print a one line summary using all four, with commas between them.

Then take the string `"0.9"`, which stands for a model temperature typed by a
user, cast it to a float, and print the result together with its type.

Use `isinstance()` to check that the cast really produced a float, and print
that check on its own line. You do not need an `if` for this, just print the
result of the check.
""",
        [
            "Four values, each a different type",
            "One summary line that includes all four",
            "The string \"0.9\" is cast to a float, not left as text",
            "isinstance() is printed to prove the cast worked",
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
        ],
        "You can now store values in variables, name them properly, and convert between types safely.",
    ),
]

# ---------------------------------------------------------------- Module 3

M3 = [
    header(
        3,
        "Strings",
        "Create, slice, format, and clean up text, from a single word to a multi-line AI prompt.",
        [
            "Say what immutable, indexed and iterable mean for a string",
            "Build multi-line text with triple quotes and with parentheses",
            "Pull pieces out of a string with indexing and slicing",
            "Clean and reshape text with the common string methods",
            "Build strings from values with f-strings",
        ],
        "It follows the Module 3 slide deck, slide by slide.",
        "Modules 1 and 2: `print()`, values and types, and casting. The deck's "
        "second slide shows a `for` loop to demonstrate that a string is "
        "iterable; loops get their full treatment in Module 5, so it appears "
        "here once and is not used again.",
    ),
    slide(
        2,
        "What Is a String?",
        """
A string is a sequence of characters wrapped in single quotes, double quotes or
triple quotes.

- **Immutable.** Once created, a string cannot be changed in place.
- **Indexed.** Every character has a position, so you can grab one directly.
- **Iterable.** You can loop through a string one character at a time.
""",
    ),
    heads_up(
        "The `for` loop below is here only to show what *iterable* means. "
        "Module 5 teaches loops properly. Nothing else in this notebook uses one."
    ),
    code(
        """
word = "Python"

# indexed
print(word[0])

# iterable
for char in word:
    print(char)

# immutable
# word[0] = "J"     -> this raises an error
"""
    ),
    slide(
        3,
        "Creating Strings",
        """
Single quotes, double quotes or triple quotes all work. Triple quotes let a
string span several lines.

**AI framing.** A system prompt for an AI assistant is really just a multi-line
string. This is exactly the pattern behind a `SYSTEM_PROMPT` variable.
""",
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
    code(
        """
SYSTEM_PROMPT = '''You are a senior AI consultant.
Give exactly 5 ideas. No intro. No explanation.'''

print(SYSTEM_PROMPT)
"""
    ),
    slide(
        4,
        "Building Prompts with Parentheses",
        """
You can also join string literals together with parentheses. This is handy for
building a long, structured piece of text line by line, instead of one long
triple-quoted block.

**Why bother?** Each line stays short and easy to edit, which matters once a
prompt grows past a few lines.
""",
    ),
    code(
        """
SYSTEM_CONTRACT = (
    "You are a senior SRE assistant.\\n"
    "LINE1: <one short diagnostic step>\\n"
    "LINE2: <one short follow-up check>\\n"
)

print(SYSTEM_CONTRACT)
"""
    ),
    slide(
        5,
        "Indexing and Slicing",
        """
Each character in a string has a position, starting at `0` from the left, or
`-1` from the right. A slice `[start:stop]` includes `start` and excludes
`stop`.

Using `word = "Programming"`:

| Slice | Result |
|---|---|
| `word[0:5]` | `Progr` |
| `word[3:]` | `gramming` |
| `word[::2]` | `Pormig` |
| `word[::-1]` | `gnimmargorP` |
""",
    ),
    code(
        """
word = "Python"
print(word[0])
print(word[-1])

word = "Programming"
print(word[0:5])
print(word[3:])
print(word[::2])
print(word[::-1])
"""
    ),
    code(
        """
instance_id = "i-0a1b2c3d4e5f"
print(instance_id[0])          # the prefix
print(instance_id[-4:])        # the last four characters

log_entry = "2024-08-19 [ERROR] Database Connection Failed"
print(log_entry[:10])          # the date
print(log_entry[11:18])        # the severity
print(log_entry[19:])          # the message
"""
    ),
    turn(
        1,
        "Pull the region code out of an instance id using slicing only. The "
        "region is everything after the last hyphen, and it is nine characters "
        "long.",
    ),
    todo(
        """
instance_id = "i-0123456789-us-east-1"

# TODO: slice the last nine characters, then slice off the leading "i-".
region = instance_id[____:]
prefix = instance_id[:____]

print("region:", region)
print("prefix:", prefix)
""",
        """
instance_id = "i-0123456789-us-east-1"

region = instance_id[-9:]
prefix = instance_id[:2]

print("region:", region)
print("prefix:", prefix)
""",
    ),
    slide(
        6,
        "Common String Methods",
        """
These are the methods you will reach for constantly.

| Method | What it does |
|---|---|
| `upper()` / `lower()` | Change case |
| `strip()` | Remove whitespace |
| `find()` / `count()` | Search inside a string |
| `replace()` | Substitute text |
| `split()` | Break into a list |
| `join()` | Glue a list back together |
""",
    ),
    slide(
        7,
        "Methods in Action",
        """
Chaining a few of these together is a normal part of cleaning up text.

**Reading the chain.** `text.split()` breaks a sentence into a list of words.
`"-".join(words)` glues that list back together with a dash between each word.

**Order matters.** `split()` has to run before `join()` has a list to work
with. You cannot join a plain string.

`split()` hands you back a **list**. Module 6 covers lists in full; here it is
just the thing `join()` takes back.
""",
    ),
    code(
        """
text = "Python programming"
print(text.find("prog"))

text = "I love Python"
print(text.replace("love", "like"))

words = text.split()
print(words)

joined = "-".join(words)
print(joined)
"""
    ),
    code(
        """
trace_id = "  req_001_auth_service  "
clean_id = trace_id.strip().upper()
print(repr(clean_id))

tags = "env:prod,service:orders,region:us-east-1"
tag_list = tags.split(",")
print(tag_list)
print(";".join(tag_list))
"""
    ),
    slide(
        8,
        "String Formatting with f-strings",
        """
f-strings are the modern way to build strings with values inside them. Put an
`f` before the opening quote, and wrap any value in curly braces.

A format spec like `:.1f` inside the braces controls how a number is displayed,
here to one decimal place.
""",
    ),
    code(
        """
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

temperature = 0.7
waited = 2.3
print(f"--- temp={temperature} ---")
print(f"Waited {waited:.1f}s in silence.")
"""
    ),
    turn(
        2,
        "Build a status line with an f-string. Put the service name in upper "
        "case and show the uptime to two decimal places.",
    ),
    todo(
        """
service = "auth-service"
uptime = 99.9812

# TODO: mark this as an f-string, upper case the name, round to 2 places.
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
    slide(
        9,
        "Escape Sequences and Raw Strings",
        """
Backslash sequences insert characters that are hard to type directly, like a
newline `\\n` or a tab `\\t`.

A raw string, written with an `r` before the quote, tells Python to ignore
those escape sequences, which is what you want for Windows file paths.

Common escapes: `\\n` newline, `\\t` tab, `\\\\` backslash, `\\"` quote.
""",
    ),
    code(
        """
print("Hello\\nWorld")
print("Name:\\tAlice")
print(r"C:\\newfolder\\test")
"""
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
retry count as a number rather than as text.

Use slicing for the date, `split()` for the fields, `strip()` to clean up the
spaces that splitting leaves behind, and `int()` from Module 2 for the retry
count.

Finish with an f-string that reassembles a one line summary.
""",
        [
            "The date is extracted by slicing",
            "The severity prints without its brackets",
            "The retry count is a number, proven with type()",
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
        ],
        "You can now create, slice, format and clean up strings, including multi-line prompts.",
    ),
]

# ---------------------------------------------------------------- Module 4

M4 = [
    header(
        4,
        "Operators and Expressions",
        "Do math, compare values, combine conditions, and check what's inside a collection.",
        [
            "Say what an operator and an expression are",
            "Use the arithmetic operators, including `//` and `%`",
            "Compare values and combine conditions with and, or and not",
            "Update a value in place with `+=` and friends",
            "Tell `is` from `==`, and test membership with `in`",
        ],
        "It follows the Module 4 slide deck, slide by slide.",
        "Modules 1 to 3. There are still no `if` statements or loops here: every "
        "comparison result is simply printed. The identity slide uses a list, "
        "exactly as the deck does, and flags it as a Module 6 topic.",
    ),
    slide(
        2,
        "What Is an Operator?",
        """
An **operator** performs an operation on values. An **expression** is any
combination of values, variables and operators that produces a result.

| Group | Operators |
|---|---|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` |
| Logical | `and or not` |
| Identity and membership | `is`, `is not`, `in`, `not in` |
""",
    ),
    code(
        """
# an expression combines values and operators into a result
a = 10
b = 3

result = a + b * 2
print(result)

# operators follow the usual order of operations
print((a + b) * 2)
"""
    ),
    slide(
        3,
        "Arithmetic Operators",
        """
Python's maths operators work the way you would expect, using `a = 10` and
`b = 3`.

| Operator | Name | Result |
|---|---|---|
| `+` | Addition | 13 |
| `-` | Subtraction | 7 |
| `*` | Multiplication | 30 |
| `/` | Division | 3.33... |
| `//` | Floor Division | 3 |
| `%` | Modulus | 1 |
| `**` | Exponentiation | 1000 |
""",
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
    slide(
        4,
        "Comparison Operators",
        """
These always return `True` or `False`.

`==` equal to &middot; `!=` not equal to &middot; `>` `<` greater or less than
&middot; `>=` `<=` greater or less than or equal
""",
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
    turn(
        1,
        "Decide whether a build number goes to the canary group. Even build "
        "numbers go to canary. Use the remainder operator and a comparison, and "
        "print the answer.",
    ),
    todo(
        """
build_number = 4118

# TODO: use the remainder operator, then compare the remainder to zero.
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
    slide(
        5,
        "Logical Operators",
        """
`and`, `or` and `not` combine or invert conditions. With `a = True` and
`b = False`:

- `a and b` is `False`, because both must be true
- `a or b` is `True`, because at least one is true
- `not a` is `False`, because it flips the value
""",
    ),
    code(
        """
a = True
b = False

print(a and b)
print(a or b)
print(not a)
"""
    ),
    code(
        """
# A realistic combination: page someone only if it is severe AND in hours.
severity = 1
business_hours = False

print("page on call:", severity == 1 and business_hours)
print("send email  :", severity == 1 or not business_hours)
"""
    ),
    slide(
        6,
        "Assignment Operators",
        """
These update a variable in place, a shorthand for reassigning it based on its
current value.

`+=` is `x = x + 5` &middot; `-=` is `x = x - 5` &middot; `*=` is `x = x * 5`
&middot; `/=` is `x = x / 5`
""",
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
    slide(
        7,
        "Identity: is vs ==",
        """
`is` checks whether two variables point to the **exact same object in memory**,
a stricter test than `==`, which only checks whether the values match.

**Heads up.** The square brackets below create a **list**, which Module 6
covers in full. For now just read `[1, 2, 3]` as an ordered group of values.
""",
    ),
    code(
        """
a = [1, 2, 3]
b = a                # same object, new name
c = [1, 2, 3]        # different object, same values

print("a is b:", a is b)
print("a is c:", a is c)
print("a == c:", a == c)
"""
    ),
    slide(
        8,
        "Membership: in and not in",
        """
`in` and `not in` check whether a value exists inside a collection, such as a
string, list or dictionary. A string is the simplest case: `in` looks for a
smaller piece of text inside a bigger one.
""",
    ),
    code(
        """
word = "apple"

print("a" in word)
print("z" in word)
print("app" not in word)
"""
    ),
    turn(
        2,
        "Screen a user prompt for a banned term with `in`, and confirm that two "
        "separately built lists hold equal values without being the same object.",
    ),
    todo(
        """
prompt = "what is my api key"

# TODO: which operator tests whether one piece of text is inside another?
blocked = "api key" ____ prompt

primary = ["10.0.1.5", "10.0.1.6"]
alias = primary
replica = ["10.0.1.5", "10.0.1.6"]

print("blocked           :", blocked)

# TODO: first blank tests the same object, second tests equal values.
print("alias is primary  :", alias ____ primary)
print("replica == primary:", replica ____ primary)
""",
        """
prompt = "what is my api key"

blocked = "api key" in prompt

primary = ["10.0.1.5", "10.0.1.6"]
alias = primary
replica = ["10.0.1.5", "10.0.1.6"]

print("blocked           :", blocked)

print("alias is primary  :", alias is primary)
print("replica == primary:", replica == primary)
""",
    ),
    lab(
        "A budget and paging check",
        """
You have a monthly cloud budget of 500 dollars and a running spend of 612.40
dollars. An incident arrived with severity 2, outside business hours.

Work out and print four things, one per line:

1. Whether the spend has gone over budget
2. By what percentage it is over, shown to one decimal place with an f-string
3. Whether the incident should page someone, where paging needs severity 1
   **or** any severity during business hours
4. Whether the text `"eu-west"` appears inside the region name you are on call
   for

You do not need an `if` for any of this. Each answer is an expression you can
print directly.
""",
        [
            "A comparison operator answers the over-budget question",
            "The percentage uses arithmetic and an f-string to one decimal place",
            "The paging decision combines conditions with and / or / not",
            "The region check uses the in operator on a string",
        ],
    ),
    code(
        """
budget = 500.0
spend = 612.40
severity = 2
business_hours = False
on_call_region = "eu-west-1"

# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Use the modulus operator to decide whether a build number is even or odd, to route it to a canary group.",
            "Use a comparison operator to check whether a monthly cloud bill has gone over a set budget threshold.",
            "Use and/or to decide whether an alert should page someone, based on high severity and it being business hours.",
            "Use the in operator to check whether a keyword appears in a list of banned prompt terms.",
        ],
        "You can now do maths, compare values, combine conditions and check membership.",
    ),
]
