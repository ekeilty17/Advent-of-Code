from pathlib import Path
from typing import Dict

from Day_14.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_14.load_input import load_input
from utils.solve import test, solve

def compute_reindeer_distance(race_duration: int, flight_speed: int, flight_time: int, rest_time: int, **kwargs) -> int:
    cycle_time = flight_time + rest_time
    num_cycles = race_duration // cycle_time
    remainder_time = race_duration % cycle_time
    last_leg_flight_time = min(remainder_time, flight_time)
    return flight_speed * flight_time * num_cycles + flight_speed * last_leg_flight_time

def solution(reindeer_stats: Dict[str, Dict[str, int]], race_duration: int) -> int:
    for reindeer, stats in reindeer_stats.items():
        distance = compute_reindeer_distance(race_duration, **stats)
        stats["distance"] = distance
    
    return max(reindeer_stats.values(), key=lambda val: val["distance"])["distance"]

if __name__ == "__main__":
    example_reindeer_stats = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_race_duration = 1000
    expected_answer = 1120
    test(expected_answer, solution, example_reindeer_stats, example_race_duration)

    reindeer_stats = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    race_duration = 2503
    solve(solution, reindeer_stats, race_duration)