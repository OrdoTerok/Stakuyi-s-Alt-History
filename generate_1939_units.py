import os
from scenario_automator import SCENARIOS

def generate_unit_adjustments():
    payload = "SAH_adjust_1939_units = {\n"
    payload += "\thidden_effect = {\n"
    
    for country, config in SCENARIOS.items():
        payload += f"\t\t{country} = {{\n"
        for opt_key, opt_data in config.get('starts', {}).items():
            rule_name = config['rule_name']
            payload += f"\t\t\tif = {{\n\t\t\t\tlimit = {{ has_game_rule = {{ rule = {rule_name} option = {opt_key} }} }}\n"
            
            payload += f"\t\t\t\t# Remove invalid historical units and spawn alt-history placeholder OOB if necessary.\n"
            payload += f"\t\t\t\t# Remove this comment block and utilize logic such as:\n"
            payload += f"\t\t\t\t# every_unit = {{ set_location = PREV.capital }}\n"
            payload += f"\t\t\t\t# OR\n"
            payload += f"\t\t\t\t# load_oob = \"SAH_{country}_1939_{opt_key}\"\n"
            
            payload += "\t\t\t}\n"
        payload += "\t\t}\n"
    
    payload += "\t}\n}\n"
    
    with open("common/scripted_effects/SAH_1939_units.txt", "w", encoding="utf-8") as f:
        f.write(payload)
    print("Generated SAH_1939_units.txt!")

if __name__ == '__main__':
    generate_unit_adjustments()
