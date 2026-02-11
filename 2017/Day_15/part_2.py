from pathlib import Path
from typing import List, Dict

from Day_15.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_15.load_input import load_input
from Day_15.part_1 import judge
from Day_15.part_1 import generate_next_value as generate_next_value_part_1

from utils.solve import test, solve

def generate_next_value(value: int, factor: int, modulus: int, multiple: int) -> int:
    value = generate_next_value_part_1(value, factor, modulus)
    while value % multiple:
        value = generate_next_value_part_1(value, factor, modulus)

    return value

def brute_force(A: Dict[str, int], B: Dict[str, int], N:int) -> int:

    total = 0
    for _ in range(N):
        A["value"] = generate_next_value(**A)
        B["value"] = generate_next_value(**B)

        if judge(A["value"], B["value"]):
            total += 1
    
    return total

def solution(generators: Dict[str, int], factors: Dict[str, int], modulus: int, N:int) -> int:
    A = {"value": generators["A"], "factor": factors["A"], "modulus": modulus, "multiple": 4}
    B = {"value": generators["B"], "factor": factors["B"], "modulus": modulus, "multiple": 8}
    return brute_force(A, B, N)

if __name__ == "__main__":
    factors = {"A": 16_807, "B": 48_271}
    modulus = 2_147_483_647
    N = 5_000_000

    example_generators = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 309
    test(expected_answer, solution, example_generators, factors, modulus, N)

    generators = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, generators, factors, modulus, N)