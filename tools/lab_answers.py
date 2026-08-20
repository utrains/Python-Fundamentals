"""One worked answer per lab.

A lab is open ended, so these are not the only right answers. They are a
complete, working version a student can compare against once they have had a
go themselves.

Each one stays inside its module's vocabulary, the same rule the exercises
follow, and each is executed by `python tools/build.py --run` along with
everything else, so none of them can quietly rot.
"""

ANSWERS = {

    # ---------------------------------------------------------------- 1
    1: '''
service = "payment-gateway"
latency_ms = 45
status = "OK"

print("=== Utrains health check ===")
print("Service:", service, "| Latency:", latency_ms, "ms | Status:", status)

total_requests = 5000
failed_requests = 12

print("Error rate:", (failed_requests / total_requests) * 100, "%")

print("Token 1 ", end="", flush=True)
print("Token 2 ", end="", flush=True)
print("Token 3")
''',

    # ---------------------------------------------------------------- 2
    2: '''
cpu_count = 4
memory_gb = 16.5
hostname = "web-01"
in_production = True

print("Host:", hostname, "| CPUs:", cpu_count, "| Memory:", memory_gb,
      "GB | Production:", in_production)

# The temperature arrives as text, the way input() would hand it to you.
temperature_text = "0.9"
temperature = float(temperature_text)

print("Temperature     :", temperature, type(temperature))
print("Cast gave a float:", isinstance(temperature, float))
print("Still text?      :", isinstance(temperature_text, str))
''',

    # ---------------------------------------------------------------- 3
    3: '''
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
''',

    # ---------------------------------------------------------------- 4
    4: '''
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
''',

    # ---------------------------------------------------------------- 5
    5: '''
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
''',

    # ---------------------------------------------------------------- 6
    6: '''
messages = [
    {"role": "user", "content": "Hi, I am Serge."},
    {"role": "assistant", "content": "Hello Serge! Nice to meet you."},
    {"role": "user", "content": "What was covered in week 2?"},
    {"role": "assistant", "content": "Linux, SSH keys and file permissions."},
    {"role": "user", "content": "Thanks."},
]

# 1. only the assistant's replies, with a comprehension
replies = [m["content"] for m in messages if m["role"] == "assistant"]

print("Assistant replies:")
for reply in replies:
    print(" -", reply)

# 2. turns per role, built as you loop
counts = {}
for m in messages:
    counts[m["role"]] = counts.get(m["role"], 0) + 1

print()
print("Turns per role:", counts)

# 3. the unique roles
roles = set(m["role"] for m in messages)
print("Unique roles  :", roles)

# 4. the longest message, found by comparing lengths
longest = messages[0]
for m in messages:
    if len(m["content"]) > len(longest["content"]):
        longest = m

print()
print(f"Longest came from {longest['role']}: {longest['content']}")
''',

    # ---------------------------------------------------------------- 7
    7: '''
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
''',

    # ---------------------------------------------------------------- 8
    8: '''
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
''',

    # ---------------------------------------------------------------- 9
    9: '''
import json
from pathlib import Path

WORK = Path("scratch")
WORK.mkdir(exist_ok=True)

servers_file = Path("..") / "data" / "servers.txt"

inventory = []

with open(servers_file) as f:
    for line in f:
        name = line.strip()
        if not name:
            continue
        parts = name.split("-")
        inventory.append({
            "name": name,
            "region": "-".join(parts[2:]),
            "status": "unknown",
        })

with open(WORK / "inventory.json", "w") as f:
    json.dump(inventory, f, indent=2)

with open(WORK / "inventory.json") as f:
    restored = json.load(f)

print("servers recovered:", len(restored))
print("last one         :", restored[-1]["name"], "in", restored[-1]["region"])

with open(WORK / "audit.log", "a") as f:
    f.write(f"processed {len(restored)} servers\\n")

with open(WORK / "audit.log") as f:
    print()
    print("audit log now holds", len(f.readlines()), "line(s)")
    print("run the cell again and that number goes up")
''',

    # --------------------------------------------------------------- 10
    10: '''
import os
import time
import datetime as dt

MODEL = os.environ.get("LAB_MODEL", "gpt-4o-mini")
api_key = os.environ.get("LAB_API_KEY")


def run_healthcheck():
    time.sleep(0.2)
    return "healthy"


start = time.time()
status = run_healthcheck()
elapsed = time.time() - start

file_count = len(os.listdir("."))

print("=== health report ===")
print("date         :", dt.date.today())
print("model        :", MODEL)
print("API key set  :", bool(api_key))     # never the key itself
print("files here   :", file_count)
print(f"health check : {status} in {elapsed:.2f}s")
''',

    # --------------------------------------------------------------- 11
    11: '''
import asyncio
import time

from pydantic import BaseModel, ValidationError


class ChatTurn(BaseModel):
    role: str
    content: str


# prove it rejects a bad role
try:
    ChatTurn(role=123, content="nope")
    print("that should not have been accepted")
except ValidationError:
    print("ChatTurn rejected a numeric role, as it should")


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.3f}s")
        return result
    return wrapper


class ChatClient:
    def __init__(self, model):
        self.model = model
        self.history = []

    async def ask(self, message):
        await asyncio.sleep(0.2)          # stands in for the network
        self.history.append(ChatTurn(role="user", content=message))
        reply = f"[{self.model}] reply to: {message}"
        self.history.append(ChatTurn(role="assistant", content=reply))
        return reply

    @timed
    def report(self):
        for turn in self.history:
            print(f"  {turn.role:>9}: {turn.content}")
        return len(self.history)


client = ChatClient("claude-sonnet-4-6")

start = time.time()
replies = await asyncio.gather(
    client.ask("What is my name?"),
    client.ask("What was covered in week 2?"),
    client.ask("Summarise that."),
)
print(f"three questions answered in {time.time() - start:.2f}s, not 0.60s")

print()
turns = client.report()
print("history holds", turns, "turns")
''',
}
