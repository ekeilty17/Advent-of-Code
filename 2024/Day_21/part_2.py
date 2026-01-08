from pathlib import Path
from typing import List
import numpy as np
from numpy.typing import NDArray

from Day_21.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_21.load_input import load_input
from Day_21.part_1 import compute_complixity#, compute_directional_keypad_sequences
from utils.solve import test, solve

def compute_directional_keypad_sequences(code: str, keypad: NDArray[str]) -> List[str]:
    keypad_indexes = {button: idx for idx, button in np.ndenumerate(keypad)}
    curr_position = keypad_indexes["A"]
    
    sequence = ""
    for button in code:
        target_position = keypad_indexes[button]
        
        vertical_displacement = target_position[0] - curr_position[0]
        horizontal_displacement = target_position[1] - curr_position[1]

        vertical_direction = "v" if vertical_displacement > 0 else "^"
        horizontal_direction = ">" if horizontal_displacement > 0 else "<"

        vertical_str = vertical_direction * abs(vertical_displacement)
        horizontal_str = horizontal_direction * abs(horizontal_displacement)

        if keypad[target_position[0], curr_position[1]] is None:
            sequence += horizontal_str + vertical_str + "A"
        elif keypad[curr_position[0], target_position[1]] is None:
            sequence += vertical_str + horizontal_str + "A"
        else:
            if abs(horizontal_displacement) < abs(vertical_displacement):
                sequence += horizontal_str + vertical_str + "A"
            else:
                sequence += vertical_str + horizontal_str + "A"
        
        curr_position = target_position
    
    return sequence

def solution(codes: List[str], num_robots: int) -> int:

    numeric_keypad = np.array([
        ["7",  "8", "9"],
        ["4",  "5", "6"],
        ["1",  "2", "3"],
        [None, "0", "A"]
    ])

    directional_keypad = np.array([
        [None, "^", "A"],
        ["<",  "v", ">"]
    ])
    
    shortest_sequences = []
    for numeric_code in codes:

        sequence_layer_0 = compute_directional_keypad_sequences(numeric_code, numeric_keypad)

        sequence_layer_n = sequence_layer_0
        for n in range(num_robots):
            print(n, len(sequence_layer_n), sequence_layer_n)
            sequence_layer_n = compute_directional_keypad_sequences(sequence_layer_n, directional_keypad)

        print(n, len(sequence_layer_n), sequence_layer_n)
        shortest_sequences.append(sequence_layer_n)

    return sum([compute_complixity(code, sequence) for code, sequence in zip(codes, shortest_sequences)])

if __name__ == "__main__":
    example_codes = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_num_robots = 3
    expected_answer = 126384
    test(expected_answer, solution, example_codes, example_num_robots)

    # codes = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    # num_robots = 25
    # solve(solution, codes, num_robots)