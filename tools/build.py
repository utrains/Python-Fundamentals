#!/usr/bin/env python3
"""Build the student notebooks and the verified solution notebooks.

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
import content_a
import content_b
import content_c

ROOT = Path(__file__).resolve().parent.parent

MODULES = [
    ("01_getting_started", content_a.M1),
    ("02_variables_and_types", content_a.M2),
    ("03_strings", content_a.M3),
    ("04_operators", content_a.M4),
    ("05_control_flow", content_b.M5),
    ("06_collections", content_b.M6),
    ("07_handling_errors", content_b.M7),
    ("08_functions", content_b.M8),
    ("09_file_handling", content_c.M9),
    ("10_important_modules", content_c.M10),
    ("11_advanced_python", content_c.M11),
]


def write_all():
    (ROOT / "notebooks").mkdir(exist_ok=True)
    (ROOT / "solutions").mkdir(exist_ok=True)

    for name, cells in MODULES:
        student = build(cells, solved=False)
        solved = build(cells, solved=True)

        nbf.write(student, str(ROOT / "notebooks" / f"{name}.ipynb"))
        nbf.write(solved, str(ROOT / "solutions" / f"{name}_solved.ipynb"))

        n_ex = sum(1 for k, _, _ in cells if k == "todo")
        n_code = sum(1 for k, _, _ in cells if k in ("code", "todo"))
        print(f"  {name:26s} {len(cells):3d} cells  {n_code:3d} code  {n_ex} exercises")


def run_all():
    from nbclient import NotebookClient

    failures = []
    for name, _ in MODULES:
        path = ROOT / "solutions" / f"{name}_solved.ipynb"
        nb = nbf.read(str(path), as_version=4)
        client = NotebookClient(
            nb,
            timeout=180,
            kernel_name="python3",
            resources={"metadata": {"path": str(path.parent)}},
        )
        try:
            client.execute()
            print(f"  PASS  {name}")
        except Exception as exc:  # noqa: BLE001
            failures.append((name, exc))
            print(f"  FAIL  {name}: {type(exc).__name__}")
            first = str(exc).strip().splitlines()
            for line in first[:12]:
                print("        " + line)
    return failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="execute the solutions")
    args = parser.parse_args()

    print("building notebooks")
    write_all()

    if args.run:
        print("\nexecuting solution notebooks")
        failures = run_all()
        if failures:
            print(f"\n{len(failures)} notebook(s) failed")
            sys.exit(1)
        print("\nall solution notebooks executed cleanly")
