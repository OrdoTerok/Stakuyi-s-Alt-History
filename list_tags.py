import re

with open("common/scripted_triggers/stakuyi_triggers.txt", "r", encoding="utf-8") as f:
    text = f.read()

# is_xxx_yyyy_path = {
tags = set(re.findall(r'^is_([a-z]{3})_[a-zA-Z0-9_]+_path\s*=', text, re.MULTILINE))
print("Tags found in triggers:")
print(sorted(tags))
