from pathlib import Path
from typing import List, Dict, Any

from Day_22.const import DAY, INPUT_FILE_NAME
from Day_22.load_input import load_input
from utils.solve import solve

def is_viable_pair(usage_A: Dict[str, Any], usage_B: Dict[str, Any]) -> bool:
    return usage_A["Used"] != 0 and usage_A["Used"] <= usage_B["Avail"]

def solution(disk_usage: List[Dict[str, Any]]) -> int:

    viable_pairs = 0
    for usage_A in disk_usage:
        for usage_B in disk_usage:
            if usage_A["Filesystem"] == usage_B["Filesystem"]:
                continue

            if is_viable_pair(usage_A, usage_B):
                viable_pairs += 1

    return viable_pairs

if __name__ == "__main__":
    _, disk_usage = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, disk_usage)