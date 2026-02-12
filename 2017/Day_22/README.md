# Day 22: Sporifica Virus

[Problem Link](https://adventofcode.com/2017/day/22)

## Part 1

Since the grid is infinite, the best way to store the infected nodes is with a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)). In my implementation, I have a set `infected` which contains all of the grid coordinates which are infected.

The concept of a "direction" is implemented with grid offsets. For example, "up" is equivalent to the offset `(-1, 0)` since `(x-1, y)` is the cell "above" `(x, y)`. This makes it very easy to "move" the virus in the desired direction. Furthermore, it is easy to "turn" the virus (essentially by multiplying by a rotation matrix). All of this logic is implemented in `turn_left()`, `turn_right()`, and `move_in_direction()` in `part_1.py`.

Now we just execute the virus algorithm as described. To toggle a node from clean to infected, add the node to the set `infected`. To toggle a node from infected to clean, remove the node from the set `infected`. The solution is to count the number of times a call is toggled from clean to infected.

## Part 2 

Part 2 is essentially the same as part 1, except we have more states that a cell can be in. Now instead of a set, I use a [Python dictionary](https://www.w3schools.com/python/python_dictionaries.asp) which maps a grid coordinate to its corresponding state. If a coordinate is not present in the dictionary, then it is assumed to be in the "cleaned" state.

Now we just implement the grid update logic as described by the problem, counting the number of times a cell state becomes "infected".