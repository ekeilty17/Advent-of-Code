from pathlib import Path
from typing import List, Dict, Any, Tuple

from Day_08.const import DAY, INPUT_FILE_NAME
from Day_08.load_input import load_input
from Day_08.part_1 import execute_instructions
from utils.solve import solve
from utils.display_np import display_np_bool

def solution(instructions: List[Dict[str, Any]], screen_shape: Tuple[int, int]) -> int:
    screen = execute_instructions(instructions, screen_shape)
    return "\n" + display_np_bool(screen, supress=True)

if __name__ == "__main__":
    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    screen_shape = (6, 50)
    solve(solution, instructions, screen_shape)