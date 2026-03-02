FILTERED_REWARDS = [
    "add_political_power",
    "add_army_experience",
    "add_navy_experience",
    "add_air_experience",
    "add_command_power",
    "custom_effect_tooltip",
    "add_named_threat",
    "start_civil_war",
    "country_event",
    "news_event",
    "declare_war",
    "create_wargoal"
]

DATE_GATED_REWARDS = [
    "add_building_construction",
    "add_extra_state_shared_building_slots",
    "create_unit",
    "load_oob",
    "spawn_unit",
    "add_offsite_building"
]

def clean_rewards(reward_block: str) -> str:
    if not reward_block: return ""
    lines = reward_block.split('\n')
    out: list[str] = []
    
    skip_depth = 0
    wrap_depths: list[int] = []
    current_depth = 0
    
    for line in lines:
        opens = line.count('{')
        closes = line.count('}')
        
        if skip_depth > 0:
            skip_depth += opens
            skip_depth -= closes
            current_depth += opens - closes
            continue
            
        if any(keyword in line for keyword in FILTERED_REWARDS):
            if opens > closes:
                skip_depth = opens - closes
            continue
            
        date_gated = any(keyword in line for keyword in DATE_GATED_REWARDS)
        
        if date_gated:
            out.append("\t\t\t\t\tif = { limit = { date < 1938.1.1 }")
            if opens > closes:
                wrap_depths.append(current_depth)
                out.append(line)
            else:
                out.append(line)
                out.append("\t\t\t\t\t}")
            
            current_depth += opens - closes
            continue
            
        out.append(line)
        current_depth += opens - closes
        
        if wrap_depths and current_depth == wrap_depths[-1]:
            out.append("\t\t\t\t\t}")
            wrap_depths.pop()
            
    return '\n'.join(out)

if __name__ == '__main__':
    reward = r"""completion_reward = {
    add_political_power = 120
    custom_effect_tooltip = {
        name = Hello
        days = { 1 2 3 }
    }
    country_event = { id = test.1 }
    random_owned_controlled_state = {
        limit = { always = yes }
        add_building_construction = {
            type = arms_factory
            level = 2
        }
    }
    
    add_building_construction = { type = industrial_complex level = 1 }
    add_ideas = foo
}"""
    print(clean_rewards(reward))
