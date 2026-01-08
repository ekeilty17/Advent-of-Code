from pathlib import Path
from typing import List, Tuple

from Day_01.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import test, solve

def apply_rotation_brute_force(dial_start: int, rotation: int) -> Tuple[int, int]:

    dial = dial_start
    direction = 1 if rotation > 0 else -1
    count_0 = 0
    for _ in range(abs(rotation)):
        if dial % 100 == 0:
            count_0 += 1
        dial += direction
    dial %= 100

    # if the dial ends at 0, we are not counting that here
    # we count that at the start of the next iteration

    return dial, count_0

def apply_rotation(dial_start: int, rotation: int) -> Tuple[int, int]:

    dial = (dial_start + rotation) % 100
    count_0 = abs((dial_start + rotation) // 100)
    
    # Some corrections due to when the dial either starts or ends at 0
    if dial_start == 0 and rotation > 0:
        count_0 += 1
    if dial == 0 and rotation > 0:
        count_0 -= 1

    return dial, count_0

def solution(dial_start: int, rotations: List[int]) -> int:
    count_0 = 0

    dial = dial_start
    for rotation in rotations:
        # dial, sub_count_0 = apply_rotation_brute_force(dial, rotation)
        dial, sub_count_0 = apply_rotation(dial, rotation)
        count_0 += sub_count_0

    # Since the last position of the dial was not counted
    if dial == 0:
        count_0 += 1

    return count_0

if __name__ == "__main__":
    dial_start = 50

    example_rotations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_answer = 6
    test(example_answer, solution, dial_start, example_rotations)

    rotations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, dial_start, rotations)