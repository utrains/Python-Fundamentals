#!/usr/bin/env python3
"""Fail the build if a notebook uses a language feature before its module.

A student working through Module 2 has not met `if` yet, so a Module 2 exercise
must not need one. This walks the syntax tree of every code cell and compares
the features it finds against the module where the course introduces them.

A few forward references are deliberate, because the slide decks themselves
make them and flag them on the slide. Those are listed in ALLOWED_EARLY with
the reason, and everything else is an error.

The solution notebooks are parsed rather than the student ones, since the
student copies contain ____ blanks that will not parse. The two differ only in
those cells, and the solution is what the student is being asked to write.
"""

import ast
import sys
from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parent.parent

# Which module first teaches each feature.
INTRODUCED_IN = {
    "f-string": 3,
    "augmented assignment": 4,
    "boolean operator": 4,
    "comparison": 4,
    "if": 5,
    "for": 5,
    "while": 5,
    "break": 5,
    "continue": 5,
    "pass": 5,
    "list literal": 6,
    "list comprehension": 6,
    "tuple literal": 6,
    "dict literal": 6,
    "dict comprehension": 6,
    "set literal": 6,
    "set comprehension": 6,
    "try": 7,
    "raise": 7,
    "def": 8,
    "return": 8,
    "yield": 8,
    "lambda": 8,
    "with": 9,
    "import": 10,
    "class": 11,
    "async def": 11,
    "await": 11,
    "decorator": 11,
}

NODE_FEATURES = {
    ast.JoinedStr: "f-string",
    ast.AugAssign: "augmented assignment",
    ast.BoolOp: "boolean operator",
    ast.Compare: "comparison",
    ast.If: "if",
    ast.For: "for",
    ast.While: "while",
    ast.Break: "break",
    ast.Continue: "continue",
    ast.Pass: "pass",
    ast.List: "list literal",
    ast.ListComp: "list comprehension",
    ast.Tuple: "tuple literal",
    ast.Dict: "dict literal",
    ast.DictComp: "dict comprehension",
    ast.Set: "set literal",
    ast.SetComp: "set comprehension",
    ast.Try: "try",
    ast.Raise: "raise",
    ast.FunctionDef: "def",
    ast.Return: "return",
    ast.Yield: "yield",
    ast.Lambda: "lambda",
    ast.With: "with",
    ast.Import: "import",
    ast.ImportFrom: "import",
    ast.ClassDef: "class",
    ast.AsyncFunctionDef: "async def",
    ast.Await: "await",
}

# Forward references the decks make on purpose, and say so on the slide.
ALLOWED_EARLY = {
    3: {
        "for": "deck slide 2 uses a for loop to show that a string is iterable",
    },
    4: {
        "list literal": "deck slide 7 uses a list for is vs ==, with a heads up",
        "tuple literal": "isinstance(x, (int, float)) needs a tuple of types",
    },
    2: {
        "tuple literal": "isinstance(x, (int, float)) needs a tuple of types",
    },
    7: {
        "import": "json and time are needed here; the deck flags Module 10",
        "def": "the retry example is built as a function, as on deck slide 5",
        "return": "the retry example returns a value, as on deck slide 5",
    },
    9: {
        "import": "os, json and pathlib are needed; deck slide 9 flags it",
    },
    11: {
        "decorator": "decorators are a Module 11 topic",
    },
}


def features_in(source):
    found = set()
    tree = ast.parse(source)
    for node in ast.walk(tree):
        name = NODE_FEATURES.get(type(node))
        if name:
            found.add(name)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.decorator_list:
                found.add("decorator")
    return found


def main():
    problems = []
    scanned = 0

    for path in sorted((ROOT / "solutions").glob("*.ipynb")):
        module = int(path.name[:2])
        allowed = ALLOWED_EARLY.get(module, {})
        nb = nbf.read(str(path), as_version=4)

        for i, cell in enumerate(nb.cells):
            if cell.cell_type != "code" or not cell.source.strip():
                continue
            scanned += 1
            try:
                found = features_in(cell.source)
            except SyntaxError as exc:
                problems.append(f"module {module:02d} cell {i}: will not parse: {exc}")
                continue

            for feature in sorted(found):
                first = INTRODUCED_IN[feature]
                if first > module and feature not in allowed:
                    problems.append(
                        f"module {module:02d} cell {i}: uses '{feature}', "
                        f"which is not taught until module {first}"
                    )

    print(f"scanned {scanned} code cells across 11 notebooks")

    if problems:
        for p in problems:
            print("  OUT OF SCOPE:", p)
        print(f"\n{len(problems)} scope problem(s)")
        return 1

    print("no notebook uses a feature before the module that teaches it")
    for module, entries in sorted(ALLOWED_EARLY.items()):
        for feature, why in sorted(entries.items()):
            print(f"  allowed early in module {module:02d}: {feature} ({why})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
