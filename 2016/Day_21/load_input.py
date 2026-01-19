from pathlib import Path
from typing import List
import re

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return [parse_operation(operation) for operation in lines]

def parse_operation(operation_str: str):
    swap_position_pattern = r"swap position (\d+) with position (\d+)"
    m = re.fullmatch(swap_position_pattern, operation_str)
    if m:
        return {
            "raw": operation_str,
            "operation": "swap_position",
            "positions": (int(m.group(1)), int(m.group(2)))
        }
    
    swap_letters_pattern = r"swap letter ([A-Za-z]+) with letter ([A-Za-z]+)"
    m = re.fullmatch(swap_letters_pattern, operation_str)
    if m:
        return {
            "raw": operation_str,
            "operation": "swap_letters",
            "letters": (m.group(1), m.group(2))
        }
    
    rotate_letter_pattern = r"rotate based on position of letter ([A-Za-z]+)"
    m = re.fullmatch(rotate_letter_pattern, operation_str)
    if m:
        return {
            "raw": operation_str,
            "operation": "rotate_letter",
            "letter": m.group(1)
        }
    
    rotate_steps_pattern = r"rotate (left|right) (\d+) step(s?)"
    m = re.fullmatch(rotate_steps_pattern, operation_str)
    if m:
        return {
            "raw": operation_str,
            "operation": "rotate_steps",
            "direction": m.group(1),
            "steps": int(m.group(2))
        }
    
    reverse_pattern = r"reverse positions (\d+) through (\d+)"
    m = re.fullmatch(reverse_pattern, operation_str)
    if m:
        return {
            "raw": operation_str,
            "operation": "reverse",
            "positions": (int(m.group(1)), int(m.group(2)))
        }
    
    move_pattern = r"move position (\d+) to position (\d+)"
    m = re.fullmatch(move_pattern, operation_str)
    if m:
        return {
            "raw": operation_str,
            "operation": "move",
            "positions": (int(m.group(1)), int(m.group(2)))
        }
    
    raise ValueError(f"Unable to parse line: {operation_str}")