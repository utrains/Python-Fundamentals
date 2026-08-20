# Module 6 answers: Lists, Tuples, Dictionaries, and Sets

Notebook: [`../notebooks/06_collections.ipynb`](../notebooks/06_collections.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Keep only the pipeline stages whose name contains `"test"`, using a list comprehension rather than a loop with append.

**What you start with**

```python
stages = ["build", "unit-test", "lint", "integration-test", "deploy"]

# TODO: complete the comprehension so only stages containing "test" survive.
test_stages = [s ____ s ____ stages ____ "test" ____ s]

print(test_stages)
```

**The answer**

```python
stages = ["build", "unit-test", "lint", "integration-test", "deploy"]

test_stages = [s for s in stages if "test" in s]

print(test_stages)
```

---

## Your turn 2

Total the instances across every region in a dictionary, then reduce a list of log codes to just the unique ones.

**What you start with**

```python
counts = {"us-east-1": 10, "eu-west-1": 8, "ap-south-1": 4}

# TODO: which dictionary method hands you just the numbers?
total = sum(counts.____())
print("total instances:", total)

log_codes = [500, 404, 500, 502, 404, 500]

# TODO: which collection type removes duplicates for you?
unique_codes = ____(log_codes)
print("unique codes:", sorted(unique_codes))
```

**The answer**

```python
counts = {"us-east-1": 10, "eu-west-1": 8, "ap-south-1": 4}

total = sum(counts.values())
print("total instances:", total)

log_codes = [500, 404, 500, 502, 404, 500]

unique_codes = set(log_codes)
print("unique codes:", sorted(unique_codes))
```

---

## Lab: Summarise a chat history

Build a list of dictionaries representing a short conversation, with at least
five turns alternating between `user` and `assistant`.

Then produce a summary that prints:

1. Only the assistant's replies, each on its own line, using a list
   comprehension rather than a loop with an `if` inside it
2. How many turns each role took, using a dictionary you build as you loop
3. The set of unique roles that appear
4. The longest message and which role sent it, found by comparing lengths as
   you loop rather than by eye

There is no single right answer to a lab, so none is given here. Check your work against the checklist in the notebook. If it ticks every box and runs without an error, it is right.

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
