from pathlib import Path
from typing import Dict
import numpy as np

from Day_15.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_15.load_input import load_input
from Day_15.part_1 import compositions, compute_score
from utils.solve import test, solve

def solution(ingredients: Dict[str, Dict[str, int]], N: int, max_calories: int) -> int:
    A = np.array([[val for prop, val in properties.items() if prop != "calories"] for properties in ingredients.values()]).T
    calories = np.array([prop["calories"] for prop in ingredients.values()])

    max_score = 0
    for x in compositions(len(ingredients), N):
        if calories @ x == max_calories:
            max_score = max(max_score, compute_score(A, np.array(x)))
    
    return max_score

if __name__ == "__main__":
    example_ingredients = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_N = 100
    example_max_calories = 500
    expected_answer = 57600000
    test(expected_answer, solution, example_ingredients, example_N, example_max_calories)

    ingredients = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    N = 100
    max_calories = 500
    solve(solution, ingredients, N, max_calories)