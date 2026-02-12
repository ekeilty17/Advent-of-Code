from pathlib import Path
from typing import List, Tuple, TypeAlias

from Day_20.const import DAY, INPUT_FILE_NAME
from Day_20.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_20.load_input import load_input
from utils.solve import test, solve

Position: TypeAlias = Tuple[int, int, int]
Velocity: TypeAlias = Tuple[int, int, int]
Acceleration: TypeAlias = Tuple[int, int, int]

def v(t: int, v0: int, a: int) -> int:
    return v0 + a*t

def p(t: int, p0: int, v0: int, a: int) -> int:
    return p0 + v0*t + int(0.5*t*(t+1)*a)

def V(t: int, V0: Velocity, A: Acceleration) -> Velocity:
    return tuple([v(t, v0, a) for v0, a in zip(V0, A)])

def P(t: int, P0: Position, V0: Velocity, A: Acceleration) -> Position:
    return tuple([p(t, p0, v0, a) for p0, v0, a in zip(P0, V0, A)])

def manhattan_distance(*X: int) -> int:
    return sum(abs(x) for x in X)

def empirical(particle_properties: List[Tuple[Position, Velocity, Acceleration]]) -> int:
    t_large = 1_000_000
    P_large = [P(t_large, P0, V0, A) for P0, V0, A in particle_properties]
    long_term_distance = [manhattan_distance(*X) for X in P_large]

    min_index, min_distance = min(enumerate(long_term_distance), key=lambda t: t[1])
    return min_index

def analytic(particle_properties: List[Tuple[Position, Velocity, Acceleration]]) -> int:
    scores = [(manhattan_distance(*A), manhattan_distance(*V0), manhattan_distance(*P0)) for P0, V0, A in particle_properties]
    min_index, min_score = min(enumerate(scores), key=lambda t: t[1])
    return min_index

def solution(particle_properties: List[Tuple[Position, Velocity, Acceleration]]) -> int:
    # return empirical(particle_properties)
    return analytic(particle_properties)

if __name__ == "__main__":
    example_particle_properties = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 0
    test(expected_answer, solution, example_particle_properties)

    particle_properties = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, particle_properties)