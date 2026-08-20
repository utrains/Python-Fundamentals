#!/usr/bin/env python3
"""Generate README.md: the hand written intro plus all the slide content.

The course content section is built from the same cell lists that build the
notebooks, so the README and the notebooks cannot drift apart. Exercise cells
and lab briefs are skipped, because those only make sense somewhere you can run
them.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB_PLACEHOLDER = "# Your lab answer goes here."


def demote(text):
    """Push every markdown heading down two levels."""
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
        f"solution: [`solutions/{slug}_solved.ipynb`](solutions/{slug}_solved.ipynb)",
        "",
    ]

    for kind, src, _solution in cells[1:]:      # cells[0] is the notebook header
        if kind == "todo":
            continue

        if kind == "code":
            if src.strip() == LAB_PLACEHOLDER:
                continue
            parts.append("```python")
            parts.append(src)
            parts.append("```")
            parts.append("")
            continue

        text = src.strip()

        if text.startswith("---"):
            # turn / lab / practice blocks all start with a rule
            if "## Practice exercises" in text:
                body = text.split("## Practice exercises", 1)[1]
                body = body.split("*Utrains", 1)[0].rstrip()
                parts.append("#### Practice exercises")
                parts.append("")
                parts.append(demote(body).strip())
                parts.append("")
            continue

        parts.append(demote(text))
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def build(modules):
    intro = (ROOT / "tools" / "readme_intro.md").read_text()

    chunks = [intro.rstrip(), ""]
    for slug, number, title, subtitle, cells in modules:
        chunks.append("---")
        chunks.append("")
        chunks.append(module_section(number, title, subtitle, slug, cells))
        chunks.append("")

    chunks.append("---")
    chunks.append("")
    chunks.append("Utrains &middot; support@utrains.org &middot; <https://utrains.org>")
    chunks.append("")

    text = "\n".join(chunks)
    (ROOT / "README.md").write_text(text)
    return text
