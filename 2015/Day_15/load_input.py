from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> Dict[str, Dict[str, int]]:
    lines = input_path.read_text().splitlines()
    return dict([parse_ingredient(ingredient) for ingredient in lines])

def parse_ingredient(ingredient_str: str) -> Tuple[str, Dict[str, int]]:
    ingredient, properties_str = ingredient_str.split(": ")
    properties = [s.split(" ") for s in properties_str.split(", ")]
    properties = dict([(p[0], int(p[1])) for p in properties])
    return ingredient, properties