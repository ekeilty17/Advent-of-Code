from pathlib import Path
from typing import Dict, Tuple
import re

def load_input(input_path: Path) -> Dict[str, int]:
    lines = input_path.read_text().splitlines()
    return dict([parse_generator(generator) for generator in lines])

def parse_generator(generator_str: str) -> Tuple[str, int]:
    pattern = r"Generator ([A-Z]+) starts with (\d+)"
    m = re.fullmatch(pattern, generator_str)
    if not m:
        raise Exception(f"Unable to parse generator: {generator_str}")

    return m.group(1), int(m.group(2))