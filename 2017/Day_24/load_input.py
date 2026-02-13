from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[int, int]]:
    lines = input_path.read_text().splitlines()
    return [parse_component(component) for component in lines]

def parse_component(component_str: str) -> Tuple[int, int]:
    return tuple([int(x) for x in component_str.split("/")])