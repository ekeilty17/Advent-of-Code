from pathlib import Path
from typing import List, Dict, Tuple, TypeAlias
from datetime import datetime, timedelta
import re

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.solve import test, solve

Shifts: TypeAlias = Dict[datetime, List[Tuple[datetime, datetime]]]

def parse_guard_sleep_periods(chronology: List[str]) -> Dict[int, Shifts]:
    guard_pattern = r"\[(.+)\] Guard #(\d+) begins shift"
    sleep_pattern = r"\[(.+)\] falls asleep"
    wake_pattern = r"\[(.+)\] wakes up"
    
    dt_pattern = "%Y-%m-%d %H:%M"

    guard = None
    start_shift_dt = None
    sleep_dt = None
    wake_dt = None

    shifts_by_gaurds = {}
    for event in sorted(chronology):
        m = re.fullmatch(guard_pattern, event)
        if m:
            start_shift_dt = datetime.strptime(m.group(1), dt_pattern)
            guard = int(m.group(2))
            
            if guard not in shifts_by_gaurds:
                shifts_by_gaurds[guard] = {}
            shifts_by_gaurds[guard][start_shift_dt] = []
            continue

        m = re.fullmatch(sleep_pattern, event)
        if m:
            sleep_dt = datetime.strptime(m.group(1), dt_pattern)
            continue

        m = re.fullmatch(wake_pattern, event)
        if m:
            wake_dt = datetime.strptime(m.group(1), dt_pattern)
            if wake_dt < sleep_dt:
                raise Exception(f"Failed to parse event: {event}")
            shifts_by_gaurds[guard][start_shift_dt].append((sleep_dt, wake_dt))
            continue
        
        raise Exception(f"Failed to parse event: {event}")

    return shifts_by_gaurds

def compute_total_sleep_time_by_minute_by_guard(shifts_by_gaurds: Dict[int, Shifts]) -> Dict[int, List[int]]:
    total_sleep_time_by_minute_by_guard = {}

    for guard, shifts in shifts_by_gaurds.items():
        minute_number_sleep_frequency = [0] * 60
        for sleep_intervals in shifts.values():
            for dt1, dt2 in sleep_intervals:
                dt = dt1
                while dt < dt2:
                    minute_number_sleep_frequency[dt.minute] += 1
                    dt += timedelta(minutes=1)
        
        total_sleep_time_by_minute_by_guard[guard] = minute_number_sleep_frequency
    
    return total_sleep_time_by_minute_by_guard

def solution(chronology: List[str]) -> int:
    shifts_by_gaurds = parse_guard_sleep_periods(chronology)    
    total_sleep_time_by_minute_by_guard = compute_total_sleep_time_by_minute_by_guard(shifts_by_gaurds)

    sleepiest_guard, _ = max(total_sleep_time_by_minute_by_guard.items(), key=lambda t: sum(t[1]))
    max_minute, _ = max(enumerate(total_sleep_time_by_minute_by_guard[sleepiest_guard]), key=lambda t: t[1])
    return sleepiest_guard * max_minute

if __name__ == "__main__":
    example_chronology = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 240
    test(expected_answer, solution, example_chronology)

    chronology = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, chronology)