# Day 14: Reindeer Olympics

[Problem Link](https://adventofcode.com/2015/day/14)

## Part 1

This really boils down to writing a function $x(t)$ which can calculate the distance traveled by each reindeer given a time.

The first thing to notice is that $x(t)$ is cyclic, as each reindeer flies, then rests, and then repeats. Let's formalize. Let $t_{f}$ and $t_{r}$ be the flight and rest times, respectively. Therefore, the total cycle length is 
$$
\tau = t_{f} + t_{r}
$$

So let's define $x_{\tau}(t)$ as the distance function within a cycle. Let $v$ be the reindeer's flight speed. Based on the problem description that function is

$$
x_{\tau}(t) = v \cdot \min(t_f, t)
$$

Now, the total distance is just the number of cycles + however far the reindeer gets on the last leg. The number of cycles can be calculated using $\lfloor \tfrac{t}{\tau} \rfloor$ (which is `//` in most programming languages). The time on the last leg is calculated using $t \bmod \tau$ (which is `%` in most programming languages).

$$
x(t) = \left \lfloor \tfrac{t}{\tau} \right \rfloor x_{\tau}(\tau) + x_{\tau}(t \bmod \tau)
$$

This formula is implemented in `compute_reindeer_distance()` in `part_1.py`.

## Part 2 

Using my formula for $x(t)$ from part 1, I can just iterate over every time step $[1, 2, \ldots, T]$, compute the distance of each reindeer, and incremenet the points accordingly.