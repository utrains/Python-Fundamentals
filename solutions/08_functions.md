# Module 8 answers: Functions

Notebook: [`../notebooks/08_functions.ipynb`](../notebooks/08_functions.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Write a deployment message builder. The service is passed by position, the environment has a default of `"dev"`, and the message is handed back to the caller rather than printed inside the function.

**What you start with**

```python
# TODO: give environment a default of "dev", and send the message back.
def deployment_message(service, environment____):
    ____ f"Deploying {service} to {environment}"


print(deployment_message("api-gateway"))
print(deployment_message("api-gateway", environment="prod"))
```

**The answer**

```python
def deployment_message(service, environment="dev"):
    return f"Deploying {service} to {environment}"


print(deployment_message("api-gateway"))
print(deployment_message("api-gateway", environment="prod"))
```

---

## Your turn 2

Write a generator that yields incident status updates one at a time, then a runner that takes any function as a value and applies it to a message.

**What you start with**

```python
updates = ["triage started", "root cause found", "fix deployed", "resolved"]


def status_stream(items):
    for item in items:
        # TODO: hand back one value at a time WITHOUT ending the function.
        ____ f"[update] {item}"


for line in status_stream(updates):
    print(line)


def process(callback, message):
    # TODO: call whatever function was handed in.
    return ____(message)


def shout(text):
    return text.upper()


# TODO: pass the function itself, not its result.
print(process(____, "incident closed"))
```

**The answer**

```python
updates = ["triage started", "root cause found", "fix deployed", "resolved"]


def status_stream(items):
    for item in items:
        yield f"[update] {item}"


for line in status_stream(updates):
    print(line)


def process(callback, message):
    return callback(message)


def shout(text):
    return text.upper()


print(process(shout, "incident closed"))
```

---

## Lab: A small cost calculator toolkit

Write three functions that work together, one for each of the ideas in this
module.

`monthly_cost(*resources)` takes any number of per-resource monthly costs and
returns the total.

`format_bill(total, currency="USD", warn_above=500)` returns a formatted string
with the total to two decimal places, and appends `" OVER BUDGET"` when the
total is above the threshold. Both extra parameters must have working defaults.

`report(builder, *resources)` takes a **function** as its first argument, calls
`monthly_cost` on the resources, passes the total to `builder`, and returns the
result.

Prove all three work by calling `report(format_bill, 120.0, 340.5, 88.25)`.

For extra credit, add a generator that yields each resource cost as a running
total, the way `stream_reply` did.

**One way to do it.** A lab is open ended, so this is not the only right answer. Compare it against yours once you have had a go, and check your own version against the tick list in the notebook.

```python
def monthly_cost(*resources):
    return sum(resources)


def format_bill(total, currency="USD", warn_above=500):
    line = f"{currency} {total:.2f}"
    if total > warn_above:
        line += " OVER BUDGET"
    return line


def report(builder, *resources):
    total = monthly_cost(*resources)
    return builder(total)


print(report(format_bill, 120.0, 340.5, 88.25))
print(report(format_bill, 10.0, 20.0))

print()


# extra credit: the same costs, yielded as a running total
def running_total(*resources):
    total = 0
    for cost in resources:
        total += cost
        yield total


for so_far in running_total(120.0, 340.5, 88.25):
    print(f"running total: {so_far:.2f}")
```

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
