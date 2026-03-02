import re

with open("scenario_generated_code.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract just Section 2
match = re.search(r"====== 2\. PASTE THIS INTO events/SAH_init_events\.txt[\s\S]*?======\n(.*?)====== 3\.", text, re.DOTALL)
if match:
    events_payload = match.group(1).rstrip()
else:
    print("Match failed")
    exit(1)

with open("events/SAH_init_events.txt", "r", encoding="utf-8") as f:
    target = f.read()

# Replace the immediate block in the target. We'll find `immediate = {` and `option = {`
target = re.sub(
    r"immediate\s*=\s*\{.*?\}(\s*)option\s*=",
    f"immediate = {{\n{events_payload}\n\t}}\n\\1option =",
    target, flags=re.DOTALL
)

with open("events/SAH_init_events.txt", "w", encoding="utf-8") as f:
    f.write(target)

print("Injected seamlessly into events/SAH_init_events.txt")
