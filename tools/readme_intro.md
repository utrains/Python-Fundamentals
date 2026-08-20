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

Each notebook has runnable code for every slide that has any, **two "Your turn"
cells** with deliberate `____` blanks that fail until you complete them, and a
**lab** at the end with no starter code.

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
