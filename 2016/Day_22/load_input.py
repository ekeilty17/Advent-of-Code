from pathlib import Path
from typing import List, Tuple, Dict, Any

def load_input(input_path: Path) -> Tuple[List[str], List[Dict[str, Any]]]:
    lines = input_path.read_text().splitlines()
    columns = [x.strip() for x in lines[1].split(" ")]
    data = [[x.strip() for x in row.split(" ") if x] for row in lines[2:]]
    return columns, format_data(data)

def format_data(data: List[List[str]]) -> List[Dict[str, Any]]:
    formatted_data = []
    for row in data:
        formatted_data.append({
            "Filesystem": row[0],
            "Size": int(row[1][:-1]),
            "Used": int(row[2][:-1]),
            "Avail": int(row[3][:-1]),
            "Use%": int(row[4][:-1])/100,
        })
    return formatted_data