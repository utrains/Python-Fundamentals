# Module 7 answers: Handling Errors

Notebook: [`../notebooks/07_handling_errors.ipynb`](../notebooks/07_handling_errors.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

An incident ticket must always end up marked closed, even when the update step fails. Pick the two keywords that catch the failure and guarantee the closing step.

**What you start with**

```python
ticket = {"id": "INC-4412", "status": "open"}

# TODO: catch the failure, then guarantee the closing step always runs.
try:
    raise ConnectionError("ticketing system unreachable")
____ ConnectionError as e:
    print("could not update:", e)
____:
    ticket["status"] = "closed"

print(ticket)
```

**The answer**

```python
ticket = {"id": "INC-4412", "status": "open"}

try:
    raise ConnectionError("ticketing system unreachable")
except ConnectionError as e:
    print("could not update:", e)
finally:
    ticket["status"] = "closed"

print(ticket)
```

---

## Your turn 2

Guard a model temperature setting. Anything outside 0.0 to 2.0 should signal a problem with a clear message, and the caller should catch it and read that message.

**What you start with**

```python
def set_temperature(value):
    if value < 0.0 or value > 2.0:
        # TODO: signal the problem yourself, with the right error type.
        ____ ____(f"temperature {value} is outside 0.0 to 2.0")
    return value


print("valid:", set_temperature(0.7))

# TODO: catch it, and capture the message so it can be printed.
try:
    set_temperature(3.5)
except ValueError ____ e:
    print("rejected:", e)
```

**The answer**

```python
def set_temperature(value):
    if value < 0.0 or value > 2.0:
        raise ValueError(f"temperature {value} is outside 0.0 to 2.0")
    return value


print("valid:", set_temperature(0.7))

try:
    set_temperature(3.5)
except ValueError as e:
    print("rejected:", e)
```

---

## Lab: A deployment run that refuses to crash

Write a function `deploy(stage)` that raises a `RuntimeError` when the stage
name is `"migrate"`, and otherwise returns a success message.

Loop over the stages `build`, `test`, `migrate`, `release` and call `deploy()`
for each one. A failing stage must not stop the others.

Record every outcome in a results dictionary. Use `finally` so a line is always
printed for each stage, whether it succeeded or not. At the end, print how many
stages succeeded and how many failed.

For extra credit, wrap the `migrate` stage in the retry pattern from slide 5,
giving it three attempts before recording it as failed.

**One way to do it.** A lab is open ended, so this is not the only right answer. Compare it against yours once you have had a go, and check your own version against the tick list in the notebook.

```python
def deploy(stage):
    if stage == "migrate":
        raise RuntimeError("schema lock timeout")
    return f"{stage} completed"


stages = ["build", "test", "migrate", "release"]
results = {}

for stage in stages:
    try:
        results[stage] = deploy(stage)
    except RuntimeError as e:
        results[stage] = f"FAILED: {e}"
    finally:
        # runs for every stage, whether it worked or not
        print(f"{stage:8s} -> {results[stage]}")

succeeded = 0
failed = 0

for outcome in results.values():
    if outcome.startswith("FAILED"):
        failed += 1
    else:
        succeeded += 1

print()
print(f"{succeeded} succeeded, {failed} failed")
```

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
