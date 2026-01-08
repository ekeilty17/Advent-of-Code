from pathlib import Path
from typing import List

from Day_17.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_17.load_input import load_input
from utils.solve import test, solve

def solution(containers: List[int], liters_of_eggnog: int) -> int:
    C = [[0] * (liters_of_eggnog+1)]
    C[0][0] = 1

    for i, container in enumerate(containers, 1):
        C.append(list(C[i-1]))
        
        for n in range(liters_of_eggnog+1):
            if n >= container:
                C[i][n] += C[i-1][n - container]

    return C[-1][-1]

if __name__ == "__main__":
    example_containers = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_liters_of_eggnog = 25
    expected_answer = 4
    test(expected_answer, solution, example_containers, example_liters_of_eggnog)

    containers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    liters_of_eggnog = 150
    solve(solution, containers, liters_of_eggnog)