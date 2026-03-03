import os

def check_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

    depth = 0
    for i, line in enumerate(lines):
        # Ignore comments handling correctly
        in_string = False
        clean_line = ""
        for char in line:
            if char == '"':
                in_string = not in_string
            if char == '#' and not in_string:
                break
            clean_line += char

        depth += clean_line.count('{')
        depth -= clean_line.count('}')
        if depth < 0:
            print(f"[{filepath}] ERROR: Extra closing bracket on line {i+1}")
            return False

    if depth > 0:
        print(f"[{filepath}] ERROR: Missing {depth} closing bracket(s) by EOF")
        return False
    else:
        print(f"[{filepath}] OK: Brackets matched.")
        return True

check_file('events/SAH_init_events.txt')
check_file('common/scripted_effects/SAH_1939_purges.txt')
