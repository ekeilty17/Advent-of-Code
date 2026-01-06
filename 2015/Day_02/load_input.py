from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[int, int, int]]:
    lines = input_path.read_text().splitlines()
    return [parse_dimension(dimension) for dimension in lines]

def parse_dimension(dimension_str: str) -> Tuple[int, int, int]:
    return [int(x) for x in dimension_str.split("x")]