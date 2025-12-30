from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[Tuple[int, int]]:
    product_id_ranges = input_path.read_text().strip().split(',')
    product_id_ranges = [parse_product_id_range(product_id_range_str) for product_id_range_str in product_id_ranges]
    return product_id_ranges

def parse_product_id_range(product_id_range_str):
    product_range = product_id_range_str.split("-")
    product_range = [int(x) for x in product_range]
    return tuple(product_range)