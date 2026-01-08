from pathlib import Path
from typing import List, Tuple, TypeAlias

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import milp, LinearConstraint

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.solve import test, solve

IndicatorLights: TypeAlias = List[bool]
ButtonWiringSchematic: TypeAlias = List[int]
JoltageRequirements: TypeAlias = List[int]

def index2vector(indexes, max_length) -> NDArray[np.int64]:
    I = np.zeros((len(indexes), max_length))
    for i, j in enumerate(indexes):
        I[i, j] = 1
    return I

def integer_programming(A: NDArray[np.int64], b: NDArray[np.int64]) -> NDArray[np.int64]:
    """
    Solving min x s.t. Ax = b and x >= 0 for integer solutions of x
    """
    m, n = A.shape
    if b.shape[0] != m:
        raise ValueError(f"Shape of b {b.shape} must match shape of A {A.shape}")
    c = np.ones(n)

    b_l = b.copy()
    b_u = b.copy()
    constraints = LinearConstraint(A, b_l, b_u)

    integrality = np.ones_like(c, dtype=int)        # whether the output needs is an integer

    res = milp(c=c, constraints=constraints, integrality=integrality)
    return res.x


def solution(machines: List[Tuple[IndicatorLights, List[ButtonWiringSchematic], JoltageRequirements]]) -> int:
    
    min_button_presses = []
    for _, button_wiring_schema, joltage_requirements in machines:
        
        A = index2vector(button_wiring_schema, len(joltage_requirements))
        A = A.T
        b = np.array(joltage_requirements)

        min_button_presses.append(
            int(sum(integer_programming(A, b)))
        )
    
    return sum(min_button_presses)

if __name__ == "__main__":
    example_machines = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 33
    test(expected_answer, solution, example_machines)

    machines = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))
    solve(solution, machines)