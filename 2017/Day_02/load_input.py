from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[List[int]]:
    lines = input_path.read_text().splitlines()
    return [parse_row(row) for row in lines]

def parse_row(row_str: str) -> List[int]:
    return [int(value) for value in row_str.split("\t")]