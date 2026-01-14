from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return lines