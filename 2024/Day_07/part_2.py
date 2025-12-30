from pathlib import Path
from typing import List, Dict

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from Day_07.part_1 import evaluate_operation
from Day_07.part_1 import solution as part_1_solution
from utils.test import test

def dfs(target_result: int, allowed_operations: List[str], current_result: int, operands_remaining: List[int]) -> bool:
    if len(operands_remaining) == 0:
        return current_result == target_result
    
    # Can't be >= because sometimes `1` is an operand
    if current_result > target_result:
        return False

    for operation in allowed_operations:
        operand, *updated_operands_remaining = operands_remaining
        updated_result = evaluate_operation(current_result, operation, operand)
        solution_found = dfs(target_result, allowed_operations, updated_result, updated_operands_remaining)
        if solution_found:
            return True
        
    return False

def solution(equations: Dict[int, List[int]], allowed_operations: List[str]) -> int:
    # return part_1_solution(equations, allowed_operations)      # This does work, but it's a bit slow
    
    total = 0
    for target_result, operands in equations.items():
        operand, *operands_remaining = operands
        if dfs(target_result, allowed_operations, operand, operands_remaining):
            total += target_result
    
    return total

if __name__ == "__main__":
    
    example_equations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    equations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    allowed_operations = ["+", "*", "||"]

    expected_answer = 11387
    test(expected_answer, solution, example_equations, allowed_operations)

    total = solution(equations, allowed_operations)
    print("Puzzle Answer:", total)