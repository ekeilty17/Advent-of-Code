from pathlib import Path
from typing import List, Tuple

from Day_02.const import DAY, INPUT_FILE_NAME
from Day_02.load_input import load_input

def surface_area(l: int, w: int, h:int) -> int:
    return 2*l*w + 2*w*h + 2*h*l

def solution(gift_dimensions: List[Tuple[int, int, int]]) -> int:
    total_wrapping_paper = 0
    for l, w, h in gift_dimensions:
        l, w, h = list(sorted([l, w, h]))
        total_wrapping_paper += surface_area(l, w, h) + l * w
    return total_wrapping_paper

if __name__ == "__main__":
    
    gift_dimensions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    total = solution(gift_dimensions)
    print("Puzzle Answer:", total)