from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> List[Dict[str, Tuple[int, int]]]:
    lines = input_path.read_text().splitlines()
    
    machines = []
    for i in range(0, len(lines), 4):
        button_A = parse_machine_behavior(lines[i], "Button A: ")
        button_B = parse_machine_behavior(lines[i+1], "Button B: ")
        prize = parse_machine_behavior(lines[i+2], "Prize: ")
        machines.append({
            "button_A": button_A,
            "button_B": button_B,
            "prize": prize
        })
    
    return machines

def parse_machine_behavior(button_str: str, start: str) -> Tuple[int, int]:
    label = button_str[:len(start)]
    if label != start:
        raise ValueError(f"Expecting the input to begin '{start}', got '{label}' instead")
    return parse_coordinates(button_str[len(start):])

def parse_coordinates(coord_str) -> Tuple[int, int]:
    return tuple([int(x[2:]) for x in coord_str.split(", ")])