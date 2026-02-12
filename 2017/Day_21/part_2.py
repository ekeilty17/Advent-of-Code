from pathlib import Path
from typing import List, Tuple, Dict, Any
import numpy as np
from numpy.typing import NDArray

from Day_21.const import DAY, INPUT_FILE_NAME
from Day_21.load_input import load_input
from Day_21.part_1 import solution
from utils.solve import solve

if __name__ == "__main__":
    start_pattern = ".#./..#/###"

    rules = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    N = 18
    solve(solution, rules, start_pattern, N)