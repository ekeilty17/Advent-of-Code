from pathlib import Path
from typing import Dict, Tuple

def load_input(input_path: Path) -> Tuple[str, Dict[str, str]]:
    lines = input_path.read_text().splitlines()
    return parse_initial_state(lines[0]), dict([parse_transition(transition) for transition in lines[2:]])

def parse_initial_state(initial_state_str: str) -> str:
    initial_state_str = initial_state_str[len("initial state: "):]
    return initial_state_str

def parse_transition(transition_str: str) -> Tuple[str, str]:
    key, value = transition_str.split(" => ")
    return key, value