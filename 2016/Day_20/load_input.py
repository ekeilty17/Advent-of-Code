from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[int, int]]:
    lines = input_path.read_text().splitlines()
    return [parse_IP_range(IP_range) for IP_range in lines]

def parse_IP_range(IP_range_str: str) -> Tuple[int, int]:
    return tuple([int(x) for x in IP_range_str.split("-")])