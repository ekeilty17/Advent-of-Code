from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[int]:
    contents = input_path.read_text()
    return [parse_instruction(instruction) for instruction in contents.split(", ")]

def parse_instruction(instruction_str: str) -> int:
    direction, number_of_blocks_str = instruction_str[0], instruction_str[1:]
    if direction == "R":
        return int(number_of_blocks_str)
    if direction == "L":
        return -int(number_of_blocks_str)
    raise Exception(f"Expected first character to be either 'L' or 'R', instead got {direction}")