FILTERED_REWARDS = [
    "add_political_power", "add_army_experience", "add_navy_experience",
    "add_air_experience", "add_command_power", "custom_effect_tooltip",
    "add_named_threat", "start_civil_war", "country_event", "news_event",
    "hidden_idea"
]

def clean_rewards(reward_block: str) -> str:
    if not reward_block: return ""
    
    # We will do a simple line-based parser but with bracket counting to skip blocks if they start on a filtered line
    lines = reward_block.split('\n')
    out: list[str] = []
    skip_depth = 0
    
    for line in lines:
        # Are we currently skipping a block?
        if skip_depth > 0:
            skip_depth += line.count('{')
            skip_depth -= line.count('}')
            continue
            
        # Is this a line we should start skipping?
        if any(keyword in line for keyword in FILTERED_REWARDS):
            # Did it open a block?
            if '{' in line:
                skip_depth += line.count('{')
                skip_depth -= line.count('}')
                # If it opened and closed on the same line, skip_depth will be 0, which is fine, we just skip this line.
            continue
            
        out.append(line)
        
    return '\n'.join(out)

if __name__ == '__main__':
    reward = """completion_reward = {
    add_political_power = 120
    custom_effect_tooltip = {
        name = Hello
        days = { 1 2 3 }
    }
    country_event = { id = test.1 }
    add_ideas = foo
}"""
    print(clean_rewards(reward))
