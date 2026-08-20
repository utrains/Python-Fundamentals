# Answers

One file per module, holding the two **Your turn** answers and the lab brief. The slide content is not repeated here; it is in the [README](../README.md) and in the notebooks themselves.

Work the exercise first. A blank you filled in yourself is worth more than one you read.

| # | Module | Answers |
|---|---|---|
| 1 | Getting Started with Python | [`01_getting_started.md`](01_getting_started.md) |
| 2 | Variables, Data Types, and Type Casting | [`02_variables_and_types.md`](02_variables_and_types.md) |
| 3 | Strings | [`03_strings.md`](03_strings.md) |
| 4 | Operators and Expressions | [`04_operators.md`](04_operators.md) |
| 5 | Control Flow | [`05_control_flow.md`](05_control_flow.md) |
| 6 | Lists, Tuples, Dictionaries, and Sets | [`06_collections.md`](06_collections.md) |
| 7 | Handling Errors | [`07_handling_errors.md`](07_handling_errors.md) |
| 8 | Functions | [`08_functions.md`](08_functions.md) |
| 9 | File Handling | [`09_file_handling.md`](09_file_handling.md) |
| 10 | Important Modules | [`10_important_modules.md`](10_important_modules.md) |
| 11 | Classes, Type Hints, Pydantic, Decorators and Async | [`11_advanced_python.md`](11_advanced_python.md) |

---

### Why these are not notebooks

A solved copy of a whole notebook is mostly the same slide prose you have already read, and only the filled in cells differ. So the answers live here as markdown you can read on GitHub without opening anything.

If you want a solved notebook you can actually run, build one:

```bash
python tools/build.py
```

That writes full solved notebooks into `.build/solutions/`, which is gitignored. The same files are what `python tools/build.py --run` executes to check every example in the course still works.

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
