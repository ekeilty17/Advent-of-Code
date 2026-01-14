from pathlib import Path
from typing import List, Tuple
import re

def load_input(input_path: Path) -> List[Tuple[int, int]]:
    lines = input_path.read_text().splitlines()
    discs = [parse_disc(disc) for disc in lines]
    return [(init_position, num_positions) for _, init_position, num_positions in sorted(discs)]

def parse_disc(disc_str: str) -> Tuple[int, int, int]:
    pattern = r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+)\."
    m = re.fullmatch(pattern, disc_str)
    if m:
        disc, num_positions, _, init_position = m.groups()
        return int(disc), int(init_position), int(num_positions)
    
    raise ValueError(f"Unable to parse line: {disc_str}")