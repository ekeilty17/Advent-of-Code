from pathlib import Path

from Day_03.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_03.load_input import load_input
from Day_03.part_1 import update_position
from utils.test import test

def solution(moves: str) -> int:
    santa_pos = (0, 0)
    robot_pos = (0, 0)
    present_positions = {santa_pos, robot_pos}

    for i in range(0, len(moves), 2):
        santa_move, robot_move = moves[i:i+2]
        santa_pos = update_position(santa_pos, santa_move)
        present_positions.add(santa_pos)

        robot_pos = update_position(robot_pos, robot_move)
        present_positions.add(robot_pos)
    
    return len(present_positions)

if __name__ == "__main__":
    
    example_moves = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    moves = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 3
    test(expected_answer, solution, example_moves)

    total = solution(moves)
    print("Puzzle Answer:", total)