from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    lines = input_path.read_text().splitlines()

    positions = []
    velocities = []
    for line in lines:
        position, velocity = parse_position_and_velocity(line)
        positions.append(position)
        velocities.append(velocity)
    
    return positions, velocities


def parse_position_and_velocity(line_str: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    position_str, velocity_str = line_str.split(" ")
    return parse_coordinate(position_str[2:]), parse_coordinate(velocity_str[2:])

def parse_coordinate(coord_str: str) -> Tuple[int, int]:
    x_str, y_str = coord_str.split(",")
    return int(x_str), int(y_str)