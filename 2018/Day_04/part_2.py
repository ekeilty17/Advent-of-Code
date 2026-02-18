from pathlib import Path
from typing import List

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from Day_04.part_1 import parse_guard_shifts_and_sleep_intervals, compute_total_sleep_time_by_minute_by_guard
from utils.solve import test, solve

def solution(chronology: List[str]) -> int:
    sleep_intervals_by_shifts_by_gaurds = parse_guard_shifts_and_sleep_intervals(chronology)
    total_sleep_time_by_minute_by_guard = compute_total_sleep_time_by_minute_by_guard(sleep_intervals_by_shifts_by_gaurds)

    sleepiest_guard, _ = max(total_sleep_time_by_minute_by_guard.items(), key=lambda t: max(t[1]))
    max_minute, _ = max(enumerate(total_sleep_time_by_minute_by_guard[sleepiest_guard]), key=lambda t: t[1])
    return sleepiest_guard * max_minute

if __name__ == "__main__":
    example_chronology = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 4455
    test(expected_answer, solution, example_chronology)

    chronology = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, chronology)