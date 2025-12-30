from pathlib import Path
from typing import List, Tuple

from Day_02.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_02.load_input import load_input
from utils.test import test


def is_invalid_product_id(product_id: int) -> bool:
    prod_str = str(product_id)
    if len(prod_str) % 2 == 1:
        return False
    half = len(prod_str) // 2
    return prod_str[:half] == prod_str[half:]

def get_invalid_product_ids(first_id: int, last_id: int) -> List[int]:
    invalid_product_ids: List[int] = []
    for product_id in range(first_id, last_id+1):
        if is_invalid_product_id(product_id):
            invalid_product_ids.append(product_id)
    
    return invalid_product_ids

def solution(product_id_ranges: List[Tuple[int, int]]) -> int:
    invalid_product_ids: List[int] = []
    for product_id_range in product_id_ranges:
        invalid_product_ids.extend(get_invalid_product_ids(*product_id_range))

    return sum(invalid_product_ids)

if __name__ == "__main__":
    example_product_id_ranges = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    product_id_ranges = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    example_answer = 1227775554
    test(example_answer, solution, example_product_id_ranges)

    total = solution(product_id_ranges)
    print("Puzzle Answer:", total)