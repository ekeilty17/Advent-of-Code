# Day 13: Claw Contraption

[Problem Link](https://adventofcode.com/2024/day/13)

## Part 1

This problem can be converted into a system of two equations and two unknowns. Let `A` and `B` be the number of A and B button presses, respectively. Then, for example, this machine configuration

```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
```

can be rewritten as

```
94 * A + 22 * B = 8400
34 * A + 67 * B = 5400
```

Or more generally

```
Ax * A + Bx * B = Px
Ay * A + By * B = Py
```

where `(Ax, Ay)` is where the claw moves after an A button press, `(Bx, By)` is where the claw moves after a B button press, and `(Px, Py)` is the coordinates of the prize.

Now, we have a system of 2 equations and 2 unknowns, so there will be a unique solution. There are a number of ways to code this, I re-expressed this as a matrix equation `Mx = b` and solved it using the inverse, i.e. `x = M^{-1} b`. I did this manually for fun, but I also did it in numpy, which just takes a few lines.

Once you have the solution `(A, B)`, you have to check if it's an integer solution, as we can only press buttons an integer number of times. To do this, I just rounded `A` and `B` to the nearest integers and plugged them back into the original set of equations. If we indeed found an integer solution, then all that is left is to calculate the number of tokens required as

```
num_tokens = 3*A + 1*B
```

According to the problem, non-integer solutions are disregarded.

## Part 2 

Exactly the same solution solves part 2. Since we solved this with math rather than state-space search, there is no difference in run-time.
