"""Helpers for building the Utrains Python Fundamentals lab notebooks.

Each notebook follows its module's slide deck in order, so an instructor can
teach from the deck and scroll the notebook in step with it. Section headings
carry the slide number and the slide title.

Cell kinds:

    md(text)                 a markdown cell
    slide(n, title, body)    a markdown cell headed "Slide n - title"
    code(src)                a code cell that runs cleanly as written
    todo(src, solution)      a code cell with deliberate blanks for the student

`todo` cells are tagged "exercise". The build writes two copies of every
notebook: the student copy under notebooks/ with the blanks left in, and a
verified copy under solutions/ with the blanks filled. Only the solutions copy
is executed during the build, which is what proves every example works.
"""

import nbformat as nbf

BLANK = "____"


def md(text):
    return ("md", text.strip("\n"), None)


def slide(n, title, body):
    return md(f"## Slide {n} &middot; {title}\n\n{body.strip()}")


def code(src):
    return ("code", src.strip("\n"), None)


def todo(src, solution):
    if BLANK not in src:
        raise ValueError("a todo cell must contain at least one ____ blank")
    return ("todo", src.strip("\n"), solution.strip("\n"))


def build(cells, solved):
    """Turn the cell list into a notebook. solved=True fills in the blanks."""
    nb = nbf.v4.new_notebook()
    out = []
    for kind, src, solution in cells:
        if kind == "md":
            out.append(nbf.v4.new_markdown_cell(src))
        elif kind == "code":
            out.append(nbf.v4.new_code_cell(src))
        elif kind == "todo":
            cell = nbf.v4.new_code_cell(solution if solved else src)
            cell.metadata["tags"] = ["exercise"]
            out.append(cell)
    nb.cells = out
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "version": "3.11"},
    }
    return nb


# Reusable markdown blocks -------------------------------------------------

def header(number, title, subtitle, objectives, deck_note, known):
    bullets = "\n".join(f"- {o}" for o in objectives)
    return md(
        f"""
# Module {number}: {title}

**Utrains Python Fundamentals** &middot; lab notebook

*{subtitle}*

## What you will be able to do by the end

{bullets}

## How this notebook is organised

{deck_note}

Run every cell in order with **Shift + Enter**. Read the note above each block,
then run the code and compare what you see with what you expected.

Two cells are marked **Your turn**. They contain `____` where a piece of the
syntax is missing, so they will fail if you run them as they are. That is
deliberate. Replace each `____`, then run the cell until it succeeds.

The last section is the **Lab**: a short task with no code written for you.

## What this notebook assumes

{known}
"""
    )


def turn(n, instruction):
    return md(
        f"""
---

### Your turn {n}

{instruction}

Replace each `____` below, then run the cell. It will not run until you do.
"""
    )


def lab(title, brief, checklist):
    items = "\n".join(f"- [ ] {c}" for c in checklist)
    return md(
        f"""
---

## Lab: {title}

{brief}

**Done when:**

{items}

Write your answer in the cell below. There is no starter code on purpose.
"""
    )


def practice(exercises, closing):
    items = "\n".join(f"{i}. {e}" for i, e in enumerate(exercises, 1))
    return md(
        f"""
---

## Practice exercises

These are the four exercises from the module's practice slide, word for word.

{items}

---

## Module complete

{closing}

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
"""
    )


def heads_up(text):
    return md(f"> **Heads up.** {text}")
