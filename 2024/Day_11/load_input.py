from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[int]:
    lines = input_path.read_text().splitlines()
    return [int(x) for x in lines[0].split(" ")]