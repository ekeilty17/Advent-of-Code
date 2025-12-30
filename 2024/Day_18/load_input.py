from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return [parse_position(line) for line in lines]

def parse_position(position_str: str) -> Tuple[int, int]:
    return tuple([int(x) for x in position_str.split(",")])