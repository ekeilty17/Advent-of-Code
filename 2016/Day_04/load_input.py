from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[str, int, str]]:
    lines = input_path.read_text().splitlines()
    return [parse_line(line) for line in lines]

def parse_line(line_str: str) -> Tuple[str, int, str]:
    encrypted_name_and_sector_id_str, checksum = line_str.split("[")
    checksum = checksum[:-1]

    *encrypted_name, sector_id_str = encrypted_name_and_sector_id_str.split("-")
    return "-".join(encrypted_name), int(sector_id_str), checksum