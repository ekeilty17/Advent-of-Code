from pathlib import Path
from typing import List, Dict, Tuple

from Day_10.const import DAY, INPUT_FILE_NAME
from Day_10.load_input import load_input
from Day_10.part_1 import simulate_bots
from utils.solve import solve

def solution(
        initializations: Dict[str, List[int]], 
        transfers: Dict[str, Tuple[str, int, str, int]],
        target_outputs: List[int]
    ) -> int:

    _, outputs = simulate_bots(initializations, transfers)

    total = 1
    for output_index in target_outputs:
        total *= outputs[output_index]
    
    return total

if __name__ == "__main__":
    initializations, transfers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    target_outputs = [0, 1, 2]
    solve(solution, initializations, transfers, target_outputs)