from pathlib import Path

from Day_14.const import DAY, INPUT_FILE_NAME
from Day_14.load_input import load_input
from Day_14.part_1 import compute_final_position
from Day_14.part_2 import display_robot_positions

if __name__ == "__main__":
    positions, velocities = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    floor_shape = (101, 103)
    time_with_tree_image = 6668
    
    final_positions = [
        compute_final_position(floor_shape, position, velocity, time_with_tree_image)
        for position, velocity in zip(positions, velocities)
    ]

    display_robot_positions(floor_shape, final_positions)