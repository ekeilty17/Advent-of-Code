from pathlib import Path
from typing import Dict

from Day_22.const import DAY, INPUT_FILE_NAME
from Day_22.load_input import load_input
from Day_22.part_1 import search
from utils.solve import solve

def solution(player_hit_points: int, player_mana_points: int, boss_stats: Dict[str, int]) -> int:
    player_stats = {
        "Hit Points": player_hit_points,
        "Mana": player_mana_points,
        "Damage": 0,
        "Armor": 0
    }
    min_mana, spells = search(player_stats, boss_stats, is_hard_mode=True)
    print(spells)
    return min_mana

if __name__ == "__main__":
    player_hit_points = 50
    player_mana_points = 500
    boss_stats = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, player_hit_points, player_mana_points, boss_stats)