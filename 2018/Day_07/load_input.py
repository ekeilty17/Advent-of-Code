from pathlib import Path
from typing import List, Tuple
import re

def load_input(input_path: Path) -> List[Tuple[str, str]]:
    lines = input_path.read_text().splitlines()
    return [parse_instruction_dependency(instruction_dependency) for instruction_dependency in lines]

def parse_instruction_dependency(instruction_dependency_str: str) -> Tuple[str, str]:
    pattern = r"Step ([A-Z]+) must be finished before step ([A-Z]+) can begin\."
    m = re.fullmatch(pattern, instruction_dependency_str)
    if not m:
        raise Exception(f"Failed to parse instruction dependency: {instruction_dependency_str}")
    
    return m.group(1), m.group(2)