from pathlib import Path
from typing import List, Tuple, Dict
from itertools import permutations

from Day_09.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_09.load_input import load_input
from Day_09.part_1 import compute_total_distance
from utils.solve import test, solve

def solution(city_distances: List[Tuple[str, str, int]]) -> int:
    cities = set([c1 for c1, _, _ in city_distances] + [c2 for _, c2, _ in city_distances])
    distance_by_city_pairs = {
        tuple(sorted([c1, c2])): distance for c1, c2, distance in city_distances
    }
    
    max_path = max(permutations(cities), key=lambda path: compute_total_distance(path, distance_by_city_pairs))
    return compute_total_distance(max_path, distance_by_city_pairs)

if __name__ == "__main__":
    example_city_distances = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 982
    test(expected_answer, solution, example_city_distances)

    city_distances = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, city_distances)