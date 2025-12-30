# Day 20: Race Condition

[Problem Link](https://adventofcode.com/2024/day/20)

## Part 1

This is a very nice problem. The first step is to use what we learned in Day 16 and Day 18 and write a SSSP solver using [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). This will get you the baseline picoseconds between `S` and `E` without using cheats.

Using a cheat lets you pass through walls. Consider the following example

```
###############
#...#.A#B....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

The cheat lets you go from `A` to `B` as if there was no wall (`#`) in the way. So now the cheated distance is 
```
distance(S --> A) + 2 + distance(B --> E)
```
The `+2` is for the two step it's takes to get from `A` to `B` with the cheat.

We have already run Dijkstra's algorithm starting as `S`, which lets us calculate `distance(S --> A)` for any `A`. The naive way of computing `distance(B --> E)` would be to run Dijkstra's starting at `B` for every cell in the grid. However, this would be very very slow and there is a much cleaner solution. 

We use the symmetry of the problem and notice that 
```
distance(B --> E) == distance(E --> B)
```

Therefore, we just need to run Dijkstra's twice. Once starting at `S` and once starting at `E`. This will output `dist_S` and `dist_E` respectively, such that
```
dist_S[A] == distance(S --> A)
dist_E[B] == distance(E --> B) == distance(B --> E)
```

Therefore, the solution to part 1 is to iterate through every wall cell (`#`) in the grid, and for each pair of neighbors (`A` and `B`), compute
```
cheated_picoseconds = dist_S[A] + 2 + dist_E[B]
```

The full algorithm is as follows
1. Compute `dist_S` using Dijkstra's algorithm starting at `S`
2. Compute `dist_E` using Dijkstra's algorithm starting at `E`
3. **For each** wall cell (`#`) of the racetrack 
    1. Let `A` and `B` be any pair of orthognal neighbors
    2. `cheated_picoseconds = dist_S[A] + 2 + dist_E[B]`
    3. compare `cheated_picoseconds` to `dist_S[E]`

Finally, we compare the cheated picoseconds to the baseline picoseconds to see how much time each cheat saved.

## Part 2 

I'd like to highlight this sentence from the problem statement.

> Because this cheat has the same start and end positions as the one above, it's the same cheat

I think this gives a pretty large hint at the method of solving the problem. It means that during a cheat we only have to consider the startpoint and endpoint, and we do not care about what intermediary path was taken. 

Furthermore, as long as the [manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) between two points is less than or equal to the cheat length (`20` picoseconds in this case), then we know it's possible to get to these two cells via cheats.

Therefore, conceptually part 2 is not all that different than part 1. We now just have an expanded definition of what cells we can teleport to and from. Also, the `cheated_picoseconds` calculation is generalized to 
```
cheated_picoseconds = dist_S[A] + manhattan_distance(A, B) + dist_E[B]
```

The full algorithm is as follows
1. Compute `dist_S` using Dijkstra's algorithm starting at `S`
2. Compute `dist_E` using Dijkstra's algorithm starting at `E`
3. **For each** non-wall cell in the racetrack, denote `A`
    1. **For each** non-wall cell in the racetrace, denote `B`
        1. **If** `manhattan_distance(A, B) > 20`, **then** continue to next iterate
        2. `cheated_picoseconds = dist_S[A] + manhattan_distance(A, B) + dist_E[B]`
        3. compare `cheated_picoseconds` to `dist_S[E]`


In practice, you have to be a bit more efficient with the two for loops. You can instead iterate over all positions `+/-20` cells in all directions of `A`, and that saves a lot of wasted iterations. This essentially reduces the runtime from `O(n^4)` to `O(n^2)`.
