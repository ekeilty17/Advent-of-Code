from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[str, List[int|str]]]:
    lines = input_path.read_text().splitlines()
    return [parse_instruction(instruction) for instruction in lines]

def parse_instruction(instruction_str: str) -> Tuple[str, List[int|str]]:
    opcode, *operands = instruction_str.split(" ")
    for i in range(len(operands)):
        try:
            operands[i] = int(operands[i])
        except:
            pass
    return opcode, operands