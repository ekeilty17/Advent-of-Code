from pathlib import Path

def load_input(input_path: Path) -> str:
    lines = input_path.read_text().splitlines()
    return lines[0]