from pathlib import Path
from typing import List, Tuple, Dict
import re

def load_input(input_path: Path) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    lines = input_path.read_text().splitlines()
    
    weight_by_program = {}
    children_by_program = {}
    for program in lines:
        name, weight, children_list = parse_program(program)
        weight_by_program[name] = weight
        children_by_program[name] = children_list
    
    return weight_by_program, children_by_program

def parse_program(program_str: str) -> Tuple[str, int, List[str]]:
    pattern = r"([a-z]+) \((\d+)\)( -> (.+))?"
    m = re.fullmatch(pattern, program_str)
    if not m:
        raise Exception(f"Failed to parse: {program_str}")
    
    name = m.group(1)
    weight = int(m.group(2))
    children = m.group(4).split(", ") if m.group(4) else []
    return name, weight, children