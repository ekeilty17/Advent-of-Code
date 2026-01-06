from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return [parse_distance(distance) for distance in lines]

def parse_distance(distance_str: str) -> Tuple[str, str, int]:
    edge, distance = distance_str.split(" = ")
    origin, destination = edge.split(" to ")
    return origin, destination, int(distance)