from pathlib import Path
from typing import List, Dict, TypeAlias, Tuple
import heapq

from Day_22.const import DAY, INPUT_FILE_NAME
from Day_22.load_input import load_input
from Day_22.spells import SPELLS
from utils.solve import solve

Spell: TypeAlias = Dict[str, int]
Effect: TypeAlias = Dict[str, int]
Stats: TypeAlias = Dict[str, int]

def apply_effects(player_stats: Stats, boss_stats: Stats, effects: Dict[str, Effect]) -> None:
    effects_damage = sum(effect["damage"] for effect in effects.values())
    boss_stats["Hit Points"] = max(boss_stats["Hit Points"] - effects_damage, 0)

    player_stats["Mana"] += sum(effect["mana"] for effect in effects.values())

def increment_turn(effects: List[Effect]) -> List[Effect]:
    effects = {name: effect for name, effect in effects.items() if effect["turns"] > 0}
    for effect in effects.values():
        effect["turns"] -= 1
    return effects

def player_turn(player_stats: Stats, boss_stats: Stats, instant_spell: Spell, effects: Dict[str, Effect]) -> None:
    player_damage = player_stats["Damage"] + instant_spell["damage"]
    boss_stats["Hit Points"] = max(boss_stats["Hit Points"] - player_damage, 0)

    player_stats["Hit Points"] += instant_spell["heal"]
    player_stats["Mana"] -= instant_spell["cost"]

def boss_turn(player_stats: Stats, boss_stats: Stats, instant_spell: Spell, effects: Dict[str, Effect]) -> None:
    player_armor = player_stats["Armor"] + instant_spell["armor"] + sum([effect["armor"] for effect in effects.values()])
    boss_attack = max(boss_stats["Damage"] - player_armor, 1)
    player_stats["Hit Points"] = max(player_stats["Hit Points"] - boss_attack, 0)

"""
def simulate_fight(player_stats: Stats, boss_stats: Stats, player_spells: List[Spell], hard_mode: bool=True) -> bool:
    mana_spent = 0
    effects = {}

    for spell_name in player_spells:
        spell = SPELLS[spell_name]
        mana_spent += spell["instant"]["cost"]
        
        if hard_mode:
            player_stats["Hit Points"] -= 1
        if player_stats["Hit Points"] <= 0:
            return False

        player_turn(player_stats, boss_stats, spell["instant"], effects)
        apply_effects(player_stats, boss_stats, effects)
        effects[spell_name] = spell["effect"].copy()
        effects = increment_turn(effects)

        if boss_stats["Hit Points"] <= 0:
            return True

        boss_turn(player_stats, boss_stats, spell["instant"], effects)
        apply_effects(player_stats, boss_stats, effects)
        effects = increment_turn(effects)

        if player_stats["Hit Points"] <= 0:
            return False
    
    return boss_stats["Hit Points"] == 0
"""

def search(init_player_stats: Stats, init_boss_stats: Stats, is_hard_mode: bool=False) -> Tuple[int, List[str]]:

    COUNTER = 0     # the counter is just used to break ties in the priority queue

    queue = []
    heapq.heappush(queue, (0, COUNTER, init_player_stats, init_boss_stats, {}, []))

    while queue:
        COUNTER += 1
        popped_mana_spent, _, popped_player_stats, popped_boss_stats, popped_effects, popped_spells = heapq.heappop(queue)

        for spell_name, spell in sorted(SPELLS.items(), key=lambda t: t[1]["instant"]["cost"]):
            player_stats = popped_player_stats.copy()
            boss_stats = popped_boss_stats.copy()
            effects = {spell_name: effect.copy() for spell_name, effect in popped_effects.items()}
            
            spells = list(popped_spells) + [spell_name]
            mana_spent = popped_mana_spent + spell["instant"]["cost"]

            if spell_name in [name for name, effect in effects.items() if effect["turns"] > 0]:
                continue
            if spell["instant"]["cost"] > player_stats["Mana"]:
                continue

            if is_hard_mode:
                player_stats["Hit Points"] -= 1
            if player_stats["Hit Points"] <= 0:
                continue
            
            # Player Turn
            player_turn(player_stats, boss_stats, spell["instant"], effects)
            apply_effects(player_stats, boss_stats, effects)
            effects[spell_name] = spell["effect"].copy()
            effects = increment_turn(effects)

            if boss_stats["Hit Points"] <= 0:
                return mana_spent, spells
            
            # Boss Turn
            boss_turn(player_stats, boss_stats, spell["instant"], effects)
            apply_effects(player_stats, boss_stats, effects)
            effects = increment_turn(effects)

            if boss_stats["Hit Points"] <= 0:
                return mana_spent, spells
            if player_stats["Hit Points"] <= 0:
                continue
            
            heapq.heappush(queue, (mana_spent, COUNTER, player_stats, boss_stats, effects, spells))

    # No solution found
    return -1, []

def solution(player_hit_points: int, player_mana_points: int, boss_stats: Dict[str, int]) -> int:
    player_stats = {
        "Hit Points": player_hit_points,
        "Mana": player_mana_points,
        "Damage": 0,
        "Armor": 0
    }
    min_mana, spells = search(player_stats, boss_stats)
    print(spells)
    return min_mana

if __name__ == "__main__":
    player_hit_points = 50
    player_mana_points = 500
    boss_stats = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, player_hit_points, player_mana_points, boss_stats)
    # 1289
    # spells = ["Poison", "Recharge", "Shield", "Poison", "Recharge", "Drain", "Poison", "Drain", "Magic Missile"]