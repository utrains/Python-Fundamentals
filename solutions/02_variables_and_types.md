# Module 2 answers: Variables, Data Types, and Type Casting

Notebook: [`../notebooks/02_variables_and_types.ipynb`](../notebooks/02_variables_and_types.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Test three values against the type you expect each one to be, and print the answers. Use the function that can also accept a tuple of types, not `type()`.

**What you start with**

```python
severity = 2
uptime = "99.98"
threshold = 1.5

# TODO: name the safe type test, then fill in each expected type.
print("severity is a whole number:", ____(severity, ____))
print("uptime is text            :", isinstance(uptime, ____))
print("threshold is a number     :", isinstance(threshold, (int, ____)))
```

**The answer**

```python
severity = 2
uptime = "99.98"
threshold = 1.5

print("severity is a whole number:", isinstance(severity, int))
print("uptime is text            :", isinstance(uptime, str))
print("threshold is a number     :", isinstance(threshold, (int, float)))
```

---

## Your turn 2

A cloud bill arrives as text. Convert it to a decimal number and print what a 10 percent increase would come to. `round(value, 2)` tidies the result to two decimal places.

**What you start with**

```python
bill = "248.50"

# TODO: cast the text to a decimal number, then apply the increase.
bill_value = ____(bill)
increased = bill_value ____ 1.10

print("Current         :", bill_value)
print("After 10 percent:", round(increased, 2))
print("Type after cast :", type(bill_value))
```

**The answer**

```python
bill = "248.50"

bill_value = float(bill)
increased = bill_value * 1.10

print("Current         :", bill_value)
print("After 10 percent:", round(increased, 2))
print("Type after cast :", type(bill_value))
```

---

## Lab: Describe a server safely

Store a server's CPU count as an `int`, its memory in GB as a `float`, its
hostname as a `str` and whether it is in production as a `bool`.

Print a one line summary using all four, with commas between them.

Then take the string `"0.9"`, which stands for a model temperature typed by a
user, cast it to a float, and print the result together with its type.

Use `isinstance()` to check that the cast really produced a float, and print
that check on its own line. You do not need an `if` for this, just print the
result of the check.

There is no single right answer to a lab, so none is given here. Check your work against the checklist in the notebook. If it ticks every box and runs without an error, it is right.

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
