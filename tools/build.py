#!/usr/bin/env python3
"""Build the student notebooks, the solution notebooks, and the README.

    python tools/build.py           build only
    python tools/build.py --run     build, then execute every solution notebook

Executing the solutions is the verification step: if any example in the course
is wrong, the build fails here rather than in front of a class.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import nbformat as nbf

from nbcore import build
import build_readme
import build_solutions
import lab_answers
import content_a
import content_b
import content_c

ROOT = Path(__file__).resolve().parent.parent

# slug, module number, title, subtitle, cells
MODULES = [
    ("01_getting_started", 1, "Getting Started with Python",
     "Install Python, meet print() and input(), run your first script, and do a little arithmetic.",
     content_a.M1),
    ("02_variables_and_types", 2, "Variables, Data Types, and Type Casting",
     "Store values in variables, meet Python's core data types, and convert safely between them.",
     content_a.M2),
    ("03_strings", 3, "Strings",
     "Create, slice, format, and clean up text, from a single word to a multi-line AI prompt.",
     content_a.M3),
    ("04_operators", 4, "Operators and Expressions",
     "Do math, compare values, combine conditions, and check what's inside a collection.",
     content_a.M4),
    ("05_control_flow", 5, "Control Flow",
     "Make decisions with if, repeat work with for and while, and steer loops with break, continue, and pass.",
     content_b.M5),
    ("06_collections", 6, "Lists, Tuples, Dictionaries, and Sets",
     "Four ways to hold a group of values, and how to pick the right one.",
     content_b.M6),
    ("07_handling_errors", 7, "Handling Errors",
     "Catch problems instead of crashing, retry what's worth retrying, and raise your own errors.",
     content_b.M7),
    ("08_functions", 8, "Functions",
     "Package reusable logic, pass arguments four different ways, and stream results with yield.",
     content_b.M8),
    ("09_file_handling", 9, "File Handling",
     "Read and write files, work safely with with, and handle JSON, including real API responses.",
     content_c.M9),
    ("10_important_modules", 10, "Important Modules",
     "Import the standard library, set up a virtual environment, and meet openai, langchain, and langgraph.",
     content_c.M10),
    ("11_advanced_python", 11, "Classes, Type Hints, Pydantic, Decorators and Async",
     "The tools that round out your Python toolkit for AI engineering work.",
     content_c.M11),
]


BUILD_DIR = ROOT / ".build" / "solutions"


def write_all():
    """Student notebooks are committed. Solved notebooks are build artifacts."""
    (ROOT / "notebooks").mkdir(exist_ok=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    for slug, num, _title, _sub, cells in MODULES:
        student = build(cells, solved=False)
        solved = build(cells, solved=True, lab_answer=lab_answers.ANSWERS.get(num))

        nbf.write(student, str(ROOT / "notebooks" / f"{slug}.ipynb"))
        nbf.write(solved, str(BUILD_DIR / f"{slug}_solved.ipynb"))

        _ = num
        n_ex = sum(1 for k, _, _ in cells if k == "todo")
        n_code = sum(1 for k, _, _ in cells if k in ("code", "todo"))
        n_slides = sum(1 for k, _, _ in cells if k == "slide")
        print(
            f"  {slug:26s} {len(cells):3d} cells  {n_code:3d} code  "
            f"{n_slides:2d} slides  {n_ex} exercises"
        )


def write_answers():
    n = build_solutions.build(MODULES)
    total = sum(
        (ROOT / "solutions" / f).stat().st_size
        for f in ["README.md"] + [f"{m[0]}.md" for m in MODULES]
    )
    print(f"  solutions/  {n} answer sheets plus an index, {total / 1024:.1f} KB total")


def write_readme():
    text = build_readme.build(MODULES)
    lines = text.count("\n")
    words = len(text.split())
    print(f"  README.md  {lines} lines, about {words:,} words")


def run_all():
    from nbclient import NotebookClient

    failures = []
    for slug, _num, _title, _sub, _cells in MODULES:
        path = BUILD_DIR / f"{slug}_solved.ipynb"
        nb = nbf.read(str(path), as_version=4)
        client = NotebookClient(
            nb,
            timeout=180,
            kernel_name="python3",
            resources={"metadata": {"path": str(path.parent)}},
        )
        try:
            client.execute()
            print(f"  PASS  {slug}")
        except Exception as exc:  # noqa: BLE001
            failures.append((slug, exc))
            print(f"  FAIL  {slug}: {type(exc).__name__}")
            for line in str(exc).strip().splitlines()[:12]:
                print("        " + line)
    return failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="execute the solutions")
    args = parser.parse_args()

    print("building notebooks")
    write_all()

    print("\nbuilding answer sheets")
    write_answers()

    print("\nbuilding README")
    write_readme()

    if args.run:
        print("\nexecuting solution notebooks")
        failures = run_all()
        if failures:
            print(f"\n{len(failures)} notebook(s) failed")
            sys.exit(1)
        print("\nall solution notebooks executed cleanly")
