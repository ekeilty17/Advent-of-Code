from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> Tuple[List[int], List[int]]:
    lines = input_path.read_text().splitlines()
    line_pairs = [[x for x in line.split(" ") if x] for line in lines]
    left_location_ids = [int(left_location_id) for left_location_id, _ in line_pairs]
    right_location_ids = [int(right_location_id) for _, right_location_id in line_pairs]
    return left_location_ids, right_location_ids