# Python Fundamentals Lab

Hands-on Jupyter notebooks for the **Utrains Python Fundamentals** course. One
notebook per module, eleven in all, each one runnable from top to bottom.

Every notebook follows the same shape:

- **Markdown commentary** before each block, explaining what the code does and
  why it matters
- **Runnable code cells** that work as written, so you can execute first and
  read second if you prefer
- **Two "Your turn" cells** per notebook with deliberate `____` blanks. They
  will not run until you complete them. That is the point.
- **A lab** at the end: a short task with no starter code, so you have to put
  the module together yourself
- **Practice exercises** taken straight from the course reference guide

## Quick start

```bash
git clone <this-repo>
cd python-fundamental-lab

# create an isolated environment (uv, as taught in Module 10)
uv venv
source .venv/bin/activate          # Linux / macOS
.venv\Scripts\activate             # Windows

uv pip install -r requirements.txt
jupyter lab
```

If you prefer the classic tools, `python -m venv .venv` and `pip install -r
requirements.txt` do the same job.

Then open `notebooks/01_getting_started.ipynb` and work down the list.

You can also open the folder in VS Code and run the notebooks there. The Python
and Jupyter extensions are all you need.

## The modules

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
| 10 | `10_important_modules.ipynb` | import, time, os, config vs secrets, venv, AI packages |
| 11 | `11_advanced_python.ipynb` | classes, dataclasses, Pydantic, decorators, async |

## Repository layout

```
notebooks/     the student notebooks, blanks left in
solutions/     the same notebooks with every blank filled
data/          sample input files used by the labs
tools/         the build script that generates both sets
requirements.txt
```

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

## Notes on the environment

Modules 1 to 9 use nothing but the Python standard library, so they run on a
plain Python 3.10 or newer install with Jupyter.

Module 11 uses **Pydantic**, which is in `requirements.txt`.

Module 10 discusses `openai`, `langchain` and `langgraph`. Those need network
access and an API key, so the notebook shows them as reference code in markdown
and gives you a standard-library stand-in that runs without a key. Nothing in
this repo will ever try to call a paid API.

`input()` is explained in Module 1 but never called in a cell, because a
notebook cell that calls `input()` sits and waits. Where the course would read
from the keyboard, the notebook assigns the value directly and says so.

## For instructors

`tools/build.py` regenerates both sets of notebooks from a single source, so a
correction is made once and lands in the student copy and the solution copy
together.

```bash
python tools/build.py            # regenerate the notebooks
python tools/build.py --run      # regenerate, then execute every solution
python tools/check_exercises.py  # confirm the blanks are still incomplete
```

`--run` is the verification step. It executes all eleven solution notebooks and
fails the build if any example in the course no longer works.

To change a lesson, edit the matching module list in `tools/content_a.py`
(modules 1 to 4), `content_b.py` (5 to 8) or `content_c.py` (9 to 11), then
rebuild.

---

Utrains &middot; support@utrains.org &middot; <https://utrains.org>
