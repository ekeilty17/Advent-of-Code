from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> List[Dict[str, int]]:
    lines = input_path.read_text().splitlines()
    return dict([parse_stat(stat) for stat in lines])

def parse_stat(stat_str: str) -> Tuple[str, int]:
    name, value = stat_str.split(": ") 
    return name, int(value)