from typing import List, Dict, Any, Callable
import hashlib
from utils.solve import test, solve

def preprocess_hash(h: str):
    first_triplet_char = None
    for i in range(len(h)-2):
        a, b, c = h[i:i+3]
        if a == b == c:
            first_triplet_char = a
            break
    
    all_quintuplet_chars = set([])
    for i in range(len(h)-4):
        a, b, c, d, e = h[i:i+5]
        if a == b == c == d == e:
            all_quintuplet_chars.add(a)
    
    return {
        "hash": h,
        "triplet": first_triplet_char,
        "quintuplets": all_quintuplet_chars
    }

def is_key(h: Dict[str, Any], next_n_hashes: List[Dict[str, Any]]) -> bool:
    return any(h["triplet"] in next_h["quintuplets"] for next_h in next_n_hashes)

def hash_func(string: str, salt: str="") -> str:
    return hashlib.md5(f"{salt}{string}".encode()).hexdigest()

def get_valid_keys(salt: str, num_hashes: int, num_keys:int, hash_func: Callable[[str, str], str]) -> List[int]:
    hash_sequence = []
    for i in range(num_hashes+1):
        h = hash_func(i, salt)
        hash_sequence.append(preprocess_hash(h))
    
    key_indices = []
    index = 0
    while len(key_indices) < num_keys:
        h = hash_sequence[index]
        next_n_hashes = hash_sequence[index+1:index+1+num_hashes]
        if is_key(h, next_n_hashes):
            key_indices.append(index)

        index += 1

        # adding next hash to the end of the preprocessed sequence
        h = hash_func(len(hash_sequence), salt)
        hash_sequence.append(preprocess_hash(h))

    return key_indices

def solution(salt: str, num_hashes: int, num_keys:int) -> int:
    key_indices = get_valid_keys(salt, num_hashes, num_keys, hash_func)
    return key_indices[-1]

if __name__ == "__main__":
    num_hashes = 1000
    num_keys = 64

    example_salt = "abc"
    expected_answer = 22728
    test(expected_answer, solution, example_salt, num_hashes, num_keys)
    
    salt = "jlmsuwbz"
    solve(solution, salt, num_hashes, num_keys)