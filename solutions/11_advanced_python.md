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

There is no single right answer to a lab, so none is given here. Check your work against the checklist in the notebook. If it ticks every box and runs without an error, it is right.

---

*Utrains &middot; support@utrains.org &middot; https://utrains.org*
