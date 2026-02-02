from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[str]:
    contents = input_path.read_text().strip()
    return contents.split(",")