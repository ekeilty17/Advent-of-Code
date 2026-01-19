from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[str, List[str|int]]]:
    lines = input_path.read_text().splitlines()
    return [parse_instruction(instruction) for instruction in lines]

def parse_operand(operand_str: str) -> str|int:
    try:
        return int(operand_str)
    except:
        return operand_str

def parse_instruction(instruction_str: str) -> Tuple[str, List[str|int]]:
    opcode, *operands = instruction_str.split(" ")
    operands = [parse_operand(operand) for operand in operands]
    return opcode, operands