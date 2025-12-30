from pathlib import Path
from typing import List, Dict

def load_input(input_path: Path) -> Dict[str, List[str]]:
    lines = input_path.read_text().splitlines()
    return dict([parse_device_and_output(line) for line in lines])

def parse_device_and_output(device_and_output_str):
    device, output_str = device_and_output_str.split(": ")
    output = output_str.split(" ")
    return device, output