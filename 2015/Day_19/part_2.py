from pathlib import Path
from typing import List, Dict, Set

from Day_19.const import DAY, INPUT_FILE_NAME
from Day_19.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_19.load_input import load_input
from Day_19.part_1 import parse_elements, get_all_fabricatable_molecules
from utils.solve import test, solve

def get_all_substring_replacements(string: str, substring: str, replacement: str) -> Set[str]:
    replacement_strings = set([])
    n = len(substring)
    for i in range(len(string) - n+1):
        if string[i: i+n] == substring:
            replacement_strings.add( string[:i] + replacement + string[i+n:] )
    return replacement_strings

def solution(replacements_by_element: Dict[str, List[str]], medicine_molecule: List[str]) -> int:
    pass
    """
    terminal_elements = replacements_by_element["e"]
    elements_by_replacement = {
        new_element: element 
        for element, replacements in replacements_by_element.items() for new_element in replacements
        if element != "e"
    }
    print(terminal_elements)
    print(elements_by_replacement)
    print()
    layer = [medicine_molecule]
    step = 0
    while not any(molecule in terminal_elements for molecule in layer):
        new_layer = set([])
        for molecule in layer:
            for new_element, element in elements_by_replacement.items():
                new_layer.update(get_all_substring_replacements(molecule, new_element, element))
        layer = list(new_layer)
        print(len(layer), layer[0])
        step += 1
    
    return step + 1
    """

    """
    layer = ["e"]
    all_previous_molecules = set([])

    steps = 0
    while medicine_molecule not in layer:
        new_layer = set([])
        for molecule in layer:
            new_layer.update(get_all_fabricatable_molecules(replacements_by_element, molecule))
        layer = [molecule for molecule in new_layer if len(molecule) <= len(medicine_molecule) and molecule not in all_previous_molecules]
        all_previous_molecules.update(layer)
        print(len(layer), len(layer[0]), layer[0])
        steps += 1
    
    return steps
    """

if __name__ == "__main__":
    example_replacements_by_element, example_medicine_molecule = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 6
    test(expected_answer, solution, example_replacements_by_element, example_medicine_molecule)

    replacements_by_element, medicine_molecule = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, replacements_by_element, medicine_molecule)