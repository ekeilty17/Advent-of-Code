# Day 22: Wizard Simulator 20XX

[Problem Link](https://adventofcode.com/2015/day/22)

## Part 1

The first part of this problem is to just write the game simulation. I'll be the first to admit that my code is not the best. Personally, I'm not super into RPGs, so this just felt tedius to me and once I got something working I just left it. Spending a bit more time decomposing the game and doing proper [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) would definitely make the code much cleaner.

Let's talk about the game simulation a high level. Each spell is a dictionary/object with a bunch of attributes, found in `spells.py`. Then you essentially have 3 objects which are the _game state_: `player_stats`, `boss_stats`, and `effects`. The `effects` object holds all of the active effects and maintains the number of time steps left. Then, you just have to similate a player's turn (`player_turn()`), the boss's turn (`boss_turn`), and the result of each active effect (`apply_effects()`). You can see how a fight would be simulated in `simulate_fight()`.

The next part of the problem is to search for a sequence of spells which let you win with the minimum mana. I did this using a [Best-First Search](https://en.wikipedia.org/wiki/Best-first_search) implemented using a [priority queue](https://www.geeksforgeeks.org/dsa/priority-queue-set-1-introduction/) on the amount of mana spent. This is elegant because the first sequence of spells found which causes the boss's HP to hit `0` is an optimal solution. No need to maintain a `min_mana` variable and prune.

## Part 2 

Exactly the same as part 1, just in `hard_mode`.