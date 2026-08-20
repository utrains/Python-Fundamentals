# Module 10 answers: Important Modules

Notebook: [`../notebooks/10_important_modules.ipynb`](../notebooks/10_important_modules.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Measure how long a fake health check takes and print the answer to two decimal places. Two ideas here: the import statement, and the call that reads the clock.

**What you start with**

```python
# TODO: bring in the module that can pause and read the clock.
____ time


def run_healthcheck():
    time.sleep(0.25)
    return "healthy"


# TODO: read the clock before and after.
start = time.____()
status = run_healthcheck()
elapsed = time.____() - start

print(f"health check returned {status} in {elapsed:.2f}s")
```

**The answer**

```python
import time


def run_healthcheck():
    time.sleep(0.25)
    return "healthy"


start = time.time()
status = run_healthcheck()
elapsed = time.time() - start

print(f"health check returned {status} in {elapsed:.2f}s")
```

---

## Your turn 2

Extend the tiny agent with a second condition so it also answers a simple addition question, and still declines everything else.

**What you start with**

```python
def agent_node(state):
    question = state["question"].lower()

    if "weather" in question:
        answer = get_weather("Boston")
    # TODO: add a branch that catches a maths question, then a catch-all.
    ____ "plus" ____ question:
        answer = "That is 4."
    ____:
        answer = "I can only answer weather or simple maths right now."

    return {"answer": answer}


for q in ["What is the weather like?", "what is 2 plus 2", "Who won the game?"]:
    print(q, "->", agent_node({"question": q})["answer"])
```

**The answer**

```python
def agent_node(state):
    question = state["question"].lower()

    if "weather" in question:
        answer = get_weather("Boston")
    elif "plus" in question:
        answer = "That is 4."
    else:
        answer = "I can only answer weather or simple maths right now."

    return {"answer": answer}


for q in ["What is the weather like?", "what is 2 plus 2", "Who won the game?"]:
    print(q, "->", agent_node({"question": q})["answer"])
```

---

## Lab: A timed, config-driven health reporter

Write a small script in this notebook that does four things.

Read a model name from an environment variable called `LAB_MODEL`, falling back
to `"gpt-4o-mini"` when it is not set. Print the model, and separately print
whether an API key called `LAB_API_KEY` is present, without ever printing its
value.

Use `os.listdir` to count how many files sit in the current folder.

Time a fake `run_healthcheck()` function that sleeps briefly and returns a
status, and print the elapsed time to two decimal places.

Stamp the report with today's date using `datetime`.

Print all of it as one tidy report block.

There is no single right answer to a lab, so none is given here. Check your work against the checklist in the notebook. If it ticks every box and runs without an error, it is right.

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
