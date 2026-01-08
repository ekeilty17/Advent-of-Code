from pathlib import Path
from typing import Tuple
import re

def load_input(input_path: Path) -> Tuple[int, int]:
    lines = input_path.read_text().splitlines()
    pattern = r"To continue, please consult the code grid in the manual\.  Enter the code at row (\d+), column (\d+)\."
    m = re.fullmatch(pattern, lines[0])
    if not m:
        raise ValueError("Unable to parse input")
    return tuple([int(x) for x in m.groups()])