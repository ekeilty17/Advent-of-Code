from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> List[int | None]:
    lines = input_path.read_text().splitlines()
    disk_map = parse_disk_map(lines[0])
    return disk_map

def parse_disk_map(disk_map_str: str) -> Tuple[List[int | None], List[Tuple[int, int]], List[Tuple[int, int]]]:
    ID = 0
    disk_map = []
    file_blocks = []
    free_space = []
    for i, n in enumerate(disk_map_str):
        if n == "0":
            continue

        disk_map_index = len(disk_map)
        if i % 2:
            disk_map.extend([None] * int(n))
            free_space.append((disk_map_index, len(disk_map)))
        else:
            disk_map.extend([ID] * int(n))
            file_blocks.append((disk_map_index, len(disk_map)))
            ID += 1
    
    return disk_map, file_blocks, free_space