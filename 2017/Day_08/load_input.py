from pathlib import Path
from typing import List, Tuple
import re

def load_input(input_path: Path) -> List[Tuple[Tuple[str, str, int], Tuple[str, str, int]]]:
    lines = input_path.read_text().splitlines()
    return [parse_instruction(instruction) for instruction in lines]

def parse_instruction(instruction_str: str) -> Tuple[Tuple[str, str, int], Tuple[str, str, int]]:
    pattern = r"([a-z]+) ([a-z]+) (-?\d+) if ([a-z]+) (.+) (-?\d+)"
    m = re.fullmatch(pattern, instruction_str)
    if not m:
        raise Exception(f"Failed to parse instruction: {instruction_str}")
    
    operation = m.group(1), m.group(2), int(m.group(3))
    condition = m.group(4), m.group(5), int(m.group(6))
    return operation, condition