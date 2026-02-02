from pathlib import Path
from typing import List

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from Day_08.part_1 import Instruction, execute_condition, execute_operation
from utils.solve import test, solve

def solution(instructions: List[Instruction]) -> int:
    registers = {}
    max_register_value = 0
    
    for operation, condition in instructions:
        if execute_condition(registers, condition):
            execute_operation(registers, operation)

        if registers:
            max_register_value = max(max_register_value, max(registers.values()))

    return max_register_value

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 10
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)