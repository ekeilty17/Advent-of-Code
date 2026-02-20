# Day 10: The Stars Align

[Problem Link](https://adventofcode.com/2018/day/10)

## Part 1 and Part 2 

Both part 1 and part 2 share a solution. One is the hidden message and the other is the number of steps to get there. 

### The Position Update Function

The puzzle input is a list of positions $\boldsymbol{p}(0)$ and corresponding list of velocities $\boldsymbol{v}$. Given an time $t$ we can determine the corresponding position $\boldsymbol{p}(t)$ at that time. This is given by

$$
\boldsymbol{p}(t) = \boldsymbol{p}(0) + t \cdot \boldsymbol{v}
$$

This is implemented in `update_position()` in `part_2.py`.

### How Can We Detect The Hidden Message?

Let's compare the target grid to the grid from the time immediately before and after

```
..........#...                      ........#....
#..#...####..#      #...#..###      ....##...#.#.
..............      #...#...#.      ..#.....#..#.
....#....#....      #...#...#.      .#..##.##.#..
..#.#.........      #####...#.      ...##.#....#.
...#...#...... -->  #...#...#. -->  .......#....#
...#..#..#.#..      #...#...#.      ..........#..
#....#.#......      #...#...#.      #......#...#.
.#...#...##.#.      #...#..###      .#.....##....
....#.........                      ...........#.
                                    ...........#.
```

Since the velocities are constant, all of the points originally start out far away from each other, eventually meet in a clump which forms the letters `HI`, and then continue forward and fly away from each other.

So, the target grid represents a **minimum state** where **all of the points are clumped closely together**. 

### A Convex Function

Consider the following function

```python
def total_pairwise_distance(positions):
    return sum([
        manhattan_distance(positions[i], positions[j])
        for i in range(len(positions))
        for j in range(i+1, len(positions))
    ])

def f(t):
    positions = update_positions(positions, velocities, t)
    return total_pairwise_distance(positions)
```

This function is summing the pairwise distance between [Manhattan Distance](https://en.wikipedia.org/wiki/Taxicab_geometry) between each pair of points at a given time $t$. **This function will be take its minimum value at the target grid.**

Therefore, we now just have to compute

$$
t^* = \argmin_{t \geq 0} f(t)
$$

Based on the properties of the problem, I claim this function is convex. Therefore it has a single, unique local minimum, which is also the global minimum.

### Discrete Convex Optimization

I implement the [Golden Section Search](https://en.wikipedia.org/wiki/Golden-section_search) to find the minimum of the function $f$. The details of how this algorithm works are very interesting. It would take too many characters to explain here. This is not the most entertaining video, but it is comprehensive - [Golden Section Search Method Theory and Example](https://www.youtube.com/watch?v=VmJHxJktsOU&list=PLkLO93SRHC-GM6bULdSlBKZ93IIZEEhlL).

The Golden Section Search is essentially a way to implement a binary search in order to find a minimum of a function.