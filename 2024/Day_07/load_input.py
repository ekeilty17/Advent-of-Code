from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> Dict[int, List[int]]:
    lines = input_path.read_text().splitlines()
    equations = [parse_equation(equation) for equation in lines]
    return dict(equations)

def parse_equation(equation_str: str) -> Tuple[int, List[int]]:
    result, operand_str = equation_str.split(": ")
    operands = operand_str.split(" ")
    return int(result), [int(x) for x in operands]