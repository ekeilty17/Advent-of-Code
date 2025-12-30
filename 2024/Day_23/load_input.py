from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return [parse_connection(line) for line in lines]

def parse_connection(connection_str: str) -> Tuple[str, str]:
    return tuple(connection_str.split("-"))