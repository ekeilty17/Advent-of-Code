from pathlib import Path
from typing import List, Dict, Tuple
import numpy as np

from Day_13.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_13.load_input import load_input
from utils.test import test

def to_int(x: float) -> int:
    return int(round(x, 0))

def invert_2x2_matrix(a, b, c, d):
    iD = a*d - b*c
    if iD == 0:
        return None, None, None, None
    return d/iD, -b/iD, -c/iD, a/iD, 

def find_minimium_button_presses(button_A: Tuple[int, int], button_B: Tuple[int, int], prize: Tuple[int, int]) -> Tuple[float, float]:
    a, c = button_A
    b, d = button_B
    Px, Py = prize
    
    ia, ib, ic, id = invert_2x2_matrix(a, b, c, d)
    if ia is None:
        return 0, 0
    
    A = Px * ia + Py * ib
    B = Px * ic + Py * id

    return A, B

def is_solution(button_A: Tuple[int, int], button_B: Tuple[int, int], prize: Tuple[int, int], A: int, B: int) -> bool:
    a, c = button_A
    b, d = button_B
    Px, Py = prize

    return (a * A + b * B == Px) and (c * A + d * B == Py)

###########################################
# same as above, just implemented in numpy
###########################################
def find_minimium_button_presses_numpy(button_A: Tuple[int, int], button_B: Tuple[int, int], prize: Tuple[int, int]) -> Tuple[float, float]:
    M = np.array([button_A, button_B]).T
    b = np.array(prize)
    x = np.linalg.solve(M, b)

    A, B = x
    return A, B

def is_solution_numpy(button_A: Tuple[int, int], button_B: Tuple[int, int], prize: Tuple[int, int], A: int, B: int) -> bool:
    M = np.array([button_A, button_B]).T
    b = np.array(prize)
    x = np.array([A, B])

    b_star = M @ x
    return np.array_equal(b, b_star)
###########################################
# same as above, just implemented in numpy
###########################################

def solution(machines: List[Dict[str, Tuple[int, int]]]) -> int:
    total_prizes = 0
    total_tokens = 0
    for machine in machines:
        A, B = find_minimium_button_presses(**machine)
        
        # we only care about integer solutions
        A, B = to_int(A), to_int(B)
        if is_solution(**machine, A=A, B=B):
            total_prizes += 1
            total_tokens += 3*A + 1*B
    
    return total_tokens

if __name__ == "__main__":
    
    example_machines = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    machines = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 480
    test(expected_answer, solution, example_machines)

    total = solution(machines)
    print("Puzzle Answer:", total)