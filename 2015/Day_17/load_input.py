from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[int]:
    lines = input_path.read_text().splitlines()
    return [parse_container(container) for container in lines]

def parse_container(container_str: str) -> int:
    return int(container_str)