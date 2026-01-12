from pathlib import Path
from typing import List

from Day_01.const import DAY, INPUT_FILE_NAME
from Day_01.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import test, solve

def solution(instructions: List[int]) -> int:
    instructions = [-x if i % 2 else x for i, x in enumerate(instructions)]
    
    blocks = [0, 0]
    visited = set([tuple(blocks)])
    orientation = 1

    for i, instruction in enumerate(instructions):
        direction = 1 if orientation * instruction > 0 else -1

        for _ in range(abs(instruction)):
            blocks[i%2] += direction
            if tuple(blocks) in visited:
                return sum([abs(b) for b in blocks])
            visited.add(tuple(blocks))
        
        orientation *= 1 if instruction > 0 else -1
    
    return None

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 4
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)