from pathlib import Path
from typing import List, Tuple, Dict, TypeAlias

from Day_25.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_25.load_input import load_input
from utils.solve import test, solve

Instruction: TypeAlias = Tuple[int, str, str]

def simulate_turing_machine(start_state: str, num_steps: int, instructions_by_state: Dict[str, List[Instruction]]) -> Dict[int, int]:
    tape = {}
    cursor = 0
    state = start_state

    for _ in range(num_steps):
        instructions = instructions_by_state[state]
        value = tape.get(cursor, 0)
        
        write, cursor_direction, next_state = instructions[value]
        tape[cursor] = write
        cursor += 1 if cursor_direction == "right" else -1
        state = next_state

    return tape

def solution(start_state: str, num_steps: int, instructions_by_state: Dict[str, List[Instruction]]) -> int:
    tape = simulate_turing_machine(start_state, num_steps, instructions_by_state)
    return sum(tape.values())

if __name__ == "__main__":
    example_start_state, example_num_steps, example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_start_state, example_num_steps, example_instructions)

    start_state, num_steps, instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, start_state, num_steps, instructions)