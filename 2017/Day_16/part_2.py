from pathlib import Path
from typing import List

from Day_16.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_16.load_input import load_input
from Day_16.part_1 import init_programs, execute_moves
from utils.solve import test, solve

def brute_force(dance_moves: str, programs: List[str], num_dances: int) -> List[int]:
    for _ in range(num_dances):
        programs = execute_moves(programs, dance_moves)
    return programs

def cycle_solution(dance_moves: str, programs: List[str], num_dances: int) -> List[str]:

    cycle = []
    while tuple(programs) not in cycle:
        cycle.append(tuple(programs))
        programs = execute_moves(programs, dance_moves)
    
    return list(cycle[num_dances % len(cycle)])

def solution(dance_moves: str, num_programs: int, num_dances: int) -> str:
    programs = init_programs(num_programs)
    # programs = brute_force(dance_moves, programs, num_dances)
    programs = cycle_solution(dance_moves, programs, num_dances)
    return "".join(programs)

if __name__ == "__main__":
    example_dance_moves = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_num_programs = 5
    example_num_dances = 2
    expected_answer = "ceadb"
    test(expected_answer, solution, example_dance_moves, example_num_programs, example_num_dances)

    dance_moves = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    num_programs = 16
    num_dances = 1_000_000_000
    solve(solution, dance_moves, num_programs, num_dances)