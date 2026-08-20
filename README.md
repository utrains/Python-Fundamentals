# Python Fundamentals Lab

Hands-on Jupyter notebooks for the **Utrains Python Fundamentals** course. One
notebook per module, eleven in all, each runnable from top to bottom.

**Every notebook follows its slide deck section by section.** Headings are
labelled `Slide 6 · The print() Function`, matching the deck, so you can teach
from the deck and scroll the notebook in step with it. Module 11 is the one
module with no deck, so it follows the course reference guide instead and uses
numbered sections.

Each notebook has:

- **Markdown commentary** before every block, in the deck's own words
- **Runnable code cells** that work as written
- **Two "Your turn" cells** with deliberate `____` blanks. They will not run
  until you complete them. That is the point.
- **A lab** at the end: a short task with no starter code
- **The four practice exercises** from the module's practice slide, word for
  word

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

### 2. Get the repo and create the virtual environment

A virtual environment is a folder holding this project's packages, separate
from everything else on your machine. Module 10 explains why in full.

```bash
cd python-fundamental-lab

uv venv
```

That creates a `.venv` folder in the project.

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

### 4. Install the requirements

```bash
uv pip install -r requirements.txt
```

That installs JupyterLab, `ipykernel`, and `pydantic`, which is the only third
party package any notebook imports. Everything else the course uses ships with
Python.

Check it worked:

```bash
uv pip list
```

### 5. Register the environment as a Jupyter kernel

This is the step people skip, and it is the reason a notebook says
`ModuleNotFoundError: No module named 'pydantic'` when the package is clearly
installed. Jupyter needs to be told this environment exists.

```bash
python -m ipykernel install --user --name pyfund --display-name "Python (pyfund)"
```

Then start JupyterLab:

```bash
jupyter lab
```

Open `notebooks/01_getting_started.ipynb` and **pick the kernel**:

- **In JupyterLab**, click the kernel name in the top right of the notebook
  (it will say something like `Python 3 (ipykernel)`), and choose
  **Python (pyfund)** from the list. Or use the menu:
  *Kernel → Change Kernel… → Python (pyfund)*.
- **In VS Code**, click **Select Kernel** in the top right, choose
  **Python Environments…**, then pick the `.venv` inside this project.

You only have to do this once per notebook. Jupyter remembers it after that.

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

### Optional: the AI packages from Module 10

Module 10 discusses `openai`, `langchain` and `langgraph`. Those slides need
network access and an API key, so the notebook shows them as reference code and
gives you a standard library stand-in that runs without a key. **You do not
need them to finish the course.**

When you are ready to call a real API:

```bash
uv pip install -r requirements-ai.txt
```

Then create a `.env` file in the project root and put your key in it. `.env` is
already in `.gitignore`, so it will never be committed:

```
OPENAI_API_KEY=sk-...
```

---

## The modules

| # | Notebook | Deck slides | Covers |
|---|---|---|---|
| 1 | `01_getting_started.ipynb` | 2 to 11 | print(), end and flush, input(), arithmetic |
| 2 | `02_variables_and_types.ipynb` | 2 to 9 | naming, the six core types, type(), casting |
| 3 | `03_strings.ipynb` | 2 to 9 | quotes, slicing, string methods, f-strings |
| 4 | `04_operators.ipynb` | 2 to 8 | arithmetic, comparison, logical, is vs ==, in |
| 5 | `05_control_flow.ipynb` | 2 to 8 | if/elif/else, for, while, break/continue/pass |
| 6 | `06_collections.ipynb` | 2 to 15 | lists, tuples, dictionaries, sets, comprehensions |
| 7 | `07_handling_errors.ipynb` | 2 to 6 | try/except/else/finally, retries, raise |
| 8 | `08_functions.ipynb` | 2 to 8 | parameters, defaults, *args/**kwargs, yield, callbacks |
| 9 | `09_file_handling.ipynb` | 2 to 13 | modes, with, JSON, pathlib |
| 10 | `10_important_modules.ipynb` | 2 to 15 | import, time, os, secrets, venv, AI packages |
| 11 | `11_advanced_python.ipynb` | no deck | classes, dataclasses, Pydantic, decorators, async |

## Repository layout

```
notebooks/            the student notebooks, blanks left in
solutions/            the same notebooks with every blank filled
data/servers.txt      sample input for the Module 9 lab
tools/                the build and verification scripts
requirements.txt      everything the notebooks need
requirements-ai.txt   optional extras for Module 10
```

`scratch/` folders appear inside `notebooks/` and `solutions/` when you run
Module 9. They are gitignored, so nothing you write there gets committed.

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

If you get stuck, the matching notebook in `solutions/` has the answer. Try it
yourself first; the answer is much less useful than the attempt.

**Every exercise stays inside its own module.** A Module 2 exercise will never
need an `if`, because `if` is not taught until Module 5. The build enforces
this, so you will never be asked for something you have not been shown.

---

## Things worth knowing before you teach it

**`input()` is explained but never called in a cell.** A notebook cell that
calls `input()` sits and waits, which breaks a run-all. Where the course would
read from the keyboard, the notebook assigns the value directly and says so in
a comment. The `input()` version is always shown alongside it.

**Module 11 uses `await` at top level, not `asyncio.run()`.** A notebook
already has an event loop running, so `asyncio.run()` raises an error inside
one. The notebook explains the difference, which is a good thing for students
to hit early rather than in their own code.

**Three forward references are deliberate**, because the decks make them and
flag them on the slide: Module 3 uses a `for` loop once to show a string is
iterable, Module 4 uses a list to demonstrate `is` against `==`, and Modules 7
and 9 use `import` before Module 10 formally teaches it. Every one carries a
"Heads up" note in the notebook.

**Module 5 has no lists**, because the deck defers them to Module 6. Its first
practice exercise needs one, so the notebook tells students to come back to it
after Module 6, and Module 6 reminds them.

---

## For instructors

`tools/build.py` regenerates both sets of notebooks from a single source, so a
correction is made once and lands in the student copy and the solution copy
together.

```bash
python tools/build.py             # regenerate the notebooks
python tools/build.py --run       # regenerate, then execute every solution
python tools/check_exercises.py   # confirm the blanks are still incomplete
python tools/check_scope.py       # confirm nothing is used before its module
```

The three checks are what keep the material honest:

- `--run` executes all eleven solution notebooks and fails if any example in
  the course no longer works.
- `check_exercises.py` confirms all 22 exercise cells still contain blanks and
  still fail when run as written. An exercise that quietly succeeds teaches
  nothing.
- `check_scope.py` walks the syntax tree of every code cell and fails the build
  if a notebook uses a language feature before the module that introduces it.
  The deliberate exceptions are listed at the top of that file with the reason
  for each.

To change a lesson, edit the matching module list in `tools/content_a.py`
(modules 1 to 4), `content_b.py` (5 to 8) or `content_c.py` (9 to 11), then
rebuild.

---

Utrains &middot; support@utrains.org &middot; <https://utrains.org>
