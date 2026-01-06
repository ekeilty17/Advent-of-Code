from typing import List
from utils.test import test

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
BLACKLIST = "iol"

def is_valid_password(numeric_password: List[int]) -> bool:
    condition_1 = False
    for i in range(len(numeric_password)-2):
        a, b, c = numeric_password[i:i+3]
        if a+2 == b+1 == c:
            condition_1 = True
            break
    
    condition_2 = not any(ALPHABET[n] in BLACKLIST for n in numeric_password)

    condition_3 = False
    repeating_pairs = set([])
    for i in range(len(numeric_password)-1):
        a, b = numeric_password[i:i+2]
        if a == b:
            repeating_pairs.add(a)
        if len(repeating_pairs) >= 2:
            condition_3 = True
            break
    
    return condition_1 and condition_2 and condition_3


def increment(numeric_password: List[int]) -> List[int]:

    numeric_blacklist = [ALPHABET.index(char) for char in BLACKLIST]

    i = len(numeric_password)-1
    while i > 0:
        numeric_password[i] += 1
        if numeric_password[i] in numeric_blacklist:
            numeric_password[i] += 1
        
        if numeric_password[i] < len(ALPHABET):
            break
        
        numeric_password[i] = 0
        i -= 1

    return numeric_password


def solution(password: str) -> str:
    
    inverse_index = {char: i for i, char in enumerate(ALPHABET)}
    numeric_password = [inverse_index[char] for char in password]
    
    while not is_valid_password(increment(numeric_password)):
        continue
        
    return "".join([ALPHABET[n] for n in numeric_password])

if __name__ == "__main__":
    
    example_password = "ghijklmn"
    password = "hepxcrrq"

    expected_answer = "ghjaabcc"
    test(expected_answer, solution, example_password)

    total = solution(password)
    print("Puzzle Answer:", total)