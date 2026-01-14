from pathlib import Path
from typing import List, Dict, Tuple
import re

def load_input(input_path: Path) -> Tuple[Dict[str, List[int]], Dict[str, Tuple[str, int, str, int]]]:
    lines = input_path.read_text().splitlines()
    return parse_lines(lines)

def parse_lines(lines: List[str]) -> Tuple[Dict[str, List[int]], Dict[str, Tuple[str, int, str, int]]]:

    initializations = {}
    transfers = {}

    for line in lines:
        value_pattern = r"value (\d+) goes to bot (\d+)"
        m = re.fullmatch(value_pattern, line)
        if m:
            value, bot = [int(x) for x in m.groups()]
            if bot in initializations:
                initializations[bot].append(value)
            else:
                initializations[bot] = [value]
            continue
        
        bot_pattern = r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
        m = re.fullmatch(bot_pattern, line)
        if m:
            bot, low, low_index, high, high_index = m.groups()
            bot = int(bot)
            low_index, high_index = int(low_index), int(high_index)
            transfers[bot] = (low, low_index, high, high_index)
            continue
        
        raise ValueError(f"Unable to parse line: {line}")
    
    return initializations, transfers