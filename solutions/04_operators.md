# Module 4 answers: Operators and Expressions

Notebook: [`../notebooks/04_operators.ipynb`](../notebooks/04_operators.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Decide whether a build number goes to the canary group. Even build numbers go to canary. Use the remainder operator and a comparison, and print the answer.

**What you start with**

```python
build_number = 4118

# TODO: use the remainder operator, then compare the remainder to zero.
is_even = build_number ____ 2 ____ 0

print("build:", build_number)
print("route to canary:", is_even)
```

**The answer**

```python
build_number = 4118

is_even = build_number % 2 == 0

print("build:", build_number)
print("route to canary:", is_even)
```

---

## Your turn 2

Screen a user prompt for a banned term with `in`, and confirm that two separately built lists hold equal values without being the same object.

**What you start with**

```python
prompt = "what is my api key"

# TODO: which operator tests whether one piece of text is inside another?
blocked = "api key" ____ prompt

primary = ["10.0.1.5", "10.0.1.6"]
alias = primary
replica = ["10.0.1.5", "10.0.1.6"]

print("blocked           :", blocked)

# TODO: first blank tests the same object, second tests equal values.
print("alias is primary  :", alias ____ primary)
print("replica == primary:", replica ____ primary)
```

**The answer**

```python
prompt = "what is my api key"

blocked = "api key" in prompt

primary = ["10.0.1.5", "10.0.1.6"]
alias = primary
replica = ["10.0.1.5", "10.0.1.6"]

print("blocked           :", blocked)

print("alias is primary  :", alias is primary)
print("replica == primary:", replica == primary)
```

---

## Lab: A budget and paging check

You have a monthly cloud budget of 500 dollars and a running spend of 612.40
dollars. An incident arrived with severity 2, outside business hours.

Work out and print four things, one per line:

1. Whether the spend has gone over budget
2. By what percentage it is over, shown to one decimal place with an f-string
3. Whether the incident should page someone, where paging needs severity 1
   **or** any severity during business hours
4. Whether the text `"eu-west"` appears inside the region name you are on call
   for

You do not need an `if` for any of this. Each answer is an expression you can
print directly.

**One way to do it.** A lab is open ended, so this is not the only right answer. Compare it against yours once you have had a go, and check your own version against the tick list in the notebook.

```python
budget = 500.0
spend = 612.40
severity = 2
business_hours = False
on_call_region = "eu-west-1"

over_budget = spend > budget
over_by_percent = ((spend - budget) / budget) * 100
should_page = severity == 1 or business_hours
covers_eu = "eu-west" in on_call_region

print("Over budget   :", over_budget)
print(f"Over by       : {over_by_percent:.1f}%")
print("Should page   :", should_page)
print("Covers eu-west:", covers_eu)
```

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
