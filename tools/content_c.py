"""Modules 9 to 11: files and JSON, important modules, advanced Python."""

from nbcore import header, md, code, todo, turn, lab, practice

# ---------------------------------------------------------------- Module 9

M9 = [
    header(
        9,
        "File Handling",
        [
            "Open a file in the right mode for what you are about to do",
            "Prefer with open(...) so files always get closed",
            "Read and write JSON, the format every API speaks",
            "Locate a config file on disk with pathlib",
        ],
        "Part 5 of the course: Working with the Outside World.",
    ),
    md(
        """
File handling lets your program read and write data outside of memory, so it
survives after the script finishes running.

## Setting up a scratch folder

Everything in this notebook writes into a `scratch/` folder next to it, so
nothing else on your machine is touched. Run this cell first.
"""
    ),
    code(
        """
from pathlib import Path

WORK = Path("scratch")
WORK.mkdir(exist_ok=True)

print("writing files into:", WORK.resolve())
"""
    ),
    md(
        """
## File modes

You choose a mode when you open a file, which controls what you may do with it.

- `"r"` read, and the default
- `"w"` write, and **overwrites** anything already there
- `"a"` append, adding to the end
- `"x"` create, and fails if the file already exists
- `"rb"` and `"wb"` the same as r and w, but for binary data such as images

## Opening, writing and reading

The long form uses `open()` and `close()` as a pair.
"""
    ),
    code(
        """
file = open(WORK / "sample.txt", "w")
file.write("Hello, this is a test file.")
file.close()

file = open(WORK / "sample.txt", "r")
content = file.read()
print(content)
file.close()
"""
    ),
    md(
        """
## The with statement

Opening a file with `with` closes it for you automatically, even if an error
happens partway through. This is the pattern you should reach for by default.

> If you forget to close a file it can stay locked or lose unsaved data. `with`
> removes that risk entirely.
"""
    ),
    code(
        """
with open(WORK / "output.txt", "w") as file:
    file.writelines(["Line 1\\n", "Line 2\\n", "Line 3\\n"])

with open(WORK / "output.txt", "a") as file:
    file.write("This line will be appended.\\n")

with open(WORK / "output.txt", "r") as file:
    print(file.read())

# Reading one line at a time, or all lines into a list.
with open(WORK / "output.txt") as file:
    print("first line:", repr(file.readline()))

with open(WORK / "output.txt") as file:
    print("as a list :", file.readlines())
"""
    ),
    md(
        """
## Reading a file that ships with the repo

`data/servers.txt` sits alongside this notebook's folder. Reading a real file
from disk is the same code, just a different path.
"""
    ),
    code(
        """
servers_file = Path("..") / "data" / "servers.txt"

with open(servers_file) as f:
    for line in f:
        print("-", line.strip())
"""
    ),
    turn(
        1,
        "Append a new incident summary to a running log file, then read the "
        "whole log back. Pick the mode that adds without wiping the file.",
    ),
    todo(
        """
log_path = WORK / "incidents.log"

# TODO: choose the mode that ADDS to the end rather than overwriting.
with open(log_path, ____) as f:
    f.write("INC-4412 database connection failures resolved\\n")

with open(log_path, ____) as f:
    print(f.read())
""",
        """
log_path = WORK / "incidents.log"

with open(log_path, "a") as f:
    f.write("INC-4412 database connection failures resolved\\n")

with open(log_path, "r") as f:
    print(f.read())
""",
    ),
    md(
        """
Run that cell two or three times. The log grows each time, which is exactly
what append mode is for. Change the mode to `"w"` and run it again to watch the
earlier lines disappear.

## Checking and deleting files

Checking whether a file exists and deleting one both live in the `os` module,
which ships with Python.
"""
    ),
    code(
        """
import os

target = WORK / "sample.txt"

if os.path.exists(target):
    print("File exists")
    os.remove(target)
    print("and now it does not:", os.path.exists(target))
else:
    print("File not found")
"""
    ),
    md(
        """
## Working with JSON

JSON is a text format almost every API uses. It maps directly onto a Python
dictionary. `json.dumps` turns a Python object into a JSON **string**, and
`json.loads` turns a JSON string back into a Python object. The `s` stands for
string; without it, `json.dump` and `json.load` work on **files** instead.
"""
    ),
    code(
        """
import json

person = {"name": "Alice", "age": 25}

as_text = json.dumps(person)
print(as_text, type(as_text))

back_to_dict = json.loads(as_text)
print(back_to_dict["name"], type(back_to_dict))
"""
    ),
    md(
        """
A real model API response arrives as JSON text over the network. Parsing it is
the same skill applied to something you did not write yourself.
"""
    ),
    code(
        """
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
"""
    ),
    code(
        """
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
"""
    ),
    turn(
        2,
        "Save a dictionary of resource tags to a JSON file and read one value "
        "back. Note carefully which of the four json functions each step needs.",
    ),
    todo(
        """
tags = {"env": "prod", "owner": "platform-team", "cost-center": "CC-1180"}

# TODO: write to a FILE, then read from a FILE. Mind the s.
with open(WORK / "tags.json", "w") as f:
    json.____(tags, f, indent=2)

with open(WORK / "tags.json", "r") as f:
    restored = json.____(f)

print(restored["owner"])
""",
        """
tags = {"env": "prod", "owner": "platform-team", "cost-center": "CC-1180"}

with open(WORK / "tags.json", "w") as f:
    json.dump(tags, f, indent=2)

with open(WORK / "tags.json", "r") as f:
    restored = json.load(f)

print(restored["owner"])
""",
    ),
    md(
        """
## Finding a .env file with pathlib

`pathlib` is another built in module, this time for working with paths. This
pattern searches a few likely folders for a config file, which is exactly how
AI projects locate API keys stored outside the code.
"""
    ),
    code(
        """
from pathlib import Path

here = Path.cwd().resolve()
loaded_from = None

for candidate in [here / ".env", here.parent / ".env", here.parent.parent / ".env"]:
    if candidate.is_file():
        loaded_from = candidate
        break

print("searched from:", here)
print("would load .env from:", loaded_from)
"""
    ),
    lab(
        "A server inventory round trip",
        """
Read `../data/servers.txt`, which holds one server name per line.

Turn it into a list of dictionaries, where each entry has a `name`, a `region`
derived from the part of the name after the last hyphen, and a `status` of
`"unknown"`.

Save that list to `scratch/inventory.json` with an indent of 2, then read it
back from disk into a fresh variable and print how many servers you recovered
and the name of the last one.

Finish by appending a single audit line to `scratch/audit.log` recording how
many servers were processed. Run the whole lab twice and confirm the audit log
has two lines while the inventory JSON still has the right count.
""",
        [
            "The text file is read with a with statement, not open/close",
            "Each line becomes a dictionary in a list",
            "json.dump writes the file and json.load reads it back",
            "The audit log uses append mode and grows on a second run",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Write a script that reads a list of server names from a text file, one per line, and prints each one.",
            "Save a dictionary of cloud resource tags to a JSON file, then read it back and print one of the tag values.",
            "Append a new incident summary line to a running incident log file each time the script runs.",
            "Save a short conversation history (a list of role/content dictionaries) to a .json file, then reload it and print the last message.",
        ]
    ),
]

# --------------------------------------------------------------- Module 10

M10 = [
    header(
        10,
        "Important Modules",
        [
            "Import a module three different ways and know when to use each",
            "Use time, os, datetime and math from the standard library",
            "Separate config from secrets, and keep API keys out of your code",
            "Recognise what openai, langchain and langgraph each do",
        ],
        "Part 5 of the course: Working with the Outside World.",
    ),
    md(
        """
A module is a file of pre-written Python code that you bring into your own
program with `import`. This is where most of Python's real power comes from:
you rarely have to write something from scratch.

## What import actually does

`import` loads a module so its functions and variables become available in your
file. Without importing it first, Python has no idea the name exists.

Three patterns:

- `import module_name` gives you `module_name.something`
- `import module_name as alias` lets you use a shorter name
- `from module_name import something` brings in just one name directly
"""
    ),
    code(
        """
import datetime as dt
from math import sqrt

print(dt.date.today())
print(sqrt(16))
"""
    ),
    md("## Measuring time"),
    code(
        """
import time

t0 = time.time()
time.sleep(0.3)
print(f"Waited {time.time() - t0:.1f}s")
"""
    ),
    md("## Working with the operating system"),
    code(
        """
import os

print("current directory:", os.getcwd())
print("files here:", sorted(os.listdir("."))[:10])
"""
    ),
    turn(
        1,
        "Measure how long a fake health check takes, and print the answer to "
        "two decimal places. Two blanks: the import and the timing call.",
    ),
    todo(
        """
# TODO: bring in the module that can pause and measure, then use it twice.
____ time


def run_healthcheck():
    time.sleep(0.25)
    return "healthy"


start = time.____()
status = run_healthcheck()
elapsed = time.____() - start

print(f"health check returned {status} in {elapsed:.2f}s")
""",
        """
import time


def run_healthcheck():
    time.sleep(0.25)
    return "healthy"


start = time.time()
status = run_healthcheck()
elapsed = time.time() - start

print(f"health check returned {status} in {elapsed:.2f}s")
""",
    ),
    md(
        """
## Config values versus secrets

**Config** is safe to keep in your code, such as which model to use. **Secrets**
such as API keys should never be committed to source control. Keep them in a
`.env` file and load them with `dotenv`.

```python
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "claude-sonnet-4-6"                      # config, fine to commit
api_key = os.environ.get("ANTHROPIC_API_KEY")    # secret, never commit

print("API key loaded:", bool(api_key))          # never print the raw key
```

The `.env` file itself, kept out of version control by `.gitignore`:

```
ANTHROPIC_API_KEY=sk-...
```

The cell below does the same job using only the standard library, so it runs
here without installing anything. Notice it prints whether the key exists, and
never the key itself.
"""
    ),
    code(
        """
import os

MODEL = "claude-sonnet-4-6"
api_key = os.environ.get("ANTHROPIC_API_KEY")

print("model:", MODEL)
print("API key loaded:", bool(api_key))
"""
    ),
    md(
        """
## Setting up a virtual environment

Everything so far has needed only the standard library, which ships with
Python. The packages below do not.

A virtual environment is a folder holding its own copy of installed packages,
separate from everything else on your machine. Without one, every project
shares the same packages, and installing one project's dependencies can quietly
break another's.

```bash
uv venv                        # creates a .venv folder here

source .venv/bin/activate      # Linux / macOS
.venv\\Scripts\\activate         # Windows

uv pip install openai langchain langgraph

deactivate                     # leave when you are done
```

> Create a fresh virtual environment per project. You can delete the `.venv`
> folder and start clean without touching anything else on your machine.

## API, SDK and client, defined

- **API** the remote interface your program talks to over the network
- **SDK** the official library you import so you do not write raw HTTP calls,
  such as `anthropic` or `openai`
- **client** the object the SDK gives you to make calls, such as
  `client = Anthropic()`

## The three packages you will meet

These need network access and an API key, so they are shown here as reference
rather than run. The cell after them simulates the same shapes with plain
Python, so you can see the structure without a key.

**openai** &mdash; the official SDK for OpenAI models:

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
print(response.choices[0].message.content)
```

**langchain** &mdash; wraps different providers behind one interface:

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke([HumanMessage(content="Say hello in one sentence.")])
print(response.content)
```

**langgraph** &mdash; structures a program as a graph of steps called nodes,
connected by edges. Each node is a plain function that receives the current
state and returns an update to it:

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
print(result["message"])
```
"""
    ),
    code(
        """
# A stand-in for the graph above, using nothing but the standard library.
# The point is the shape: a node is a function, state flows through it.

def greet_node(state):
    return {"message": f"Hello, {state['name']}!"}


def run_graph(nodes, state):
    for node in nodes:
        state.update(node(state))
    return state


result = run_graph([greet_node], {"name": "Alice"})
print(result["message"])
"""
    ),
    md(
        """
## LangChain agents compared with LangGraph

Both can build an **agent**, an AI program that decides what to do rather than
always running the same fixed steps. They hand you different amounts of
control.

LangChain's agent tools give you a ready made loop: hand it a model and a list
of tools and it repeatedly asks the model what to do next until it decides it
is done. Faster to set up for a standard pattern.

LangGraph gives you the loop itself instead of hiding it. You define the nodes,
the edges and the state, which means you control exactly when to loop, branch,
pause for a human, or stop. More code to wire up, but every step is visible.

Complex or multi-agent workflows tend to move toward LangGraph as they grow,
since a single hidden loop stops being enough control.

> There is no wrong choice. Reach for LangChain's agent tools for a quick
> standard tool-calling loop. Reach for LangGraph when you need to see and
> control the steps yourself.

## A tiny agent

Underneath, every agent does the same three things: read the state, decide what
to do, and return an update. The `if` below stands in for a model deciding
which tool to call.
"""
    ),
    code(
        """
def get_weather(city):
    # pretend this calls a real weather API
    return f"It is sunny in {city}."


def agent_node(state):
    question = state["question"]
    if "weather" in question.lower():
        answer = get_weather("Boston")
    else:
        answer = "I can only answer weather questions right now."
    return {"answer": answer}


print(agent_node({"question": "What is the weather like?"})["answer"])
print(agent_node({"question": "Who won the game?"})["answer"])
"""
    ),
    turn(
        2,
        "Extend the tiny agent with a second condition so it can also answer "
        "a simple addition question, and fall through to the refusal otherwise.",
    ),
    todo(
        """
def agent_node(state):
    question = state["question"].lower()

    if "weather" in question:
        answer = get_weather("Boston")
    # TODO: add a branch that catches a maths question and answers it.
    ____ "plus" ____ question:
        answer = "That is 4."
    ____:
        answer = "I can only answer weather or simple maths right now."

    return {"answer": answer}


for q in ["What is the weather like?", "what is 2 plus 2", "Who won the game?"]:
    print(q, "->", agent_node({"question": q})["answer"])
""",
        """
def agent_node(state):
    question = state["question"].lower()

    if "weather" in question:
        answer = get_weather("Boston")
    elif "plus" in question:
        answer = "That is 4."
    else:
        answer = "I can only answer weather or simple maths right now."

    return {"answer": answer}


for q in ["What is the weather like?", "what is 2 plus 2", "Who won the game?"]:
    print(q, "->", agent_node({"question": q})["answer"])
""",
    ),
    lab(
        "A timed, config-driven health reporter",
        """
Write a small script inside this notebook that does four things.

Read a model name from an environment variable called `LAB_MODEL`, falling back
to `"gpt-4o-mini"` when it is not set. Print the model, and separately print
whether an API key called `LAB_API_KEY` is present, without ever printing its
value.

Use `os.listdir` to count how many files sit in the current folder.

Time a fake `run_healthcheck()` function that sleeps for a fraction of a second
and returns a status, and print the elapsed time to two decimal places.

Stamp the report with today's date using `datetime`.

Print all of it as one tidy report block.
""",
        [
            "The model comes from the environment with a fallback",
            "The key is reported as present or absent, never printed",
            "os is used to count files in the folder",
            "time measures the health check, datetime stamps the report",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Use the os module to list every file in the current deployment directory.",
            "Use dotenv to load a cloud provider's API key from a .env file, printing only whether it loaded, never the key itself.",
            "Use the time module to measure how long a fake health check function takes to run.",
            "Extend the tiny agent above with a second condition, so it also answers a simple math question like \"what is 2 plus 2\".",
        ]
    ),
]

# --------------------------------------------------------------- Module 11

M11 = [
    header(
        11,
        "Classes, Type Hints, Pydantic, Decorators and Async",
        [
            "Bundle data and behaviour together in a class, and read dotted SDK output",
            "Describe a shape with type hints and a dataclass",
            "Validate untrusted data with a Pydantic model",
            "Wrap a function with a decorator, and run slow calls concurrently with async",
        ],
        "Part 6 of the course: Advanced Python for AI Engineering.",
    ),
    md(
        """
This module covers the tools that round out your Python toolkit. Each section
starts with the basic shape, then a slightly bigger example.

## Classes and objects

A class is a blueprint for a data type that bundles values and behaviour
together. `__init__` sets up what a new object starts with, and `self` refers
to the specific object being worked on.
"""
    ),
    code(
        """
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"


b = Book("Dune", "Frank Herbert")
print(b.describe())
"""
    ),
    md(
        """
Wrapping a model API in a class keeps its configuration and its conversation
history bundled together, instead of scattered across separate variables.
"""
    ),
    code(
        """
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
"""
    ),
    md(
        """
### Reading dotted objects

Now that you know a class holds attributes on `self`, you can read SDK output
the same way: an object, then an attribute, then maybe a list index, then
another attribute. Real SDK responses look exactly like this.
"""
    ),
    code(
        """
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
"""
    ),
    turn(
        1,
        "Write a Deployment class that starts as pending and can be marked "
        "complete. Fill in the constructor and the method.",
    ),
    todo(
        """
class Deployment:
    # TODO: name the constructor, and store the two values on the object.
    def ____(self, service):
        ____.service = service
        ____.status = "pending"

    def complete(self):
        # TODO: change this object's own status.
        ____.status = "done"


d = Deployment("api-gateway")
print(d.service, "->", d.status)
d.complete()
print(d.service, "->", d.status)
""",
        """
class Deployment:
    def __init__(self, service):
        self.service = service
        self.status = "pending"

    def complete(self):
        self.status = "done"


d = Deployment("api-gateway")
print(d.service, "->", d.status)
d.complete()
print(d.service, "->", d.status)
""",
    ),
    md(
        """
## Type hints and dataclasses

A type hint is a note saying what type a variable or function expects. Python
does not enforce it by itself, but your editor and several AI libraries read it
and catch mistakes early.

A **dataclass** uses type hints to define the exact shape of structured data
without writing a full class by hand. This is how function-calling schemas are
described in code.
"""
    ),
    code(
        """
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


m = Message(role="user", content="Hi there")
call = WeatherLookup(city="Boston")

print(m)
print(call)
print("a dataclass will NOT stop this:", Message(role=123, content=None))
"""
    ),
    md(
        """
## Pydantic models

A dataclass describes a shape but will not stop you putting the wrong type in a
field, as the last line above showed. **Pydantic** does the same job and
validates every field automatically, raising a clear error the moment something
does not match.

This is the standard way to describe a structured response you expect back from
an AI model: instead of trusting that the model's JSON is shaped correctly, you
validate it on the way in.
"""
    ),
    code(
        """
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
"""
    ),
    code(
        """
bad_response = '{"title": "Arrival", "year": "not-a-year", "reason": "..."}'

try:
    MovieRecommendation.model_validate_json(bad_response)
except ValidationError as e:
    print("The model returned something unexpected:")
    print(e)
"""
    ),
    md(
        """
## Decorators

A decorator is a function that wraps another function to add behaviour, without
changing the code inside that function. It is written as an `@` placed directly
above a `def` line.
"""
    ),
    code(
        """
def announce(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper


@announce
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))
"""
    ),
    code(
        """
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
"""
    ),
    md(
        """
## Async and await

Everything so far has been **synchronous**: Python runs one line, waits for it
to finish, then moves to the next. Asynchronous code, written with `async` and
`await`, lets a program start a slow task such as a network call and work on
something else while it waits, instead of sitting idle.

> **In a script** you start the whole thing with `asyncio.run(main())`.
> **In a notebook** there is already an event loop running, so `asyncio.run()`
> raises an error. Use a bare `await main()` instead, as the cells below do.
"""
    ),
    code(
        """
import asyncio


async def greet():
    print("Starting...")
    await asyncio.sleep(0.5)      # pretend this is waiting on a network call
    print("Done!")


await greet()          # in a script this line would be: asyncio.run(greet())
"""
    ),
    md(
        """
The real payoff shows up when you need several slow calls at once.
`asyncio.gather` runs them together instead of one after another. Watch the
elapsed time: three half-second calls finish in about half a second, not one
and a half.
"""
    ),
    code(
        """
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

print(f"\\nthree calls finished in {elapsed:.2f}s, not {3 * 0.5:.2f}s")
"""
    ),
    md(
        """
> `async def` and a generator with `yield` both pause and resume, but for
> different reasons. A generator pauses to hand back the next value in a
> sequence. An async function pauses to let something else run while it waits
> on a slow task. `await` is only valid inside a function defined with
> `async def`.
"""
    ),
    turn(
        2,
        "Validate a cloud resource request with Pydantic, then run three fake "
        "model calls at the same time.",
    ),
    todo(
        """
from pydantic import BaseModel
import asyncio


# TODO: inherit from the Pydantic base class, and give each field a type.
class ResourceRequest(____):
    name: ____
    region: ____
    size: ____


req = ResourceRequest(name="web-01", region="us-east-1", size=2)
print(req)


async def fake_call(n):
    await asyncio.sleep(0.2)
    return f"call {n} done"


# TODO: which asyncio function runs them all together?
results = await asyncio.____(fake_call(1), fake_call(2), fake_call(3))
print(results)
""",
        """
from pydantic import BaseModel
import asyncio


class ResourceRequest(BaseModel):
    name: str
    region: str
    size: int


req = ResourceRequest(name="web-01", region="us-east-1", size=2)
print(req)


async def fake_call(n):
    await asyncio.sleep(0.2)
    return f"call {n} done"


results = await asyncio.gather(fake_call(1), fake_call(2), fake_call(3))
print(results)
""",
    ),
    lab(
        "A validated, timed, async chat client",
        """
Put the whole module together.

Define a Pydantic model `ChatTurn` with a `role` and a `content`, both strings.
Prove it rejects a turn where `role` is a number.

Write a `ChatClient` class that holds a model name and a list of `ChatTurn`
objects. Give it an `async def ask(self, message)` method that sleeps for a
fraction of a second to simulate the network, appends both the user turn and
the assistant reply to its history, and returns the reply.

Decorate a `report()` method with a `@timed` decorator you write yourself, so
printing the history also prints how long it took.

Finally, use `asyncio.gather` to ask three questions concurrently, then print
the full history and confirm it holds six turns.
""",
        [
            "ChatTurn is a Pydantic model and rejects a bad role",
            "ask() is an async method and is awaited",
            "A hand-written @timed decorator wraps report()",
            "asyncio.gather runs the three questions together",
            "The final history has six turns",
        ],
    ),
    code(
        """
# Your lab answer goes here.
"""
    ),
    practice(
        [
            "Write a class that represents a Deployment with a status attribute and a method that marks it complete.",
            "Write a Pydantic model that validates a cloud resource request with a name, a region, and a size.",
            "Write a decorator that logs how long any function takes, and use it on a fake run_healthcheck function.",
            "Write an async function that calls three model prompts concurrently using asyncio.gather, and print all three results.",
        ]
    ),
]
