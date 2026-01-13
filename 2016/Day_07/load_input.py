from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return [parse_IP(IP) for IP in lines]

def parse_IP(IP_str: str) -> Tuple[List[str], List[str]]:
    outside_brackets = [""]
    inside_brackets = [""]
    
    inside = False
    for char in IP_str:
        if char == "[":
            inside = True
            inside_brackets.append("")
            continue
        if char == "]":
            inside = False
            outside_brackets.append("")
            continue
        if inside:
            inside_brackets[-1] += char
        else:
            outside_brackets[-1] += char

    outside_brackets = [s for s in outside_brackets if s]
    inside_brackets = [s for s in inside_brackets if s]
    return outside_brackets, inside_brackets