import os
from scenario_automator import SCENARIOS

def generate_unit_adjustments():
    os.makedirs("history/units", exist_ok=True)
    
    payload = "SAH_adjust_1939_units = {\n"
    payload += "\thidden_effect = {\n"
    
    for country, config in SCENARIOS.items():
        payload += f"\t\t{country} = {{\n"
        for opt_key, opt_data in config.get('starts', {}).items():
            rule_name = config['rule_name']
            payload += f"\t\t\tif = {{\n\t\t\t\tlimit = {{ has_game_rule = {{ rule = {rule_name} option = {opt_key} }} }}\n"
            
            oob_name = f"SAH_{country}_1939_{opt_key}"
            
            payload += f"\t\t\t\t# Wipe existing historical units that might spawn in invalid territories\n"
            payload += f"\t\t\t\t# delete_unit_template_and_units = {{ template = \"Historical Division Name\" }}\n"
            payload += f"\t\t\t\tload_oob = \"{oob_name}\"\n"
            
            payload += "\t\t\t}\n"
            
            # Generate the OOB file if it doesn't exist
            oob_path = f"history/units/{oob_name}.txt"
            if not os.path.exists(oob_path):
                with open(oob_path, "w", encoding="utf-8") as oob_file:
                    oob_file.write(f"### 1939 Alternative OOB for {country} ({opt_key}) ###\n")
                    oob_file.write(f"# Add division_template, division, navy, and air movements/placements here.\n")
                    
        payload += "\t\t}\n"
    
    payload += "\t}\n}\n"
    
    with open("common/scripted_effects/SAH_1939_units.txt", "w", encoding="utf-8") as f:
        f.write(payload)
    print("Generated SAH_1939_units.txt and blank OOB files!")

if __name__ == '__main__':
    generate_unit_adjustments()
