from pathlib import Path
from typing import List, Tuple, Callable

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.solve import test, solve

def update_position(position: Tuple[int, int], velocity: Tuple[int, int], t: int=1) -> Tuple[int, int]:
    return tuple([x + t*v for x, v in zip(position, velocity)])

def manhattan_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2 - x1) + abs(y2 - y1)

def total_pairwise_distance(positions: List[Tuple[int, int]]) -> int:
    return sum([
        manhattan_distance(positions[i], positions[j])
        for i in range(len(positions))
        for j in range(i+1, len(positions))
    ])

def binary_search_for_minimum(f: Callable[[int], int], a0: int = 0, b0: int = 1e6) -> int:
    a = a0
    b = b0
    phi = (1 + 5**0.5)/2

    while a < b-2:
        x1 = int(b - (b - a) / phi)
        x2 = int(a + (b - a) / phi)
        if f(x1) < f(x2):
            a, b = a, x2
        else:
            a, b = x1, b
    
    return min(range(a, b+1), key=lambda x: f(x))

def solution(positions: List[Tuple[int, int]], velocities: List[Tuple[int, int]]) -> int:
    
    def f(t: int) -> int:
        final_positions = [update_position(position, velocity, t) for position, velocity in zip(positions, velocities)]
        return total_pairwise_distance(final_positions)

    t_star = binary_search_for_minimum(f)
    return t_star

if __name__ == "__main__":
    example_positions, example_velocities = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_positions, example_velocities)

    positions, velocities = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, positions, velocities)