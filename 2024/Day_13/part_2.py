from pathlib import Path
from typing import List, Dict, Tuple

from Day_13.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_13.load_input import load_input
from Day_13.part_1 import solution as part_1_solution
from utils.test import test

def correct_prize_locations(machines: List[Dict[str, Tuple[int, int]]], correction: int) -> None:
    for machine in machines:
        machine["prize"] = tuple([coord + correction for coord in machine["prize"]])

def solution(machines: List[Dict[str, Tuple[int, int]]]) -> int:
    return part_1_solution(machines)

if __name__ == "__main__":
    
    example_machines = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    machines = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    prize_correction = 10000000000000
    correct_prize_locations(example_machines, prize_correction)
    correct_prize_locations(machines, prize_correction)

    expected_answer = 875318608908
    test(expected_answer, solution, example_machines)

    total = solution(machines)
    print("Puzzle Answer:", total)