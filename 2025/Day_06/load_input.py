from pathlib import Path
from typing import List, Tuple

def load_input(input_path: Path) -> List[List[str]]:
    lines = input_path.read_text().splitlines()
    operation_line = lines[-1]
    
    non_empty_character_indexes = [i for i, c in enumerate(operation_line) if c != " "]

    # All of this is to maintain the spaces between the numbers
    # because we need that information for part 2
    parsed_lines = []
    for line in lines:
        parsed_line = []
        for k in range(len(non_empty_character_indexes)-1):
            i = non_empty_character_indexes[k]
            j = non_empty_character_indexes[k+1]
            parsed_line.append(line[i:j-1])
        parsed_line.append(line[non_empty_character_indexes[-1]:])
        parsed_lines.append(parsed_line)
    return parsed_lines