from pathlib import Path
from typing import List

def load_input(input_path: Path) -> List[int]:
    banks = input_path.read_text().splitlines()
    banks = [parse_bank(bank_str) for bank_str in banks]
    return banks

def parse_bank(bank_str: str) -> List[int]:
    return [int(battery_str) for battery_str in bank_str]