from pathlib import Path
from typing import List
import numpy as np
from numpy.typing import NDArray

def load_input(input_path: Path) -> NDArray[np.bool_]:
    grid = input_path.read_text().splitlines()
    grid = [parse_paper_roll(row_str) for row_str in grid]
    grid = np.array(grid)
    return grid

def parse_paper_roll(row_str: str) -> List[int]:
    return [char == "@" for char in row_str]