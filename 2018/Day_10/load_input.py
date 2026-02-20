from pathlib import Path
from typing import List, Tuple
import re

def load_input(input_path: Path) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    lines = input_path.read_text().splitlines()
    points = [parse_point(point) for point in lines]
    positions = [position for position, _ in points]
    velocities = [velocity for _, velocity in points]
    return positions, velocities

def parse_point(point_str: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    pattern = r"position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>"
    m = re.fullmatch(pattern, point_str)
    if not m:
        raise Exception(f"Failed to parse point: {point_str}")
    
    position = (int(m.group(1)), int(m.group(2)))
    velocity = (int(m.group(3)), int(m.group(4)))
    return position, velocity