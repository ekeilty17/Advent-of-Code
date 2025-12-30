from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> Tuple[List[Tuple[int, int]], List[int]]:
    lines = input_path.read_text().splitlines()
    try:
        blank_space_index = lines.index("")
    except:
        raise ValueError("Expected a blank space in the input file, but did not find one.")
    
    ingredient_id_ranges = lines[:blank_space_index]
    ingredient_ids = lines[blank_space_index+1:]

    ingredient_id_ranges = [parse_ingredient_id_ranges(ingredient_id_range) for ingredient_id_range in ingredient_id_ranges]
    ingredient_ids = [int(x) for x in ingredient_ids]

    return ingredient_id_ranges, ingredient_ids

def parse_ingredient_id_ranges(ingredient_id_range_str: str) -> List[Tuple[int, int]]:
    ingredient_id_range = ingredient_id_range_str.split("-")
    ingredient_id_range = [int(x) for x in ingredient_id_range]
    return tuple(ingredient_id_range)