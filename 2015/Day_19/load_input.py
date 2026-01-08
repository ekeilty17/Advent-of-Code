from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> Tuple[Dict[str, List[str]], str]:
    contents = input_path.read_text()
    replacements, molecules = contents.split("\n\n")

    replacements = parse_replacements(replacements)
    return replacements, molecules

def parse_replacements(replacements_contents: str) -> Dict[str, List[str]]:
    replacements = {}
    for replacement_str in replacements_contents.splitlines():
        key, value = replacement_str.split(" => ")
        if key in replacements:
            replacements[key].append(value)
        else:
            replacements[key] = [value]
    return replacements