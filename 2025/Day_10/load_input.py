from pathlib import Path
from typing import List, Tuple
import re

def load_input(input_path: Path) -> Tuple[List[int], List[List[int]], List[int]]:
    lines = input_path.read_text().splitlines()
    machines = [parse_machine(machine_str) for machine_str in lines]
    return machines

def parse_machine(machine_str):
    pattern = r"(\[.+\]) (\(.+\))+ (\{.+\})"
    match = re.search(pattern, machine_str)
    if not match:
        raise ValueError(f"Regex pattern failed to parse row\n{machine_str}")
    
    indicator_lights = parse_indicator_lights(match.group(1))
    button_wiring_schematics = parse_button_wiring_schematics(match.group(2))
    joltage_requirements = parse_joltage_requirements(match.group(3))

    return indicator_lights, button_wiring_schematics, joltage_requirements

def parse_indicator_lights(indicator_lights_str: str) -> List[bool]:
    indicator_lights = []
    for char in indicator_lights_str:
        if char in ["[", "]"]:
            continue
        if char == "#":
            indicator_lights.append(True)
        elif char == ".":
            indicator_lights.append(False)
        else:
            raise Exception(f"Unexpected character '{char}'")
    return indicator_lights

def parse_button_wiring_schematics(button_wiring_schematics_str: str) -> List[List[int]]:
    button_wiring_schematics = []
    for schematic_str in button_wiring_schematics_str.split(" "):
        schematic_str = schematic_str[1:-1]
        button_wiring_schematics.append([int(x) for x in schematic_str.split(",")])
    return button_wiring_schematics

def parse_joltage_requirements(joltage_requirements_str: str) -> List[int]:
    joltage_requirements_str = joltage_requirements_str[1:-1]
    return [int(x) for x in joltage_requirements_str.split(",")]