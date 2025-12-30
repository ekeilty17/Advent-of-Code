from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[int, int]]:
    lines = input_path.read_text().splitlines()
    return [parse_grid_location(location) for location in lines]

def parse_grid_location(location):
    return tuple([int(x.strip()) for x in location.split(",")])