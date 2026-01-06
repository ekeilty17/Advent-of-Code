from pathlib import Path
from typing import List, Dict

def load_input(input_path: Path) -> List[Dict[str, int]]:
    lines = input_path.read_text().splitlines()
    return [parse_Sue(Sue) for Sue in lines]

def parse_Sue(Sue_str: str) -> Dict[str, int]:
    Sue_num_str, *gift_str = Sue_str.split(": ")
    gift_str = ": ".join(gift_str)
    gift = [gift.split(": ") for gift in gift_str.split(", ")]
    gift = [(name, int(quantity)) for name, quantity in gift]
    return dict(gift)