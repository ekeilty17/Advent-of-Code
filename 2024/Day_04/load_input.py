from pathlib import Path
import numpy as np
from numpy.typing import NDArray

def load_input(input_path: Path) -> NDArray[str]:
    lines = input_path.read_text().splitlines()
    return np.array([[char for char in line] for line in lines])