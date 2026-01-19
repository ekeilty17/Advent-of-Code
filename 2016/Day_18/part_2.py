from pathlib import Path

from Day_18.const import DAY, INPUT_FILE_NAME
from Day_18.load_input import load_input
from utils.solve import solve

def update(center: int, bit_length: int) -> int:
    ones  = (1 << bit_length) - 1
    
    left  = ((center >> 1) & ones) | (1 << (bit_length-1))
    not_left = ~left & ones
    
    right = ((center << 1) & ones) | 1
    not_right = ~right & ones
    
    return (not_left | right) & (left | not_right)

def solution(tiles: str, num_rows: int) -> int:
    center = int("".join(["1" if t == "." else "0" for t in tiles]), 2)
    num_tiles = len(tiles)

    num_safe_tiles = center.bit_count()

    for _ in range(num_rows-1):
        center = update(center, num_tiles)
        num_safe_tiles += center.bit_count()

    return num_safe_tiles

if __name__ == "__main__":
    tiles = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    num_rows = 400000
    solve(solution, tiles, num_rows)