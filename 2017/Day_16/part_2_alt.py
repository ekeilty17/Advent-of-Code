from pathlib import Path
from typing import List, Tuple, Dict, Any

from Day_16.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_16.load_input import load_input
from Day_16.part_1 import init_programs, execute_moves, spin, exchange, partner
from utils.solve import test, solve

def brute_force(dance_moves: str, programs: List[str], num_dances: int) -> List[int]:
    for _ in range(num_dances):
        programs = execute_moves(programs, dance_moves)
    return programs

def get_permutations(programs: List[Any], dance_moves: List[str]) -> Tuple[List[int], Dict[str, str]]:
    
    index_perm = list(range(len(programs)))
    element_perm = list(programs)
    
    for move in dance_moves:
        if move[0] == "s":
            X = move[1:]
            index_perm = spin(index_perm, int(X))
        
        elif move[0] == "x":
            X, Y = move[1:].split("/")
            index_perm = exchange(index_perm, int(X), int(Y))

        elif move[0] == "p":
            A, B = move[1:].split("/")
            element_perm = partner(element_perm, A, B)

        else:
            raise Exception(f"Unable to parse dance move: {move}")

    element_perm = {A: B for A, B in zip(programs, element_perm)}
    
    return index_perm, element_perm

def execute_index_permutation(lst: List[Any], perm: List[int]) -> List[Any]:
    return [lst[i] for i in perm]

def execute_element_permutation(lst: List[Any], perm: Dict[Any, Any]) -> List[Any]:
    return [perm[A] for A in lst]

def compose_index_permutations(perm1: List[int], perm2: List[int]) -> List[int]:
    return execute_index_permutation(perm1, perm2)

def compose_element_permutations(perm1: Dict[Any, Any], perm2: Dict[Any, Any]) -> Dict[Any, Any]:
    return {A: perm2[B] for A, B in perm1.items()}

def better_brute_force(dance_moves: str, programs: List[str], num_dances: int) -> List[str]:
    programs = init_programs(num_programs)
    index_perm, element_perm = get_permutations(programs, dance_moves)

    for _ in range(num_dances):
        programs = execute_index_permutation(programs, index_perm)
        programs = execute_element_permutation(programs, element_perm)

    return programs

def compose_n_index_permutations(index_perm: List[int], n: int) -> List[int]:
    binary_digits = list(reversed([int(b) for b in bin(n)[2:]]))

    intermediates = [index_perm]
    for _ in range(1, len(binary_digits)):
        intermediates.append( compose_index_permutations(intermediates[-1], intermediates[-1]) )
    
    P = list(range(len(index_perm)))
    for b, perm in zip(binary_digits, intermediates):
        if b:
            P = compose_index_permutations(P, perm)
    return P

def compose_n_element_permutations(element_perm: Dict[str, str], n: int) -> Dict[str, str]:
    binary_digits = list(reversed([int(b) for b in bin(n)[2:]]))

    intermediates = [element_perm]
    for _ in range(1, len(binary_digits)):
        intermediates.append( compose_element_permutations(intermediates[-1], intermediates[-1]) )

    P = {A: A for A in element_perm.keys()}
    for b, perm in zip(binary_digits, intermediates):
        if b:
            P = compose_element_permutations(P, perm)
    return P

def efficient_permutation_solution(dance_moves: str, programs: List[str], num_dances: int) -> List[int]:
    index_perm, element_perm = get_permutations(programs, dance_moves)

    total_index_perm = compose_n_index_permutations(index_perm, num_dances)
    total_element_perm = compose_n_element_permutations(element_perm, num_dances)

    programs = execute_index_permutation(programs, total_index_perm)
    programs = execute_element_permutation(programs, total_element_perm)

    return programs

def solution(dance_moves: str, num_programs: int, num_dances: int) -> str:
    programs = init_programs(num_programs)
    # programs = brute_force(dance_moves, programs, num_dances)
    # programs = better_brute_force(dance_moves, programs, num_dances)
    programs = efficient_permutation_solution(dance_moves, programs, num_dances)
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