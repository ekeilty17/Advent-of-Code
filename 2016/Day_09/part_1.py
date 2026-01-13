from pathlib import Path
from typing import List

from Day_09.const import DAY, INPUT_FILE_NAME
from Day_09.load_input import load_input
from utils.solve import test, solve

def get_end_of_marker(compressed_text: str, i: int) -> int:
    j = i
    while compressed_text[j] != ")":
        j += 1
    return j

def get_decompression_length(compressed_text: str) -> int:
    if compressed_text == "":
        return 0
    
    if compressed_text[0] == "(":
        j = get_end_of_marker(compressed_text, 0)
        marker_string = compressed_text[1: j]
        encapsulation, repeat = [int(n) for n in marker_string.split("x")]
        
        k = j+1+encapsulation
        return encapsulation * repeat + get_decompression_length(compressed_text[k:])

    return 1 + get_decompression_length(compressed_text[1:])

def solution(compressed_text: str) -> int:
    return get_decompression_length(compressed_text)
        

if __name__ == "__main__":
    example_compressed_text = "X(8x2)(3x3)ABCY"
    expected_answer = 18
    test(expected_answer, solution, example_compressed_text)

    compressed_text = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, compressed_text)