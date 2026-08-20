"""Extra worked use cases, three or four per module.

The decks teach each idea once, with one small example. That is right for a
slide and thin for practice. These are more situations per module, each one a
thing you would actually do, using only what the module has taught by that
point.

Most of them are the AI work this course leads into: prompts, tokens, context
windows, streaming replies, rate limits, model responses and run logs. Those
are marked **AI** in the title. The rest are the infrastructure jobs the same
syntax turns up in.

They are spliced into the notebook after the last slide and before the lab, so
the shape stays: learn it, see it used several ways, do it yourself, then the
lab.

Each entry is (title, why it matters, code). The title and the code go into the
notebook; the explanation goes into the README, the same split the slides use.
"""

CASES = {

# ==================================================================== 1
1: [
    (
        "AI &middot; What did that API call cost?",
        "Model pricing is quoted per million tokens, so working out the cost "
        "of one call is two multiplications and an addition. Do this early and "
        "often: the difference between a cheap prompt and an expensive one is "
        "usually a decision you made without noticing.\n\n"
        "One of the numbers below prints with a long tail of digits. That is "
        "how computers store decimals, not a mistake. Module 3's f-strings are "
        "what tidy it up.",
        '''
input_tokens = 1_450
output_tokens = 320

input_price_per_million = 3.00
output_price_per_million = 15.00

input_cost = (input_tokens / 1_000_000) * input_price_per_million
output_cost = (output_tokens / 1_000_000) * output_price_per_million

print("input tokens :", input_tokens, "costing", input_cost)
print("output tokens:", output_tokens, "costing", output_cost)
print("this call    :", input_cost + output_cost)
print("10,000 calls :", (input_cost + output_cost) * 10000)

# One of those numbers has a long tail of digits. That is not a bug: it is
# how computers store decimals. Module 3 shows how to print it to 4 places.
''',
    ),
    (
        "AI &middot; A reply arriving token by token",
        "A model does not hand you a finished answer, it sends pieces. The end "
        "and flush pair from the slide is exactly what puts those pieces on "
        "one line as they arrive, instead of a screenful of fragments.",
        '''
print("Assistant: ", end="", flush=True)
print("The ", end="", flush=True)
print("target ", end="", flush=True)
print("group ", end="", flush=True)
print("is ", end="", flush=True)
print("unhealthy.")

print()
print("Thinking ", end="", flush=True)
print("." * 3, end="", flush=True)
print(" done")
''',
    ),
    (
        "A deployment banner",
        "Multiplying a string repeats it, which is the quickest way to draw a "
        "rule across the terminal. Every deployment script prints something "
        "like this so a human scrolling the logs can find where a run began.",
        '''
line = "=" * 46

print(line)
print("  UTRAINS DEPLOYMENT  |  payment-gateway 2.1.0")
print(line)
print("  target   : us-east-1")
print("  triggered: automatic")
print(line)
''',
    ),
    (
        "What will this infrastructure cost?",
        "The same arithmetic, pointed at servers instead of tokens. Three "
        "instances, on all month, at an hourly rate. Working it out is the "
        "easy part; remembering to do it before you launch is the habit.",
        '''
instances = 3
hours_per_month = 730
rate_per_hour = 0.0416

monthly = instances * hours_per_month * rate_per_hour

print("Instances    :", instances)
print("Monthly cost :", monthly)
print("Yearly cost  :", monthly * 12)
''',
    ),
],

# ==================================================================== 2
2: [
    (
        "AI &middot; Model settings arrive as text",
        "Every setting read from an environment variable or a config file is a "
        "string, whatever it looks like. Hand a string temperature to an SDK "
        "and you get an error at the worst moment; hand it a string "
        "max_tokens and some libraries silently do the wrong thing.",
        '''
temperature_text = "0.7"
max_tokens_text = "512"
stream_text = "1"

temperature = float(temperature_text)
max_tokens = int(max_tokens_text)
stream = bool(int(stream_text))

print("temperature:", temperature, type(temperature))
print("max_tokens :", max_tokens, type(max_tokens))
print("stream     :", stream, type(stream))

print()
print("as text, this would have been wrong:", max_tokens_text + max_tokens_text)
print("as numbers, it is right             :", max_tokens + max_tokens)
''',
    ),
    (
        "AI &middot; None means no reply yet",
        "None is not zero and it is not an empty string. It is the value a "
        "reply holds before the model has answered. All three look empty and "
        "all three are different types, which matters when you decide whether "
        "to retry, and matters again in Module 4 when you start comparing.",
        '''
reply = None              # the model has not answered yet
tokens_used = 0           # it answered, and used nothing
empty_reply = ""          # it answered with nothing at all

print("reply      :", reply, type(reply))
print("tokens used:", tokens_used, type(tokens_used))
print("empty reply:", repr(empty_reply), type(empty_reply))

print()
print("three different types, and every one of them is falsy:")
print("  bool(None):", bool(reply))
print("  bool(0)   :", bool(tokens_used))
print('  bool("")  :', bool(empty_reply))
''',
    ),
    (
        "The truthiness gotcha",
        "bool() turns anything into True or False, and the surprises are worth "
        "seeing now rather than in a config parser at midnight. The string "
        '"0" is True, because it is a string with a character in it.',
        '''
print('bool(1)       ->', bool(1))
print('bool(0)       ->', bool(0))
print('bool(0.0)     ->', bool(0.0))
print('bool("")      ->', bool(""))
print('bool("0")     ->', bool("0"))       # a non-empty string
print('bool("False") ->', bool("False"))   # also non-empty
print('bool(None)    ->', bool(None))
''',
    ),
],

# ==================================================================== 3
3: [
    (
        "AI &middot; Assemble a system prompt from parts",
        "A long prompt built as one triple-quoted block becomes unreadable and "
        "hard to edit. Joining short literals inside parentheses, the pattern "
        "from slide 4, keeps each rule on its own line where you can change "
        "one without disturbing the rest.",
        '''
persona = "senior SRE assistant"
max_steps = 3

SYSTEM_PROMPT = (
    f"You are a {persona}.\\n"
    f"Give at most {max_steps} diagnostic steps.\\n"
    "Each step must be one short sentence.\\n"
    "No preamble. No apology. No markdown.\\n"
)

print(SYSTEM_PROMPT)
print("characters:", len(SYSTEM_PROMPT))
print("rough tokens:", len(SYSTEM_PROMPT) // 4)
''',
    ),
    (
        "AI &middot; Mask a key before it reaches a log",
        "Sometimes you need to show which key is in use without showing the "
        "key. Slicing the front and the back and hiding the middle gives you "
        "something identifiable that is useless if it leaks.",
        '''
api_key = "sk-proj-9f2b7c41a8de4b0f93e2"

masked = api_key[:7] + "..." + api_key[-4:]

print("using key:", masked)
print("length   :", len(api_key), "characters")
print("looks like a project key:", api_key.startswith("sk-proj-"))

# never do this, in any environment
# print(api_key)
''',
    ),
    (
        "AI &middot; Pull the answer out of a raw response",
        "Before you learn JSON parsing in Module 9, you can still get at the "
        "content of a response with the string methods from this module. It is "
        "also a fair description of what a parser does underneath.",
        '''
raw = 'assistant: The capital of France is Paris. [tokens=8]'

speaker = raw.split(":")[0].strip()
body = raw.split(":", 1)[1]
answer = body.split("[")[0].strip()
tokens = int(raw.split("tokens=")[1].strip("]"))

print("speaker:", speaker)
print("answer :", answer)
print("tokens :", tokens, type(tokens))

print()
print(f"{speaker.title()} replied in {tokens} tokens: {answer!r}")
''',
    ),
    (
        "Normalise a service name",
        "Names arrive inconsistently: extra spaces, mixed case, underscores "
        "where hyphens belong. Cleaning them the same way every time is what "
        "stops two spellings of one service becoming two rows in a report.",
        '''
raw = "  Payment_Gateway  "

clean = raw.strip().lower().replace("_", "-")

print("raw   :", repr(raw))
print("clean :", repr(clean))
print("starts with 'pay':", clean.startswith("pay"))
''',
    ),
],

# ==================================================================== 4
4: [
    (
        "AI &middot; Will this prompt fit in the context window?",
        "Every model has a hard limit, and it has to hold the prompt and the "
        "answer. Checking before you send is the difference between a clear "
        "message from your own code and a rejection from the API.",
        '''
context_window = 8192
system_tokens = 240
history_tokens = 5100
question_tokens = 180
max_output = 1000

prompt_total = system_tokens + history_tokens + question_tokens
needed = prompt_total + max_output
headroom = context_window - needed

print("prompt tokens:", prompt_total)
print("plus output  :", needed)
print("window       :", context_window)
print("headroom     :", headroom)
print("it fits      :", needed <= context_window)
print("cutting it fine:", needed <= context_window and headroom < 500)
''',
    ),
    (
        "AI &middot; Are these settings valid?",
        "Range checks are two comparisons joined with and. Doing them yourself "
        "gives a message that says which setting is wrong, instead of a stack "
        "trace from somebody else's library.",
        '''
temperature = 0.7
top_p = 1.4
max_tokens = 512

temperature_ok = 0.0 <= temperature <= 2.0
top_p_ok = 0.0 <= top_p <= 1.0
max_tokens_ok = 1 <= max_tokens <= 4096

print("temperature", temperature, "valid:", temperature_ok)
print("top_p      ", top_p, "valid:", top_p_ok)
print("max_tokens ", max_tokens, "valid:", max_tokens_ok)

print()
print("safe to send:", temperature_ok and top_p_ok and max_tokens_ok)
print("something is wrong:", not (temperature_ok and top_p_ok and max_tokens_ok))
''',
    ),
    (
        "AI &middot; Spread calls across a pool of keys",
        "The remainder operator spreads work evenly over a fixed number of "
        "things. With API keys it keeps any one key from hitting its rate "
        "limit first, and the choice is repeatable rather than random.",
        '''
key_count = 3

print("request 7  -> key", 7 % key_count)
print("request 8  -> key", 8 % key_count)
print("request 9  -> key", 9 % key_count)
print("request 10 -> key", 10 % key_count)

# the same idea, deciding which shard a user's embeddings live on
user_id = 90210
print()
print("user", user_id, "-> shard", user_id % 16)
''',
    ),
    (
        "Disk headroom",
        "Floor division converts units without leaving a decimal tail, and a "
        "comparison turns the number into the decision you actually want: is "
        "this worth waking someone up for.",
        '''
used_gb = 823
total_gb = 1000

percent_used = (used_gb / total_gb) * 100
free_gb = total_gb - used_gb

print(f"used: {percent_used:.1f}%")
print("free:", free_gb, "GB")
print("over the warning line:", percent_used > 80)
print("critical             :", percent_used > 90 and free_gb < 50)
''',
    ),
],

# ==================================================================== 5
5: [
    (
        "AI &middot; Back off when you hit a rate limit",
        "A 429 means slow down, and retrying immediately makes it worse. "
        "Doubling the wait each time is what every serious client library does "
        "underneath, and it is a while loop with one multiplication.",
        '''
attempt = 0
wait = 1

while attempt < 5:
    attempt += 1
    print(f"attempt {attempt}: rate limited, waiting {wait}s")
    wait = wait * 2

    if attempt == 4:
        print("request accepted")
        break

print("attempts used:", attempt)
print("would have waited", 1 + 2 + 4, "seconds in total")
''',
    ),
    (
        "AI &middot; Stream a reply and stop at the sentinel",
        "A streamed answer arrives piece by piece, and some models mark the "
        "end with a stop sequence rather than simply closing. break is how you "
        "leave the loop the moment you see it, instead of printing the marker.",
        '''
stream = "The target group is unhealthy.<END>Ignore everything after this."

reply = ""

for char in stream:
    if char == "<":
        print()
        print("stop sequence reached, ignoring the rest")
        break
    reply += char
    print(char, end="", flush=True)

print()
print("captured:", repr(reply))
print("characters kept:", len(reply), "of", len(stream))
''',
    ),
    (
        "AI &middot; Count the failures in a run history",
        "A counter outside the loop, updated inside it, is the pattern behind "
        "every tally you will write. Here it is turning a run of results into "
        "the success rate you would put on a dashboard.",
        '''
run_history = "SSSFSSSSFSSFSSS"

passed = 0
failed = 0

for result in run_history:
    if result == "S":
        passed += 1
    else:
        failed += 1

print("runs   :", len(run_history))
print("passed :", passed)
print("failed :", failed)
print(f"success: {(passed / len(run_history)) * 100:.1f}%")
print("healthy:", failed < 4)
''',
    ),
    (
        "Classify a run of status codes",
        "An if and elif chain inside a loop is how a log processor decides "
        "what each line means. This one walks a range of codes rather than a "
        "list, because lists arrive in the next module.",
        '''
for code in range(500, 505):
    if code == 500:
        print(code, "internal error, check the application logs")
    elif code == 502:
        print(code, "bad gateway, the upstream did not answer")
    elif code == 503:
        print(code, "service unavailable, probably still starting")
    elif code == 504:
        print(code, "gateway timeout, the upstream was too slow")
    else:
        print(code, "unrecognised, look it up")
''',
    ),
],

# ==================================================================== 6
6: [
    (
        "AI &middot; How big is this conversation?",
        "Chat history is a list of dictionaries, so measuring it is a loop and "
        "a sum. A rough count of four characters per token is close enough to "
        "tell you whether you are approaching a model's limit.",
        '''
messages = [
    {"role": "system", "content": "You are a senior SRE assistant."},
    {"role": "user", "content": "The api-gateway is returning 502s."},
    {"role": "assistant", "content": "Check the target group health first."},
    {"role": "user", "content": "Two of three targets are unhealthy."},
]

characters = sum(len(m["content"]) for m in messages)
rough_tokens = characters // 4

print("turns       :", len(messages))
print("characters  :", characters)
print("rough tokens:", rough_tokens)
print("roles       :", sorted(set(m["role"] for m in messages)))
print("longest turn:", max(len(m["content"]) for m in messages), "characters")
''',
    ),
    (
        "AI &middot; Trim a history that has grown too long",
        "When a conversation outgrows the context window you drop the middle, "
        "not the ends. The system prompt sets the behaviour and the recent "
        "turns carry the thread, so those are the ones worth keeping.",
        '''
history = [
    {"role": "system", "content": "You are a senior SRE assistant."},
    {"role": "user", "content": "turn 1"},
    {"role": "assistant", "content": "reply 1"},
    {"role": "user", "content": "turn 2"},
    {"role": "assistant", "content": "reply 2"},
    {"role": "user", "content": "turn 3"},
    {"role": "assistant", "content": "reply 3"},
]

keep_last = 4

system = [m for m in history if m["role"] == "system"]
rest = [m for m in history if m["role"] != "system"]
trimmed = system + rest[-keep_last:]

print("before:", len(history), "turns")
print("after :", len(trimmed), "turns")
print()
for m in trimmed:
    print(f"  {m['role']:>9}: {m['content']}")
''',
    ),
    (
        "AI &middot; Which documents came back more than once?",
        "A retrieval step often returns the same document from several "
        "queries. A set gives you the unique ids, and a dictionary counts how "
        "often each one appeared, which is a crude but useful relevance score.",
        '''
retrieved = ["doc-4", "doc-1", "doc-4", "doc-9", "doc-1", "doc-4"]

hits = {}
for doc in retrieved:
    hits[doc] = hits.get(doc, 0) + 1

unique = sorted(set(retrieved))

print("retrieved     :", retrieved)
print("unique docs   :", unique)
print("hit counts    :", hits)
print("most relevant :", max(hits, key=hits.get))
print("seen once only:", [d for d in unique if hits[d] == 1])
''',
    ),
    (
        "Group instances by region",
        "A dictionary whose values are lists is the shape of almost every "
        "grouping job. Build it as you loop, creating the empty list the first "
        "time you meet a new key.",
        '''
instances = [
    ("web-01", "us-east-1"),
    ("web-02", "us-east-1"),
    ("api-01", "eu-west-1"),
    ("db-01", "eu-west-1"),
    ("cache-01", "ap-south-1"),
]

by_region = {}

for name, region in instances:
    if region not in by_region:
        by_region[region] = []
    by_region[region].append(name)

for region, names in by_region.items():
    print(f"{region:12s} {len(names)}  {names}")
''',
    ),
],

# ==================================================================== 7
7: [
    (
        "AI &middot; A response that is not the shape you expected",
        "Two different failures look identical from the outside: the key is "
        "missing, or the thing you indexed into was never a dictionary. "
        "Separate except blocks let you say which one happened, which is the "
        "difference between a five minute fix and an afternoon.",
        '''
def read_reply(response):
    try:
        return response["choices"][0]["message"]["content"]
    except KeyError as e:
        return f"missing key in the response: {e}"
    except IndexError:
        return "the response came back with no choices"
    except TypeError:
        return "that was not shaped like a response at all"


good = {"choices": [{"message": {"content": "All targets healthy."}}]}
missing = {"choices": [{"message": {}}]}
empty = {"choices": []}

print(read_reply(good))
print(read_reply(missing))
print(read_reply(empty))
print(read_reply("just a string"))
''',
    ),
    (
        "AI &middot; Retry the model, then give up honestly",
        "A retry loop that never gives up is a hung process. Counting the "
        "attempts and raising a clear error at the end means the caller finds "
        "out what happened rather than waiting forever.",
        '''
import time

calls = {"n": 0}


def call_model(prompt):
    calls["n"] += 1
    if calls["n"] < 3:
        raise TimeoutError("model did not respond in time")
    return f"answer to: {prompt}"


def ask(prompt, attempts=4):
    for attempt in range(1, attempts + 1):
        try:
            return call_model(prompt)
        except TimeoutError as e:
            print(f"  attempt {attempt}: {e}")
            time.sleep(0.1)
    raise RuntimeError(f"gave up after {attempts} attempts")


print(ask("summarise the incident"))
print("calls made:", calls["n"])
''',
    ),
    (
        "Parse a value that might be junk",
        "Configuration is written by people, so it will eventually contain "
        "something that is not a number. Catching the failure and falling back "
        "to a default keeps the service starting instead of dying on boot.",
        '''
def read_port(text, default=8080):
    try:
        return int(text)
    except ValueError:
        print(f"  could not read {text!r} as a port, using {default}")
        return default


print("8080       ->", read_port("8080"))
print("not-a-port ->", read_port("not-a-port"))
print("empty      ->", read_port(""))
''',
    ),
    (
        "Always release the lock",
        "A deployment lock that is never released blocks every future run. "
        "finally is the only thing that guarantees the release happens whether "
        "the work succeeded, failed, or raised something you did not expect.",
        '''
lock_held = False


def deploy_with_lock(should_fail):
    global lock_held
    lock_held = True
    print("  lock acquired")
    try:
        if should_fail:
            raise RuntimeError("deployment failed halfway")
        print("  deployment finished")
    except RuntimeError as e:
        print("  caught:", e)
    finally:
        lock_held = False
        print("  lock released")


deploy_with_lock(should_fail=False)
print("lock still held?", lock_held)

deploy_with_lock(should_fail=True)
print("lock still held?", lock_held)
''',
    ),
],

# ==================================================================== 8
8: [
    (
        "AI &middot; Build a call payload with **kwargs",
        "This is the shape of every AI SDK call you will make. The required "
        "arguments are named, and anything else the caller passes is collected "
        "and merged in, so the function does not need changing each time the "
        "provider adds an option.",
        '''
def build_request(model, prompt, **options):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    payload.update(options)
    return payload


basic = build_request("gpt-4o-mini", "Say hello.")
tuned = build_request(
    "gpt-4o-mini",
    "Say hello.",
    temperature=0.2,
    max_tokens=100,
    stream=True,
)

print(basic)
print()
for key, value in tuned.items():
    print(f"  {key}: {value}")
''',
    ),
    (
        "AI &middot; Stream tokens and keep a running total",
        "yield hands back one piece at a time. Accumulating as you go gives "
        "the caller both the growing answer and, at the end, the count you "
        "need for a cost line.",
        '''
def stream(tokens):
    so_far = ""
    for token in tokens:
        so_far += token
        yield so_far


pieces = ["The ", "target ", "group ", "is ", "unhealthy."]

count = 0
for partial in stream(pieces):
    count += 1
    print(f"  {count:>2}  {partial}")

print()
print("tokens streamed:", count)
print("final answer   :", partial)
''',
    ),
    (
        "AI &middot; Let the caller decide how to format",
        "Passing a function as a value means one pipeline can print to a "
        "terminal, write JSON, or push to a UI, without the pipeline knowing "
        "which. Gradio and most chat frameworks are built on this.",
        '''
def plain(role, text):
    return f"{role}: {text}"


def bracketed(role, text):
    return f"[{role.upper():>9}] {text}"


def render(formatter, history):
    for role, text in history:
        print(formatter(role, text))


history = [("user", "Why is it slow?"), ("assistant", "Two targets are down.")]

render(plain, history)
print()
render(bracketed, history)
''',
    ),
    (
        "A retry helper worth reusing",
        "Default arguments turn one function into several. Callers who do not "
        "care get sensible behaviour, and callers who do can turn the dials "
        "without you writing a second function.",
        '''
def call_with_retry(name, attempts=3, succeed_on=2):
    for attempt in range(1, attempts + 1):
        if attempt >= succeed_on:
            return f"{name} succeeded on attempt {attempt}"
        print(f"  {name}: attempt {attempt} failed")
    return f"{name} gave up after {attempts} attempts"


print(call_with_retry("health-check"))
print(call_with_retry("slow-service", attempts=5, succeed_on=4))
print(call_with_retry("broken-service", attempts=2, succeed_on=99))
''',
    ),
],

# ==================================================================== 9
9: [
    (
        "AI &middot; A run log, one JSON object per line",
        "JSON Lines is the format almost every evaluation and fine tuning run "
        "writes. Each line is a complete JSON object, so a file can be "
        "appended to forever and read back one record at a time without "
        "loading the lot.",
        '''
import json

log_path = WORK / "runs.jsonl"

runs = [
    {"run": 1, "prompt": "summarise", "tokens": 128, "ok": True},
    {"run": 2, "prompt": "translate", "tokens": 96, "ok": True},
    {"run": 3, "prompt": "classify", "tokens": 64, "ok": False},
]

with open(log_path, "w") as f:
    for record in runs:
        f.write(json.dumps(record) + "\\n")

total_tokens = 0
failures = 0

with open(log_path) as f:
    for line in f:
        record = json.loads(line)
        total_tokens += record["tokens"]
        if not record["ok"]:
            failures += 1

print("records    :", len(runs))
print("tokens used:", total_tokens)
print("failures   :", failures)
''',
    ),
    (
        "AI &middot; Save a conversation and pick it up later",
        "A chat that survives a restart is a chat saved to disk. Write the "
        "history as JSON, read it back, append the next turn, and the "
        "assistant carries on where it left off.",
        '''
import json

chat_path = WORK / "chat.json"

history = [
    {"role": "user", "content": "Hi, I am Serge."},
    {"role": "assistant", "content": "Hello Serge."},
]

with open(chat_path, "w") as f:
    json.dump(history, f, indent=2)

# ... the program stops and starts again here ...

with open(chat_path) as f:
    resumed = json.load(f)

resumed.append({"role": "user", "content": "What is my name?"})
resumed.append({"role": "assistant", "content": "You said you are Serge."})

with open(chat_path, "w") as f:
    json.dump(resumed, f, indent=2)

print("turns after resuming:", len(resumed))
print("last exchange:")
print("  ", resumed[-2]["content"])
print("  ", resumed[-1]["content"])
''',
    ),
    (
        "AI &middot; Defaults, overridden by a config file",
        "Start from a dictionary of defaults, read whatever the file supplies, "
        "and let the file win. Anything the file leaves out keeps working, "
        "which is what makes a config file safe to add to later.",
        '''
import json

defaults = {"model": "gpt-4o-mini", "temperature": 0.7, "max_tokens": 512}

with open(WORK / "config.json", "w") as f:
    json.dump({"temperature": 0.2}, f)

with open(WORK / "config.json") as f:
    from_file = json.load(f)

settings = dict(defaults)
settings.update(from_file)

print("defaults :", defaults)
print("file says:", from_file)
print("in effect:", settings)
''',
    ),
    (
        "Pull the errors out of a log file",
        "Read a file line by line, keep the lines that matter, write those to "
        "a second file. This is the shape of most log triage, and it never "
        "holds the whole file in memory.",
        '''
source = WORK / "app.log"
errors_only = WORK / "errors.log"

with open(source, "w") as f:
    f.writelines([
        "2024-08-19 INFO  service started\\n",
        "2024-08-19 ERROR database connection refused\\n",
        "2024-08-19 INFO  retrying\\n",
        "2024-08-19 ERROR database connection refused\\n",
        "2024-08-19 INFO  connected\\n",
    ])

kept = 0

with open(source) as src, open(errors_only, "w") as dst:
    for line in src:
        if "ERROR" in line:
            dst.write(line)
            kept += 1

print("errors found:", kept)

with open(errors_only) as f:
    print(f.read())
''',
    ),
],

# =================================================================== 10
10: [
    (
        "AI &middot; Read your whole config in one block",
        "Every setting comes from the environment with a fallback, so the same "
        "code runs on a laptop with nothing set and in production with "
        "everything set. The key is reported as present or absent and never "
        "printed.",
        '''
import os

config = {
    "model": os.environ.get("LAB_MODEL", "gpt-4o-mini"),
    "temperature": float(os.environ.get("LAB_TEMPERATURE", "0.7")),
    "max_tokens": int(os.environ.get("LAB_MAX_TOKENS", "512")),
    "region": os.environ.get("AWS_REGION", "us-east-1"),
}

for key, value in config.items():
    print(f"  {key:12s} {value}  {type(value).__name__}")

print()
print("API key set:", bool(os.environ.get("LAB_API_KEY")))
''',
    ),
    (
        "AI &middot; What did this run cost, and how long did it take?",
        "time measures the wall clock, the token counts give you the money. "
        "Printing both at the end of a run is how you notice that the clever "
        "prompt is also the expensive one.",
        '''
import time

start = time.time()

# stands in for three model calls
time.sleep(0.3)

input_tokens = 4_200
output_tokens = 850
elapsed = time.time() - start

cost = (input_tokens / 1_000_000) * 3.00 + (output_tokens / 1_000_000) * 15.00

print("=== run summary ===")
print("input tokens :", input_tokens)
print("output tokens:", output_tokens)
print(f"wall clock   : {elapsed:.2f}s")
print(f"cost         : ${cost:.4f}")
print(f"cost per 1000 runs: ${cost * 1000:.2f}")
''',
    ),
    (
        "AI &middot; Summarise a set of latencies",
        "statistics ships with Python and saves you writing the maths by hand. "
        "The median barely moves when one request is slow and the mean does "
        "not survive it, which is why dashboards show the median.",
        '''
import statistics

latencies_ms = [45, 52, 38, 512, 47, 41, 60, 44]

print("count  :", len(latencies_ms))
print("mean   :", round(statistics.mean(latencies_ms), 1))
print("median :", statistics.median(latencies_ms))
print("slowest:", max(latencies_ms))
print("fastest:", min(latencies_ms))
''',
    ),
    (
        "A timestamped artefact name",
        "Anything a job writes needs a name that will not collide with the "
        "next run. strftime controls the format so the names sort correctly "
        "when listed.",
        '''
import datetime as dt

now = dt.datetime(2026, 8, 19, 14, 30, 5)      # fixed so the output is stable

stamp = now.strftime("%Y%m%d-%H%M%S")
report = f"eval-run-{stamp}.jsonl"

print("stamp :", stamp)
print("report:", report)
print("today would be:", dt.date.today())
''',
    ),
],

# =================================================================== 11
11: [
    (
        "AI &middot; dataclass and Pydantic, same bad input",
        "Both describe the same shape. Only one of them checks. Run this once "
        "and the reason AI SDKs standardised on Pydantic for structured "
        "output stops needing an explanation.",
        '''
from dataclasses import dataclass
from pydantic import BaseModel, ValidationError


@dataclass
class PlainTurn:
    role: str
    content: str


class CheckedTurn(BaseModel):
    role: str
    content: str


bad = PlainTurn(role=123, content=None)
print("dataclass accepted it:", bad)

try:
    CheckedTurn(role=123, content=None)
except ValidationError as e:
    first = e.errors()[0]
    print()
    print("pydantic refused it:", first["msg"], "on field", first["loc"])
''',
    ),
    (
        "AI &middot; Validate what the model sent back",
        "Asking a model for JSON does not guarantee JSON of the right shape. "
        "Validating on the way in means a malformed answer fails at your "
        "boundary with a clear message, rather than three functions later.",
        '''
from pydantic import BaseModel, ValidationError


class Triage(BaseModel):
    severity: int
    service: str
    summary: str


good = '{"severity": 2, "service": "api-gateway", "summary": "502s from two targets"}'
bad = '{"severity": "high", "service": "api-gateway", "summary": "502s"}'

result = Triage.model_validate_json(good)
print("parsed:", result.service, "severity", result.severity)
print("type of severity:", type(result.severity))

try:
    Triage.model_validate_json(bad)
except ValidationError as e:
    print()
    print("the model returned severity as text, which is not usable:")
    print(" ", e.errors()[0]["msg"])
''',
    ),
    (
        "AI &middot; A decorator that retries",
        "The retry logic from Module 7, moved into a decorator. The function "
        "it wraps knows nothing about retrying, so you add or remove the "
        "behaviour by changing one line above the def.",
        '''
def retry(attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:
                    print(f"  attempt {attempt} failed: {e}")
            raise RuntimeError(f"{func.__name__} failed after {attempts} attempts")
        return wrapper
    return decorator


calls = {"n": 0}


@retry(attempts=4)
def fetch_metrics():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("connection reset")
    return "metrics retrieved"


print(fetch_metrics())
print("it took", calls["n"], "calls")
''',
    ),
    (
        "AI &middot; Fan out calls of different lengths",
        "Run three things at once and the total is the slowest one, not the "
        "sum. This is the whole argument for async in an AI application, where "
        "almost all the time is spent waiting on somebody else's server.",
        '''
import asyncio
import time


async def call(name, seconds):
    await asyncio.sleep(seconds)
    return f"{name} took {seconds}s"


start = time.time()

results = await asyncio.gather(
    call("summarise", 0.5),
    call("translate", 0.2),
    call("classify", 0.3),
)

elapsed = time.time() - start

for r in results:
    print(r)

print()
print("one after another would be 1.00s")
print(f"all at once took {elapsed:.2f}s, the slowest one")
''',
    ),
],

}
