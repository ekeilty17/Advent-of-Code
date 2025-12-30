from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> Tuple[List[List[List[str]]], List[List[List[str]]]]:
    contents = input_path.read_text()
    schematics = contents.split("\n\n")
    schematics = [parse_schematic(schematic) for schematic in schematics]

    locks = []
    keys = []
    for schematic in schematics:
        if is_lock(schematic):
            locks.append(schematic)
        elif is_key(schematic):
            keys.append(schematic)
        else:
            raise ValueError("Schematic is neither lock nor key.")
    
    return locks, keys

def parse_schematic(schematic_str: str) -> List[List[str]]:
    return [[x for x in line] for line in schematic_str.splitlines()]

def is_lock(schematic: List[List[str]]) -> bool:
    return all(x == "#" for x in schematic[0])

def is_key(schematic: List[List[str]]) -> bool:
    return all(x == "#" for x in schematic[-1])