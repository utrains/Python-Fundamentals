# Module 3 answers: Strings

Notebook: [`../notebooks/03_strings.ipynb`](../notebooks/03_strings.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Pull the region code out of an instance id using slicing only. The region is everything after the last hyphen, and it is nine characters long.

**What you start with**

```python
instance_id = "i-0123456789-us-east-1"

# TODO: slice the last nine characters, then slice off the leading "i-".
region = instance_id[____:]
prefix = instance_id[:____]

print("region:", region)
print("prefix:", prefix)
```

**The answer**

```python
instance_id = "i-0123456789-us-east-1"

region = instance_id[-9:]
prefix = instance_id[:2]

print("region:", region)
print("prefix:", prefix)
```

---

## Your turn 2

Build a status line with an f-string. Put the service name in upper case and show the uptime to two decimal places.

**What you start with**

```python
service = "auth-service"
uptime = 99.9812

# TODO: mark this as an f-string, upper case the name, round to 2 places.
line = ____"{service.____()} uptime={uptime:____}%"

print(line)
```

**The answer**

```python
service = "auth-service"
uptime = 99.9812

line = f"{service.upper()} uptime={uptime:.2f}%"

print(line)
```

---

## Lab: Parse a log line

You are given this log line:

```
2024-08-19 [ERROR] payment-service | Database Connection Failed | retry=3
```

Pull it apart and print each piece on its own labelled line: the date, the
severity without its square brackets, the service name, the message, and the
retry count as a number rather than as text.

Use slicing for the date, `split()` for the fields, `strip()` to clean up the
spaces that splitting leaves behind, and `int()` from Module 2 for the retry
count.

Finish with an f-string that reassembles a one line summary.

**One way to do it.** A lab is open ended, so this is not the only right answer. Compare it against yours once you have had a go, and check your own version against the tick list in the notebook.

```python
line = "2024-08-19 [ERROR] payment-service | Database Connection Failed | retry=3"

date = line[:10]
rest = line[11:]

severity = rest.split("]")[0].strip("[")

fields = rest.split("|")
service = fields[0].split("]")[1].strip()
message = fields[1].strip()
retry = int(fields[2].split("=")[1])

print("Date    :", date)
print("Severity:", severity)
print("Service :", service)
print("Message :", message)
print("Retry   :", retry, type(retry))

print()
print(f"{date} {severity} on {service}: {message} (retry {retry})")
```

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
