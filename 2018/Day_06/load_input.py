from pathlib import Path
from typing import Set, Tuple

def load_input(input_path: Path) -> Set[Tuple[int, int]]:
    lines = input_path.read_text().splitlines()
    return set([parse_coordinate(coordinate) for coordinate in lines])

def parse_coordinate(coordinate_str: str) -> Tuple[int, int]:
    return tuple([int(x) for x in coordinate_str.split(", ")])