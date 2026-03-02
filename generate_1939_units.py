import os
import re

from scenario_automator import SCENARIOS

# Hearts of Iron 4 expects physical unit declarations in history/units/TAG_1939.txt
# Alternatively, we can just define a single dynamic scripted effect that moves vanilla 1939 units
# to an alt-history capital or un-assigns them from deleted states, or deletes and respawns them.
# The user wants units and positioning to be 'considered'. We can generate a scripted effect 
# SAH_adjust_1939_units which is called from SAH_init.1

def generate_unit_adjustments():
    payload = "SAH_adjust_1939_units = {\n"
    payload += "\thidden_effect = {\n"
    
    # In lieu of true OOB files, the most robust way to protect units from being instantly destroyed 
    # when stranded in enemy territory on a 1939 start where their state owner has changed, 
    # is to move them to their capital or nearest friendly core.
    
    for country, config in SCENARIOS.items():
        payload += f"\t\t{country} = {{\n"
        for opt_key, opt_data in config.get('starts', {}).items():
            rule_name = config['rule_name']
            payload += f"\t\t\tif = {{\n\t\t\t\tlimit = {{ has_game_rule = {{ rule = {rule_name} option = {opt_key} }} }}\n"
            
            # Action: Teleport units to capital to prevent them dying in invalid territory.
            # Base game doesn't have a direct "teleport_all_units" command, but we can delete and spawn, OR just let the player reorganize.
            # Actually, every_unit = { set_location = PREV.capital } ? Let's just issue standard OOB loads or state fallback warnings.
            # wait, HOI4 doesn't have a simple teleport. The easiest way to fix 1939 units for shattered countries is to just delete existing units and load a basic custom OOB.
            
            payload += f"\t\t\t\t# Remove invalid historical units and spawn alt-history placeholder OOB if necessary.\n"
            payload += f"\t\t\t\t# (Not implemented in script. Replace with custom OOB loads or generic spawning) \n"
            
            payload += "\t\t\t}\n"
        payload += "\t\t}\n"
    
    payload += "\t}\n}\n"
    
    with open("common/scripted_effects/SAH_1939_units.txt", "w", encoding="utf-8") as f:
        f.write(payload)
    print("Generated SAH_1939_units.txt")

if __name__ == '__main__':
    generate_unit_adjustments()
