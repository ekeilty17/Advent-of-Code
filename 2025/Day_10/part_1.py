from pathlib import Path
from typing import List, Tuple, TypeAlias

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.solve import test, solve

IndicatorLights: TypeAlias = List[bool]
ButtonWiringSchematic: TypeAlias = List[int]
JoltageRequirements: TypeAlias = List[int]

def display_indicator_lights(indicator_lights):
    print([int(x) for x in indicator_lights])

def apply_button_wiring_schema(indicator_lights: IndicatorLights, button_wiring_schema: ButtonWiringSchematic) -> IndicatorLights:
    indicator_lights = list(indicator_lights)       # make a copy
    for index in button_wiring_schema:
        indicator_lights[index] = (not indicator_lights[index])
    return indicator_lights

def indicator_lights_match(indicator_lights_1: IndicatorLights, indicator_lights_2: IndicatorLights) -> bool:
    return all(x == y for x, y in zip(indicator_lights_1, indicator_lights_2))

def get_fewest_button_presses(start_indicator_lights: IndicatorLights,  final_indicator_lights: IndicatorLights, button_wiring_schemas: List[ButtonWiringSchematic], max_recusion=100) -> int:
    
    if indicator_lights_match(start_indicator_lights, final_indicator_lights):
        return 0

    # BFS down a tree
    # I'm essentially doing a level traversal
    leafs = set([tuple(start_indicator_lights)])
    for depth in range(1, max_recusion):
        
        if len(leafs) == 0:
            break

        new_leafs = set([])
        for indicator_lights in leafs:
            for schema in button_wiring_schemas:
                updated_indicator_lights = apply_button_wiring_schema(indicator_lights, schema)
                if indicator_lights_match(updated_indicator_lights, final_indicator_lights):
                    return depth
                
                new_leafs.add(tuple(updated_indicator_lights))
        leafs = new_leafs

    return None

def solution(machines: List[Tuple[IndicatorLights, List[ButtonWiringSchematic], JoltageRequirements]]) -> int:
    
    min_button_presses = []
    for indicator_lights, button_wiring_schema, _ in machines:
        start_indicator_lights = [False] * len(indicator_lights)
        min_button_presses.append(
            get_fewest_button_presses(start_indicator_lights, indicator_lights, button_wiring_schema)
        )
    
    return sum(min_button_presses)

if __name__ == "__main__":
    example_machines = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 7
    test(expected_answer, solution, example_machines)

    machines = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))
    solve(solution, machines)