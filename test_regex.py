import re

raw_reward = """
    add_popularity = { ideology = fascism popularity = 0.1 }
    set_politics = { ruling_party = fascism elections_allowed = no }
    add_popularity = { ideology = fascism popularity = 0.2 }
"""

match = re.search(r"set_politics\s*=\s*\{\s*ruling_party\s*=\s*(\w+)", raw_reward)
if match:
    print(f"Found ruling party: {match.group(1)}")
