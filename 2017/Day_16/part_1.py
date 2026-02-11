from pathlib import Path
from typing import List, Any
import string

from Day_16.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_16.load_input import load_input
from utils.solve import test, solve

def init_programs(num_programs: int) -> List[Any]:
    return list(string.ascii_lowercase[:num_programs])

def spin(programs: List[Any], X: int) -> List[Any]:
    X = (-X) % len(programs)
    return programs[X:] + programs[:X]

def exchange(programs: List[Any], X: int, Y: int) -> List[Any]:
    programs[X], programs[Y] = programs[Y], programs[X]
    return programs

def partner(programs: List[Any], A: Any, B: Any) -> List[Any]:
    X = programs.index(A)
    Y = programs.index(B)
    return exchange(programs, X, Y)

def parse_move(programs: List[Any], move: str) -> List[Any]:
    if move[0] == "s":
        X = move[1:]
        return spin(programs, int(X))
    
    if move[0] == "x":
        X, Y = move[1:].split("/")
        return exchange(programs, int(X), int(Y))

    if move[0] == "p":
        A, B = move[1:].split("/")
        return partner(programs, A, B)

    raise Exception(f"Unable to parse dance move: {move}")

def execute_moves(programs: List[str], dance_moves: List[str]) -> List[str]:
    programs = list(programs)
    for move in dance_moves:
        programs = parse_move(programs, move)
    return programs

def solution(dance_moves: str, num_programs: int) -> str:
    programs = init_programs(num_programs)
    programs = execute_moves(programs, dance_moves)
    return "".join(programs)

if __name__ == "__main__":
    example_dance_moves = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_num_programs = 5
    expected_answer = "baedc"
    test(expected_answer, solution, example_dance_moves, example_num_programs)

    dance_moves = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    num_programs = 16
    solve(solution, dance_moves, num_programs)