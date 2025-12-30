from pathlib import Path
from typing import List, Tuple

from Day_09.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_09.load_input import load_input
from Day_09.part_1 import checksum
from utils.test import test

def solution(disk_map: List[int | None], file_blocks: List[Tuple[int, int]], free_spaces: List[Tuple[int, int]]) -> int:

    for b, file_block in reversed(list(enumerate(file_blocks))):
        for i in range(len(free_spaces)):
            free_space = free_spaces[i]
            

            free_space_length = free_space[1] - free_space[0]
            file_block_length = file_block[1] - file_block[0]

            if free_space[0] >= file_block[0]:           # at or passed the file_block's current position
                break
            if free_space_length < file_block_length:    # not enough room for file_block
                continue
            
            if free_space_length == file_block_length:
                free_spaces = free_spaces[:i] + free_spaces[i+1:]
            else:
                free_spaces = free_spaces[:i] + [(free_space[0] + file_block_length, free_space[1])] + free_spaces[i+1:]
            
            disk_map[free_space[0]: free_space[0] + file_block_length] = [b] * file_block_length
            disk_map[file_block[0]: file_block[1]] = [None] * file_block_length
            break
    
    return checksum(disk_map)

if __name__ == "__main__":
    
    example_disk_map, example_file_blocks, example_free_spaces = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    disk_map, file_blocks, free_spaces = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    
    expected_answer = 2858
    test(expected_answer, solution, example_disk_map, example_file_blocks, example_free_spaces)

    total = solution(disk_map, file_blocks, free_spaces)
    print("Puzzle Answer:", total)