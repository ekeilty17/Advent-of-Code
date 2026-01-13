from pathlib import Path
from typing import List, Dict, Any
import re

def load_input(input_path: Path) -> List[Dict[str, Any]]:
    lines = input_path.read_text().splitlines()
    return [parse_line(line) for line in lines]

def parse_line(line: str) -> Dict[str, Any]:
    
    rect_pattern = r"(rect) (\d+)x(\d+)"
    m = re.fullmatch(rect_pattern, line)
    if m:
        groups = m.groups()
        return {
            "raw": line,
            "type": groups[0],
            "shape": (int(groups[1]), int(groups[2]))
        }
    
    rotate_pattern = r"(rotate row|rotate column) (x|y)=(\d+) by (\d+)"
    m = re.fullmatch(rotate_pattern, line)
    if m:
        groups = m.groups()
        return {
            "raw": line,
            "type": groups[0],
            "index": int(groups[2]),
            "shift": int(groups[3])
        }
    
    raise ValueError(f"Unable to parse line: {line}")