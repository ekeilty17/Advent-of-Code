from pathlib import Path
from typing import Dict

from Day_14.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_14.load_input import load_input
from Day_14.part_1 import compute_reindeer_distance
from utils.solve import test, solve

def solution(reindeer_stats: Dict[str, Dict[str, int]], race_duration: int) -> int:
    for reindeer, stats in reindeer_stats.items():
        stats["name"] = reindeer
        stats["points"] = 0
    
    for T in range(1, race_duration+1):
        for reindeer, stats in reindeer_stats.items():
            distance = compute_reindeer_distance(T, **stats)
            stats["distance"] = distance
        
        max_distance = max(reindeer_stats.values(), key=lambda val: val["distance"])["distance"]
        for reindeer, stats in reindeer_stats.items():
            if stats["distance"] == max_distance:
                stats["points"] += 1
    
    return max(reindeer_stats.values(), key=lambda val: val["points"])["points"]

if __name__ == "__main__":
    example_reindeer_stats = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_race_duration = 1000
    expected_answer = 689
    test(expected_answer, solution, example_reindeer_stats, example_race_duration)

    reindeer_stats = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    race_duration = 2503
    solve(solution, reindeer_stats, race_duration)