# Module 9 answers: File Handling

Notebook: [`../notebooks/09_file_handling.ipynb`](../notebooks/09_file_handling.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Append an incident summary to a running log, then read the whole log back. Pick the mode that adds to the end rather than wiping the file.

**What you start with**

```python
log_path = WORK / "incidents.log"

# TODO: choose the mode that ADDS to the end rather than overwriting.
with open(log_path, ____) as f:
    f.write("INC-4412 database connection failures resolved\n")

# TODO: choose the mode that reads.
with open(log_path, ____) as f:
    print(f.read())
```

**The answer**

```python
log_path = WORK / "incidents.log"

with open(log_path, "a") as f:
    f.write("INC-4412 database connection failures resolved\n")

with open(log_path, "r") as f:
    print(f.read())
```

---

## Your turn 2

Save a dictionary of resource tags to a JSON file and read one value back. Watch carefully which of the four json functions each step needs.

**What you start with**

```python
tags = {"env": "prod", "owner": "platform-team", "cost-center": "CC-1180"}

# TODO: write to a FILE, then read from a FILE. Mind the s.
with open(WORK / "tags.json", "w") as f:
    json.____(tags, f, indent=2)

with open(WORK / "tags.json", "r") as f:
    restored = json.____(f)

print(restored["owner"])
```

**The answer**

```python
tags = {"env": "prod", "owner": "platform-team", "cost-center": "CC-1180"}

with open(WORK / "tags.json", "w") as f:
    json.dump(tags, f, indent=2)

with open(WORK / "tags.json", "r") as f:
    restored = json.load(f)

print(restored["owner"])
```

---

## Lab: A server inventory round trip

Read `../data/servers.txt`, which holds one server name per line.

Turn it into a list of dictionaries, where each entry has a `name`, a `region`
taken from the part of the name after the first hyphen that follows the number,
and a `status` of `"unknown"`.

Save that list to `scratch/inventory.json` with an indent of 2, then read it
back from disk into a fresh variable, and print how many servers you recovered
and the name of the last one.

Finish by appending one audit line to `scratch/audit.log` recording how many
servers were processed. Run the whole lab twice: the audit log should have two
lines while the inventory JSON still holds the right count.

There is no single right answer to a lab, so none is given here. Check your work against the checklist in the notebook. If it ticks every box and runs without an error, it is right.

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
