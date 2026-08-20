#!/usr/bin/env python3
"""Generate README.md: the hand written intro plus all the slide content.

This is the reading copy. Every slide appears here in full, in deck order, with
the code from the notebook underneath it. The notebooks carry only the slide
headings, so nothing is duplicated between the two.

Exercises and labs are left out on purpose: they belong somewhere you can run
them.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def demote(text):
    """Push every markdown heading down two levels, leaving code fences alone."""
    out = []
    fenced = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("#"):
            line = "##" + line
        out.append(line)
    return "\n".join(out)


def module_section(number, title, subtitle, slug, cells):
    parts = [
        f"### Module {number}: {title}",
        "",
        f"*{subtitle}*",
        "",
        f"Notebook: [`notebooks/{slug}.ipynb`](notebooks/{slug}.ipynb) &middot; "
        f"answers: [`solutions/{slug}.md`](solutions/{slug}.md)",
        "",
    ]

    for kind, meta, payload in cells:
        if kind in ("header", "turn", "lab", "todo", "only_nb"):
            continue

        if kind == "slide":
            parts += [f"#### {meta}", "", payload, ""]

        elif kind == "md":
            parts += [demote(payload), ""]

        elif kind == "code":
            if payload.strip() == "# Your lab answer goes here.":
                continue
            parts += ["```python", payload, "```", ""]

        elif kind == "practice":
            items = "\n".join(f"{i}. {e}" for i, e in enumerate(payload, 1))
            parts += [
                "#### Practice exercises",
                "",
                items,
                "",
                "#### Module complete",
                "",
                meta,
                "",
            ]

    return "\n".join(parts).rstrip() + "\n"


def build(modules):
    intro = (ROOT / "tools" / "readme_intro.md").read_text()

    chunks = [intro.rstrip(), ""]
    for slug, number, title, subtitle, cells in modules:
        chunks += ["---", "", module_section(number, title, subtitle, slug, cells), ""]

    chunks += [
        "---",
        "",
        "Utrains &middot; support@utrains.org &middot; <https://utrains.org>",
        "",
    ]

    text = "\n".join(chunks)
    (ROOT / "README.md").write_text(text)
    return text
