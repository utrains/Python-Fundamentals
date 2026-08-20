#!/usr/bin/env python3
"""Write the answer sheets: one small markdown file per module.

A solved copy of a whole notebook is mostly slide prose the student has already
read, and only the filled in exercise cells carry any information. So the
committed answers are markdown: the instruction, the student's starting cell,
and the finished code.

The full solved notebooks still get built into .build/ so that
`python tools/build.py --run` can execute them, but they are not committed.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _instruction_for(cells, index):
    """The 'Your turn' brief that sits just above an exercise cell."""
    for kind, _meta, payload in reversed(cells[:index]):
        if kind == "turn":
            return payload
    return ""


def _lab_for(cells):
    for kind, meta, payload in cells:
        if kind == "lab":
            return meta, payload[0]
    return None, None


def module_answers(number, title, slug, cells):
    lines = [
        f"# Module {number} answers: {title}",
        "",
        f"Notebook: [`../notebooks/{slug}.ipynb`](../notebooks/{slug}.ipynb)",
        "",
        "Try each one yourself before reading on. The attempt is worth more "
        "than the answer.",
        "",
    ]

    n = 0
    for i, (kind, solution, src) in enumerate(cells):
        if kind != "todo":
            continue
        n += 1
        lines += [
            "---",
            "",
            f"## Your turn {n}",
            "",
            _instruction_for(cells, i),
            "",
            "**What you start with**",
            "",
            "```python",
            src,
            "```",
            "",
            "**The answer**",
            "",
            "```python",
            solution,
            "```",
            "",
        ]

    lab_title, lab_brief = _lab_for(cells)
    if lab_title:
        lines += [
            "---",
            "",
            f"## Lab: {lab_title}",
            "",
            lab_brief,
            "",
            "There is no single right answer to a lab, so none is given here. "
            "Check your work against the checklist in the notebook. If it ticks "
            "every box and runs without an error, it is right.",
            "",
        ]

    lines += [
        "---",
        "",
        "*Utrains &middot; support@utrains.org &middot; https://utrains.org*",
        "",
    ]
    return "\n".join(lines)


def index_page(modules):
    rows = ["| # | Module | Answers |", "|---|---|---|"]
    for slug, number, title, _sub, _cells in modules:
        rows.append(f"| {number} | {title} | [`{slug}.md`]({slug}.md) |")

    return "\n".join(
        [
            "# Answers",
            "",
            "One file per module, holding the two **Your turn** answers and the "
            "lab brief. The slide content is not repeated here; it is in the "
            "[README](../README.md) and in the notebooks themselves.",
            "",
            "Work the exercise first. A blank you filled in yourself is worth "
            "more than one you read.",
            "",
        ]
        + rows
        + [
            "",
            "---",
            "",
            "### Why these are not notebooks",
            "",
            "A solved copy of a whole notebook is mostly the same slide prose "
            "you have already read, and only the filled in cells differ. So the "
            "answers live here as markdown you can read on GitHub without "
            "opening anything.",
            "",
            "If you want a solved notebook you can actually run, build one:",
            "",
            "```bash",
            "python tools/build.py",
            "```",
            "",
            "That writes full solved notebooks into `.build/solutions/`, which "
            "is gitignored. The same files are what `python tools/build.py "
            "--run` executes to check every example in the course still works.",
            "",
            "*Utrains &middot; support@utrains.org &middot; https://utrains.org*",
            "",
        ]
    )


def build(modules):
    out = ROOT / "solutions"
    out.mkdir(exist_ok=True)

    written = 0
    for slug, number, title, _sub, cells in modules:
        (out / f"{slug}.md").write_text(module_answers(number, title, slug, cells))
        written += 1

    (out / "README.md").write_text(index_page(modules))
    return written
