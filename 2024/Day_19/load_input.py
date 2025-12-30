from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[str]:
    contents = input_path.read_text()
    patterns, target_towels = contents.split("\n\n")

    patterns = parse_patterns(patterns)
    target_towels = parse_target_towels(target_towels)
    return patterns, target_towels

def parse_patterns(patterns_str: str) -> List[str]:
    return [x.strip() for x in patterns_str.split(", ")]

def parse_target_towels(target_towels_str: str) -> List[str]:
    return [x.strip() for x in target_towels_str.split("\n")]