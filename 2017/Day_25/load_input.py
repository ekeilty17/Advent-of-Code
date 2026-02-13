from pathlib import Path
from typing import List, Dict, Tuple
import re

def load_input(input_path: Path) -> List[str]:
    contents = input_path.read_text()
    return parse_blueprint(contents)

def parse_blueprint(blueprint_str: str):
    start_state = parse_start_state(blueprint_str)
    num_steps = parse_number_of_steps(blueprint_str)
    instructions = parse_instructions(blueprint_str)

    return start_state, num_steps, instructions

def parse_start_state(blueprint_str: str) -> str:
    pattern = r"Begin in state ([A-Z]+)\."
    m = re.findall(pattern, blueprint_str)
    if not m:
        raise Exception("Unable to parse start state")
    return m[0]

def parse_number_of_steps(blueprint_str: str) -> int:
    pattern = r"Perform a diagnostic checksum after (\d+) steps\."
    m = re.findall(pattern, blueprint_str)
    if not m:
        raise Exception("Unable to parse number of steps")
    return int(m[0])

def parse_instructions(blueprint_str: str) -> Dict[str, List[Tuple[int, str, str]]]:
    pattern = r"""
In state ([A-Z]+):
  If the current value is (\d+):
    - Write the value (\d+)\.
    - Move one slot to the (left|right)\.
    - Continue with state ([A-Z]+)\.
  If the current value is (\d+):
    - Write the value (\d+)\.
    - Move one slot to the (left|right)\.
    - Continue with state ([A-Z]+)\.
    """.strip()

    m = re.findall(pattern, blueprint_str)
    if not m:
        raise Exception("Unable to parse instructions")
    
    instructions_by_state = {}
    for group in m:
        state, *instructions = group
        instructions_by_state[state] = [None, None]

        for i in range(0, len(instructions), 4):
            current_value, write, cursor_direction, next_state = instructions[i:i+4]
        
            instructions_by_state[state][int(current_value)] = (int(write), cursor_direction, next_state)
    
    return instructions_by_state