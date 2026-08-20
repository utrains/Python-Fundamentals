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

**One way to do it.** A lab is open ended, so this is not the only right answer. Compare it against yours once you have had a go, and check your own version against the tick list in the notebook.

```python
# 1. classify each severity level
page_count = 0

for severity in range(1, 4):
    if severity == 1:
        print(f"severity {severity}: paging the on-call engineer")
        page_count += 1
    elif severity == 2:
        print(f"severity {severity}: logging a warning")
    else:
        print(f"severity {severity}: no action required")

# 2. the counter, printed once the loop has finished
print("page level incidents:", page_count)
print()

# 3. up to six attempts, stopping early on the fourth
attempt = 0

while attempt < 6:
    attempt += 1
    print("deployment attempt", attempt)

    if attempt == 4:
        print("deployment succeeded")
        break

print()

# 4. skip the digits, print only the letters
for char in "ERR404":
    if char in "0123456789":
        continue
    print(char, end="")

print()
```

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
