from pathlib import Path
from typing import List

from Day_17.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_17.load_input import load_input
from utils.solve import test, solve

def get_all_combinations(weights: List[int], total: int) -> List[List[int]]:
    C = [[[] for _ in range(total+1)]]
    C[0][0].append([0])

    for i, weight in enumerate(weights, 1):
        C.append([
            [list(combination) for combination in combinations] for combinations in C[i-1]
        ])
        
        for n in range(total+1):
            if n >= weight:
                C[i][n].extend(
                    [list(combination) + [weight] for combination in C[i-1][n - weight]]
                )

    combinations = [combination[1:] for combination in C[-1][-1]]
    return combinations

def solution(containers: List[int], liters_of_eggnog: int) -> int:
    combinations = get_all_combinations(containers, liters_of_eggnog)
    min_length = len(min(combinations, key=len))
    return len([combination for combination in combinations if len(combination) == min_length])

if __name__ == "__main__":
    example_containers = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_liters_of_eggnog = 25
    expected_answer = 3
    test(expected_answer, solution, example_containers, example_liters_of_eggnog)

    containers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    liters_of_eggnog = 150
    solve(solution, containers, liters_of_eggnog)