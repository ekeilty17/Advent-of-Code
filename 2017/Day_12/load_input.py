from pathlib import Path
from typing import Tuple, Set, Dict

def load_input(input_path: Path) -> Dict[int, Set[int]]:
    lines = input_path.read_text().splitlines()
    return dict([parse_connection(connection) for connection in lines])

def parse_connection(connection_str: str) -> Tuple[int, Set[int]]:
    LHS, RHS = connection_str.split(" <-> ")
    return int(LHS), set([int(x) for x in RHS.split(", ")])