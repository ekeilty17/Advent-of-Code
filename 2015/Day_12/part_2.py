from pathlib import Path
from typing import Any
import json

from Day_12.const import DAY, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.part_1 import solution as part_1_solution
from utils.solve import solve

def filter_red(obj: Any) -> Any:
    if isinstance(obj, dict):
        if "red" in obj.values():
            return {}
        return {key: filter_red(value) for key, value in obj.items()}
    
    if isinstance(obj, list):
        return [filter_red(e) for e in obj]
    
    return obj

def solution(json_string: str) -> int:
    json_obj = json.loads(json_string)
    filterd_json_obj = filter_red(json_obj)
    filterd_json_string = json.dumps(filterd_json_obj)
    return part_1_solution(filterd_json_string)

if __name__ == "__main__":
    json_string = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, json_string)