from pathlib import Path
from typing import Dict, Tuple
import re

def load_input(input_path: Path) -> Dict[str, Dict[str, int]]:
    lines = input_path.read_text().splitlines()
    return dict([parse_reindeer_stats(reindeer_stats) for reindeer_stats in lines])

def parse_reindeer_stats(reindeer_stats_str: str) -> Tuple[str, Dict[str, int]]:
    pattern = r"([a-zA-Z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\."
    m = re.fullmatch(pattern, reindeer_stats_str)

    if not m:
        raise ValueError(f"Unable to parse: '{reindeer_stats_str}'")
    
    reindeer = m.group(1)
    flight_speed = m.group(2)
    flight_time = m.group(3)
    rest_time = m.group(4)

    return reindeer, {"flight_speed": int(flight_speed), "flight_time": int(flight_time), "rest_time": int(rest_time)}