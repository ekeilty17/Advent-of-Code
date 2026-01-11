from pathlib import Path
from typing import List, Dict
from itertools import combinations

from Day_21.const import DAY, INPUT_FILE_NAME
from Day_21.load_input import load_input
from Day_21.shop import SHOP
from Day_21.part_1 import is_player_winning_fight
from utils.solve import solve


def solution(boss_stats: Dict[str, int], player_hit_points: int, shop: Dict[str, List[Dict[str, str|int]]]) -> int:
    
    # This is a more elegant way to do the case of no armor and no rings
    shop["armor"].append({ "name": "No Armor",              "cost": 0,  "damage": 0, "armor": 0 })
    shop["rings"].append({ "name": "No Ring in Left Hand",  "cost": 0,  "damage": 0, "armor": 0 })
    shop["rings"].append({ "name": "No Ring in Right Hand", "cost": 0,  "damage": 0, "armor": 0 })

    max_cost = 0
    for weapon in shop["weapons"]:
        for armor in shop["armor"]:
            for ring1, ring2 in combinations(shop["rings"], 2):

                    items = [weapon, armor, ring1, ring2]
                    player_stats = {
                        "Hit Points": player_hit_points,
                        "Damage": sum([item["damage"] for item in items]),
                        "Armor": sum([item["armor"] for item in items]),
                    }
                    cost = sum([item["cost"] for item in items])

                    if not is_player_winning_fight(player_stats, boss_stats):
                        max_cost = max(max_cost, cost)
    
    return max_cost

if __name__ == "__main__":
    boss_stats = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    player_hit_points = 100
    solve(solution, boss_stats, player_hit_points, SHOP)