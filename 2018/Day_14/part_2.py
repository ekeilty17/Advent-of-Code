from typing import List
from Day_14.part_1 import get_digits_of_sum
from utils.solve import test, solve

def solution(initial_recipes: List[int], target_sequence: str) -> int:
    recipe_scores = list(initial_recipes)
    target_sequence = [int(x) for x in target_sequence]
    e1, e2 = 0, 1
    
    while True:
        
        # standard update
        new_recipe_scores = [int(x) for x in get_digits_of_sum(recipe_scores[e1], recipe_scores[e2])]
        recipe_scores.extend(new_recipe_scores)
        e1 = (e1 + recipe_scores[e1] + 1) % len(recipe_scores)
        e2 = (e2 + recipe_scores[e2] + 1) % len(recipe_scores)

        # Checking sequences produced by newly added recipe scores
        for i in reversed(range(len(new_recipe_scores))):
            sequence = recipe_scores[-i-len(target_sequence):len(recipe_scores)-i]
            if all(x == y for x, y in zip(sequence, target_sequence)):
                return len(recipe_scores)-i-len(target_sequence)

if __name__ == "__main__":
    initial_recipes = [3, 7]
    
    examples = [
        ("01245", 5),
        ("51589", 9),
        ("92510", 18),
        ("59414", 2018)
    ]
    for example_target_sequence, expected_answer in examples:
        test(expected_answer, solution, initial_recipes, example_target_sequence)

    target_sequence = "236021"
    solve(solution, initial_recipes, target_sequence)