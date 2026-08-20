# Module 5 answers: Control Flow

Notebook: [`../notebooks/05_control_flow.ipynb`](../notebooks/05_control_flow.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Print a countdown from 5 down to 1 using `range()`. You need all three arguments, because you are counting backwards.

**What you start with**

```python
# TODO: count down 5, 4, 3, 2, 1 using range(start, stop, step).
for n in range(____, ____, ____):
    print(f"restarting in {n}...")

print("restarting now")
```

**The answer**

```python
for n in range(5, 0, -1):
    print(f"restarting in {n}...")

print("restarting now")
```

---

## Your turn 2

Poll a resource up to five times, waiting for it to become ready. It becomes ready on the third attempt. Stop the loop the moment it is ready, rather than running the remaining attempts.

**What you start with**

```python
attempt = 0
ready_on = 3

# TODO: allow at most 5 attempts, and leave the loop early once ready.
while attempt < ____:
    attempt += 1
    print("attempt", attempt, "checking resource...")

    if attempt == ready_on:
        print("resource is ready")
        ____

print("finished after", attempt, "attempts")
```

**The answer**

```python
attempt = 0
ready_on = 3

while attempt < 5:
    attempt += 1
    print("attempt", attempt, "checking resource...")

    if attempt == ready_on:
        print("resource is ready")
        break

print("finished after", attempt, "attempts")
```

---

## Lab: A triage simulation

Work only with `range()`, strings, and the loop statements from this module.

First, loop over the severity levels 1, 2 and 3 with `range()`. For each one,
use an `if` / `elif` / `else` chain to print what happens: severity 1 pages the
on-call engineer, severity 2 logs a warning, anything else needs no action.

Second, count how many of those levels were page-level, using a counter you
update inside the loop, and print the total once the loop has finished.

Third, write a `while` loop that simulates up to six deployment attempts and
stops early with `break` on the fourth, printing the attempt number each time.

Fourth, loop over the string `"ERR404"` and use `continue` to skip the digits,
printing only the letters.

There is no single right answer to a lab, so none is given here. Check your work against the checklist in the notebook. If it ticks every box and runs without an error, it is right.

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
