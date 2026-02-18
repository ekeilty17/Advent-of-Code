from pathlib import Path
from typing import List, Tuple, Dict, Set, TypeAlias

Claim: TypeAlias = Tuple[int, Tuple[int, int], Tuple[int, int]]

from Day_03.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_03.load_input import load_input
from utils.solve import test, solve

def generate_claim_squares(top_left: Tuple[int, int], dimensions: Tuple[int, int]) -> Set[Tuple[int, int]]:
    x0, y0 = top_left
    X, Y = dimensions
    for x in range(X):
        for y in range(Y):
            yield x0 + x, y0 + y

def compute_claim_cover(claims: List[Claim]) -> Dict[Tuple[int, int], Set[int]]:
    claims_by_square = {}
    for claim_id, top_left, dimensions in claims:
        for square in generate_claim_squares(top_left, dimensions):
            if square not in claims_by_square:
                claims_by_square[square] = []
            claims_by_square[square].append(claim_id)
    
    return claims_by_square

def solution(claims: List[Claim]) -> int:
    claims_by_square = compute_claim_cover(claims)
    return sum([len(claims) > 1 for claims in claims_by_square.values()])

if __name__ == "__main__":
    example_claims = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 4
    test(expected_answer, solution, example_claims)

    claims = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, claims)