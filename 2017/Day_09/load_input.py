from pathlib import Path

def load_input(input_path: Path) -> str:
    contents = input_path.read_text()
    return contents