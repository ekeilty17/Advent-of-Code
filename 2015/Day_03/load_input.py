from pathlib import Path
from typing import List

def load_input(input_path: Path) -> str:
    lines = input_path.read_text().splitlines()
    return lines[0]