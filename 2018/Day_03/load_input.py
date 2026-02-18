from pathlib import Path
from typing import List, Tuple
import re

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return [parse_claim(claim) for claim in lines]

def parse_claim(claim_str: str) -> Tuple[int, Tuple[int, int], Tuple[int, int]]:
    pattern = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    m = re.fullmatch(pattern, claim_str)
    if not m:
        raise Exception(f"Failed to parse claim: {claim_str}")

    claim_id = int(m.group(1))
    top_left = (int(m.group(2)), int(m.group(3)))
    dimensions = (int(m.group(4)), int(m.group(5)))
    return claim_id, top_left, dimensions