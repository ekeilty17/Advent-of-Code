from pathlib import Path
from typing import Dict

from Day_12.const import DAY, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.part_1 import update_state
from utils.solve import solve

def solution(initial_state: str, transitions: Dict[str, str], context_size: int, num_generations: int) -> int:
    state = initial_state
    leftmost_pot = 0
    
    for k in range(num_generations):
        prev_state = state
        prev_leftmost_pot = leftmost_pot

        state, leftmost_pot = update_state(state, leftmost_pot, transitions, context_size)
        
        if state == prev_state:
            leftmost_pot_difference = leftmost_pot - prev_leftmost_pot
            break
    
    leftmost_pot += leftmost_pot_difference * (num_generations - k - 1)
    return sum([pot for pot, plant in enumerate(state, leftmost_pot) if plant == "#"])

if __name__ == "__main__":
    context_size = 5
    num_generations = 50_000_000_000

    initial_state, transitions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, initial_state, transitions, context_size, num_generations)