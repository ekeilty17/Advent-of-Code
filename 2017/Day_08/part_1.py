from pathlib import Path
from typing import List, Tuple, Dict, TypeAlias

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from utils.solve import test, solve

Operation: TypeAlias = Tuple[str, str, int]
Condition: TypeAlias = Tuple[str, str, int]
Instruction: TypeAlias = Tuple[Operation, Condition]

def execute_condition(registers: Dict[str, int], condition: Condition) -> bool:
    compare_func_map = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        "<": lambda x, y: x < y,
        "<=": lambda x, y: x <= y,
        ">": lambda x, y: x > y,
        ">=": lambda x, y: x >= y,
    }
    
    r, compare_type, y = condition
    x = registers.get(r, 0)
    return compare_func_map[compare_type](x, y)

def execute_operation(registers: Dict[str, int], operation: Operation) -> None:
    opcode_func_map = {
        "inc": lambda x, y: x + y,
        "dec": lambda x, y: x - y,
    }

    r, opcode, y = operation
    x = registers.get(r, 0)
    registers[r] = opcode_func_map[opcode](x, y)

def solution(instructions: List[Instruction]) -> int:
    registers = {}
    
    for operation, condition in instructions:
        if execute_condition(registers, condition):
            execute_operation(registers, operation)
    
    return max(registers.values())

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 1
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)