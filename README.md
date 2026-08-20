# Python Fundamentals Lab

Hands-on Jupyter notebooks for the **Utrains Python Fundamentals** course.
Eleven modules, one notebook each, every cell runnable.

**The full slide content is in this README**, module by module, in deck order.
That is where you read. The notebooks are where you run things, so they carry
the slide headings as signposts and then get straight to the code, without
repeating the explanation you just read.

Three places, each holding one thing:

| Where | What it is |
|---|---|
| this README | every slide, in full, in deck order, with its code |
| `notebooks/` | the working copy: slide headings, code cells, exercises, labs |
| `solutions/` | the 22 exercise answers and a worked answer for each lab |

Each notebook has runnable code for every slide that has any, a **More use
cases** section with three or four further worked scenarios, **two "Your turn"
cells** with deliberate `____` blanks that fail until you complete them, and a
**lab** at the end with no starter code.

Most of the use cases are the AI work this course leads into: tokens and what
they cost, context windows, streaming replies, rate limits, model responses
that are the wrong shape, chat history, and run logs. They carry an **AI** tag
in the heading. The rest are the infrastructure jobs the same syntax turns up
in.

---

## Setup

Five steps. Do them once, then everything after that is Shift + Enter.

### 1. Install uv

`uv` is the fast replacement for pip and venv that Module 1 asks you to
install. If you already have it, skip to step 2.

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen your terminal, then confirm it is on your PATH:

```bash
uv --version
```

### 2. Create the virtual environment

A virtual environment is a folder holding this project's packages, separate
from everything else on your machine. Module 10 explains why in full.

```bash
cd python-fundamental-lab

uv venv
```

That creates a `.venv` folder inside the project.

### 3. Activate it

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

# Git Bash on Windows
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Your prompt should now start with `(.venv)`. That is how you know packages will
land in the project rather than on your whole system.

### 4. Install everything from requirements.txt

```bash
uv pip install -r requirements.txt
```

One file, everything the course needs: JupyterLab, `ipykernel`, `pydantic`, and
the Module 10 AI packages (`openai`, `langchain`, `langgraph`, `python-dotenv`).

Check it worked:

```bash
uv pip list
```

### 5. Register the environment as a Jupyter kernel

This is the step people skip, and it is the reason a notebook reports
`ModuleNotFoundError: No module named 'pydantic'` when the package is clearly
installed. Jupyter has to be told this environment exists.

```bash
python -m ipykernel install --user --name pyfund --display-name "Python (pyfund)"
```

Then start JupyterLab:

```bash
jupyter lab
```

Open `notebooks/01_getting_started.ipynb` and **pick the kernel**:

- **In JupyterLab**, click the kernel name in the top right of the notebook (it
  will say something like `Python 3 (ipykernel)`) and choose
  **Python (pyfund)**. Or use the menu: *Kernel → Change Kernel… → Python
  (pyfund)*.
- **In VS Code**, click **Select Kernel** in the top right, choose **Python
  Environments…**, then pick the `.venv` inside this project.

You only do this once per notebook. Jupyter remembers it afterwards.

### Checking the kernel is right

Run this in any notebook cell. The path it prints must contain `.venv`:

```python
import sys
print(sys.executable)
```

If it does not, you are on the wrong kernel. Go back to *Kernel → Change
Kernel…* and pick **Python (pyfund)**.

### If you would rather not use uv

Plain Python does the same job, just slower:

```bash
python -m venv .venv
source .venv/bin/activate          # or the Windows line from step 3
pip install -r requirements.txt
python -m ipykernel install --user --name pyfund --display-name "Python (pyfund)"
jupyter lab
```

### Adding your API key

Module 10 covers secrets. When you are ready to call a real API, create a
`.env` file in the project root:

```
OPENAI_API_KEY=sk-...
```

`.env` is already in `.gitignore`, so it will never be committed. Nothing in
the course requires a key: every notebook runs to completion without one.

---

## Working the exercises

A "Your turn" cell looks like this:

```python
# TODO: fill in the blanks so all three pieces land on ONE line.
print("Deploying ", end=____, flush=True)
```

Run it as it is first. It will fail, either with a `SyntaxError` or a
`NameError` on the name `____`. Read the error, fix the blank, run it again.
Getting used to reading the error message is half of what these cells teach.

If you get stuck, [`solutions/`](solutions/) has one markdown file per module
with the answer to both exercises and a worked answer for the lab. Try it
yourself first; the answer is much less useful than the attempt.

A lab is open ended, so the answer there is one way to do it rather than the
only way. Every answer is executed by the build, so what you are comparing
against is known to work.

**Every exercise stays inside its own module.** A Module 2 exercise will never
need an `if`, because `if` is not taught until Module 5. The build enforces
this, so you will never be asked for something you have not been shown.

---

## Repository layout

```
README.md             this file, including all the slide content
requirements.txt      every package the course needs
notebooks/            the student notebooks, blanks left in
solutions/            one markdown answer sheet per module
data/servers.txt      sample input for the Module 9 lab
tools/                the build and verification scripts
```

A `scratch/` folder appears inside `notebooks/` when you run Module 9, and a
`.build/` folder appears when you run the build. Both are gitignored.

| # | Notebook | Covers |
|---|---|---|
| 1 | `01_getting_started.ipynb` | print(), end and flush, input(), arithmetic |
| 2 | `02_variables_and_types.ipynb` | naming, the six core types, type(), casting |
| 3 | `03_strings.ipynb` | quotes, slicing, string methods, f-strings |
| 4 | `04_operators.ipynb` | arithmetic, comparison, logical, is vs ==, in |
| 5 | `05_control_flow.ipynb` | if/elif/else, for, while, break/continue/pass |
| 6 | `06_collections.ipynb` | lists, tuples, dictionaries, sets, comprehensions |
| 7 | `07_handling_errors.ipynb` | try/except/else/finally, retries, raise |
| 8 | `08_functions.ipynb` | parameters, defaults, *args/**kwargs, yield, callbacks |
| 9 | `09_file_handling.ipynb` | modes, with, JSON, pathlib |
| 10 | `10_important_modules.ipynb` | import, time, os, secrets, venv, AI packages |
| 11 | `11_advanced_python.ipynb` | classes, dataclasses, Pydantic, decorators, async |

---

## Things worth knowing before you teach it

**`input()` is explained but never called in a cell.** A notebook cell that
calls `input()` sits and waits, which breaks a run-all. Where the course would
read from the keyboard, the notebook assigns the value directly and says so in
a comment. The `input()` version is always shown alongside.

**Module 11 uses `await` at top level, not `asyncio.run()`.** A notebook
already has an event loop running, so `asyncio.run()` raises an error inside
one. The notebook explains the difference, which is a good thing for students
to hit early rather than in their own code.

**Three forward references are deliberate**, because the decks make them and
flag them on the slide: Module 3 uses a `for` loop once to show a string is
iterable, Module 4 uses a list to demonstrate `is` against `==`, and Modules 7
and 9 use `import` before Module 10 formally teaches it. Each carries a "Heads
up" note.

**Module 5 has no lists**, because the deck defers them to Module 6. Its first
practice exercise needs one, so the notebook tells students to come back after
Module 6, and Module 6 reminds them.

---

## For instructors

`tools/build.py` regenerates the notebooks, the answer sheets **and this
README** from a single source. A slide correction is made once, in one file,
and lands in all three. Nothing is written twice, so nothing can disagree.

```bash
python tools/build.py             # regenerate notebooks, answers and README
python tools/build.py --run       # also execute every solved notebook
python tools/check_exercises.py   # confirm the blanks are still incomplete
python tools/check_scope.py       # confirm nothing is used before its module
```

Fully solved notebooks are build artifacts, not committed. `build.py` writes
them into `.build/solutions/`, which is what `--run` executes. If you want one
to hand to a student, build it and send that file.

The three checks are what keep the material honest:

- `--run` executes all eleven solution notebooks and fails if any example no
  longer works.
- `check_exercises.py` confirms all 22 exercise cells still contain blanks and
  still fail when run as written. An exercise that quietly succeeds teaches
  nothing.
- `check_scope.py` walks the syntax tree of every code cell and fails the build
  if a notebook uses a language feature before the module that introduces it.
  The deliberate exceptions are listed at the top of that file with a reason
  for each.

To change a lesson, edit the matching module list in `tools/content_a.py`
(modules 1 to 4), `content_b.py` (5 to 8) or `content_c.py` (9 to 11), then
rebuild. The intro you are reading lives in `tools/readme_intro.md`.

---

# Course content

Everything below is generated from the same source as the notebooks, so it
cannot drift out of step with them. Slide numbers match the decks.

The **Your turn** exercises and the **Labs** are deliberately left out of this
README. They live in the notebooks, where you can actually run them.

---

### Module 1: Getting Started with Python

*Install Python, meet print() and input(), run your first script, and do a little arithmetic.*

Notebook: [`notebooks/01_getting_started.ipynb`](notebooks/01_getting_started.ipynb) &middot; answers: [`solutions/01_getting_started.md`](solutions/01_getting_started.md)

#### Slide 2 &middot; What Is Python?

Python is a high level, interpreted language created by Guido van Rossum in
1991.

**High level** means you write code close to plain English, rather than close
to the machine. **Interpreted** means Python reads and runs your code line by
line, so there is no separate compile step.

```python
# Python runs top to bottom, line by line
print("Step 1")
print("Step 2")
print("Step 3")

# no compiling, no build step, just run the file
```

#### Slide 3 &middot; Why People Choose Python

**A. Simple, readable syntax.** Code reads close to plain English.

**B. Cross platform.** The same code runs on Windows, macOS and Linux.

**C. Huge library ecosystem.** The standard library plus third party packages
for almost anything.

**D. Fits many domains.** Web apps (Django, Flask), data and AI (Pandas, NumPy,
TensorFlow), automation scripts.

#### Slide 4 &middot; Installing Python

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

#### Slide 5 &middot; Installing with uv

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

#### Slide 6 &middot; The print() Function

`print()` is how a Python program shows something on the screen. You call it
with the value you want displayed inside the parentheses.

`print()` can also take several items separated by commas, and Python inserts a
space between them automatically.

```python
print("Welcome to Python!")
print("My name is John.")
print("The sum of 5 and 3 is:", 5 + 3)
```

```python
print("Initializing deployment pipeline...")
print("Service: payment-gateway | Version: 2.1.0")
```

#### Slide 7 &middot; Printing Without a New Line

By default `print()` adds a new line after every call. When you want several
calls to stay on the same line, for example to show tokens streaming in from an
AI model one after another, pass `end` and `flush`.

`end=""` replaces the default newline with nothing. `flush=True` makes sure the
text appears immediately rather than waiting in a buffer.

```python
print("Token 1 ", end="", flush=True)
print("Token 2 ", end="", flush=True)
print("Token 3")          # this one adds the final newline
```

#### Slide 8 &middot; Your First Script

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

```python
print("Hello, World!")
print("Health Check: OK | Latency: 45ms")
```

#### Slide 9 &middot; The input() Function

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

```python
# In a script this line would be:  name = input("Enter your name: ")
name = "Serge"

print(name)
print("Hello,", name)
```

#### Slide 10 &middot; A First Look at Arithmetic

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

```python
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)
```

```python
total_requests = 5000
failed_requests = 12

print("Current Error Rate:", (failed_requests / total_requests) * 100, "%")
```

#### Slide 11 &middot; Putting It Together

This short program combines everything from the module: `input()` to collect
two values, the `+` operator to join them, and `print()` to show the result.

1. Ask for the first name
2. Ask for the last name
3. Join them together
4. Print a greeting

```python
# In a script these two lines would be input() calls.
first_name = "Serge"
last_name = "Kamgang"

full_name = first_name + " " + last_name
print("hello,", full_name)
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; What did that API call cost?

Model pricing is quoted per million tokens, so working out the cost of one call is two multiplications and an addition. Do this early and often: the difference between a cheap prompt and an expensive one is usually a decision you made without noticing.

One of the numbers below prints with a long tail of digits. That is how computers store decimals, not a mistake. Module 3's f-strings are what tidy it up.

```python
input_tokens = 1_450
output_tokens = 320

input_price_per_million = 3.00
output_price_per_million = 15.00

input_cost = (input_tokens / 1_000_000) * input_price_per_million
output_cost = (output_tokens / 1_000_000) * output_price_per_million

print("input tokens :", input_tokens, "costing", input_cost)
print("output tokens:", output_tokens, "costing", output_cost)
print("this call    :", input_cost + output_cost)
print("10,000 calls :", (input_cost + output_cost) * 10000)

# One of those numbers has a long tail of digits. That is not a bug: it is
# how computers store decimals. Module 3 shows how to print it to 4 places.
```

#### Use case 2 &middot; AI &middot; A reply arriving token by token

A model does not hand you a finished answer, it sends pieces. The end and flush pair from the slide is exactly what puts those pieces on one line as they arrive, instead of a screenful of fragments.

```python
print("Assistant: ", end="", flush=True)
print("The ", end="", flush=True)
print("target ", end="", flush=True)
print("group ", end="", flush=True)
print("is ", end="", flush=True)
print("unhealthy.")

print()
print("Thinking ", end="", flush=True)
print("." * 3, end="", flush=True)
print(" done")
```

#### Use case 3 &middot; A deployment banner

Multiplying a string repeats it, which is the quickest way to draw a rule across the terminal. Every deployment script prints something like this so a human scrolling the logs can find where a run began.

```python
line = "=" * 46

print(line)
print("  UTRAINS DEPLOYMENT  |  payment-gateway 2.1.0")
print(line)
print("  target   : us-east-1")
print("  triggered: automatic")
print(line)
```

#### Use case 4 &middot; What will this infrastructure cost?

The same arithmetic, pointed at servers instead of tokens. Three instances, on all month, at an hourly rate. Working it out is the easy part; remembering to do it before you launch is the habit.

```python
instances = 3
hours_per_month = 730
rate_per_hour = 0.0416

monthly = instances * hours_per_month * rate_per_hour

print("Instances    :", instances)
print("Monthly cost :", monthly)
print("Yearly cost  :", monthly * 12)
```

#### Practice exercises

1. Write a script that prints a deployment banner with your service name and version number using variables and print().
2. Use input() to ask for a cloud region name, then print a one-line confirmation message using that region.
3. Use the arithmetic operators from this module to calculate the percentage of failed requests, given a total request count and a failed count.
4. Use end and flush to print three fake response tokens on the same line, then a final newline, the way a model's reply might stream in.

#### Module complete

You can now install Python, print and read input, and run your first script.


---

### Module 2: Variables, Data Types, and Type Casting

*Store values in variables, meet Python's core data types, and convert safely between them.*

Notebook: [`notebooks/02_variables_and_types.ipynb`](notebooks/02_variables_and_types.ipynb) &middot; answers: [`solutions/02_variables_and_types.md`](solutions/02_variables_and_types.md)

#### Slide 2 &middot; What Is a Variable?

A variable is a name that points to a value stored in memory. You do not have
to declare a type in Python. The type is decided automatically based on the
value you assign.

Unlike some languages, you never write `int score` or `string name`. You just
assign a value, and you can assign a different kind of value to the same name
later.

```python
score = 100
print(score)

score = "high score!"
print(score)

# same variable, new type, Python figures it out
```

#### Slide 3 &middot; Naming Variables

Rules for a valid variable name:

- Must start with a letter or an underscore
- Can contain letters, numbers and underscores after that
- Is case sensitive, so `name` and `Name` are different variables
- Cannot be a reserved keyword such as `if`, `while` or `import`

**Style tip.** Most Python code uses `snake_case` for variable names, like
`max_users`, rather than `camelCase` or `PascalCase`.

```python
# Valid
my_variable = 10
_myVar = "Python"
age_2024 = 30

print(my_variable, _myVar, age_2024)

# Invalid, left commented out on purpose:
# 2name = "John"        -> cannot start with a number
# my-variable = 50      -> hyphens are not allowed
# if = 25               -> "if" is a reserved keyword
```

#### Slide 4 &middot; Constants

A constant is just a variable written in all uppercase, by convention. It
signals to other readers that the value should not change. Python does not
actually enforce this. It is a naming habit, not a language rule.

```python
PI = 3.14159
MAX_USERS = 100

print(PI, MAX_USERS)
```

#### Slide 5 &middot; The Core Data Types

Python has six built in number and value types you will run into constantly.

| Type | Example | `type()` gives |
|---|---|---|
| `int` | `age = 25` | int |
| `float` | `price = 19.99` | float |
| `complex` | `c = 3 + 4j` | complex |
| `str` | `message = "Hi"` | str |
| `bool` | `flag = True` | bool |
| `NoneType` | `x = None` | NoneType |

```python
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
```

#### Slide 6 &middot; Complex Numbers

A complex number has a real part and an imaginary part. Python writes the
imaginary part with a trailing `j` instead of `i`.

Electrical engineering already uses `i` for current, so Python, and the maths
in that field, uses `j` instead.

You will not need these often, but Python supports them natively with no extra
import required.

```python
c = 3 + 4j

print(c)
print(type(c))
print("real part:", c.real, "| imaginary part:", c.imag)
```

#### Slide 7 &middot; Checking a Type

Use `type()` to see a value's type, and `isinstance()` to test it against one
or more expected types.

**Why `isinstance()`?** It can check against more than one type at once by
passing a tuple, which is handy when a value could reasonably be an `int` or a
`float`.

```python
x = 42
y = "Python"
z = 3.14

print(type(x))
print(isinstance(42, int))
print(isinstance(3.14, (int, float)))
print(isinstance(y, str))
```

#### Slide 8 &middot; Type Casting

Type casting converts a value from one type to another using a small set of
built in functions.

- `int(x)` so `int(3.9)` becomes `3`. Note that it truncates, it does not round.
- `float(x)` so `float("10")` becomes `10.0`
- `str(x)` so `str(123)` becomes `"123"`
- `bool(x)` so `bool(0)` is `False` and `bool(1)` is `True`

```python
num = 10
print(type(num))

num_str = str(num)
print(type(num_str))

pi = "3.14"
pi_float = float(pi)
print(type(pi_float))

print("int(3.9) ->", int(3.9))
```

```python
cpu_limit = "4"
cpu_int = int(cpu_limit)

memory_gb = 16.5
mem_str = str(memory_gb) + "GB"

is_prod = 1
active_status = bool(is_prod)

print("CPU:", cpu_int, type(cpu_int))
print("Memory:", mem_str, type(mem_str))
print("Is Production:", active_status)
```

#### Slide 9 &middot; Why This Matters with input()

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

```python
# Simulating two typed values, as if the person entered 5 and 3.
num1 = "5"
num2 = "3"

print("Wrong ->", num1 + num2)                 # 53, glued together
print("Right ->", int(num1) + int(num2))       # 8, actually added
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; Model settings arrive as text

Every setting read from an environment variable or a config file is a string, whatever it looks like. Hand a string temperature to an SDK and you get an error at the worst moment; hand it a string max_tokens and some libraries silently do the wrong thing.

```python
temperature_text = "0.7"
max_tokens_text = "512"
stream_text = "1"

temperature = float(temperature_text)
max_tokens = int(max_tokens_text)
stream = bool(int(stream_text))

print("temperature:", temperature, type(temperature))
print("max_tokens :", max_tokens, type(max_tokens))
print("stream     :", stream, type(stream))

print()
print("as text, this would have been wrong:", max_tokens_text + max_tokens_text)
print("as numbers, it is right             :", max_tokens + max_tokens)
```

#### Use case 2 &middot; AI &middot; None means no reply yet

None is not zero and it is not an empty string. It is the value a reply holds before the model has answered. All three look empty and all three are different types, which matters when you decide whether to retry, and matters again in Module 4 when you start comparing.

```python
reply = None              # the model has not answered yet
tokens_used = 0           # it answered, and used nothing
empty_reply = ""          # it answered with nothing at all

print("reply      :", reply, type(reply))
print("tokens used:", tokens_used, type(tokens_used))
print("empty reply:", repr(empty_reply), type(empty_reply))

print()
print("three different types, and every one of them is falsy:")
print("  bool(None):", bool(reply))
print("  bool(0)   :", bool(tokens_used))
print('  bool("")  :', bool(empty_reply))
```

#### Use case 3 &middot; The truthiness gotcha

bool() turns anything into True or False, and the surprises are worth seeing now rather than in a config parser at midnight. The string "0" is True, because it is a string with a character in it.

```python
print('bool(1)       ->', bool(1))
print('bool(0)       ->', bool(0))
print('bool(0.0)     ->', bool(0.0))
print('bool("")      ->', bool(""))
print('bool("0")     ->', bool("0"))       # a non-empty string
print('bool("False") ->', bool("False"))   # also non-empty
print('bool(None)    ->', bool(None))
```

#### Practice exercises

1. Store a server's CPU count as an int and its memory in GB as a float, then print a one-line summary using both.
2. Take a cloud bill amount as a string, cast it to a float, and print what a 10 percent increase would look like.
3. Use isinstance() to check whether an incoming alert's severity level is an int before comparing it to a threshold.
4. Store a model's temperature setting as a float, then cast a string like "0.9" into a float to update it safely.

#### Module complete

You can now store values in variables, name them properly, and convert between types safely.


---

### Module 3: Strings

*Create, slice, format, and clean up text, from a single word to a multi-line AI prompt.*

Notebook: [`notebooks/03_strings.ipynb`](notebooks/03_strings.ipynb) &middot; answers: [`solutions/03_strings.md`](solutions/03_strings.md)

#### Slide 2 &middot; What Is a String?

A string is a sequence of characters wrapped in single quotes, double quotes or
triple quotes.

- **Immutable.** Once created, a string cannot be changed in place.
- **Indexed.** Every character has a position, so you can grab one directly.
- **Iterable.** You can loop through a string one character at a time.

```python
word = "Python"

# indexed
print(word[0])

# iterable
for char in word:
    print(char)

# immutable
# word[0] = "J"     -> this raises an error
```

#### Slide 3 &middot; Creating Strings

Single quotes, double quotes or triple quotes all work. Triple quotes let a
string span several lines.

**AI framing.** A system prompt for an AI assistant is really just a multi-line
string. This is exactly the pattern behind a `SYSTEM_PROMPT` variable.

```python
str1 = 'Hello'
str2 = "World"
str3 = '''Multiline
string using triple quotes.'''

print(str1, str2)
print(str3)
```

```python
SYSTEM_PROMPT = '''You are a senior AI consultant.
Give exactly 5 ideas. No intro. No explanation.'''

print(SYSTEM_PROMPT)
```

#### Slide 4 &middot; Building Prompts with Parentheses

You can also join string literals together with parentheses. This is handy for
building a long, structured piece of text line by line, instead of one long
triple-quoted block.

**Why bother?** Each line stays short and easy to edit, which matters once a
prompt grows past a few lines.

```python
SYSTEM_CONTRACT = (
    "You are a senior SRE assistant.\n"
    "LINE1: <one short diagnostic step>\n"
    "LINE2: <one short follow-up check>\n"
)

print(SYSTEM_CONTRACT)
```

#### Slide 5 &middot; Indexing and Slicing

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

```python
word = "Python"
print(word[0])
print(word[-1])

word = "Programming"
print(word[0:5])
print(word[3:])
print(word[::2])
print(word[::-1])
```

```python
instance_id = "i-0a1b2c3d4e5f"
print(instance_id[0])          # the prefix
print(instance_id[-4:])        # the last four characters

log_entry = "2024-08-19 [ERROR] Database Connection Failed"
print(log_entry[:10])          # the date
print(log_entry[11:18])        # the severity
print(log_entry[19:])          # the message
```

#### Slide 6 &middot; Common String Methods

These are the methods you will reach for constantly.

| Method | What it does |
|---|---|
| `upper()` / `lower()` | Change case |
| `strip()` | Remove whitespace |
| `find()` / `count()` | Search inside a string |
| `replace()` | Substitute text |
| `split()` | Break into a list |
| `join()` | Glue a list back together |

#### Slide 7 &middot; Methods in Action

Chaining a few of these together is a normal part of cleaning up text.

**Reading the chain.** `text.split()` breaks a sentence into a list of words.
`"-".join(words)` glues that list back together with a dash between each word.

**Order matters.** `split()` has to run before `join()` has a list to work
with. You cannot join a plain string.

`split()` hands you back a **list**. Module 6 covers lists in full; here it is
just the thing `join()` takes back.

```python
text = "Python programming"
print(text.find("prog"))

text = "I love Python"
print(text.replace("love", "like"))

words = text.split()
print(words)

joined = "-".join(words)
print(joined)
```

```python
trace_id = "  req_001_auth_service  "
clean_id = trace_id.strip().upper()
print(repr(clean_id))

tags = "env:prod,service:orders,region:us-east-1"
tag_list = tags.split(",")
print(tag_list)
print(";".join(tag_list))
```

#### Slide 8 &middot; String Formatting with f-strings

f-strings are the modern way to build strings with values inside them. Put an
`f` before the opening quote, and wrap any value in curly braces.

A format spec like `:.1f` inside the braces controls how a number is displayed,
here to one decimal place.

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

temperature = 0.7
waited = 2.3
print(f"--- temp={temperature} ---")
print(f"Waited {waited:.1f}s in silence.")
```

#### Slide 9 &middot; Escape Sequences and Raw Strings

Backslash sequences insert characters that are hard to type directly, like a
newline `\n` or a tab `\t`.

A raw string, written with an `r` before the quote, tells Python to ignore
those escape sequences, which is what you want for Windows file paths.

Common escapes: `\n` newline, `\t` tab, `\\` backslash, `\"` quote.

```python
print("Hello\nWorld")
print("Name:\tAlice")
print(r"C:\newfolder\test")
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; Assemble a system prompt from parts

A long prompt built as one triple-quoted block becomes unreadable and hard to edit. Joining short literals inside parentheses, the pattern from slide 4, keeps each rule on its own line where you can change one without disturbing the rest.

```python
persona = "senior SRE assistant"
max_steps = 3

SYSTEM_PROMPT = (
    f"You are a {persona}.\n"
    f"Give at most {max_steps} diagnostic steps.\n"
    "Each step must be one short sentence.\n"
    "No preamble. No apology. No markdown.\n"
)

print(SYSTEM_PROMPT)
print("characters:", len(SYSTEM_PROMPT))
print("rough tokens:", len(SYSTEM_PROMPT) // 4)
```

#### Use case 2 &middot; AI &middot; Mask a key before it reaches a log

Sometimes you need to show which key is in use without showing the key. Slicing the front and the back and hiding the middle gives you something identifiable that is useless if it leaks.

```python
api_key = "sk-proj-9f2b7c41a8de4b0f93e2"

masked = api_key[:7] + "..." + api_key[-4:]

print("using key:", masked)
print("length   :", len(api_key), "characters")
print("looks like a project key:", api_key.startswith("sk-proj-"))

# never do this, in any environment
# print(api_key)
```

#### Use case 3 &middot; AI &middot; Pull the answer out of a raw response

Before you learn JSON parsing in Module 9, you can still get at the content of a response with the string methods from this module. It is also a fair description of what a parser does underneath.

```python
raw = 'assistant: The capital of France is Paris. [tokens=8]'

speaker = raw.split(":")[0].strip()
body = raw.split(":", 1)[1]
answer = body.split("[")[0].strip()
tokens = int(raw.split("tokens=")[1].strip("]"))

print("speaker:", speaker)
print("answer :", answer)
print("tokens :", tokens, type(tokens))

print()
print(f"{speaker.title()} replied in {tokens} tokens: {answer!r}")
```

#### Use case 4 &middot; Normalise a service name

Names arrive inconsistently: extra spaces, mixed case, underscores where hyphens belong. Cleaning them the same way every time is what stops two spellings of one service becoming two rows in a report.

```python
raw = "  Payment_Gateway  "

clean = raw.strip().lower().replace("_", "-")

print("raw   :", repr(raw))
print("clean :", repr(clean))
print("starts with 'pay':", clean.startswith("pay"))
```

```python
line = "2024-08-19 [ERROR] payment-service | Database Connection Failed | retry=3"

# Your lab answer goes here.
```

#### Practice exercises

1. Use a triple-quoted string to write a short multi-line deployment changelog entry.
2. Use string slicing to pull the region code out of an instance id like "i-0123456789-us-east-1".
3. Use split() and join() to reformat a log line so the timestamp and message are separated by a single dash.
4. Build a SYSTEM_PROMPT string with an f-string that inserts a variable holding the assistant's persona name.

#### Module complete

You can now create, slice, format and clean up strings, including multi-line prompts.


---

### Module 4: Operators and Expressions

*Do math, compare values, combine conditions, and check what's inside a collection.*

Notebook: [`notebooks/04_operators.ipynb`](notebooks/04_operators.ipynb) &middot; answers: [`solutions/04_operators.md`](solutions/04_operators.md)

#### Slide 2 &middot; What Is an Operator?

An **operator** performs an operation on values. An **expression** is any
combination of values, variables and operators that produces a result.

| Group | Operators |
|---|---|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` |
| Logical | `and or not` |
| Identity and membership | `is`, `is not`, `in`, `not in` |

```python
# an expression combines values and operators into a result
a = 10
b = 3

result = a + b * 2
print(result)

# operators follow the usual order of operations
print((a + b) * 2)
```

#### Slide 3 &middot; Arithmetic Operators

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

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
```

#### Slide 4 &middot; Comparison Operators

These always return `True` or `False`.

`==` equal to &middot; `!=` not equal to &middot; `>` `<` greater or less than
&middot; `>=` `<=` greater or less than or equal

```python
x = 10
y = 5

print(x > y)
print(x < y)
print(x == 10)
print(y != 5)
```

#### Slide 5 &middot; Logical Operators

`and`, `or` and `not` combine or invert conditions. With `a = True` and
`b = False`:

- `a and b` is `False`, because both must be true
- `a or b` is `True`, because at least one is true
- `not a` is `False`, because it flips the value

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

```python
# A realistic combination: page someone only if it is severe AND in hours.
severity = 1
business_hours = False

print("page on call:", severity == 1 and business_hours)
print("send email  :", severity == 1 or not business_hours)
```

#### Slide 6 &middot; Assignment Operators

These update a variable in place, a shorthand for reassigning it based on its
current value.

`+=` is `x = x + 5` &middot; `-=` is `x = x - 5` &middot; `*=` is `x = x * 5`
&middot; `/=` is `x = x / 5`

```python
x = 10

x += 5
print(x)

x *= 2
print(x)

x -= 10
x //= 2
print(x)
```

#### Slide 7 &middot; Identity: is vs ==

`is` checks whether two variables point to the **exact same object in memory**,
a stricter test than `==`, which only checks whether the values match.

**Heads up.** The square brackets below create a **list**, which Module 6
covers in full. For now just read `[1, 2, 3]` as an ordered group of values.

```python
a = [1, 2, 3]
b = a                # same object, new name
c = [1, 2, 3]        # different object, same values

print("a is b:", a is b)
print("a is c:", a is c)
print("a == c:", a == c)
```

#### Slide 8 &middot; Membership: in and not in

`in` and `not in` check whether a value exists inside a collection, such as a
string, list or dictionary. A string is the simplest case: `in` looks for a
smaller piece of text inside a bigger one.

```python
word = "apple"

print("a" in word)
print("z" in word)
print("app" not in word)
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; Will this prompt fit in the context window?

Every model has a hard limit, and it has to hold the prompt and the answer. Checking before you send is the difference between a clear message from your own code and a rejection from the API.

```python
context_window = 8192
system_tokens = 240
history_tokens = 5100
question_tokens = 180
max_output = 1000

prompt_total = system_tokens + history_tokens + question_tokens
needed = prompt_total + max_output
headroom = context_window - needed

print("prompt tokens:", prompt_total)
print("plus output  :", needed)
print("window       :", context_window)
print("headroom     :", headroom)
print("it fits      :", needed <= context_window)
print("cutting it fine:", needed <= context_window and headroom < 500)
```

#### Use case 2 &middot; AI &middot; Are these settings valid?

Range checks are two comparisons joined with and. Doing them yourself gives a message that says which setting is wrong, instead of a stack trace from somebody else's library.

```python
temperature = 0.7
top_p = 1.4
max_tokens = 512

temperature_ok = 0.0 <= temperature <= 2.0
top_p_ok = 0.0 <= top_p <= 1.0
max_tokens_ok = 1 <= max_tokens <= 4096

print("temperature", temperature, "valid:", temperature_ok)
print("top_p      ", top_p, "valid:", top_p_ok)
print("max_tokens ", max_tokens, "valid:", max_tokens_ok)

print()
print("safe to send:", temperature_ok and top_p_ok and max_tokens_ok)
print("something is wrong:", not (temperature_ok and top_p_ok and max_tokens_ok))
```

#### Use case 3 &middot; AI &middot; Spread calls across a pool of keys

The remainder operator spreads work evenly over a fixed number of things. With API keys it keeps any one key from hitting its rate limit first, and the choice is repeatable rather than random.

```python
key_count = 3

print("request 7  -> key", 7 % key_count)
print("request 8  -> key", 8 % key_count)
print("request 9  -> key", 9 % key_count)
print("request 10 -> key", 10 % key_count)

# the same idea, deciding which shard a user's embeddings live on
user_id = 90210
print()
print("user", user_id, "-> shard", user_id % 16)
```

#### Use case 4 &middot; Disk headroom

Floor division converts units without leaving a decimal tail, and a comparison turns the number into the decision you actually want: is this worth waking someone up for.

```python
used_gb = 823
total_gb = 1000

percent_used = (used_gb / total_gb) * 100
free_gb = total_gb - used_gb

print(f"used: {percent_used:.1f}%")
print("free:", free_gb, "GB")
print("over the warning line:", percent_used > 80)
print("critical             :", percent_used > 90 and free_gb < 50)
```

```python
budget = 500.0
spend = 612.40
severity = 2
business_hours = False
on_call_region = "eu-west-1"

# Your lab answer goes here.
```

#### Practice exercises

1. Use the modulus operator to decide whether a build number is even or odd, to route it to a canary group.
2. Use a comparison operator to check whether a monthly cloud bill has gone over a set budget threshold.
3. Use and/or to decide whether an alert should page someone, based on high severity and it being business hours.
4. Use the in operator to check whether a keyword appears in a list of banned prompt terms.

#### Module complete

You can now do maths, compare values, combine conditions and check membership.


---

### Module 5: Control Flow

*Make decisions with if, repeat work with for and while, and steer loops with break, continue, and pass.*

Notebook: [`notebooks/05_control_flow.ipynb`](notebooks/05_control_flow.ipynb) &middot; answers: [`solutions/05_control_flow.md`](solutions/05_control_flow.md)

#### Slide 2 &middot; What Is Control Flow?

Control flow statements let a program make decisions and repeat work, instead
of running the same fixed lines every time.

- **Conditionals**: `if`, `elif`, `else` choose a path
- **Loops**: `for`, `while` repeat work
- **Loop control**: `break`, `continue`, `pass` steer a loop

```python
temperature = 15

if temperature < 0:
    print("Freezing")
elif temperature < 20:
    print("Cool")
else:
    print("Warm")

# this is control flow: the path taken depends on the value
```

#### Slide 3 &middot; if, elif, and else

`if` runs a block only when its condition is `True`. `elif` checks another
condition if the first was `False`. `else` catches everything left over.

**Indentation matters.** Python uses indentation, not curly braces, to mark
what belongs inside a block. Four spaces is the standard.

```python
# In a script this would be:  num = int(input("Enter a number: "))
num = -7

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
```

```python
severity = 2

if severity == 1:
    print("Alerting On-Call SRE...")
elif severity == 2:
    print("Log warning; monitor throughput.")
else:
    print("No action required.")
```

Change `severity` to `1` and then to `3`, re-running the cell each time, so you see all three branches fire.

#### Slide 4 &middot; The for Loop

A `for` loop steps through a sequence, one item at a time. `range()` is the
most common starting point, a built in function that generates a run of
numbers.

`range(start, stop, step)`: `start` defaults to 0, `stop` is required and is
**not** included, `step` defaults to 1.

```python
for i in range(1, 6):
    print(i)
```

```python
for attempt in range(1, 4):
    print(f"Deployment attempt {attempt}...")
```

#### Slide 5 &middot; Looping Over a String

A string is also a sequence, so a `for` loop can step through it character by
character.

**Coming up.** Module 6 introduces lists and tuples, which are also sequences
you can loop through the same way. Once you have that module, come back and try
looping over a list here.

```python
word = "Python"

for char in word:
    print(char)
```

```python
# The same idea, used to imitate a reply streaming in one character at a time.
for char in "ERR404":
    print(char, end=" ", flush=True)

print()
```

#### Slide 6 &middot; The while Loop

A `while` loop repeats as long as its condition stays `True`. Remember to
update the condition inside the loop, or it will run forever.

**The three parts of a while loop.** A starting value, a condition to check,
and a step that moves toward ending the loop.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

```python
health_score = 100

while health_score > 95:
    print(f"System Healthy: {health_score}%")
    health_score -= 1

print("dropped below threshold at", health_score)
```

#### Slide 7 &middot; break and continue

`break` stops the loop immediately. `continue` skips the rest of the current
pass and moves to the next one.

```python
# break: stop at 5
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

print()
```

```python
# continue: skip vowels
for char in "education":
    if char in "aeiou":
        continue
    print(char, end="")

print()
```

#### Slide 8 &middot; pass: the Placeholder

`pass` does nothing. It exists so Python has a valid statement to run when you
are not ready to write the real logic yet.

```python
for i in range(5):
    pass          # to be filled in later

print("loop finished without doing anything")
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; Back off when you hit a rate limit

A 429 means slow down, and retrying immediately makes it worse. Doubling the wait each time is what every serious client library does underneath, and it is a while loop with one multiplication.

```python
attempt = 0
wait = 1

while attempt < 5:
    attempt += 1
    print(f"attempt {attempt}: rate limited, waiting {wait}s")
    wait = wait * 2

    if attempt == 4:
        print("request accepted")
        break

print("attempts used:", attempt)
print("would have waited", 1 + 2 + 4, "seconds in total")
```

#### Use case 2 &middot; AI &middot; Stream a reply and stop at the sentinel

A streamed answer arrives piece by piece, and some models mark the end with a stop sequence rather than simply closing. break is how you leave the loop the moment you see it, instead of printing the marker.

```python
stream = "The target group is unhealthy.<END>Ignore everything after this."

reply = ""

for char in stream:
    if char == "<":
        print()
        print("stop sequence reached, ignoring the rest")
        break
    reply += char
    print(char, end="", flush=True)

print()
print("captured:", repr(reply))
print("characters kept:", len(reply), "of", len(stream))
```

#### Use case 3 &middot; AI &middot; Count the failures in a run history

A counter outside the loop, updated inside it, is the pattern behind every tally you will write. Here it is turning a run of results into the success rate you would put on a dashboard.

```python
run_history = "SSSFSSSSFSSFSSS"

passed = 0
failed = 0

for result in run_history:
    if result == "S":
        passed += 1
    else:
        failed += 1

print("runs   :", len(run_history))
print("passed :", passed)
print("failed :", failed)
print(f"success: {(passed / len(run_history)) * 100:.1f}%")
print("healthy:", failed < 4)
```

#### Use case 4 &middot; Classify a run of status codes

An if and elif chain inside a loop is how a log processor decides what each line means. This one walks a range of codes rather than a list, because lists arrive in the next module.

```python
for code in range(500, 505):
    if code == 500:
        print(code, "internal error, check the application logs")
    elif code == 502:
        print(code, "bad gateway, the upstream did not answer")
    elif code == 503:
        print(code, "service unavailable, probably still starting")
    elif code == 504:
        print(code, "gateway timeout, the upstream was too slow")
    else:
        print(code, "unrecognised, look it up")
```

#### Practice exercises

1. Write a for loop that prints the status of each server in a list of server names, using a placeholder status.
2. Write a while loop that checks up to 5 times whether a cloud resource is ready, printing an attempt count each time.
3. Write an if/elif/else chain that classifies an incident by severity level (1, 2, or 3) and prints the right response.
4. Write a for loop that prints each character of a string one at a time, the way a streamed response might appear.

#### Module complete

You can now make decisions, repeat work, and steer a loop with break, continue and pass. Exercise 1 needs a list, so come back to it after Module 6.


---

### Module 6: Lists, Tuples, Dictionaries, and Sets

*Four ways to hold a group of values, and how to pick the right one.*

Notebook: [`notebooks/06_collections.ipynb`](notebooks/06_collections.ipynb) &middot; answers: [`solutions/06_collections.md`](solutions/06_collections.md)

#### Slide 2 &middot; What Are Collections?

Python has four built in ways to hold a group of values. Picking the right one
comes down to order, whether it can change, and whether duplicates matter.

| Written as | Type | Ordered | Changeable | Duplicates |
|---|---|---|---|---|
| `[ ]` | List | yes | yes | yes |
| `( )` | Tuple | yes | no | yes |
| `{ k: v }` | Dictionary | yes | yes | keys are unique |
| `{ }` | Set | no | yes | no |

#### Slide 3 &middot; Lists: Creating and Accessing

A list holds items in order and lets you add, remove or change them after
creation. Indexing and slicing work exactly as they did for strings in
Module 3.

```python
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
```

#### Slide 4 &middot; Common List Methods

These are the methods you will use to grow, shrink and reorder a list.

| Method | What it does |
|---|---|
| `append(x)` | Add one item to the end |
| `extend(list)` | Add several items |
| `insert(i, x)` | Insert at a position |
| `remove(x)` | Delete the first match |
| `pop(i)` | Remove and return by index |
| `sort()` / `reverse()` | Reorder in place |

```python
regions = ["us-east-1", "us-west-2"]
regions.append("eu-central-1")
print(regions)

error_codes = [404, 500]
error_codes.extend([502, 504])
print(error_codes)

error_codes.sort()
print("sorted:", error_codes)
print("popped:", error_codes.pop(), "-> remaining:", error_codes)
```

#### Slide 5 &middot; List Comprehensions

A list comprehension builds a new list in one line, combining a loop and a
condition.

**Reading the pattern.** `[expression for item in sequence if condition]`, and
the condition part is optional.

```python
squares = [x**2 for x in range(1, 6)]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)
```

```python
latencies = [12.4, 45.1, 8.9, 102.3, 15.6]

critical = [l for l in latencies if l > 50]
print(critical)

# The same thing written the long way, for comparison.
critical_long = []
for l in latencies:
    if l > 50:
        critical_long.append(l)

print(critical_long)
```

#### Slide 6 &middot; Looping Over a List

Now that lists exist, the `for` loop from Module 5 can step through one
directly. This is the exercise Module 5 told you to come back for.

**Skipping empty values.** A list can hold gaps. Checking a value inside an
`if`, called **truthiness**, skips anything empty or missing: `None`, `""` and
`[]` all count as `False`.

```python
scores = [88, 92, 79, 95]

for score in scores:
    print(f"Score: {score}")
```

```python
pieces = ["Hello", None, " ", "", "world"]
full = ""

for piece in pieces:
    if piece:                 # skips None and ""
        full += piece

print(repr(full))
```

#### Slide 7 &middot; Tuples: Ordered and Unchangeable

A tuple looks like a list but cannot be modified after creation. Use one when
the data should not change, such as coordinates or a fixed record.

**The trailing comma matters.** `(5)` is just the number 5 in parentheses.
`(5,)` with a comma is a one item tuple.

```python
mixed_tuple = (10, "Python", 3.14, True)
single_element = (5,)

numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[1:4])
print(type(single_element), type((5)))

# fruits = ("apple", "banana")
# fruits[1] = "blueberry"     -> this raises an error
```

#### Slide 8 &middot; Unpacking Tuples

Unpacking lets you assign each item in a tuple to its own variable in one line.

```python
person = ("John", 25, "Engineer")
name, age, job = person

print(name, age, job)
```

#### Slide 9 &middot; Dictionaries: Key and Value Pairs

A dictionary stores data as key value pairs. Keys must be unique and are used
to look up values quickly.

**Safe access with `get()`.** `student.get("email", "N/A")` returns `"N/A"`
instead of raising an error when the key does not exist.

```python
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
```

#### Slide 10 &middot; Useful Dictionary Methods

These make reading, combining and looping through a dictionary straightforward.

| Method | What it does |
|---|---|
| `get(key)` | Read a value safely |
| `keys()` / `values()` / `items()` | Loop over keys, values or pairs |
| `update(other)` | Merge another dictionary in |
| `pop(key)` | Remove and return a value |

```python
for key, value in student.items():
    print(f"{key} -> {value}")

print()
print("keys  :", list(student.keys()))
print("values:", list(student.values()))
```

#### Slide 11 &middot; Nested Dictionaries

A dictionary value can be another dictionary. This nesting shows up constantly
in real data.

**AI framing.** An AI API response is usually a nested dictionary. Reading it
is the same skill as reading `student["subjects"]`, just one or two levels
deeper.

```python
response = {
    "model": "llama3.2:1b",
    "message": {
        "role": "assistant",
        "content": "Hello Serge!",
    },
    "done": True,
}

print(response["message"]["content"])
```

#### Slide 12 &middot; Dictionary Comprehension

The same one-line pattern from list comprehensions works for dictionaries too.

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)
```

#### Slide 13 &middot; Lists of Dictionaries

A list can hold dictionaries as its items. Chat APIs represent conversation
history exactly this way: each item is a dictionary with a role and content,
which is the list and dictionary skills you already have, combined.

```python
messages = [
    {"role": "user", "content": "Hi, I am Serge."},
    {"role": "assistant", "content": "Hello Serge!"},
    {"role": "user", "content": "What is my name?"},
]

print(messages[0]["role"])
print(messages[-1]["content"])

for m in messages:
    print(f"[{m['role']:>9}] {m['content']}")
```

#### Slide 14 &middot; Sets: Unordered and Unique

A set automatically drops duplicates and does not preserve order. Reach for one
when you only care whether something exists.

**No indexing.** Since a set has no order, there is no `fruits[0]`. You can
only check membership or loop through it.

```python
fruits = {"apple", "banana", "apple", "cherry"}

print(fruits)
print("banana" in fruits)
print("how many unique:", len(fruits))
```

#### Slide 15 &middot; Set Operations

Sets support the same operations as maths sets, using `A = {1, 2, 3}` and
`B = {3, 4, 5}`.

| Operation | Call | Result |
|---|---|---|
| union | `A.union(B)` | `{1,2,3,4,5}` |
| intersection | `A.intersection(B)` | `{3}` |
| difference | `A.difference(B)` | `{1,2}` |
| symmetric difference | `A.symmetric_difference(B)` | `{1,2,4,5}` |

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; How big is this conversation?

Chat history is a list of dictionaries, so measuring it is a loop and a sum. A rough count of four characters per token is close enough to tell you whether you are approaching a model's limit.

```python
messages = [
    {"role": "system", "content": "You are a senior SRE assistant."},
    {"role": "user", "content": "The api-gateway is returning 502s."},
    {"role": "assistant", "content": "Check the target group health first."},
    {"role": "user", "content": "Two of three targets are unhealthy."},
]

characters = sum(len(m["content"]) for m in messages)
rough_tokens = characters // 4

print("turns       :", len(messages))
print("characters  :", characters)
print("rough tokens:", rough_tokens)
print("roles       :", sorted(set(m["role"] for m in messages)))
print("longest turn:", max(len(m["content"]) for m in messages), "characters")
```

#### Use case 2 &middot; AI &middot; Trim a history that has grown too long

When a conversation outgrows the context window you drop the middle, not the ends. The system prompt sets the behaviour and the recent turns carry the thread, so those are the ones worth keeping.

```python
history = [
    {"role": "system", "content": "You are a senior SRE assistant."},
    {"role": "user", "content": "turn 1"},
    {"role": "assistant", "content": "reply 1"},
    {"role": "user", "content": "turn 2"},
    {"role": "assistant", "content": "reply 2"},
    {"role": "user", "content": "turn 3"},
    {"role": "assistant", "content": "reply 3"},
]

keep_last = 4

system = [m for m in history if m["role"] == "system"]
rest = [m for m in history if m["role"] != "system"]
trimmed = system + rest[-keep_last:]

print("before:", len(history), "turns")
print("after :", len(trimmed), "turns")
print()
for m in trimmed:
    print(f"  {m['role']:>9}: {m['content']}")
```

#### Use case 3 &middot; AI &middot; Which documents came back more than once?

A retrieval step often returns the same document from several queries. A set gives you the unique ids, and a dictionary counts how often each one appeared, which is a crude but useful relevance score.

```python
retrieved = ["doc-4", "doc-1", "doc-4", "doc-9", "doc-1", "doc-4"]

hits = {}
for doc in retrieved:
    hits[doc] = hits.get(doc, 0) + 1

unique = sorted(set(retrieved))

print("retrieved     :", retrieved)
print("unique docs   :", unique)
print("hit counts    :", hits)
print("most relevant :", max(hits, key=hits.get))
print("seen once only:", [d for d in unique if hits[d] == 1])
```

#### Use case 4 &middot; Group instances by region

A dictionary whose values are lists is the shape of almost every grouping job. Build it as you loop, creating the empty list the first time you meet a new key.

```python
instances = [
    ("web-01", "us-east-1"),
    ("web-02", "us-east-1"),
    ("api-01", "eu-west-1"),
    ("db-01", "eu-west-1"),
    ("cache-01", "ap-south-1"),
]

by_region = {}

for name, region in instances:
    if region not in by_region:
        by_region[region] = []
    by_region[region].append(name)

for region, names in by_region.items():
    print(f"{region:12s} {len(names)}  {names}")
```

#### Practice exercises

1. Store a list of failed pipeline stage names and use a list comprehension to keep only the ones containing "test".
2. Build a dictionary mapping cloud region names to their instance counts, then print the total across all regions.
3. Use a set to find the unique error codes out of a list of incident log entries that contains duplicates.
4. Build a list of dictionaries representing a short chat history, then print only the assistant's replies.

#### Module complete

You can now pick the right collection and work with lists, tuples, dictionaries and sets. This is also the moment to go back and finish Module 5's first practice exercise.


---

### Module 7: Handling Errors

*Catch problems instead of crashing, retry what's worth retrying, and raise your own errors.*

Notebook: [`notebooks/07_handling_errors.ipynb`](notebooks/07_handling_errors.ipynb) &middot; answers: [`solutions/07_handling_errors.md`](solutions/07_handling_errors.md)

#### Slide 2 &middot; When Something Goes Wrong

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

```python
# The crashing version, kept safe inside a demonstration.
text = "abc"

try:
    number = int(text)
except ValueError as e:
    print("Python raised:", type(e).__name__)
    print("with the message:", e)

print("and the program carried on")
```

#### Slide 3 &middot; try and except

Code inside `try` runs normally. If it raises the error type named in `except`,
that block runs instead of the program crashing.

**Name the error you expect.** `except ValueError` only catches `ValueError`. A
different error still crashes the program, which is usually what you want:
catching everything hides bugs.

```python
text = "abc"

try:
    number = int(text)
except ValueError:
    print("That was not a number.")
```

```python
# The same shape, applied to a truncated API response.
import json

broken_response = '{"id": "msg_01", "content": '

try:
    data = json.loads(broken_response)
    print("parsed fine:", data["content"])
except json.JSONDecodeError:
    print("Failed to parse API response.")
```

#### Slide 4 &middot; Multiple except, else, and finally

You can catch more than one kind of error. `else` runs only if nothing went
wrong. `finally` always runs, error or not.

**Why `finally` matters.** It is for cleanup work, like closing a connection,
that needs to happen whether or not something went wrong.

```python
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
```

Change `10 / 0` to `10 / 2` and run the cell again. The `else` branch fires, and `finally` still runs. That is the whole point of the pair.

#### Slide 5 &middot; Retrying Instead of Giving Up

Calling an AI model is a network call, and network calls fail sometimes: the
connection drops, the server is slow, or you hit a rate limit. Wrapping the
call lets your program recover instead of stopping.

**Reading the retry loop.** Each failed attempt is caught, logged and tried
again, up to a limit. Only after every attempt fails does the function give up
for good.

```python
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
```

```python
try:
    call_with_retry("")
except RuntimeError as e:
    print("gave up:", e)
```

#### Slide 6 &middot; Raising Your Own Errors

You are not limited to errors Python raises on its own. `raise` lets you signal
that something in your own code has gone wrong, with a message explaining why.

**`as e` captures the message.** `except ValueError as e` lets you read the
error's message with `str(e)`, or just `print(e)`.

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age


try:
    set_age(-5)
except ValueError as e:
    print("Invalid input:", e)
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; A response that is not the shape you expected

Two different failures look identical from the outside: the key is missing, or the thing you indexed into was never a dictionary. Separate except blocks let you say which one happened, which is the difference between a five minute fix and an afternoon.

```python
def read_reply(response):
    try:
        return response["choices"][0]["message"]["content"]
    except KeyError as e:
        return f"missing key in the response: {e}"
    except IndexError:
        return "the response came back with no choices"
    except TypeError:
        return "that was not shaped like a response at all"


good = {"choices": [{"message": {"content": "All targets healthy."}}]}
missing = {"choices": [{"message": {}}]}
empty = {"choices": []}

print(read_reply(good))
print(read_reply(missing))
print(read_reply(empty))
print(read_reply("just a string"))
```

#### Use case 2 &middot; AI &middot; Retry the model, then give up honestly

A retry loop that never gives up is a hung process. Counting the attempts and raising a clear error at the end means the caller finds out what happened rather than waiting forever.

```python
import time

calls = {"n": 0}


def call_model(prompt):
    calls["n"] += 1
    if calls["n"] < 3:
        raise TimeoutError("model did not respond in time")
    return f"answer to: {prompt}"


def ask(prompt, attempts=4):
    for attempt in range(1, attempts + 1):
        try:
            return call_model(prompt)
        except TimeoutError as e:
            print(f"  attempt {attempt}: {e}")
            time.sleep(0.1)
    raise RuntimeError(f"gave up after {attempts} attempts")


print(ask("summarise the incident"))
print("calls made:", calls["n"])
```

#### Use case 3 &middot; Parse a value that might be junk

Configuration is written by people, so it will eventually contain something that is not a number. Catching the failure and falling back to a default keeps the service starting instead of dying on boot.

```python
def read_port(text, default=8080):
    try:
        return int(text)
    except ValueError:
        print(f"  could not read {text!r} as a port, using {default}")
        return default


print("8080       ->", read_port("8080"))
print("not-a-port ->", read_port("not-a-port"))
print("empty      ->", read_port(""))
```

#### Use case 4 &middot; Always release the lock

A deployment lock that is never released blocks every future run. finally is the only thing that guarantees the release happens whether the work succeeded, failed, or raised something you did not expect.

```python
lock_held = False


def deploy_with_lock(should_fail):
    global lock_held
    lock_held = True
    print("  lock acquired")
    try:
        if should_fail:
            raise RuntimeError("deployment failed halfway")
        print("  deployment finished")
    except RuntimeError as e:
        print("  caught:", e)
    finally:
        lock_held = False
        print("  lock released")


deploy_with_lock(should_fail=False)
print("lock still held?", lock_held)

deploy_with_lock(should_fail=True)
print("lock still held?", lock_held)
```

```python
stages = ["build", "test", "migrate", "release"]

# Your lab answer goes here.
```

#### Practice exercises

1. Wrap a deployment step function in try/except to catch a simulated DeploymentError and print a clear message.
2. Write a retry loop around a function that checks whether a cloud storage bucket exists, catching a simulated exception.
3. Use try/except/finally so an incident ticket always gets marked as closed, even if updating it raises an error.
4. Add retry logic around a function that simulates calling a model API which sometimes raises a TimeoutError.

#### Module complete

You can now catch errors, retry what's worth retrying, and raise your own.


---

### Module 8: Functions

*Package reusable logic, pass arguments four different ways, and stream results with yield.*

Notebook: [`notebooks/08_functions.ipynb`](notebooks/08_functions.ipynb) &middot; answers: [`solutions/08_functions.md`](solutions/08_functions.md)

#### Slide 2 &middot; What Is a Function?

A function is a reusable block of code. You define it once with `def` and call
it as many times as you need, which keeps your programs organised.

**Order matters.** A function must be defined before it is called, and the code
inside it must be indented consistently.

```python
def greet():
    print("Hello! Welcome to Python.")


greet()          # calls the function
greet()
```

#### Slide 3 &middot; Parameters, Arguments, Return

A **parameter** is the name listed in the definition. An **argument** is the
value you pass in. `return` sends a value back to whoever called the function.

**`return` stops the function.** Once `return` runs, the function ends
immediately. Any code written after it never executes.

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


def square(num):
    return num * num


result = square(4)
print("Square:", result)
```

```python
def early_exit():
    return "first"
    print("this line never runs")


print(early_exit())
```

#### Slide 4 &middot; Four Kinds of Arguments

A function can accept arguments in four different ways, and you will mix and
match them.

| Kind | Looks like | Matched by |
|---|---|---|
| Positional | `func(1, 2)` | order |
| Default | `def func(a=5)` | falls back if omitted |
| Keyword | `func(b=10, a=5)` | name |
| Variable length | `*args` / `**kwargs` | collects the extras |

```python
def add(a, b):
    return a + b


print(add(3, 5))
```

#### Slide 5 &middot; Default and Keyword Arguments

A default value fills in when the caller leaves an argument out. Keyword
arguments let a call stay readable no matter the order.

**This is how AI SDKs read.** Keyword arguments are exactly how you call real
AI SDKs, for example `ollama.chat(model=..., messages=..., options=...)`.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()
greet("Alice")


def describe_pet(animal, name):
    print(f"{name} is a {animal}.")


describe_pet(animal="dog", name="Buddy")
describe_pet(name="Kitty", animal="cat")
```

#### Slide 6 &middot; *args and **kwargs

`*args` collects any number of extra positional values into a **tuple**.
`**kwargs` collects any number of extra named values into a **dictionary**.
Both are Module 6 types you already know.

**The names are a convention.** `args` and `kwargs` are not keywords. The `*`
and `**` are what matter; you could name them anything.

```python
def add_numbers(*args):
    print("received a", type(args).__name__, ":", args)
    return sum(args)


print(add_numbers(1, 2, 3, 4))
```

```python
def describe_person(**kwargs):
    print("received a", type(kwargs).__name__)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


describe_person(name="Alice", age=25, city="New York")
```

#### Slide 7 &middot; Generators: yield Instead of return

`return` sends back one value and ends the function. `yield` sends back a value
and **pauses**, continuing later from exactly where it left off.

**AI framing.** This is how streaming AI responses are built up piece by piece
on screen.

```python
def stream_reply(tokens):
    full = ""
    for token in tokens:
        full += token
        yield full


for partial in stream_reply(["Hi, ", "I ", "am ", "an ", "AI."]):
    print(partial)
```

#### Slide 8 &middot; Passing a Function as a Value

A function name **without parentheses** is just a value, like any variable. You
can pass it into another function and call it later. Tools such as Gradio use
this pattern constantly.

```python
def run_chat(fn, user_text):
    return fn(user_text, history=[])


def my_bot(message, history):
    return f"You said: {message}"


print(run_chat(fn=my_bot, user_text="Hello"))
# note: pass my_bot, not my_bot()
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; Build a call payload with **kwargs

This is the shape of every AI SDK call you will make. The required arguments are named, and anything else the caller passes is collected and merged in, so the function does not need changing each time the provider adds an option.

```python
def build_request(model, prompt, **options):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    payload.update(options)
    return payload


basic = build_request("gpt-4o-mini", "Say hello.")
tuned = build_request(
    "gpt-4o-mini",
    "Say hello.",
    temperature=0.2,
    max_tokens=100,
    stream=True,
)

print(basic)
print()
for key, value in tuned.items():
    print(f"  {key}: {value}")
```

#### Use case 2 &middot; AI &middot; Stream tokens and keep a running total

yield hands back one piece at a time. Accumulating as you go gives the caller both the growing answer and, at the end, the count you need for a cost line.

```python
def stream(tokens):
    so_far = ""
    for token in tokens:
        so_far += token
        yield so_far


pieces = ["The ", "target ", "group ", "is ", "unhealthy."]

count = 0
for partial in stream(pieces):
    count += 1
    print(f"  {count:>2}  {partial}")

print()
print("tokens streamed:", count)
print("final answer   :", partial)
```

#### Use case 3 &middot; AI &middot; Let the caller decide how to format

Passing a function as a value means one pipeline can print to a terminal, write JSON, or push to a UI, without the pipeline knowing which. Gradio and most chat frameworks are built on this.

```python
def plain(role, text):
    return f"{role}: {text}"


def bracketed(role, text):
    return f"[{role.upper():>9}] {text}"


def render(formatter, history):
    for role, text in history:
        print(formatter(role, text))


history = [("user", "Why is it slow?"), ("assistant", "Two targets are down.")]

render(plain, history)
print()
render(bracketed, history)
```

#### Use case 4 &middot; A retry helper worth reusing

Default arguments turn one function into several. Callers who do not care get sensible behaviour, and callers who do can turn the dials without you writing a second function.

```python
def call_with_retry(name, attempts=3, succeed_on=2):
    for attempt in range(1, attempts + 1):
        if attempt >= succeed_on:
            return f"{name} succeeded on attempt {attempt}"
        print(f"  {name}: attempt {attempt} failed")
    return f"{name} gave up after {attempts} attempts"


print(call_with_retry("health-check"))
print(call_with_retry("slow-service", attempts=5, succeed_on=4))
print(call_with_retry("broken-service", attempts=2, succeed_on=99))
```

#### Practice exercises

1. Write a function that takes a service name and environment as keyword arguments and returns a formatted deployment message.
2. Write a function using *args that sums the estimated monthly costs of any number of cloud resources.
3. Write a generator function that yields incident status updates one at a time, from a list of updates.
4. Write a function that accepts another function as a callback and uses it to process a chat message, the way the Gradio example does.

#### Module complete

You can now write functions, handle arguments four ways, and stream results with yield.


---

### Module 9: File Handling

*Read and write files, work safely with with, and handle JSON, including real API responses.*

Notebook: [`notebooks/09_file_handling.ipynb`](notebooks/09_file_handling.ipynb) &middot; answers: [`solutions/09_file_handling.md`](solutions/09_file_handling.md)

##### Before you start: the scratch folder

Everything in this notebook writes into a `scratch/` folder next to it, so
nothing else on your machine is touched. `scratch/` is in `.gitignore`, so none
of it will end up in a commit. Run this cell first.

```python
from pathlib import Path

WORK = Path("scratch")
WORK.mkdir(exist_ok=True)

print("writing files into:", WORK.resolve())
```

#### Slide 2 &middot; What Is File Handling?

File handling lets your program read and write data outside of memory, so it
survives after the script finishes running.

**Two verbs, one function.** `open()` handles both reading and writing. What it
does depends entirely on the mode you pass it.

```python
# write something to disk
file = open(WORK / "notes.txt", "w")
file.write("Meeting at 3pm")
file.close()

# read it back later, even after the program restarts
file = open(WORK / "notes.txt", "r")
print(file.read())
file.close()
```

#### Slide 3 &middot; File Modes

You choose a mode when you open a file, which controls what you are allowed to
do with it.

| Mode | Meaning |
|---|---|
| `"r"` | Read. The default mode. |
| `"w"` | Write. **Overwrites** anything already there. |
| `"a"` | Append. Adds new content to the end. |
| `"x"` | Create. Fails if the file already exists. |
| `"rb"` / `"wb"` | Same as r and w, for binary data. |

#### Slide 4 &middot; Opening, Writing, and Reading

Write to a file, then open it again separately to read it back.

**Do not forget `close()`.** Skipping it can leave a file locked or lose
unsaved data. The `with` statement, coming up shortly, removes this risk
entirely.

```python
file = open(WORK / "sample.txt", "w")
file.write("Hello, this is a test file.")
file.close()

file = open(WORK / "sample.txt", "r")
content = file.read()
print(content)
file.close()
```

#### Slide 5 &middot; Reading Line by Line

You do not have to read a whole file at once. Pull one line, or every line as a
list.

```python
file = open(WORK / "sample.txt", "r")
line = file.readline()          # reads a single line
file.close()
print("readline :", repr(line))

file = open(WORK / "sample.txt", "r")
lines = file.readlines()        # reads all lines into a list
file.close()
print("readlines:", lines)
```

#### Slide 6 &middot; The with Statement

Opening a file with `with` automatically closes it for you, even if an error
happens partway through. This is the pattern to reach for by default.

**No `close()` needed.** `with` removes the risk of a locked file or lost data
entirely, so prefer it over `open()` / `close()` pairs.

```python
with open(WORK / "sample.txt", "r") as file:
    content = file.read()
    print(content)

# the file is already closed here, no need to call close()
print("closed?", file.closed)
```

#### Slide 7 &middot; Writing Multiple Lines and Appending

`writelines()` takes a list of strings and writes each one. Appending with
`"a"` adds to the end without touching what is already there.

**Remember the newline.** `writelines()` does not add `\n` for you. Each
string in the list needs its own.

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open(WORK / "output.txt", "w") as file:
    file.writelines(lines)

with open(WORK / "output.txt", "a") as file:
    file.write("This line will be appended.\n")

with open(WORK / "output.txt", "r") as file:
    print(file.read())
```

Run that cell two or three times. The log grows each time, which is exactly what append mode is for. Change the mode to `"w"`, run it again, and watch the earlier lines disappear.

#### Slide 8 &middot; Working with Binary Files

Images and other non-text files need `"rb"` and `"wb"`, the binary versions of
read and write mode. Binary content comes back as bytes rather than text.

```python
# Make a small binary file so there is something real to copy.
with open(WORK / "image.jpg", "wb") as f:
    f.write(bytes(range(40)))

with open(WORK / "image.jpg", "rb") as file:
    data = file.read()
    print("Binary content:", data[:20])

with open(WORK / "copy.jpg", "wb") as new_file:
    new_file.write(data)

print("copy written, same size:", (WORK / "copy.jpg").stat().st_size == len(data))
```

#### Slide 9 &middot; Checking and Deleting Files

Checking whether a file exists and deleting one both live in a module called
`os`, which ships with Python.

**First time seeing `import`?** Module 10 explains it in full. The short
version: it brings in code someone else already wrote, used with a dot, like
`os.path.exists()`.

```python
import os

target = WORK / "sample.txt"

if os.path.exists(target):
    print("File exists")
else:
    print("File not found")

os.remove(target)
print("after remove, exists?", os.path.exists(target))
```

#### Slide 10 &middot; Working with JSON

JSON is a text format almost every API uses to send and receive data. It maps
directly onto a Python dictionary.

**Two functions to know.** `json.dumps` turns a Python object into a JSON
string. `json.loads` turns a JSON string back into a Python object.

```python
import json

person = {"name": "Alice", "age": 25}

as_text = json.dumps(person)
print(as_text)
print(type(as_text))

back_to_dict = json.loads(as_text)
print(back_to_dict["name"])
print(type(back_to_dict))
```

#### Slide 11 &middot; Parsing a Real JSON Response

A model API response arrives as JSON text over the network. Parsing it is the
same skill applied to something you did not write yourself.

**Follow the brackets.** `data["content"][0]["text"]` is a dictionary, then a
list, then a dictionary again, one step at a time. That is exactly the nested
structure from Module 6.

```python
raw_response = '''
{
  "model": "claude-sonnet-4-6",
  "content": [{"type": "text", "text": "The capital of France is Paris."}],
  "usage": {"input_tokens": 12, "output_tokens": 8}
}
'''

data = json.loads(raw_response)

print(data["content"][0]["text"])
print(data["usage"]["output_tokens"])
```

#### Slide 12 &middot; Reading and Writing JSON Files

`json.load` and `json.dump` work the same way, but read from and write directly
to a file, so you never build the string by hand.

**dump vs dumps.** `dump` writes to a file object. `dumps`, with an `s`,
returns a string. The same pattern applies to `load` and `loads`.

```python
conversation = [
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "Paris."},
]

with open(WORK / "conversation.json", "w") as f:
    json.dump(conversation, f, indent=2)

with open(WORK / "conversation.json", "r") as f:
    loaded = json.load(f)

print(loaded[0]["content"])
print("turns saved:", len(loaded))
```

#### Slide 13 &middot; Finding a Config File with pathlib

`pathlib` is another built in module for working with file paths. This pattern
searches a few likely folders for a configuration file.

**AI framing.** This is exactly how AI projects locate API keys stored outside
the code, in a `.env` file.

```python
from pathlib import Path

here = Path.cwd().resolve()
loaded_from = None

for candidate in [
    here / ".env",
    here.parent / ".env",
    here.parent.parent / ".env",
]:
    if candidate.is_file():
        loaded_from = candidate
        break

print("searched from:", here)
print("Would load .env from:", loaded_from)
```

##### Reading a file that ships with this repo

`data/servers.txt` sits one folder up from this notebook, with one server name
per line. Reading a real file is the same code, just a different path.

```python
servers_file = Path("..") / "data" / "servers.txt"

with open(servers_file) as f:
    for line in f:
        print("-", line.strip())
```

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; A run log, one JSON object per line

JSON Lines is the format almost every evaluation and fine tuning run writes. Each line is a complete JSON object, so a file can be appended to forever and read back one record at a time without loading the lot.

```python
import json

log_path = WORK / "runs.jsonl"

runs = [
    {"run": 1, "prompt": "summarise", "tokens": 128, "ok": True},
    {"run": 2, "prompt": "translate", "tokens": 96, "ok": True},
    {"run": 3, "prompt": "classify", "tokens": 64, "ok": False},
]

with open(log_path, "w") as f:
    for record in runs:
        f.write(json.dumps(record) + "\n")

total_tokens = 0
failures = 0

with open(log_path) as f:
    for line in f:
        record = json.loads(line)
        total_tokens += record["tokens"]
        if not record["ok"]:
            failures += 1

print("records    :", len(runs))
print("tokens used:", total_tokens)
print("failures   :", failures)
```

#### Use case 2 &middot; AI &middot; Save a conversation and pick it up later

A chat that survives a restart is a chat saved to disk. Write the history as JSON, read it back, append the next turn, and the assistant carries on where it left off.

```python
import json

chat_path = WORK / "chat.json"

history = [
    {"role": "user", "content": "Hi, I am Serge."},
    {"role": "assistant", "content": "Hello Serge."},
]

with open(chat_path, "w") as f:
    json.dump(history, f, indent=2)

# ... the program stops and starts again here ...

with open(chat_path) as f:
    resumed = json.load(f)

resumed.append({"role": "user", "content": "What is my name?"})
resumed.append({"role": "assistant", "content": "You said you are Serge."})

with open(chat_path, "w") as f:
    json.dump(resumed, f, indent=2)

print("turns after resuming:", len(resumed))
print("last exchange:")
print("  ", resumed[-2]["content"])
print("  ", resumed[-1]["content"])
```

#### Use case 3 &middot; AI &middot; Defaults, overridden by a config file

Start from a dictionary of defaults, read whatever the file supplies, and let the file win. Anything the file leaves out keeps working, which is what makes a config file safe to add to later.

```python
import json

defaults = {"model": "gpt-4o-mini", "temperature": 0.7, "max_tokens": 512}

with open(WORK / "config.json", "w") as f:
    json.dump({"temperature": 0.2}, f)

with open(WORK / "config.json") as f:
    from_file = json.load(f)

settings = dict(defaults)
settings.update(from_file)

print("defaults :", defaults)
print("file says:", from_file)
print("in effect:", settings)
```

#### Use case 4 &middot; Pull the errors out of a log file

Read a file line by line, keep the lines that matter, write those to a second file. This is the shape of most log triage, and it never holds the whole file in memory.

```python
source = WORK / "app.log"
errors_only = WORK / "errors.log"

with open(source, "w") as f:
    f.writelines([
        "2024-08-19 INFO  service started\n",
        "2024-08-19 ERROR database connection refused\n",
        "2024-08-19 INFO  retrying\n",
        "2024-08-19 ERROR database connection refused\n",
        "2024-08-19 INFO  connected\n",
    ])

kept = 0

with open(source) as src, open(errors_only, "w") as dst:
    for line in src:
        if "ERROR" in line:
            dst.write(line)
            kept += 1

print("errors found:", kept)

with open(errors_only) as f:
    print(f.read())
```

#### Practice exercises

1. Write a script that reads a list of server names from a text file, one per line, and prints each one.
2. Save a dictionary of cloud resource tags to a JSON file, then read it back and print one of the tag values.
3. Append a new incident summary line to a running incident log file each time the script runs.
4. Save a short conversation history (a list of role/content dictionaries) to a .json file, then reload it and print the last message.

#### Module complete

You can now read, write and manage files, and work with JSON data confidently.


---

### Module 10: Important Modules

*Import the standard library, set up a virtual environment, and meet openai, langchain, and langgraph.*

Notebook: [`notebooks/10_important_modules.ipynb`](notebooks/10_important_modules.ipynb) &middot; answers: [`solutions/10_important_modules.md`](solutions/10_important_modules.md)

#### Slide 2 &middot; What Is a Module?

A module is a file of pre-written Python code you bring into your own program
with `import`. This is where most of Python's real power comes from: you rarely
have to write something from scratch.

**Standard library vs third party.** `time` ships with Python. Something like
`ollama` does not, so you install it first.

```python
import time            # standard library, comes with Python

# import ollama       # third party, pip install ollama first

print("time module loaded:", time.__name__)
```

#### Slide 3 &middot; Import Patterns

`import` loads a module so its functions and variables become available. There
are a few common styles.

| Pattern | Gives you |
|---|---|
| `import module_name` | `module_name.something` |
| `import module_name as alias` | a shorter name |
| `from module_name import something` | just one piece, directly |

```python
import datetime as dt
from math import sqrt

print(dt.date.today())
print(sqrt(16))
```

#### Slide 4 &middot; Measuring Time

The `time` module is the standard way to measure how long something takes to
run. `time.time()` gives you a number of seconds; take one from another to get
the elapsed time.

```python
import time

t0 = time.time()
time.sleep(0.3)
print(f"Waited {time.time() - t0:.1f}s")
```

#### Slide 5 &middot; Working with the Operating System

The `os` module reads information about the machine your script is running on.

```python
import os

print(os.getcwd())                      # current directory
print(sorted(os.listdir("."))[:10])     # files here
```

#### Slide 6 &middot; Config Values versus Secrets

Config is safe to keep in your code. Secrets, like API keys, should never be
committed to source control. Load them from a `.env` file instead.

```python
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "claude-sonnet-4-6"                    # config, fine to commit
api_key = os.environ.get("ANTHROPIC_API_KEY")  # secret, never commit

print("API key loaded:", bool(api_key))
```

The `.env` file, kept out of version control by `.gitignore`:

```
ANTHROPIC_API_KEY=sk-...
```

**Never print the raw key, even in a demo.** The cell below does the same job
with only the standard library, so it runs without installing anything, and it
prints whether the key exists rather than the key itself.

```python
import os

MODEL = "claude-sonnet-4-6"
api_key = os.environ.get("ANTHROPIC_API_KEY")

print("model:", MODEL)
print("API key loaded:", bool(api_key))
```

#### Slide 7 &middot; API, SDK, and Client, Defined

Three words you will see constantly once you start calling AI models.

- **API** &mdash; the remote interface your program talks to over the network
- **SDK** &mdash; the library you import to talk to that API without writing raw
  HTTP calls, such as `anthropic` or `openai`
- **client** &mdash; the object the SDK gives you to actually make calls, for
  example `client = Anthropic()`

```python
# from anthropic import Anthropic
# client = Anthropic()
# r = client.messages.create(model=..., messages=...)
```

#### Slide 8 &middot; Setting Up a Virtual Environment

The packages coming up do not ship with Python. Before installing anything,
isolate this project's packages from the rest of your system.

**One environment per project.** This keeps one project's packages from
colliding with another's, and lets you delete `.venv` and start clean any time.

```bash
uv venv                        # creates .venv here

source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows

uv pip install openai langchain langgraph

deactivate                     # leave when you are done
```

If you followed this repo's README, you already did exactly this to get the
notebook running. The `README.md` has the full walkthrough including how to
point Jupyter at the environment.

#### Slide 9 &middot; Popular AI Packages: openai

The official SDK for calling OpenAI's models. A client object handles the
network request, and you read the reply off the response object.

Installed inside your venv with `uv pip install openai`.

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello."}],
)
print(response.choices[0].message.content)
```

#### Slide 10 &middot; Popular AI Packages: langchain

LangChain wraps different model providers behind a common interface, so the
same code can call OpenAI, Anthropic or others with only the client changed.

**Same shape, different provider.** Swap `ChatOpenAI` for a different
provider's class and the rest of the code barely changes.

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke([HumanMessage(content="Say hello.")])
print(response.content)
```

#### Slide 11 &middot; Popular AI Packages: langgraph

LangGraph structures an AI program as a graph of steps, called **nodes**,
connected by **edges**. Each node is a plain Python function.

**State flows through the graph.** Each node receives the current state and
returns an update to it, one step at a time.

```python
from langgraph.graph import StateGraph, END

def greet_node(state):
    return {"message": f"Hello, {state['name']}!"}

graph = StateGraph(dict)
graph.add_node("greet", greet_node)
graph.set_entry_point("greet")
graph.add_edge("greet", END)

app = graph.compile()
result = app.invoke({"name": "Alice"})
print(result["message"])       # Hello, Alice!
```

The cell below is that same graph with nothing but the standard library. The
point is the shape: a node is a function, and state flows through it.

```python
def greet_node(state):
    return {"message": f"Hello, {state['name']}!"}


def run_graph(nodes, state):
    for node in nodes:
        state.update(node(state))
    return state


result = run_graph([greet_node], {"name": "Alice"})
print(result["message"])
```

#### Slide 12 &middot; LangChain Agents vs LangGraph

Both can build an **agent**, a program that decides what to do rather than
always running fixed steps. They hand you different amounts of control.

**LangChain agents.** Faster to set up for a standard tool-calling loop. Hand
it a model and tools, and it repeats until done.

**LangGraph.** More code to wire up, but you see and control every step. Add
cycles, or pause for human approval.

**No wrong choice.** Reach for LangChain's agent tools for a quick, standard
loop. Reach for LangGraph when you need to see and control the steps yourself.
Complex or multi-agent workflows tend to move toward LangGraph as they grow.

#### Slide 13 &middot; A LangChain Agent in Practice

This is the newer, tool-calling style of LangChain agent: hand it a model, a
list of tools and a prompt.

**`@tool` marks a function** as something the model is allowed to call. The
docstring tells the model what the tool does.

```python
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

@tool
def get_weather(city: str) -> str:
    """Look up the weather for a city."""
    return f"It is sunny in {city}."

agent = create_tool_calling_agent(llm, [get_weather], prompt)
executor = AgentExecutor(agent=agent, tools=[get_weather])
result = executor.invoke({"input": "Weather in Boston?"})
print(result["output"])
```

#### Slide 14 &middot; Building a Tiny Agent with LangGraph

A small agent, built with the same `StateGraph` pattern, that answers weather
questions and declines anything else.

**This is what every agent does.** Read the state, decide what to do, return an
update. The `if` / `else` here stands in for a model deciding which tool to
call.

```python
def get_weather(city):
    # pretend this calls a real weather API
    return f"It is sunny in {city}."


def agent_node(state):
    question = state["question"]
    if "weather" in question.lower():
        answer = get_weather("Boston")
    else:
        answer = "I can only answer weather questions."
    return {"answer": answer}


print(agent_node({"question": "What is the weather like?"})["answer"])
print(agent_node({"question": "Who won the game?"})["answer"])
```

#### Slide 15 &middot; Other Useful Modules

A quick map of what else is out there, for when you need it.

- **subprocess** &mdash; running shell commands from inside Python
- **requests** &mdash; making HTTP calls to APIs
- **Docker and Kubernetes** &mdash; container and orchestration helper patterns
- **boto3 and Terraform** &mdash; cloud and infrastructure as code
- **Git automation** &mdash; CI/CD pipeline integration

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; Read your whole config in one block

Every setting comes from the environment with a fallback, so the same code runs on a laptop with nothing set and in production with everything set. The key is reported as present or absent and never printed.

```python
import os

config = {
    "model": os.environ.get("LAB_MODEL", "gpt-4o-mini"),
    "temperature": float(os.environ.get("LAB_TEMPERATURE", "0.7")),
    "max_tokens": int(os.environ.get("LAB_MAX_TOKENS", "512")),
    "region": os.environ.get("AWS_REGION", "us-east-1"),
}

for key, value in config.items():
    print(f"  {key:12s} {value}  {type(value).__name__}")

print()
print("API key set:", bool(os.environ.get("LAB_API_KEY")))
```

#### Use case 2 &middot; AI &middot; What did this run cost, and how long did it take?

time measures the wall clock, the token counts give you the money. Printing both at the end of a run is how you notice that the clever prompt is also the expensive one.

```python
import time

start = time.time()

# stands in for three model calls
time.sleep(0.3)

input_tokens = 4_200
output_tokens = 850
elapsed = time.time() - start

cost = (input_tokens / 1_000_000) * 3.00 + (output_tokens / 1_000_000) * 15.00

print("=== run summary ===")
print("input tokens :", input_tokens)
print("output tokens:", output_tokens)
print(f"wall clock   : {elapsed:.2f}s")
print(f"cost         : ${cost:.4f}")
print(f"cost per 1000 runs: ${cost * 1000:.2f}")
```

#### Use case 3 &middot; AI &middot; Summarise a set of latencies

statistics ships with Python and saves you writing the maths by hand. The median barely moves when one request is slow and the mean does not survive it, which is why dashboards show the median.

```python
import statistics

latencies_ms = [45, 52, 38, 512, 47, 41, 60, 44]

print("count  :", len(latencies_ms))
print("mean   :", round(statistics.mean(latencies_ms), 1))
print("median :", statistics.median(latencies_ms))
print("slowest:", max(latencies_ms))
print("fastest:", min(latencies_ms))
```

#### Use case 4 &middot; A timestamped artefact name

Anything a job writes needs a name that will not collide with the next run. strftime controls the format so the names sort correctly when listed.

```python
import datetime as dt

now = dt.datetime(2026, 8, 19, 14, 30, 5)      # fixed so the output is stable

stamp = now.strftime("%Y%m%d-%H%M%S")
report = f"eval-run-{stamp}.jsonl"

print("stamp :", stamp)
print("report:", report)
print("today would be:", dt.date.today())
```

#### Practice exercises

1. Use the os module to list every file in the current deployment directory.
2. Use dotenv to load a cloud provider's API key from a .env file, printing only whether it loaded, never the key itself.
3. Use the time module to measure how long a fake health check function takes to run.
4. Extend the tiny agent above with a second condition, so it also answers a simple math question like "what is 2 plus 2".

#### Module complete

You can now import modules, manage secrets, and build with real AI packages. Exercise 2 needs `python-dotenv`, which is in `requirements-ai.txt`.


---

### Module 11: Classes, Type Hints, Pydantic, Decorators and Async

*The tools that round out your Python toolkit for AI engineering work.*

Notebook: [`notebooks/11_advanced_python.ipynb`](notebooks/11_advanced_python.ipynb) &middot; answers: [`solutions/11_advanced_python.md`](solutions/11_advanced_python.md)

##### Before you start: check Pydantic is available

If this cell fails, your environment is missing Pydantic. Install it with
`uv pip install -r requirements.txt`, then restart the kernel.

```python
import pydantic

print("pydantic", pydantic.VERSION)
```

#### Section 1 &middot; Classes and objects

A class is a blueprint for a data type that bundles values and behaviour
together. `__init__` sets up what a new object starts with, and `self` refers
to the specific object being worked on.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"


b = Book("Dune", "Frank Herbert")
print(b.describe())
```

Wrapping a model API in a class keeps its configuration and its conversation
history bundled together, instead of scattered across separate variables.

```python
class ChatClient:
    def __init__(self, model):
        self.model = model
        self.history = []

    def ask(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = f"[{self.model}] reply to: {user_message}"
        self.history.append({"role": "assistant", "content": reply})
        return reply


client = ChatClient("claude-sonnet-4-6")
print(client.ask("Hi, I am Serge."))
print(client.ask("What did I just say?"))
print("history length:", len(client.history))
```

##### Reading dotted objects

Now that you know a class holds attributes on `self`, you can read SDK output
the same way: an object, then an attribute, then maybe a list index, then
another attribute. Real SDK responses look exactly like this.

```python
class FakeDelta:
    def __init__(self, content):
        self.content = content


class FakeChoice:
    def __init__(self, content):
        self.delta = FakeDelta(content)


class FakeChunk:
    def __init__(self, content):
        self.choices = [FakeChoice(content)]


chunk = FakeChunk("Hello Serge!")
print(chunk.choices[0].delta.content)

# A real Anthropic response follows the same shape:  r.content[0].text
```

#### Section 2 &middot; Type hints and dataclasses

A type hint is a note saying what type a variable or function expects. Python
does not enforce it by itself, but your editor and several AI libraries read it
and catch mistakes early.

A **dataclass** uses type hints to define the exact shape of structured data
without writing a full class by hand. This is how function-calling schemas are
described in code.

```python
from dataclasses import dataclass


def add(a: int, b: int) -> int:
    return a + b


print(add(2, 3))


@dataclass
class Message:
    role: str
    content: str


@dataclass
class WeatherLookup:
    city: str
    unit: str = "celsius"


print(Message(role="user", content="Hi there"))
print(WeatherLookup(city="Boston"))
print("a dataclass will NOT stop this:", Message(role=123, content=None))
```

#### Section 3 &middot; Pydantic models

A dataclass describes a shape but will not stop you putting the wrong type in a
field, as the last line above showed. **Pydantic** does the same job and
validates every field automatically, raising a clear error the moment something
does not match.

This is the standard way to describe a structured response you expect back from
an AI model: instead of trusting that the model's JSON is shaped correctly, you
validate it on the way in.

```python
from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    name: str
    age: int


p = Person(name="Alice", age=25)
print(p.name, p.age)


class MovieRecommendation(BaseModel):
    title: str
    year: int
    reason: str


raw_response = '{"title": "Arrival", "year": 2016, "reason": "Language and time."}'

recommendation = MovieRecommendation.model_validate_json(raw_response)
print(recommendation.title, recommendation.year)
```

```python
bad_response = '{"title": "Arrival", "year": "not-a-year", "reason": "..."}'

try:
    MovieRecommendation.model_validate_json(bad_response)
except ValidationError as e:
    print("The model returned something unexpected:")
    print(e)
```

#### Section 4 &middot; Decorators

A decorator is a function that wraps another function to add behaviour, without
changing the code inside that function. It is written as an `@` placed directly
above a `def` line. It builds on Module 8's idea that a function is just a
value you can pass around.

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper


@announce
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))
```

```python
import time


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper


@timed
def call_model(prompt):
    time.sleep(0.3)          # pretend this is a network call
    return f"response to: {prompt}"


print(call_model("Summarize this document."))
```

#### Section 5 &middot; Async and await

Everything so far has been **synchronous**: Python runs one line, waits for it
to finish, then moves to the next. Asynchronous code, written with `async` and
`await`, lets a program start a slow task such as a network call and work on
something else while it waits, instead of sitting idle.

```python
import asyncio


async def greet():
    print("Starting...")
    await asyncio.sleep(0.5)      # pretend this is waiting on a network call
    print("Done!")


await greet()          # in a script this line would be: asyncio.run(greet())
```

The real payoff shows up when you need several slow calls at once.
`asyncio.gather` runs them together instead of one after another. Watch the
elapsed time: three half-second calls finish in about half a second, not one
and a half.

```python
import asyncio
import time


async def call_model(prompt):
    await asyncio.sleep(0.5)      # simulates network latency
    return f"response to: {prompt}"


async def main():
    prompts = ["Summarize A", "Summarize B", "Summarize C"]
    return await asyncio.gather(*(call_model(p) for p in prompts))


start = time.time()
results = await main()
elapsed = time.time() - start

for r in results:
    print(r)

print(f"\nthree calls finished in {elapsed:.2f}s, not {3 * 0.5:.2f}s")
```

> `async def` and a generator with `yield` both pause and resume, but for
> different reasons. A generator pauses to hand back the next value in a
> sequence. An async function pauses to let something else run while it waits
> on a slow task. `await` is only valid inside a function defined with
> `async def`.

---

### More use cases

The same ideas, applied to situations you will meet in real work. Run each one, then change a value and run it again.

#### Use case 1 &middot; AI &middot; dataclass and Pydantic, same bad input

Both describe the same shape. Only one of them checks. Run this once and the reason AI SDKs standardised on Pydantic for structured output stops needing an explanation.

```python
from dataclasses import dataclass
from pydantic import BaseModel, ValidationError


@dataclass
class PlainTurn:
    role: str
    content: str


class CheckedTurn(BaseModel):
    role: str
    content: str


bad = PlainTurn(role=123, content=None)
print("dataclass accepted it:", bad)

try:
    CheckedTurn(role=123, content=None)
except ValidationError as e:
    first = e.errors()[0]
    print()
    print("pydantic refused it:", first["msg"], "on field", first["loc"])
```

#### Use case 2 &middot; AI &middot; Validate what the model sent back

Asking a model for JSON does not guarantee JSON of the right shape. Validating on the way in means a malformed answer fails at your boundary with a clear message, rather than three functions later.

```python
from pydantic import BaseModel, ValidationError


class Triage(BaseModel):
    severity: int
    service: str
    summary: str


good = '{"severity": 2, "service": "api-gateway", "summary": "502s from two targets"}'
bad = '{"severity": "high", "service": "api-gateway", "summary": "502s"}'

result = Triage.model_validate_json(good)
print("parsed:", result.service, "severity", result.severity)
print("type of severity:", type(result.severity))

try:
    Triage.model_validate_json(bad)
except ValidationError as e:
    print()
    print("the model returned severity as text, which is not usable:")
    print(" ", e.errors()[0]["msg"])
```

#### Use case 3 &middot; AI &middot; A decorator that retries

The retry logic from Module 7, moved into a decorator. The function it wraps knows nothing about retrying, so you add or remove the behaviour by changing one line above the def.

```python
def retry(attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:
                    print(f"  attempt {attempt} failed: {e}")
            raise RuntimeError(f"{func.__name__} failed after {attempts} attempts")
        return wrapper
    return decorator


calls = {"n": 0}


@retry(attempts=4)
def fetch_metrics():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("connection reset")
    return "metrics retrieved"


print(fetch_metrics())
print("it took", calls["n"], "calls")
```

#### Use case 4 &middot; AI &middot; Fan out calls of different lengths

Run three things at once and the total is the slowest one, not the sum. This is the whole argument for async in an AI application, where almost all the time is spent waiting on somebody else's server.

```python
import asyncio
import time


async def call(name, seconds):
    await asyncio.sleep(seconds)
    return f"{name} took {seconds}s"


start = time.time()

results = await asyncio.gather(
    call("summarise", 0.5),
    call("translate", 0.2),
    call("classify", 0.3),
)

elapsed = time.time() - start

for r in results:
    print(r)

print()
print("one after another would be 1.00s")
print(f"all at once took {elapsed:.2f}s, the slowest one")
```

#### Practice exercises

1. Write a class that represents a Deployment with a status attribute and a method that marks it complete.
2. Write a Pydantic model that validates a cloud resource request with a name, a region, and a size.
3. Write a decorator that logs how long any function takes, and use it on a fake run_healthcheck function.
4. Write an async function that calls three model prompts concurrently using asyncio.gather, and print all three results.

#### Module complete

That is the whole course. You can now read and write Python confidently enough to work with real AI SDKs.


---

Utrains &middot; support@utrains.org &middot; <https://utrains.org>
