# Day 15: Warehouse Woes

[Problem Link](https://adventofcode.com/2024/day/15)

## Part 1

This is another problem where the challenge is just to efficiently simulate it (or really simulate it at all). My approach worked as follows. Suppose we have this configuration

```
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
```

and we need to make the move `>`. My code isolates everything to the right of the robot, and finds the position of the nearest `.`.

```
#..|@OO.#
       ^
```

Then, I just rotate everything one to the right.

```
#..|@OO.#   -->     #..|.@OO#
    1234                4123
```

There are 2 exception cases. 1) when there are no `.` characters in the robot's direction, and 2) when there is a `#` in the way. 
```
1) #...@OO#
2) #.@OO#.#
```

In both situations we just do nothing and return the same state.

In my original solution, I wrote the logic of each direction separately (`part_1.py`). In `part_1_alt.py`, I instead only wrote the logic for the down direction (`v`). For the other directions (`^`, `>`, `<`) I used grid transformations so I could reused the `make_down_move()` function.

## Part 2 

In part 2, going up and down versus left and right are fundamentally different. Left and right is the easier case, which is exactly the same logic as part 1. But going up and down requires a bit more thought.

To simplify, let's consider only the down case. I essentially used a modified [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) to find all of the boxes which the robot will move. Essentially this boils down to correctly defining "neighbors" of this traversal. For example, if the current position is `[`. then we have to check the right cell and the cell below. See the function `get_connected_boxes()` for more details.

Now I have a set of indices in the grid which need to be incremented downwards. I increment everything down as a group. If any of the incremented cells contain a wall (`#`), then revert everything back to the original state. Otherwise, return the new state.

The last thing to note is that I used a similar strategy to `part_1_alt.py`. I implemented the above logic for the down case. Then I used grid transformations so that I could call the same `make_down_move()` function for the up case.
