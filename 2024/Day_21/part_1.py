from pathlib import Path
from typing import List
import numpy as np
from numpy.typing import NDArray

from Day_21.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_21.load_input import load_input
from utils.test import test

def compute_complixity(code: str, shortest_sequence: str) -> int:
    # print(len(shortest_sequence), int(code.replace("A", "")))
    return len(shortest_sequence) * int(code.replace("A", ""))

def compute_directional_keypad_sequences(code: str, keypad: NDArray[str]) -> List[str]:
    keypad_indexes = {button: idx for idx, button in np.ndenumerate(keypad)}
    curr_position = keypad_indexes["A"]
    
    sequences = set([""])
    for button in code:
        target_position = keypad_indexes[button]
        
        vertical_displacement = target_position[0] - curr_position[0]
        horizontal_displacement = target_position[1] - curr_position[1]

        vertical_direction = "v" if vertical_displacement > 0 else "^"
        horizontal_direction = ">" if horizontal_displacement > 0 else "<"

        vertical_str = vertical_direction * abs(vertical_displacement)
        horizontal_str = horizontal_direction * abs(horizontal_displacement)

        new_sequences = set([])
        for sequence in sequences:
            if keypad[target_position[0], curr_position[1]] is not None:
                new_sequences.add(sequence + vertical_str + horizontal_str + "A")
            if keypad[curr_position[0], target_position[1]] is not None:
                new_sequences.add(sequence + horizontal_str + vertical_str + "A")
        
        sequences = new_sequences
        curr_position = target_position
    
    return sequences

def solution(codes: List[str]) -> int:

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

        sequences_layer_0 = compute_directional_keypad_sequences(numeric_code, numeric_keypad)

        sequences_layer_1 = set([])
        for directional_code in sequences_layer_0:
            sequences_layer_1.update( compute_directional_keypad_sequences(directional_code, directional_keypad) )

        sequences_layer_2 = set([])
        for directional_code in sequences_layer_1:
            sequences_layer_2.update( compute_directional_keypad_sequences(directional_code, directional_keypad) )
        
        shortest_layer_2_sequence = min(sequences_layer_2, key=len)
        shortest_sequences.append(shortest_layer_2_sequence)

    return sum([compute_complixity(code, sequence) for code, sequence in zip(codes, shortest_sequences)])

if __name__ == "__main__":
    
    example_codes = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    codes = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 126384
    test(expected_answer, solution, example_codes)

    total = solution(codes)
    print("Puzzle Answer:", total)