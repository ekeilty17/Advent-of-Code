from pathlib import Path
from typing import List, Tuple, TypeAlias

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.test import test

IndicatorLights: TypeAlias = List[bool]
ButtonWiringSchematic: TypeAlias = List[int]
JoltageRequirements: TypeAlias = List[int]

def display_indicator_lights(indicator_lights):
    print([int(x) for x in indicator_lights])

def apply_button_wiring_schema(joltage: JoltageRequirements, button_wiring_schema: ButtonWiringSchematic) -> IndicatorLights:
    joltage = list(joltage)       # make a copy
    for index in button_wiring_schema:
        joltage[index] += 1
    return joltage

def joltages_match(joltage_1: JoltageRequirements, joltage_2: JoltageRequirements) -> bool:
    return all(x == y for x, y in zip(joltage_1, joltage_2))

def impossible_state(joltage: JoltageRequirements, final_joltage: JoltageRequirements) -> bool:
    return any(x > y for x, y in zip(joltage, final_joltage))


# This works, but it's too slow
# Based on what other's said, even doing bidirectional BFS is still too slow
def get_fewest_button_presses(start_joltage: JoltageRequirements,  final_joltage: JoltageRequirements, button_wiring_schemas: List[ButtonWiringSchematic], max_recusion=100) -> int:
    
    if joltages_match(start_joltage, final_joltage):
        return 0

    # BFS down a tree
    # I'm essentially doing a level traversal + pruning
    all_states = set([tuple(start_joltage)])
    leafs = set([tuple(start_joltage)])
    for depth in range(1, max_recusion):

        if len(leafs) == 0:
            break

        new_leafs = set([])
        for joltage in leafs:
            for schema in button_wiring_schemas:
                updated_joltage = apply_button_wiring_schema(joltage, schema)
                if joltages_match(updated_joltage, final_joltage):
                    return depth
                if impossible_state(updated_joltage, final_joltage):
                    continue
                updated_joltage = tuple(updated_joltage)
                if updated_joltage in all_states:
                    continue
                all_states.add(updated_joltage)
                new_leafs.add(updated_joltage)
        leafs = new_leafs

    return None

def solution(machines: List[Tuple[IndicatorLights, List[ButtonWiringSchematic], JoltageRequirements]]) -> int:
    
    min_button_presses = []
    for _, button_wiring_schema, joltage_requirements in machines:
        start_joltage = [0] * len(joltage_requirements)
        min_button_presses.append(
            get_fewest_button_presses(start_joltage, joltage_requirements, button_wiring_schema)
        )
    
    return sum(min_button_presses)

if __name__ == "__main__":
    
    example_machines = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    machines = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))

    expected_answer = 33
    test(expected_answer, solution, example_machines)

    total = solution(machines)
    print("Puzzle Answer:", total)