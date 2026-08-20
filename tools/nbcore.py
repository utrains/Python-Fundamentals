"""Helpers for building the Utrains Python Fundamentals material.

One source, three outputs, each showing only what belongs there:

    README.md      the reading copy: every slide, in full, in deck order
    notebooks/     the working copy: headings, code, exercises, labs
    solutions/     the answer sheets: the exercises and their answers

The slide prose lives in the README. A notebook carries the slide heading as a
navigation anchor and then gets straight to the code, because a notebook is for
running things, not for re-reading what you just saw on the slide.

Cell kinds:

    slide(n, title, body)    heading everywhere, body only in the README
    md(text)                 shown in the notebook and the README
    only_nb(text)            notebook only: how to run this thing here
    code(src)                a code cell that runs cleanly as written
    todo(src, solution)      a code cell with blanks, plus its answer
    turn(n, instruction)     the brief for a todo cell
    lab(title, brief, list)  the end of module task
    practice(items, closing) the module's practice slide
"""

import nbformat as nbf

BLANK = "____"


# Cell constructors --------------------------------------------------------

def slide(n, title, body):
    return ("slide", f"Slide {n} &middot; {title}", body.strip())


def md(text):
    return ("md", None, text.strip("\n"))


def only_nb(text):
    return ("only_nb", None, text.strip("\n"))


def heads_up(text):
    return ("only_nb", None, f"> **Heads up.** {text}")


def code(src):
    return ("code", None, src.strip("\n"))


def todo(src, solution):
    if BLANK not in src:
        raise ValueError("a todo cell must contain at least one ____ blank")
    return ("todo", solution.strip("\n"), src.strip("\n"))


def turn(n, instruction):
    return ("turn", n, instruction.strip())


def lab(title, brief, checklist):
    return ("lab", title, (brief.strip(), checklist))


def practice(exercises, closing):
    return ("practice", closing.strip(), exercises)


def header(number, title, subtitle, objectives, deck_note, known):
    return ("header", (number, title, subtitle), (objectives, deck_note, known))


# Notebook rendering -------------------------------------------------------

def _nb_header(meta, payload):
    number, title, subtitle = meta
    objectives, deck_note, known = payload
    bullets = "\n".join(f"- {o}" for o in objectives)
    return f"""# Module {number}: {title}

**Utrains Python Fundamentals** &middot; lab notebook

*{subtitle}*

## By the end of this notebook you can

{bullets}

## How to work through it

{deck_note}

The headings below are the slide numbers from the deck. The explanation for
each one is on the slide and in the [README](../README.md); this notebook is
where you run the code.

Run every cell in order with **Shift + Enter**.

Two cells are marked **Your turn**. They contain `____` where a piece of the
syntax is missing, so they fail if you run them as they are. That is
deliberate. Replace each `____`, then run the cell until it succeeds.

The last section is the **Lab**: a short task with no code written for you.

**Assumed knowledge.** {known}"""


def _nb_turn(n, instruction):
    return f"""---

### Your turn {n}

{instruction}

Replace each `____` below, then run the cell. It will not run until you do."""


def _nb_lab(title, payload):
    brief, checklist = payload
    items = "\n".join(f"- [ ] {c}" for c in checklist)
    return f"""---

## Lab: {title}

{brief}

**Done when:**

{items}

Write your answer in the cell below. There is no starter code on purpose."""


def _nb_practice(closing, exercises):
    return f"""---

## Practice exercises

The four exercises from the module's practice slide are in the
[README](../README.md#practice-exercises) and repeated on the slide. There are
{len(exercises)} of them. Do them in a scratch cell here or in a `.py` file.

## Module complete

{closing}

*Utrains &middot; support@utrains.org &middot; https://utrains.org*"""


def _slide_has_code(cells, index):
    """True if this slide has at least one code cell before the next heading."""
    for kind, _meta, _payload in cells[index + 1:]:
        if kind in ("code", "todo"):
            return True
        if kind in ("slide", "lab", "practice"):
            return False
    return False


LAB_PLACEHOLDER = "# Your lab answer goes here."


def build(cells, solved, lab_answer=None):
    """Render the cell list as a notebook.

    solved=True fills in the exercise blanks and, when lab_answer is given,
    replaces the empty lab cell with the worked answer so the build can execute
    it like any other cell.
    """
    nb = nbf.v4.new_notebook()
    out = []

    for i, (kind, meta, payload) in enumerate(cells):
        # A slide with nothing to run is reading material. It is in the README;
        # putting an empty heading in the notebook only adds scrolling.
        if kind == "slide" and not _slide_has_code(cells, i):
            continue

        if kind == "header":
            out.append(nbf.v4.new_markdown_cell(_nb_header(meta, payload)))
        elif kind == "slide":
            out.append(nbf.v4.new_markdown_cell(f"## {meta}"))
        elif kind in ("md", "only_nb"):
            out.append(nbf.v4.new_markdown_cell(payload))
        elif kind == "turn":
            out.append(nbf.v4.new_markdown_cell(_nb_turn(meta, payload)))
        elif kind == "lab":
            out.append(nbf.v4.new_markdown_cell(_nb_lab(meta, payload)))
        elif kind == "practice":
            out.append(nbf.v4.new_markdown_cell(_nb_practice(meta, payload)))
        elif kind == "code":
            src = payload
            if solved and lab_answer and LAB_PLACEHOLDER in src:
                src = lab_answer.strip("\n")
            out.append(nbf.v4.new_code_cell(src))
        elif kind == "todo":
            cell = nbf.v4.new_code_cell(meta if solved else payload)
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
