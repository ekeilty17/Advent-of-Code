from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[str, str]]:
    lines = input_path.read_text().splitlines()
    return [parse_rule(rule) for rule in lines]

def parse_rule(rule_str: str) -> Tuple[str, str]:
    return tuple(rule_str.split(" => "))