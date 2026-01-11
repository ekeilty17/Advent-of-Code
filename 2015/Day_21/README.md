# Day 21: RPG Simulator 20XX

[Problem Link](https://adventofcode.com/2015/day/21)

## Part 1

The first thing we need to do is write a function that determine whether the player wins the boss fight. There are 2 ways to do this. The first is the brute-force way of just simulating the fight turn by turn. In general, this is `O(Hit Points)`. Unfortunately, since the `Hit Points` in this problem are like `100`, this is still pretty fast. I wish they were higher, so this solution was slower.

There is a better way. The key thing to notice is that the damage done by the player and boss are both constant throughout the fight. So instead of iteratively subtracting the damage, we can just compute the number of turns each would take to drain the other's `Hit Points`. For example.

```python
player_damage = max(player_stats["Damage"] - boss_stats["Armor"], 1)
player_turns_required = math.ceil(boss_stats["Hit Points"] / player_damage)
```

Now, you just compare `player_turns_required` to `boss_turns_required` (calculated equivalently), and see who drains the other's `Hit Points` first. This is `O(1)`. See `is_player_winning_flight()` in `part_1.py` for the full implementation.

The only other complication of the problem is dealing with the fact that armor is optional and that you can have between `0` and `2` rings. You could code this as a bunch of different loops and cases. However, the cleanest way is to make `No Armor` and `No Ring` items themselves, i.e.

```python
shop["armor"].append({ "name": "No Armor",              "cost": 0,  "damage": 0, "armor": 0 })
shop["rings"].append({ "name": "No Ring in Left Hand",  "cost": 0,  "damage": 0, "armor": 0 })
shop["rings"].append({ "name": "No Ring in Right Hand", "cost": 0,  "damage": 0, "armor": 0 })
```

Now, there are no execption cases. We just iterate through all weapons, armor, and pairs of distinct rings.

## Part 2 

Exactly the same as part 1, except we are looking for the max cost of all item configurations where we lose the fight.