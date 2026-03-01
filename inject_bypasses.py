import os
import re
from scenario_automator import read_all_focuses, get_focus_chain, SCENARIOS

def inject_bypasses():
    all_focuses = read_all_focuses()
    file_injections: dict[str, dict[str, list[str]]] = {}

    for _, config in SCENARIOS.items():
        rule_name = config['rule_name']
        for opt_key, opt_data in config['starts'].items():
            chain = get_focus_chain(opt_data['target_focus'], all_focuses)
            for f_id in chain:
                filepath = all_focuses[f_id]['file']
                if filepath not in file_injections: file_injections[filepath] = {}
                if f_id not in file_injections[filepath]: file_injections[filepath][f_id] = []
                file_injections[filepath][f_id].append(f"has_game_rule = {{ rule = {rule_name} option = {opt_key} }}")

    for filepath, injects in file_injections.items():
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()

        new_content = content
        
        # We parse the file to find where each focus is
        for f_id, conditions in injects.items():
            # Condense the generated rules
            rules_str = "\n\t\t\t\t".join(conditions)
            bypass_payload = f"\n\t\tbypass = {{\n\t\t\tOR = {{\n\t\t\t\t{rules_str}\n\t\t\t}}\n\t\t}}\n"

            # Find where this focus starts
            # Match "focus = { ... id = f_id"
            pattern = r'(focus\s*=\s*\{[^{]*?id\s*=\s*' + re.escape(f_id) + r'\b)'
            match = re.search(pattern, new_content)
            if not match: continue

            start_idx = match.start()
            
            # Find the end of this focus block
            bracket_count = 0
            end_idx = -1
            focus_start = new_content.find('{', start_idx)
            for i in range(focus_start, len(new_content)):
                if new_content[i] == '{': bracket_count += 1
                elif new_content[i] == '}':
                    bracket_count -= 1
                    if bracket_count == 0:
                        end_idx = i
                        break
            
            if end_idx != -1:
                focus_block = new_content[start_idx:end_idx+1]
                
                # Check if it already has a bypass block
                if re.search(r'\bbypass\s*=', focus_block):
                    # It has a bypass block. We need to inject our rules into its OR = {} or just add an OR at the root.
                    # Simplest robust way to extend existing bypass:
                    # Find 'bypass = {' and insert after the '{'
                    bp_match = re.search(r'\bbypass\s*=\s*\{', focus_block)
                    if bp_match:
                        insert_pos = bp_match.end()
                        modified_focus = focus_block[:insert_pos] + f"\n\t\t\t{rules_str}" + focus_block[insert_pos:]
                        new_content = new_content[:start_idx] + modified_focus + new_content[end_idx+1:]
                else:
                    # Safe to inject new bypass block after 'id = ...'
                    id_match = re.search(r'id\s*=\s*' + re.escape(f_id) + r'\b', focus_block)
                    if id_match:
                        insert_pos = id_match.end()
                        modified_focus = focus_block[:insert_pos] + bypass_payload + focus_block[insert_pos:]
                        new_content = new_content[:start_idx] + modified_focus + new_content[end_idx+1:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Injected bypasses into {os.path.basename(filepath)}")

if __name__ == '__main__':
    inject_bypasses()