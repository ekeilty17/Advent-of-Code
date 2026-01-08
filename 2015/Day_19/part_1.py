from pathlib import Path
from typing import List, Dict, Set

from Day_19.const import DAY, INPUT_FILE_NAME
from Day_19.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_19.load_input import load_input
from utils.solve import test, solve

def parse_elements(molecule_str: str) -> List[str]:
    if len(molecule_str) == 0:
        return []
    
    elements = []
    element = molecule_str[0]
    for i in range(1, len(molecule_str)):
        if molecule_str[i] == molecule_str[i].upper():
            elements.append(element)
            element = ""
        element += molecule_str[i]
    
    elements.append(element)
    return elements

def get_all_fabricatable_molecules(replacements_by_element: Dict[str, List[str]], seed_molecule: str) -> Set[str]:
    seed_elements = parse_elements(seed_molecule)
    created_molecules = set([])

    for i in range(len(seed_elements)):
        new_molecule = list(seed_elements)

        for element, replacements in replacements_by_element.items():
            if seed_elements[i] == element:
                for new_element in replacements:
                    new_molecule[i] = new_element
                    created_molecules.add("".join(new_molecule))
        
    return created_molecules

def solution(replacements_by_element: Dict[str, List[str]], seed_molecule: str) -> int:
    created_molecules = get_all_fabricatable_molecules(replacements_by_element, seed_molecule)
    return len(created_molecules)

if __name__ == "__main__":
    example_replacements_by_element, example_seed_molecule = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 4
    test(expected_answer, solution, example_replacements_by_element, example_seed_molecule)

    replacements_by_element, seed_molecule = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, replacements_by_element, seed_molecule)