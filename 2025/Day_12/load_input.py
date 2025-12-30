from pathlib import Path
from typing import List, Tuple, TypeAlias
import numpy as np
from numpy.typing import NDArray
import re

PresentShape: TypeAlias = NDArray[np.bool_]
Region: TypeAlias = Tuple[int, int, List[int]]

def load_input(input_path: Path) -> Tuple[List[PresentShape], List[Region]]:
    lines = input_path.read_text().splitlines()

    grouped_lines = [[]]
    for line in lines:
        if line == "":
            grouped_lines.append([])
        else:
            grouped_lines[-1].append(line)

    present_shape_groups = grouped_lines[:-1]
    region_group = grouped_lines[-1]

    present_shapes = [parse_present_shape(group) for group in present_shape_groups]
    regions = [parse_region(line) for line in region_group]

    return present_shapes, regions

def parse_present_shape(group: List[str]) -> PresentShape:
    index = int(group[0][:-1])      # I'm just going to assume the indexes are already in order (which they are)
    return np.array([[bool(x == "#") for x in line] for line in group[1:]])

def parse_region(line: List[str]) -> Region:
    region_pattern = r"(\d+)x(\d+): (.+)"
    match = re.search(region_pattern, line)
    if match:
        W_str = match.group(1)
        L_str = match.group(2)
        quantity_str = match.group(3)
    
    W = int(W_str)
    L = int(L_str)
    quantity = [int(x) for x in quantity_str.strip().split(" ")]
    return W, L, quantity