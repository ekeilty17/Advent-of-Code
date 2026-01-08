from pathlib import Path

from Day_01.const import DAY, INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import solve

def solution(floor_instructions: str) -> int:
    floor = 0
    for instruction in floor_instructions:
        floor += 1 if instruction == "(" else -1
    return floor

if __name__ == "__main__":
    floor_instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, floor_instructions)