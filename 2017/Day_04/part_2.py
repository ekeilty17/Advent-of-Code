from pathlib import Path
from typing import List

from Day_04.const import DAY, INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.solve import solve

def is_valid_passphrase(passphrase: List[str]) -> bool:
    unique_anagrams = set([])
    for word in passphrase:
        anagram = tuple(sorted(word))
        if anagram in unique_anagrams:
            return False
        unique_anagrams.add(anagram)
    return True

def solution(passphrases: List[List[str]]) -> int:
    return sum([is_valid_passphrase(passphrase) for passphrase in passphrases])

if __name__ == "__main__":
    passphrases = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, passphrases)