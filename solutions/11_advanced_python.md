# Module 11 answers: Classes, Type Hints, Pydantic, Decorators and Async

Notebook: [`../notebooks/11_advanced_python.ipynb`](../notebooks/11_advanced_python.ipynb)

Try each one yourself before reading on. The attempt is worth more than the answer.

---

## Your turn 1

Write a `Deployment` class that starts as pending and can be marked complete. Fill in the constructor's name and the reference to the object itself.

**What you start with**

```python
class Deployment:
    # TODO: name the constructor, and store both values on the object.
    def ____(self, service):
        ____.service = service
        ____.status = "pending"

    def complete(self):
        # TODO: change this object's own status.
        ____.status = "done"


d = Deployment("api-gateway")
print(d.service, "->", d.status)

d.complete()
print(d.service, "->", d.status)
```

**The answer**

```python
class Deployment:
    def __init__(self, service):
        self.service = service
        self.status = "pending"

    def complete(self):
        self.status = "done"


d = Deployment("api-gateway")
print(d.service, "->", d.status)

d.complete()
print(d.service, "->", d.status)
```

---

## Your turn 2

Validate a cloud resource request with Pydantic, then run three fake model calls at the same time.

**What you start with**

```python
from pydantic import BaseModel
import asyncio


# TODO: inherit from the Pydantic base class, and give each field a type.
class ResourceRequest(____):
    name: ____
    region: ____
    size: ____


req = ResourceRequest(name="web-01", region="us-east-1", size=2)
print(req)


async def fake_call(n):
    await asyncio.sleep(0.2)
    return f"call {n} done"


# TODO: which asyncio function runs them all together?
results = await asyncio.____(fake_call(1), fake_call(2), fake_call(3))
print(results)
```

**The answer**

```python
from pydantic import BaseModel
import asyncio


class ResourceRequest(BaseModel):
    name: str
    region: str
    size: int


req = ResourceRequest(name="web-01", region="us-east-1", size=2)
print(req)


async def fake_call(n):
    await asyncio.sleep(0.2)
    return f"call {n} done"


results = await asyncio.gather(fake_call(1), fake_call(2), fake_call(3))
print(results)
```

---

## Lab: A validated, timed, async chat client

Put the whole module together.

Define a Pydantic model `ChatTurn` with a `role` and a `content`, both strings.
Prove it rejects a turn where `role` is a number.

Write a `ChatClient` class that holds a model name and a list of `ChatTurn`
objects. Give it an `async def ask(self, message)` method that sleeps briefly
to simulate the network, appends both the user turn and the assistant reply to
its history, and returns the reply.

Write your own `@timed` decorator and put it on a `report()` method, so
printing the history also prints how long it took.

Finally, use `asyncio.gather` to ask three questions concurrently, then print
the full history and confirm it holds six turns.

**One way to do it.** A lab is open ended, so this is not the only right answer. Compare it against yours once you have had a go, and check your own version against the tick list in the notebook.

```python
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
```

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
