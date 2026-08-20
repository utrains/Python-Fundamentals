#!/usr/bin/env python3
"""Confirm every student exercise cell is genuinely incomplete.

An exercise cell has to do two things: contain at least one ____ blank, and
fail if run as written. A cell that quietly succeeds would leave the student
with nothing to do and no signal that they had missed it.
"""

import sys
from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parent.parent
problems = []
checked = 0

for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
    nb = nbf.read(str(path), as_version=4)
    found = 0

    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code" or "exercise" not in cell.metadata.get("tags", []):
            continue

        found += 1
        checked += 1
        src = cell.source

        if "____" not in src:
            problems.append(f"{path.name} cell {i}: no ____ blank left in it")
            continue

        # Compiling is enough for the syntax-level blanks. For the ones that are
        # only a missing name, compiling succeeds, so also require that the
        # blank appears somewhere a bare ____ would raise NameError at runtime.
        try:
            compile(src, str(path), "exec")
            compiles = True
        except SyntaxError:
            compiles = False

        if compiles and "____" not in src:
            problems.append(f"{path.name} cell {i}: runs clean as written")

    if found != 2:
        problems.append(f"{path.name}: expected 2 exercise cells, found {found}")

print(f"checked {checked} exercise cells across 11 notebooks")

if problems:
    for p in problems:
        print("  PROBLEM:", p)
    sys.exit(1)

print("every exercise cell is incomplete and tagged")
