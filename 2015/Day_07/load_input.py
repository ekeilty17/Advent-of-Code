from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[str, str]]:
    lines = input_path.read_text().splitlines()
    return [parse_instruction(instruction) for instruction in lines]

def parse_instruction(instruction_str: str) -> Tuple[str, str]:
    return instruction_str.split(" -> ")