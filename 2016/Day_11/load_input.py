from pathlib import Path
from typing import List, Tuple, Set
import re

def load_input(input_path: Path) -> List[Set[Tuple[str, str]]]:
    lines = input_path.read_text().splitlines()
    floors = [parse_floor(line) for line in lines]
    return [floor for _, floor in sorted(floors)]

def parse_floor(floor_description: str) -> Set[Tuple[str, str]]:
    floor_pattern = re.compile(r"The ([A-Za-z]+) floor")
    floor_text = floor_pattern.findall(floor_description)[0]
    floor_text_to_number = {
        "first": 1,
        "second": 2,
        "third": 3,
        "fourth": 4
    }
    floor_num = floor_text_to_number[floor_text]

    device_pattern = re.compile(r"(\S+) (microchip|generator)")
    devices = device_pattern.findall(floor_description)
    return floor_num, set([(name.replace("-compatible", ""), type) for name, type in devices])