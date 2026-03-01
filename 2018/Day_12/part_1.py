from pathlib import Path
from typing import Dict, Tuple

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.solve import test, solve

def update_state(state: str, leftmost_pot: int, transitions: Dict[str, str], context_size: int) -> Tuple[str, int]:
    padding = "." * (context_size-1)
    state = padding + state + padding
    
    # standard automata update
    new_state = ""
    for i in range(len(state)-context_size):
        pot = state[i:i+context_size]
        new_pot = transitions.get(pot, ".")
        new_state += new_pot
    new_leftmost_pot = leftmost_pot - context_size//2

    # Trim excess '.'
    for i in range(len(new_state)):
        if new_state[i] == "#":
            break
    for j in reversed(range(len(new_state))):
        if new_state[j] == "#":
            break
    new_state = new_state[i:j+1]
    new_leftmost_pot += i

    return new_state, new_leftmost_pot

def solution(initial_state: str, transitions: Dict[str, str], context_size: int, num_generations: int) -> int:
    state = initial_state
    leftmost_pot = 0
    
    for _ in range(num_generations):
        prev_state = state
        state, leftmost_pot = update_state(state, leftmost_pot, transitions, context_size)
        if state == prev_state:
            break
    
    return sum([pot for pot, plant in enumerate(state, leftmost_pot) if plant == "#"])

if __name__ == "__main__":
    context_size = 5
    num_generations = 20

    example_initial_state, example_transitions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 325
    test(expected_answer, solution, example_initial_state, example_transitions, context_size, num_generations)

    initial_state, transitions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, initial_state, transitions, context_size, num_generations)