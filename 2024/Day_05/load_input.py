from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    lines = input_path.read_text().splitlines()
    try:
        blank_space_index = lines.index("")
    except:
        raise ValueError("Expected a blank space in the input file, but did not find one.")
    
    page_ordering_rules = lines[:blank_space_index]
    page_numbers_to_update = lines[blank_space_index+1:]
    
    page_ordering_rules = [parse_rule(rule) for rule in page_ordering_rules]
    page_sequences = [parse_page_sequence(update) for update in page_numbers_to_update]

    return page_ordering_rules, page_sequences

def parse_rule(rule_str: str) -> Tuple[int, int]:
    return tuple([int(x) for x in rule_str.split("|")])

def parse_page_sequence(page_sequence_str: str) -> List[int]:
    return [int(x) for x in page_sequence_str.split(",")]