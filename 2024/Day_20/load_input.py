from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[List[str]]:
    lines = input_path.read_text().splitlines()
    return [[x for x in line] for line in lines]