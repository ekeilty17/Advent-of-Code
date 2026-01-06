from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[str, Tuple[int, int], Tuple[int, int]]]:
    lines = input_path.read_text().splitlines()
    return [parse_instruction(instruction) for instruction in lines]

def parse_instruction(instruction_str: str) -> Tuple[str, Tuple[int, int], Tuple[int, int]]:
    left, end_coord = instruction_str.split(" through ")
    *instruction_type, start_coord = left.split(" ")
    
    instruction_type = " ".join(instruction_type)
    start_coord = tuple([int(x) for x in start_coord.split(",")])
    end_coord = tuple([int(x) for x in end_coord.split(",")])

    return instruction_type, start_coord, end_coord