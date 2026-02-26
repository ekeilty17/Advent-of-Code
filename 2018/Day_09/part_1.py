from utils.solve import test, solve
from Day_09.part_2 import solution as part_2_solution

def solution(num_players: int, num_marbels: int) -> int:
    player_scores = [0] * num_players
    played_marbles = [0]

    circle = 0
    for turn in range(num_marbels):
        player = turn % num_players
        marble = turn + 1

        if marble % 23 == 0:
            circle = (circle - 7) % len(played_marbles)
            player_scores[player] += marble + played_marbles.pop(circle)
        else:
            circle = (circle + 1) % len(played_marbles) + 1
            played_marbles.insert(circle, marble)

    return max(player_scores)

if __name__ == "__main__":
    examples = [
        (9, 25, 32),
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305),
    ]
    for example_num_players, example_num_marbels, expected_answer in examples:
        test(expected_answer, solution, example_num_players, example_num_marbels)

    num_players = 427
    num_marbels = 70723
    # solve(solution, num_players, num_marbels)
    solve(part_2_solution, num_players, num_marbels)