from pathlib import Path
from typing import List, Dict
from itertools import product

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from utils.test import test

def evaluate_operation(operand1: int, operation: str, operand2: int) -> int:
    if operation == "+":
        return operand1 + operand2
    if operation == "*":
        return operand1 * operand2
    if operation == "||":
        return int(f"{operand1}{operand2}")
    raise ValueError(f"Expected one of '+', '*', or '||' for the operation, instead got '{operation}'")

def evaluate_equation(operands: List[int], operations: List[str]) -> int:
    total = operands[0]
    for operation, operand in zip(operations, operands[1:]):
        total = evaluate_operation(total, operation, operand)
    return total

def solution(equations: Dict[int, List[int]], allowed_operations: List[str]) -> int:
    
    total = 0
    for target_result, operands in equations.items():
        for operations in product(allowed_operations, repeat=len(operands)-1):
            result = evaluate_equation(operands, operations)
            if result == target_result:
                total += result
                break
    
    return total

if __name__ == "__main__":
    
    example_equations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    equations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    allowed_operations = ["+", "*"]

    expected_answer = 3749
    test(expected_answer, solution, example_equations, allowed_operations)

    total = solution(equations, allowed_operations)
    print("Puzzle Answer:", total)