from pathlib import Path
from typing import List, Dict, Optional

from Day_19.const import DAY, INPUT_FILE_NAME
from Day_19.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_19.load_input import load_input
from utils.solve import test, solve

def solution(replacements_by_element: Dict[str, List[str]], medicine_molecule: List[str]) -> int:
    terminal_elements = replacements_by_element["e"]
    elements_by_replacement = {
        new_element: element 
        for element, replacements in replacements_by_element.items() for new_element in replacements
        if element != "e"
    }

    def dfs(elements_by_replacement: Dict[str, str], molecule: str, steps: int=0) -> Optional[int]:
        
        if molecule in terminal_elements:
            return steps+1

        sorted_element_replacements = sorted(elements_by_replacement.items(), key=lambda t: len(t[0]), reverse=True)
        for new_element, element in sorted_element_replacements:
            new_molecule = molecule.replace(new_element, element, 1)
            if new_molecule == molecule:
                continue
            dfs_result = dfs(elements_by_replacement, new_molecule, steps+1)
            if dfs_result:
                return dfs_result
        
        return None

    return dfs(elements_by_replacement, medicine_molecule)
    
if __name__ == "__main__":
    example_replacements_by_element, example_medicine_molecule = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 6
    test(expected_answer, solution, example_replacements_by_element, example_medicine_molecule)

    replacements_by_element, medicine_molecule = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, replacements_by_element, medicine_molecule)