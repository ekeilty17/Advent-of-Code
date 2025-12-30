from pathlib import Path
from typing import List, Tuple

from Day_14.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_14.load_input import load_input
from utils.test import test

def compute_final_position(floor_shape: Tuple[int, int], initial_position: Tuple[int, int], velocity: Tuple[int, int], t: int=1) -> Tuple[int, int]:
    m, n = floor_shape
    x0, y0 = initial_position
    vx, vy = velocity

    xf = (x0 + vx * t) % m
    yf = (y0 + vy * t) % n
    return xf, yf

def solution(floor_shape: Tuple[int, int], initial_positions: List[Tuple[int, int]], velocities: List[Tuple[int, int]], seconds: int) -> int:
    final_positions = [
        compute_final_position(floor_shape, initial_position, velocity, seconds)
        for initial_position, velocity in zip(initial_positions, velocities)
    ]
    
    m, n = floor_shape
    middle_x, middle_y = m//2, n//2

    Q1 = Q2 = Q3 = Q4 = 0           # these are not the same quadrant definitions as in typical Cartesian geometry
    for xf, yf in final_positions:
        if xf < middle_x:
            if yf < middle_y:
                Q1 += 1
            elif yf > middle_y:
                Q2 += 1
        elif xf > middle_x:
            if yf < middle_y:
                Q3 += 1
            elif yf > middle_y:
                Q4 += 1  

    return Q1 * Q2 * Q3 * Q4

if __name__ == "__main__":
    
    example_positions, example_velocities = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    positions, velocities = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    example_floor_shape = (11, 7)
    example_seconds = 100
    expected_answer = 12
    test(expected_answer, solution, example_floor_shape, example_positions, example_velocities, example_seconds)

    floor_shape = (101, 103)
    seconds = 100
    total = solution(floor_shape, positions, velocities, seconds)
    print("Puzzle Answer:", total)