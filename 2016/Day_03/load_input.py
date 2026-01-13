from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[List[int]]:
    lines = input_path.read_text().splitlines()
    return [parse_row(row) for row in lines]

def parse_row(row_str: str) -> List[int]:
    return [int(x) for x in row_str.strip().split(" ") if x]