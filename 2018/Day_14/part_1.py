from typing import List
from utils.solve import test, solve

def get_digits_of_sum(*args: int) -> List[int]:
    return [int(x) for x in str(sum(args))]

def solution(initial_recipes: List[int], num_recipes: int, num_scores_ahead: int) -> str:
    recipe_scores = list(initial_recipes)
    e1, e2 = 0, 1

    while len(recipe_scores) < num_recipes + num_scores_ahead:
        new_recipe_scores = [int(x) for x in get_digits_of_sum(recipe_scores[e1], recipe_scores[e2])]
        recipe_scores.extend(new_recipe_scores)
        
        e1 = (e1 + recipe_scores[e1] + 1) % len(recipe_scores)
        e2 = (e2 + recipe_scores[e2] + 1) % len(recipe_scores)

    sequence = recipe_scores[num_recipes:num_recipes+num_scores_ahead]
    return "".join([str(x) for x in sequence])

if __name__ == "__main__":
    initial_recipes = [3, 7]
    num_scores_ahead = 10
    
    examples = [
        (5, "0124515891"),
        (9, "5158916779"),
        (18, "9251071085"),
        (2018, "5941429882")
    ]
    for example_num_recipes, expected_answer in examples:
        test(expected_answer, solution, initial_recipes, example_num_recipes, num_scores_ahead)

    num_recipes = 236021
    solve(solution, initial_recipes, num_recipes, num_scores_ahead)