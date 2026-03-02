import os
from scenario_automator import SCENARIOS

def generate_idea_purges():
    payload = ("# ============================================================\n"
               "# 1939 Historical Idea Purger\n"
               "# Removes vanilla national spirits that are hardcoded into the 1939\n"
               "# start if the player selects an alt-history game rule.\n"
               "# ============================================================\n\n")
    payload += "SAH_purge_1939_ideas = {\n"
    payload += "\thidden_effect = {\n"
    
    for country, config in SCENARIOS.items():
        # Only create a block if the country has non-historical starts
        non_historical_starts = {k: v for k, v in config.get('starts', {}).items() if 'historical' not in k.lower() and 'infamous_decade' not in k.lower() and 'catholic_bloc' not in k.lower() and 'fatherland_front' not in k.lower()}
        
        if not non_historical_starts:
            continue
            
        payload += f"\t\t{country} = {{\n"
        for opt_key, opt_data in non_historical_starts.items():
            rule_name = config['rule_name']
            payload += f"\t\t\tif = {{\n\t\t\t\tlimit = {{ has_game_rule = {{ rule = {rule_name} option = {opt_key} }} }}\n"
            
            payload += f"\t\t\t\t# Remove conflicting historical 1939 ideas here.\n"
            
            if country == 'USA':
                payload += "\t\t\t\tremove_ideas = USA_great_depression\n"
                payload += "\t\t\t\tremove_ideas = neutrality_idea\n"
            elif country == 'GER':
                payload += "\t\t\t\tremove_ideas = MEFO_bills\n"
                payload += "\t\t\t\tremove_ideas = anti_comintern_pact_idea\n"
            elif country == 'SOV':
                payload += "\t\t\t\tremove_ideas = officers_purged\n"
                payload += "\t\t\t\tremove_ideas = SOV_great_purge_1\n"
            elif country == 'FRA':
                payload += "\t\t\t\tremove_ideas = FRA_divided_government\n"
                payload += "\t\t\t\tremove_ideas = FRA_victors_of_the_great_war\n"
            elif country == 'ENG':
                payload += "\t\t\t\tremove_ideas = ENG_the_war_to_end_all_wars\n"
            elif country == 'JAP':
                payload += "\t\t\t\tremove_ideas = state_shintoism\n"
            else:
                payload += "\t\t\t\t# remove_ideas = vanilla_historical_idea_name\n"
            
            payload += "\t\t\t}\n"
        payload += "\t\t}\n"
    
    payload += "\t}\n}\n"
    
    with open("common/scripted_effects/SAH_1939_purges.txt", "w", encoding="utf-8") as f:
        f.write(payload)
    print("Generated SAH_1939_purges.txt!")

if __name__ == '__main__':
    generate_idea_purges()
