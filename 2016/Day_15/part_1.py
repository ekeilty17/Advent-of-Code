from pathlib import Path
from typing import List, Tuple

from Day_15.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_15.load_input import load_input
from utils.solve import test, solve

def search(discs: List[Tuple[int, int]]) -> int:
    X0 = [init_position for init_position, _ in discs]
    N =  [num_positions for _, num_positions in discs]

    # formula dependent on t
    # t = 0
    # B = [(t+x0+k) % n for k, (x0, n) in enumerate(zip(X0, N), 1)]
    # while not all(B[0] == b for b in B):
    #     B = [(t+x0+k) % n for k, (x0, n) in enumerate(zip(X0, N), 1)]
    #     t += 1
    # t -= 1

    # incremental approach
    t = 0
    B = [(x0+k) % n for k, (x0, n) in enumerate(zip(X0, N), 1)]
    while not all(B[0] == b for b in B):
        B = [(b+1) % n for b, n in zip(B, N)]
        t += 1

    return t

def solution(discs: List[Tuple[int, int, int]]) -> int:
    return search(discs)

if __name__ == "__main__":
    example_discs = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 5
    test(expected_answer, solution, example_discs)

    discs = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, discs)

