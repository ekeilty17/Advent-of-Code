from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[int]:
    rotations = input_path.read_text().splitlines()
    rotations = [parse_rotation(rotation_str) for rotation_str in rotations]
    return rotations

def parse_rotation(rotation_str: str) -> int:
    if not len(rotation_str):
        raise ValueError("parameter 'rotation_str' is empty.")
    if rotation_str[0] not in ["L", "R"]:
        raise ValueError("parameter 'rotation_str' must start with either 'L' or 'R'")
    
    direction = 1 if rotation_str[0] == "R" else -1

    try:
        distance = int(rotation_str[1:])
    except:
        raise ValueError("the second position and afterwards of the parameter 'rotation_str' must be an integer")
    
    return direction * distance