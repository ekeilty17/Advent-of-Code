from pathlib import Path
from typing import List, Dict, Any, Tuple

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.solve import test, solve

def excecute_transfer(
        bots: Dict[int, List[int]], 
        outputs: Dict[int, List[int]],
        bot: int, 
        low: str, 
        low_index: int, 
        high: str, 
        high_index: int
    ) -> bool:
    
    if len(bots.get(bot, [])) != 2:
        return False
    
    low_microchip, high_microchip = bots[bot]

    transfer_dict = bots if low == "bot" else outputs
    if low_index in transfer_dict:
        transfer_dict[low_index].append(low_microchip)
    else:
        transfer_dict[low_index] = [low_microchip]
    transfer_dict[low_index] = list(sorted(transfer_dict[low_index]))

    transfer_dict = bots if high == "bot" else outputs
    if high_index in transfer_dict:
        transfer_dict[high_index].append(high_microchip)
    else:
        transfer_dict[high_index] = [high_microchip]
    transfer_dict[high_index] = list(sorted(transfer_dict[high_index]))

    return True

def simulate_bots(
        initializations: Dict[str, List[int]], 
        transfers: Dict[str, Tuple[str, int, str, int]]
    ) -> Tuple[Dict[str, List[int]], Dict[str, int]]:

    bots = {}
    outputs = {}

    for bot, microchip in initializations.items():
        bots[bot] = list(sorted(microchip))

    while transfers:
        remaining_transfers = {}
        for bot, (low, low_index, high, high_index) in transfers.items():
            successful = excecute_transfer(bots, outputs, bot, low, low_index, high, high_index)
            if not successful:
                remaining_transfers[bot] = (low, low_index, high, high_index)
        
        transfers = remaining_transfers
    
    outputs = {index: microchips[0] for index, microchips in outputs.items()}
    return bots, outputs

def solution(
        initializations: Dict[str, List[int]], 
        transfers: Dict[str, Tuple[str, int, str, int]],
        microchip_responsibility: Tuple
    ) -> int:
    
    bots, _ = simulate_bots(initializations, transfers)

    microchip_responsibility = tuple(sorted(microchip_responsibility))
    for bot, microchips in bots.items():
        if tuple(sorted(microchips)) == microchip_responsibility:
            return bot

if __name__ == "__main__":
    example_initializations, example_transfers = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_microchip_responsibility = (5, 2)
    expected_answer = 2
    test(expected_answer, solution, example_initializations, example_transfers, example_microchip_responsibility)

    initializations, transfers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    microchip_responsibility = (61, 17)
    solve(solution, initializations, transfers, microchip_responsibility)