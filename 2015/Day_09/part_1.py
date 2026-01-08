from pathlib import Path
from typing import List, Tuple, Dict
from itertools import permutations

from Day_09.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_09.load_input import load_input
from utils.solve import test, solve

def compute_total_distance(path: List[str], distance_by_city_pairs: Dict[Tuple[str, str], int]):
    total_distance = 0
    for c1, c2 in zip(path[:-1], path[1:]):
        total_distance += distance_by_city_pairs[tuple(sorted([c1, c2]))]
    return total_distance

def solution(city_distances: List[Tuple[str, str, int]]) -> int:
    cities = set([c1 for c1, _, _ in city_distances] + [c2 for _, c2, _ in city_distances])
    distance_by_city_pairs = {
        tuple(sorted([c1, c2])): distance for c1, c2, distance in city_distances
    }
    
    min_path = min(permutations(cities), key=lambda path: compute_total_distance(path, distance_by_city_pairs))
    return compute_total_distance(min_path, distance_by_city_pairs)

if __name__ == "__main__":
    example_city_distances = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 605
    test(expected_answer, solution, example_city_distances)

    city_distances = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, city_distances)