from pathlib import Path
import re

from Day_12.const import DAY, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.solve import solve

def solution(json_string: str) -> int:
    pattern = r'[+-]?\d+'
    matches = re.findall(pattern, json_string)
    return sum([int(x) for x in matches])

if __name__ == "__main__":
    json_string = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, json_string)