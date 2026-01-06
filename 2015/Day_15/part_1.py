from pathlib import Path
from typing import Dict
import numpy as np

from Day_15.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_15.load_input import load_input
from utils.test import test

def compositions(n, N):
    if n == 1:
        if N >= 1:
            yield (N,)
        return

    for i in range(1, N - n + 2):
        for rest in compositions(n - 1, N - i):
            yield (i,) + rest

def compute_score(A, x):
    return np.prod(np.maximum(A @ x, 0))

def solution(ingredients: Dict[str, Dict[str, int]], N: int) -> int:
    A = np.array([[val for prop, val in properties.items() if prop != "calories"] for properties in ingredients.values()]).T
    
    max_score = max(compute_score(A, np.array(x)) for x in compositions(len(ingredients), N))
    return max_score

if __name__ == "__main__":
    
    example_ingredients = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    ingredients = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    example_N = 100
    expected_answer = 62842880
    test(expected_answer, solution, example_ingredients, example_N)

    N = 100
    total = solution(ingredients, N)
    print("Puzzle Answer:", total)


"""
f(x, y) = max(c1*x + c2*y, 0) * max(d1*x + d2*y, 0) * max(f1*x + f2*y, 0) * max(t1*x + t2*y, 0)


maximize
f(x, y) = (c1*x + c2*y) * (d1*x + d2*y) * (f1*x + f2*y) * (t1*x + t2*y)
st. x > 0
    y > 0
    c1*x + c2*y > 0
    d1*x + d2*y > 0
    f1*x + f2*y > 0
    t1*x + t2*y > 0
"""