from pathlib import Path
from typing import List, Tuple
import re

def load_input(input_path: Path) -> List[str]:
    lines = input_path.read_text().splitlines()
    return [parse_happiness(happiness) for happiness in lines]

def parse_happiness(happiness_str: str) -> Tuple[str, str, int]:
    pattern = r"([a-zA-Z]+) would (gain|lose) (\d+) happiness units by sitting next to ([a-zA-Z]+)\."
    m = re.fullmatch(pattern, happiness_str)

    if not m:
        raise ValueError(f"Unable to parse: '{happiness_str}'")
    
    name1 = m.group(1)
    action = m.group(2)
    amount = m.group(3)
    name2 = m.group(4)

    happiness = int(amount) if action == "gain" else -int(amount)
    return name1, name2, happiness