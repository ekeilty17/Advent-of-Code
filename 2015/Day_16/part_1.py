from pathlib import Path
from typing import Optional, Dict, List

from Day_16.const import DAY, INPUT_FILE_NAME
from Day_16.load_input import load_input

def is_match(gift: Dict[str, int], ticker_tape: Dict[str, int]):
    known_gift_set = set(ticker_tape.items())
    gift_set = set(gift.items())
    return len(gift_set - known_gift_set) == 0

def solution(gifts: List[Dict[str, int]], ticker_tape: Dict[str, int]) -> Optional[int]:
    for i, gift in enumerate(gifts, 1):
        if is_match(gift, ticker_tape):
            return i

if __name__ == "__main__":
    
    gifts = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    ticker_tape = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    total = solution(gifts, ticker_tape)
    print("Puzzle Answer:", total)