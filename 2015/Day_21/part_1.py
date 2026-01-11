from pathlib import Path
from typing import List, Dict, Tuple
import math
from itertools import combinations

from Day_21.const import DAY, INPUT_FILE_NAME
from Day_21.load_input import load_input
from Day_21.shop import SHOP
from utils.solve import solve

def fight_turn_by_turn_simulation(player_1_stats: Dict[str, int], player_2_stats: Dict[str, int]) -> Tuple[int, int]:
    player_1_stats = player_1_stats.copy()
    player_2_stats = player_2_stats.copy()

    def turn(attacker_stats: Dict[str, int], defender_stats: Dict[str, int]) -> None:
        damage = max(attacker_stats["Damage"] - defender_stats["Armor"], 1)
        defender_stats["Hit Points"] = max(defender_stats["Hit Points"] - damage, 0)

    is_player_1_turn = True     # assume player 1 goes first
    while player_1_stats["Hit Points"] > 0 and player_2_stats["Hit Points"] > 0:
        if is_player_1_turn:
            turn(player_1_stats, player_2_stats)
        else:
            turn(player_2_stats, player_1_stats)
        is_player_1_turn = not is_player_1_turn

    return player_1_stats["Hit Points"], player_2_stats["Hit Points"]


def is_player_winning_fight(player_stats: Dict[str, int], boss_stats: Dict[str, int]) -> bool:
    player_damage = max(player_stats["Damage"] - boss_stats["Armor"], 1)
    player_turns_required = math.ceil(boss_stats["Hit Points"] / player_damage)

    boss_damage = max(boss_stats["Damage"] - player_stats["Armor"], 1)
    boss_turns_required = math.ceil(player_stats["Hit Points"] / boss_damage)

    return player_turns_required <= boss_turns_required
    

def solution(boss_stats: Dict[str, int], player_hit_points: int, shop: Dict[str, List[Dict[str, str|int]]]) -> int:
    min_cost = float("inf")
    
    # This is a more elegant way to do the case of no armor and no rings
    shop["armor"].append({ "name": "No Armor",              "cost": 0,  "damage": 0, "armor": 0 })
    shop["rings"].append({ "name": "No Ring in Left Hand",  "cost": 0,  "damage": 0, "armor": 0 })
    shop["rings"].append({ "name": "No Ring in Right Hand", "cost": 0,  "damage": 0, "armor": 0 })

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

                    # final_player_hit_points, final_boss_hit_points = fight_turn_by_turn_simulation(player_stats, boss_stats)
                    # if final_boss_hit_points == 0:
                    #     min_cost = min(min_cost, cost)
                    if is_player_winning_fight(player_stats, boss_stats):
                        min_cost = min(min_cost, cost)
    
    return min_cost

if __name__ == "__main__":
    boss_stats = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    player_hit_points = 100
    solve(solution, boss_stats, player_hit_points, SHOP)