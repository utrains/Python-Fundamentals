# Module 1 answers: Getting Started with Python

Notebook: [`../notebooks/01_getting_started.ipynb`](../notebooks/01_getting_started.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Print a deployment banner on a single line, built from three separate `print()` calls. Only the last one may break onto a new line.

**What you start with**

```python
# TODO: fill in the blanks so all three pieces land on ONE line.
print("Deploying ", end=____, flush=True)
print("payment-gateway ", ____="", flush=True)
print("to us-east-1")
```

**The answer**

```python
print("Deploying ", end="", flush=True)
print("payment-gateway ", end="", flush=True)
print("to us-east-1")
```

---

## Your turn 2

Build a deployment tag the same way, joining a region and an environment with a hyphen between them, then print it with a label.

**What you start with**

```python
# TODO: join the two pieces with a hyphen, then print with a label.
region = "eu-west-1"
environment = "stage"

deploy_tag = region ____ "-" ____ environment
____("Artifact tag:", deploy_tag)
```

**The answer**

```python
region = "eu-west-1"
environment = "stage"

deploy_tag = region + "-" + environment
print("Artifact tag:", deploy_tag)
```

---

## Lab: Your first health check banner

Store a service name, a latency in milliseconds and a status in three separate
values.

Print a banner line on its own. Then print the service, latency and status
together in a single `print()` call, using commas to separate them.

Work out the error rate as a percentage from a total request count and a failed
count, and print it.

Finish by printing three fake response tokens on the same line using `end` and
`flush`, followed by a final line break.

Everything you need is `print()`, the arithmetic operators, and joining text
with `+`.

There is no single right answer to a lab, so none is given here. Check your work against the checklist in the notebook. If it ticks every box and runs without an error, it is right.

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
