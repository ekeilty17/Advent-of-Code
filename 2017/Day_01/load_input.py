from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[int]:
    contents = input_path.read_text()
    return contents