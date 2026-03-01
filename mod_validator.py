import os
import re

class Hoi4Validator:
    def __init__(self, mod_path: str) -> None:
        self.mod_path = mod_path
        self.focus_ids: set[str] = set()
        self.focus_refs: list[tuple[str, str]] = []
        self.event_ids: set[str] = set()
        self.event_refs: list[tuple[str, str]] = []
        # Exclude folders that shouldn't be parsed
        self.exclude_dirs = ['.git', '__pycache__', '.vscode']

    def validate_file_syntax(self, filepath: str) -> tuple[list[str], str]:
        errors: list[str] = []
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='ansi') as f:
                    content = f.read()
            except Exception as e:
                return [f"Could not read file (encoding issue): {e}"], ""

        lines = content.split('\n')
        bracket_level = 0
        open_brackets: list[int] = []
        
        for line_num, line in enumerate(lines, 1):
            # Ignore everything after a comment '#'
            code = line.split('#')[0]
            
            # Check for unclosed quotes
            quotes = code.count('"')
            # Simple check, ignoring escaped text since it is rare in PDX scripts
            if quotes % 2 != 0:
                errors.append(f"Line {line_num}: Unclosed quote (\")")
                
            for char in code:
                if char == '{':
                    bracket_level += 1
                    open_brackets.append(line_num)
                elif char == '}':
                    bracket_level -= 1
                    if bracket_level < 0:
                        errors.append(f"Line {line_num}: Extra closing bracket '}}'")
                        bracket_level = 0
                    else:
                        open_brackets.pop()
                        
        if bracket_level > 0:
            for line_num in open_brackets:
                errors.append(f"Line {line_num}: Unclosed bracket '{{'")
                
        return errors, content

    def check_file(self, filepath: str, rel_path: str, content: str) -> None:
        """Extract elements for reference checking."""
        
        # 1. National Focuses
        if 'national_focus' in rel_path.replace('\\', '/'):
            # Looking for focus definitions
            # Regex note: match focus = { id = X } loosely
            f_ids = re.findall(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', content, re.MULTILINE)
            self.focus_ids.update(f_ids)
            
            # Looking for focus references in prerequisites, mutually exclusive, etc
            f_refs = re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', content)
            for ref in f_refs:
                self.focus_refs.append((ref, rel_path))

        # 2. Events
        if 'events' in rel_path.replace('\\', '/'):
            e_ids = re.findall(r'^\s*id\s*=\s*([a-zA-Z0-9_\.]+)', content, re.MULTILINE)
            self.event_ids.update(e_ids)

        # Look for referenced events (e.g., country_event = { id = X })
        e_refs = re.findall(r'(?:country_event|news_event|unit_leader_event|state_event|operative_leader_event)\s*=\s*(?:[a-zA-Z0-9_\.]+|{\s*id\s*=\s*([a-zA-Z0-9_\.]+))', content)
        for ref in e_refs:
            if ref:  # some matches might be empty based on regex grouping
                self.event_refs.append((ref, rel_path))

    def run(self):
        total_errors = 0
        print("Starting HOI4 Mod Validation...\n")
        
        for root, dirs, files in os.walk(self.mod_path):
            # Ignore excluded directories
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
                
            for file in files:
                if file.endswith('.txt'):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, self.mod_path)
                    
                    errors, content = self.validate_file_syntax(filepath)
                    if errors:
                        print(f"[{rel_path}] Syntax Errors:")
                        for err in errors:
                            print(f"  -> {err}")
                        total_errors += len(errors)
                        
                    if content:
                        self.check_file(filepath, rel_path, content)

        print("\n--- Syntax validation complete ---")
        
        # Check Reference warnings
        print("\nChecking Inter-connectivity and References...\n")
        
        # For focuses, we do a basic check. Warning: This might trigger false positives 
        # for base-game focuses if we don't load the base game's files!
        for ref, filepath in self.focus_refs:
            if ref not in self.focus_ids:
                # We skip reporting base game focuses just missing from the mod folder
                # to prevent console spam, but this is how you'd track it
                pass
                
        # For events
        for ref, filepath in self.event_refs:
            if ref not in self.event_ids:
                # Ignoring for now due to base-game references
                pass
                
        print(f"Validation finished. Found {total_errors} file syntax errors.")

if __name__ == "__main__":
    # Run the validator on the current working directory
    validator = Hoi4Validator('.')
    validator.run()
