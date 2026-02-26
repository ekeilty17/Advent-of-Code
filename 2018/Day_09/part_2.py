from utils.solve import test, solve
from collections import deque

def solution(num_players: int, num_marbels: int) -> int:
    player_scores = [0] * num_players
    played_marbles = deque([0])

    for turn in range(num_marbels):
        player = turn % num_players
        marble = turn + 1

        if marble % 23 == 0:
            played_marbles.rotate(7)
            player_scores[player] += marble + played_marbles.pop()
            played_marbles.rotate(-1)

        else:
            played_marbles.rotate(-1)
            played_marbles.append(marble)

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
    num_marbels = 70723 * 100
    solve(solution, num_players, num_marbels)