from pathlib import Path
from typing import List, Tuple, Dict
import re

def load_input(input_path: Path) -> List[Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]]:
    lines = input_path.read_text().splitlines()
    return [parse_partical_properties(partical_properties) for partical_properties in lines]

def parse_partical_properties(partical_properties_str: str) -> Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]:
    pattern = r"p=<(.+)>, v=<(.+)>, a=<(.+)>"
    m = re.fullmatch(pattern, partical_properties_str)
    if not m:
        raise Exception("Unable to parse partical properties")
    
    return (
        parse_coordinates(m.group(1)),
        parse_coordinates(m.group(2)),
        parse_coordinates(m.group(3)),
    )

def parse_coordinates(coordinate_str: str) -> Tuple[int, int, int]:
    return tuple([int(x.strip()) for x in coordinate_str.split(",")])