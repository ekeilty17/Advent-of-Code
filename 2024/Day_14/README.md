# Day 14: Restroom Redoubt

[Problem Link](https://adventofcode.com/2024/day/14)

## Part 1

The solution requires us to compute the final positions of the robots after some number of time steps `t`. The solution is ultimately figuring out the following set of equations.

```python
xf = (x0 + vx * t) % m
yf = (y0 + vy * t) % n
```

where `(x0, y0)` is the initial position of the robot, `(vx, vy)` is the velocity of the robot, `(m, n)` is the dimensions of the floor, and `t` is the time step. This is about as efficiently as the final positions can be computed.

Note this could be made slightly more efficient by vectorizing using numpy. But ultimately it's not a huge time gain.

```python
Xf = (X0 + Vx * t) % m
Yf = (Y0 + Vy * t) % n
```

Only thing that is left to solve the problem is to compute the quadrant counts, which just takes some trial and error.

## Part 2 

Ultimately, finding the christmas tree grid boils down to figuring out some way to measure how random a given grid of robots is. 

The first thing I thought of was to sum [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) between every pair of coordinates. I figured the christmas tree grid would on average require robots closer together compared to a random grid. Thus, my algorithm iterates through every robot position under `10_000` time steps and returns the time with the minimum aggregated distance. The search can be found in `part_2.py` and you can see the christmas tree grid in `part_2_solution_grid.py`.

I don't love my solution for part 2. For one it's slow to compute. Secondly, the method is somewhat empirical. For example, why `10_000` time steps? Becuase I tried it and it gave the right answer. 

I was playing around with comparing each time-step grid to a truly random grid, and using a statistical test like [chi-squared](https://en.wikipedia.org/wiki/Chi-squared_test) to determine if it was random or not. The issue with this approach is that many intermediary positions are also statistically not random. So I don't think there is any universal filter here. I think the solution will always be somewhat tailored to the problem in this case.

If I could find a faster _randomness scoring_ function. I would be more satified with the solution.
