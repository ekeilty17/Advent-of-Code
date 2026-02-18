from pathlib import Path
from typing import List

from Day_03.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_03.load_input import load_input
from Day_03.part_1 import Claim, compute_claim_cover
from utils.solve import test, solve

def solution(claims: List[Claim]) -> int:
    claims_by_square = compute_claim_cover(claims)

    is_overlapping_by_claim_id = {claim_id: False for claim_id, _, _ in claims}
    for claim_ids in claims_by_square.values():
        if len(claim_ids) > 1:
            for claim_id in claim_ids:
                is_overlapping_by_claim_id[claim_id] = True

    nonoverlapping_claim_ids = [claim_id for claim_id, is_overlapping in is_overlapping_by_claim_id.items() if not is_overlapping]
    return nonoverlapping_claim_ids[0]

if __name__ == "__main__":
    example_claims = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_claims)

    claims = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, claims)