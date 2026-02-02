# Day 11: Hex Ed

[Problem Link](https://adventofcode.com/2017/day/11)

## Part 1 and Part 2

I really like this problem. It has very nice geometry

### The Hexagonal Grid

The first trick is we need to map these hexagonal movements onto a typical Cartesian grid. Consider the following

![Hex Grid](hex_grid.png)

So, each direction maps to a horizontal/vertical displacement on the typical Cartesian grid.

```python
displacement_map = {
    "n": (0, 2),
    "ne": (1, 1),
    "se": (1, -1),
    "s": (0, -2),
    "sw": (-1, -1),
    "nw": (-1, 1)
}
```

Notice now, that `ne + nw == n`, These directions work exactly how you would expect them to, and that can be seen visually by the grid above.

### Determining the Final Cartesian Position

Now, given a sequence of hexagon moves, we can determine the final position in our Cartesian coordinate system.

For each hex step, we sum the Cartesian displacements in `displacement_map`. Here is an example.

![Hex Grid Path](hex_grid_path.png)

This is implemented in `update_hex_position()`.

### Finding the Optimal Number of Steps

Now the problem has reduced to _what is the minimum number of hexagon steps required to get to a given coordinate_. This what is implemented in `get_hex_distance()`.

First, we notice that the problem is symmetric. Without loss of generality, we can assume the target coordinates are in the northeast quadrant. This is the purpose of the line
```python
x, y = abs(x), abs(y)
```

There are 2 cases. **Case 1** is when `y <= x`. In this case, we never need to use the north direction. An optimal solution can be reached with the correct zig-zag of northeast and southeast steps. For example

![Hex Grid Shortest Path Case 1](hex_grid_shortest_path_case_1.png)

Therefore, for case 1, the optimal number of steps is just equal to `x`.

**Case 2** is when `y > x`. Here, an optimal solution is to just two "straight" lines. First, we use only northeast steps until we are directly below the target. Then, we use only north steps to reach the final target coordinate.

![Hex Grid Shortest Path Case 2](hex_grid_shortest_path_case_2.png)

Therefore, for case 2, the optimal number of steps is
```
(number of northeast steps) + (number of north steps)
= (x) + ((y-x)//2)
```

We divide by `2` because each north step is 2 units in the grid, but only 1 hexagon step.

Both cases can be expressed as a single formula
```python
def get_hex_distance(x, y):
    x, y = abs(x), abs(y)
    return x + max(y - x, 0) // 2
```