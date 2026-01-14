import hashlib
from Day_14.part_1 import get_valid_keys
from utils.solve import test, solve

def hash_func(string: str, salt: str="") -> str:
    h = f"{salt}{string}"
    for _ in range(2017):
        h = hashlib.md5(h.encode()).hexdigest()
    return h

def solution(salt: str, num_hashes: int, num_keys:int) -> int:
    key_indices = get_valid_keys(salt, num_hashes, num_keys, hash_func)
    return key_indices[-1]

if __name__ == "__main__":
    num_hashes = 1000
    num_keys = 64

    example_salt = "abc"
    expected_answer = 22551
    test(expected_answer, solution, example_salt, num_hashes, num_keys)
    
    salt = "jlmsuwbz"
    solve(solution, salt, num_hashes, num_keys)