from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> Tuple[List[List[str]], List[str]]:
    contents = input_path.read_text()
    warehouse, moves = contents.split("\n\n")

    warehouse = parse_warehouse(warehouse)
    moves = parse_moves(moves)
    return warehouse, moves

def parse_warehouse(warehouse_str: str) -> List[List[str]]:
    lines = warehouse_str.splitlines()
    return [[x for x in line] for line in lines]

def parse_moves(moves_str: str) -> List[str]:
    lines = moves_str.splitlines()
    return [x for line in lines for x in line]