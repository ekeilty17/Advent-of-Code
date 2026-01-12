from pathlib import Path
from typing import List, Tuple
import heapq
import math

from Day_24.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.load_input import load_input
from utils.solve import test, solve

def get_entanglement(group: List[int]) -> int:
    return math.prod(group)

def equal_weight_partition(weights: List[int], num_groups: int) -> Tuple[List[int], ...]:
    if num_groups == 1:
        return [list(sorted(weights, reverse=True))]
    
    target_weight = sum(weights) // num_groups

    queue = []
    heapq.heappush(queue, (0, 0, []))

    while queue:

        _, _, group_1 = heapq.heappop(queue)
        
        if sum(group_1) == target_weight:
            remaining_weights = [weight for weight in weights if weight not in group_1]
            remaining_groups = equal_weight_partition(remaining_weights, num_groups-1)
            if remaining_groups:
                return group_1, *remaining_groups

        if sum(group_1) > target_weight:
            continue

        for weight in weights:
            if any(weight >= w for w in group_1):   # this makes sure we aren't counting the same set of weights multiple times
                continue
            new_group_1 = list(group_1) + [weight]
            heapq.heappush(queue, (len(new_group_1), get_entanglement(new_group_1), new_group_1))

    return None

def solution(weights: List[int], num_groups: int) -> int:
    groups = equal_weight_partition(weights, num_groups)
    print(groups)
    return get_entanglement(groups[0])

if __name__ == "__main__":
    num_groups = 3

    example_weights = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 99
    test(expected_answer, solution, example_weights, num_groups)

    weights = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, weights, num_groups)