from pathlib import Path
from typing import List, Tuple, Dict

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from utils.solve import test, solve

def compute_redistribution(init_memory: List[int]) -> Tuple[List[int], Dict[Tuple[int, ...], int]]:
    memory = list(init_memory)
    history = {}
    
    while tuple(memory) not in history:
        history[tuple(memory)] = len(history)

        max_bank, max_blocks = max(enumerate(memory), key=lambda t: (t[1], -t[0]))
        redistribution = max_blocks // len(memory)
        extra = max_blocks % len(memory)

        memory[max_bank] = 0
        for bank in range(len(memory)):
            memory[bank] += redistribution
        for i in range(extra):
            memory[(max_bank + 1 + i) % len(memory)] += 1

    return memory, history

def solution(memory: List[int]) -> int:
    _, history = compute_redistribution(memory)
    return len(history)

if __name__ == "__main__":
    example_memory = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 5
    test(expected_answer, solution, example_memory)

    memory = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, memory)