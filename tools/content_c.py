"""Modules 9 to 11.

Modules 9 and 10 follow their slide decks section by section. Module 11 has no
deck, so it follows the course reference guide's section order instead.
"""

from nbcore import header, md, only_nb, slide, code, todo, turn, lab, practice, heads_up

# ---------------------------------------------------------------- Module 9

M9 = [
    header(
        9,
        "File Handling",
        "Read and write files, work safely with with, and handle JSON, including real API responses.",
        [
            "Pick the right file mode for what you are about to do",
            "Read a whole file, one line, or every line as a list",
            "Prefer with open(...) so files always get closed",
            "Turn Python data into JSON and back, as a string and as a file",
            "Locate a config file on disk with pathlib",
        ],
        "It follows the Module 9 slide deck, slide by slide.",
        "Modules 1 to 8. `import` appears throughout because `os`, `json` and "
        "`pathlib` need it; the deck flags this too, and Module 10 explains "
        "`import` properly.",
    ),
    md(
        """
### Before you start: the scratch folder

Everything in this notebook writes into a `scratch/` folder next to it, so
nothing else on your machine is touched. `scratch/` is in `.gitignore`, so none
of it will end up in a commit. Run this cell first.
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
    slide(
        2,
        "What Is File Handling?",
        """
File handling lets your program read and write data outside of memory, so it
survives after the script finishes running.

**Two verbs, one function.** `open()` handles both reading and writing. What it
does depends entirely on the mode you pass it.
""",
    ),
    code(
        """
# write something to disk
file = open(WORK / "notes.txt", "w")
file.write("Meeting at 3pm")
file.close()

# read it back later, even after the program restarts
file = open(WORK / "notes.txt", "r")
print(file.read())
file.close()
"""
    ),
    slide(
        3,
        "File Modes",
        """
You choose a mode when you open a file, which controls what you are allowed to
do with it.

| Mode | Meaning |
|---|---|
| `"r"` | Read. The default mode. |
| `"w"` | Write. **Overwrites** anything already there. |
| `"a"` | Append. Adds new content to the end. |
| `"x"` | Create. Fails if the file already exists. |
| `"rb"` / `"wb"` | Same as r and w, for binary data. |
""",
    ),
    slide(
        4,
        "Opening, Writing, and Reading",
        """
Write to a file, then open it again separately to read it back.

**Do not forget `close()`.** Skipping it can leave a file locked or lose
unsaved data. The `with` statement, coming up shortly, removes this risk
entirely.
""",
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
    slide(
        5,
        "Reading Line by Line",
        """
You do not have to read a whole file at once. Pull one line, or every line as a
list.
""",
    ),
    code(
        """
file = open(WORK / "sample.txt", "r")
line = file.readline()          # reads a single line
file.close()
print("readline :", repr(line))

file = open(WORK / "sample.txt", "r")
lines = file.readlines()        # reads all lines into a list
file.close()
print("readlines:", lines)
"""
    ),
    slide(
        6,
        "The with Statement",
        """
Opening a file with `with` automatically closes it for you, even if an error
happens partway through. This is the pattern to reach for by default.

**No `close()` needed.** `with` removes the risk of a locked file or lost data
entirely, so prefer it over `open()` / `close()` pairs.
""",
    ),
    code(
        """
with open(WORK / "sample.txt", "r") as file:
    content = file.read()
    print(content)

# the file is already closed here, no need to call close()
print("closed?", file.closed)
"""
    ),
    slide(
        7,
        "Writing Multiple Lines and Appending",
        """
`writelines()` takes a list of strings and writes each one. Appending with
`"a"` adds to the end without touching what is already there.

**Remember the newline.** `writelines()` does not add `\\n` for you. Each
string in the list needs its own.
""",
    ),
    code(
        """
lines = ["Line 1\\n", "Line 2\\n", "Line 3\\n"]

with open(WORK / "output.txt", "w") as file:
    file.writelines(lines)

with open(WORK / "output.txt", "a") as file:
    file.write("This line will be appended.\\n")

with open(WORK / "output.txt", "r") as file:
    print(file.read())
"""
    ),
    turn(
        1,
        "Append an incident summary to a running log, then read the whole log "
        "back. Pick the mode that adds to the end rather than wiping the file.",
    ),
    todo(
        """
log_path = WORK / "incidents.log"

# TODO: choose the mode that ADDS to the end rather than overwriting.
with open(log_path, ____) as f:
    f.write("INC-4412 database connection failures resolved\\n")

# TODO: choose the mode that reads.
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
        "Run that cell two or three times. The log grows each time, which is "
        "exactly what append mode is for. Change the mode to `\"w\"`, run it "
        "again, and watch the earlier lines disappear."
    ),
    slide(
        8,
        "Working with Binary Files",
        """
Images and other non-text files need `"rb"` and `"wb"`, the binary versions of
read and write mode. Binary content comes back as bytes rather than text.
""",
    ),
    code(
        """
# Make a small binary file so there is something real to copy.
with open(WORK / "image.jpg", "wb") as f:
    f.write(bytes(range(40)))

with open(WORK / "image.jpg", "rb") as file:
    data = file.read()
    print("Binary content:", data[:20])

with open(WORK / "copy.jpg", "wb") as new_file:
    new_file.write(data)

print("copy written, same size:", (WORK / "copy.jpg").stat().st_size == len(data))
"""
    ),
    slide(
        9,
        "Checking and Deleting Files",
        """
Checking whether a file exists and deleting one both live in a module called
`os`, which ships with Python.

**First time seeing `import`?** Module 10 explains it in full. The short
version: it brings in code someone else already wrote, used with a dot, like
`os.path.exists()`.
""",
    ),
    code(
        """
import os

target = WORK / "sample.txt"

if os.path.exists(target):
    print("File exists")
else:
    print("File not found")

os.remove(target)
print("after remove, exists?", os.path.exists(target))
"""
    ),
    slide(
        10,
        "Working with JSON",
        """
JSON is a text format almost every API uses to send and receive data. It maps
directly onto a Python dictionary.

**Two functions to know.** `json.dumps` turns a Python object into a JSON
string. `json.loads` turns a JSON string back into a Python object.
""",
    ),
    code(
        """
import json

person = {"name": "Alice", "age": 25}

as_text = json.dumps(person)
print(as_text)
print(type(as_text))

back_to_dict = json.loads(as_text)
print(back_to_dict["name"])
print(type(back_to_dict))
"""
    ),
    slide(
        11,
        "Parsing a Real JSON Response",
        """
A model API response arrives as JSON text over the network. Parsing it is the
same skill applied to something you did not write yourself.

**Follow the brackets.** `data["content"][0]["text"]` is a dictionary, then a
list, then a dictionary again, one step at a time. That is exactly the nested
structure from Module 6.
""",
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
    slide(
        12,
        "Reading and Writing JSON Files",
        """
`json.load` and `json.dump` work the same way, but read from and write directly
to a file, so you never build the string by hand.

**dump vs dumps.** `dump` writes to a file object. `dumps`, with an `s`,
returns a string. The same pattern applies to `load` and `loads`.
""",
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
        "back. Watch carefully which of the four json functions each step needs.",
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
    slide(
        13,
        "Finding a Config File with pathlib",
        """
`pathlib` is another built in module for working with file paths. This pattern
searches a few likely folders for a configuration file.

**AI framing.** This is exactly how AI projects locate API keys stored outside
the code, in a `.env` file.
""",
    ),
    code(
        """
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
"""
    ),
    md(
        """
### Reading a file that ships with this repo

`data/servers.txt` sits one folder up from this notebook, with one server name
per line. Reading a real file is the same code, just a different path.
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
    lab(
        "A server inventory round trip",
        """
Read `../data/servers.txt`, which holds one server name per line.

Turn it into a list of dictionaries, where each entry has a `name`, a `region`
taken from the part of the name after the first hyphen that follows the number,
and a `status` of `"unknown"`.

Save that list to `scratch/inventory.json` with an indent of 2, then read it
back from disk into a fresh variable, and print how many servers you recovered
and the name of the last one.

Finish by appending one audit line to `scratch/audit.log` recording how many
servers were processed. Run the whole lab twice: the audit log should have two
lines while the inventory JSON still holds the right count.
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
        ],
        "You can now read, write and manage files, and work with JSON data confidently.",
    ),
]

# --------------------------------------------------------------- Module 10

M10 = [
    header(
        10,
        "Important Modules",
        "Import the standard library, set up a virtual environment, and meet openai, langchain, and langgraph.",
        [
            "Say what a module is and what import actually does",
            "Use all three import patterns",
            "Measure time and read the operating system with time and os",
            "Keep secrets out of your code and out of source control",
            "Say what openai, langchain and langgraph each do, and when to pick which",
        ],
        "It follows the Module 10 slide deck, slide by slide.",
        "Modules 1 to 9. The AI package slides need network access and an API "
        "key, so their code is shown as reference and paired with a standard "
        "library stand-in you can actually run.",
    ),
    slide(
        2,
        "What Is a Module?",
        """
A module is a file of pre-written Python code you bring into your own program
with `import`. This is where most of Python's real power comes from: you rarely
have to write something from scratch.

**Standard library vs third party.** `time` ships with Python. Something like
`ollama` does not, so you install it first.
""",
    ),
    code(
        """
import time            # standard library, comes with Python

# import ollama       # third party, pip install ollama first

print("time module loaded:", time.__name__)
"""
    ),
    slide(
        3,
        "Import Patterns",
        """
`import` loads a module so its functions and variables become available. There
are a few common styles.

| Pattern | Gives you |
|---|---|
| `import module_name` | `module_name.something` |
| `import module_name as alias` | a shorter name |
| `from module_name import something` | just one piece, directly |
""",
    ),
    code(
        """
import datetime as dt
from math import sqrt

print(dt.date.today())
print(sqrt(16))
"""
    ),
    slide(
        4,
        "Measuring Time",
        """
The `time` module is the standard way to measure how long something takes to
run. `time.time()` gives you a number of seconds; take one from another to get
the elapsed time.
""",
    ),
    code(
        """
import time

t0 = time.time()
time.sleep(0.3)
print(f"Waited {time.time() - t0:.1f}s")
"""
    ),
    turn(
        1,
        "Measure how long a fake health check takes and print the answer to two "
        "decimal places. Two ideas here: the import statement, and the call "
        "that reads the clock.",
    ),
    todo(
        """
# TODO: bring in the module that can pause and read the clock.
____ time


def run_healthcheck():
    time.sleep(0.25)
    return "healthy"


# TODO: read the clock before and after.
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
    slide(
        5,
        "Working with the Operating System",
        """
The `os` module reads information about the machine your script is running on.
""",
    ),
    code(
        """
import os

print(os.getcwd())                      # current directory
print(sorted(os.listdir("."))[:10])     # files here
"""
    ),
    slide(
        6,
        "Config Values versus Secrets",
        """
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
""",
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
    slide(
        7,
        "API, SDK, and Client, Defined",
        """
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
""",
    ),
    slide(
        8,
        "Setting Up a Virtual Environment",
        """
The packages coming up do not ship with Python. Before installing anything,
isolate this project's packages from the rest of your system.

**One environment per project.** This keeps one project's packages from
colliding with another's, and lets you delete `.venv` and start clean any time.

```bash
uv venv                        # creates .venv here

source .venv/bin/activate      # Linux / macOS
.venv\\Scripts\\activate         # Windows

uv pip install openai langchain langgraph

deactivate                     # leave when you are done
```

If you followed this repo's README, you already did exactly this to get the
notebook running. The `README.md` has the full walkthrough including how to
point Jupyter at the environment.
""",
    ),
    slide(
        9,
        "Popular AI Packages: openai",
        """
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
""",
    ),
    slide(
        10,
        "Popular AI Packages: langchain",
        """
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
""",
    ),
    slide(
        11,
        "Popular AI Packages: langgraph",
        """
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
""",
    ),
    code(
        """
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
    slide(
        12,
        "LangChain Agents vs LangGraph",
        """
Both can build an **agent**, a program that decides what to do rather than
always running fixed steps. They hand you different amounts of control.

**LangChain agents.** Faster to set up for a standard tool-calling loop. Hand
it a model and tools, and it repeats until done.

**LangGraph.** More code to wire up, but you see and control every step. Add
cycles, or pause for human approval.

**No wrong choice.** Reach for LangChain's agent tools for a quick, standard
loop. Reach for LangGraph when you need to see and control the steps yourself.
Complex or multi-agent workflows tend to move toward LangGraph as they grow.
""",
    ),
    slide(
        13,
        "A LangChain Agent in Practice",
        """
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
    \"\"\"Look up the weather for a city.\"\"\"
    return f"It is sunny in {city}."

agent = create_tool_calling_agent(llm, [get_weather], prompt)
executor = AgentExecutor(agent=agent, tools=[get_weather])
result = executor.invoke({"input": "Weather in Boston?"})
print(result["output"])
```
""",
    ),
    slide(
        14,
        "Building a Tiny Agent with LangGraph",
        """
A small agent, built with the same `StateGraph` pattern, that answers weather
questions and declines anything else.

**This is what every agent does.** Read the state, decide what to do, return an
update. The `if` / `else` here stands in for a model deciding which tool to
call.
""",
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
        answer = "I can only answer weather questions."
    return {"answer": answer}


print(agent_node({"question": "What is the weather like?"})["answer"])
print(agent_node({"question": "Who won the game?"})["answer"])
"""
    ),
    turn(
        2,
        "Extend the tiny agent with a second condition so it also answers a "
        "simple addition question, and still declines everything else.",
    ),
    todo(
        """
def agent_node(state):
    question = state["question"].lower()

    if "weather" in question:
        answer = get_weather("Boston")
    # TODO: add a branch that catches a maths question, then a catch-all.
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
    slide(
        15,
        "Other Useful Modules",
        """
A quick map of what else is out there, for when you need it.

- **subprocess** &mdash; running shell commands from inside Python
- **requests** &mdash; making HTTP calls to APIs
- **Docker and Kubernetes** &mdash; container and orchestration helper patterns
- **boto3 and Terraform** &mdash; cloud and infrastructure as code
- **Git automation** &mdash; CI/CD pipeline integration
""",
    ),
    lab(
        "A timed, config-driven health reporter",
        """
Write a small script in this notebook that does four things.

Read a model name from an environment variable called `LAB_MODEL`, falling back
to `"gpt-4o-mini"` when it is not set. Print the model, and separately print
whether an API key called `LAB_API_KEY` is present, without ever printing its
value.

Use `os.listdir` to count how many files sit in the current folder.

Time a fake `run_healthcheck()` function that sleeps briefly and returns a
status, and print the elapsed time to two decimal places.

Stamp the report with today's date using `datetime`.

Print all of it as one tidy report block.
""",
        [
            "The model comes from the environment with a fallback",
            "The key is reported as present or absent, never printed",
            "os is used to count the files in the folder",
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
        ],
        "You can now import modules, manage secrets, and build with real AI packages. "
        "Exercise 2 needs `python-dotenv`, which is in `requirements-ai.txt`.",
    ),
]

# --------------------------------------------------------------- Module 11

M11 = [
    header(
        11,
        "Classes, Type Hints, Pydantic, Decorators and Async",
        "The tools that round out your Python toolkit for AI engineering work.",
        [
            "Bundle data and behaviour together in a class, and read dotted SDK output",
            "Describe a shape with type hints and a dataclass",
            "Validate untrusted data with a Pydantic model",
            "Wrap a function with a decorator without changing its code",
            "Run several slow calls at once with async and await",
        ],
        "Module 11 is the one module with no slide deck, so this notebook "
        "follows the course reference guide's section order instead. Sections "
        "are numbered rather than labelled with a slide number.",
        "Modules 1 to 10. This is the only notebook that needs a third party "
        "package: **Pydantic**, which is in `requirements.txt`.",
    ),
    md(
        """
### Before you start: check Pydantic is available

If this cell fails, your environment is missing Pydantic. Install it with
`uv pip install -r requirements.txt`, then restart the kernel.
"""
    ),
    code(
        """
import pydantic

print("pydantic", pydantic.VERSION)
"""
    ),
    md("## Section 1 &middot; Classes and objects"),
    md(
        """
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
        "Write a `Deployment` class that starts as pending and can be marked "
        "complete. Fill in the constructor's name and the reference to the "
        "object itself.",
    ),
    todo(
        """
class Deployment:
    # TODO: name the constructor, and store both values on the object.
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
    md("## Section 2 &middot; Type hints and dataclasses"),
    md(
        """
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


print(Message(role="user", content="Hi there"))
print(WeatherLookup(city="Boston"))
print("a dataclass will NOT stop this:", Message(role=123, content=None))
"""
    ),
    md("## Section 3 &middot; Pydantic models"),
    md(
        """
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
    md("## Section 4 &middot; Decorators"),
    md(
        """
A decorator is a function that wraps another function to add behaviour, without
changing the code inside that function. It is written as an `@` placed directly
above a `def` line. It builds on Module 8's idea that a function is just a
value you can pass around.
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
    md("## Section 5 &middot; Async and await"),
    md(
        """
Everything so far has been **synchronous**: Python runs one line, waits for it
to finish, then moves to the next. Asynchronous code, written with `async` and
`await`, lets a program start a slow task such as a network call and work on
something else while it waits, instead of sitting idle.
"""
    ),
    heads_up(
        "**In a script** you start the whole thing with `asyncio.run(main())`. "
        "**In a notebook** there is already an event loop running, so "
        "`asyncio.run()` raises an error. Use a bare `await main()` instead, as "
        "the cells below do. This catches almost everyone out once."
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
objects. Give it an `async def ask(self, message)` method that sleeps briefly
to simulate the network, appends both the user turn and the assistant reply to
its history, and returns the reply.

Write your own `@timed` decorator and put it on a `report()` method, so
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
        ],
        "That is the whole course. You can now read and write Python confidently "
        "enough to work with real AI SDKs.",
    ),
]
