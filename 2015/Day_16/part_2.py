from pathlib import Path
from typing import List, Dict, Optional

from Day_16.const import DAY, INPUT_FILE_NAME
from Day_16.load_input import load_input
from Day_16.ticker_tape import TICKER_TAPE
from utils.solve import solve

def is_match(gift: Dict[str, int], ticker_tape: Dict[str, int]):
    for name in gift:
        if name in ["cats", "trees"]:
            if gift[name] <= ticker_tape[name]:
                return False
        elif name in ["pomeranians", "goldfish"]:
            if gift[name] >= ticker_tape[name]:
                return False
        else:
            if gift[name] != ticker_tape[name]:
                return False
    
    return True

def solution(gifts: List[Dict[str, int]], ticker_tape: Dict[str, int]) -> Optional[int]:
    for i, gift in enumerate(gifts, 1):
        if is_match(gift, ticker_tape):
            return i

if __name__ == "__main__":
    gifts = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, gifts, TICKER_TAPE)