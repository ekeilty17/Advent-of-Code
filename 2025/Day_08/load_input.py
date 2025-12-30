from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[int, int, int]]:
    lines = input_path.read_text().splitlines()
    return [parse_coordinate(coordinate) for coordinate in lines]

def parse_coordinate(coordinate):
    return tuple([int(x.strip()) for x in coordinate.split(",")])