from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[List[int]]:
    lines = input_path.read_text().splitlines()
    return [parse_report(report) for report in lines]

def parse_report(report_str: str) -> List[int]:
    return [int(x) for x in report_str.split(" ")]