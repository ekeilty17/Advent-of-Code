from pathlib import Path
from typing import Dict, Tuple

def load_input(input_path: Path) -> Dict[int, int]:
    lines = input_path.read_text().splitlines()
    return dict([parse_firewall(firewall) for firewall in lines])

def parse_firewall(firewall_str: str) -> Tuple[int, int]:
    depth, scan_range = firewall_str.split(": ")
    return int(depth), int(scan_range)