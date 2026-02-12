# Day 20: Particle Swarm

[Problem Link](https://adventofcode.com/2017/day/20)

## Equations of Motion of the Particle

For each particle, we are given the **initial position**, **initial velocity**, and **acceleration** as $\boldsymbol{p}_0$, $\boldsymbol{v}_0$, and $\boldsymbol{a}$ respectively, which are 3D coordinates. 

Let $t$ denote **discrete** time steps, then the problem says that

$$
\begin{cases}
    \boldsymbol{v}_t = \boldsymbol{v}_{t-1} + \boldsymbol{a} \\
    \boldsymbol{p}_t = \boldsymbol{p}_{t-1} + \boldsymbol{v}_{t-1} \\
\end{cases}
$$

Solving the recurrence, we get that

$$
\begin{cases}
    \boldsymbol{v}_t = \boldsymbol{v}_0 + \boldsymbol{a} t \\
    \boldsymbol{p}_t = \boldsymbol{p}_0 + \boldsymbol{v}_0 t + \tfrac{1}{2} t(t+1) \boldsymbol{a} \\
\end{cases}
$$

And now we can compute the particle's position at any time step.

## Part 1

The question asks us to figure out which particle stays closest to the origin as $t$ tends towards infinity. Here, distance is defined as the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)

$$
d(\boldsymbol{x}) = \sum_{\ell=0}^k \lvert x_{\ell} \rvert
$$

We want to find the particle $i$ such that $d(\boldsymbol{p}_t^{(i)})$ grows the slowest.

### Empirical Solution

We can just plug in a very large time step $T$ into our formula for $\boldsymbol{p}_t$ and take the minimum distance. Written formally

$$
i^* = \argmin_{i} \ d(\boldsymbol{p}_{T}^{(i)}) \quad \text{for sufficiently large } T
$$

I used $T = 1,000,000$, but through experimentation it seems like you only needed $T = 1000$.


### Analytical Solution

While the above approach is conceptually simple, you can't know _for certain_ that you have a sufficiently large $T$. Instead, we can do a theoretical analysis any analyze end behavior.

#### End Behavior Analysis

Suppose I have two particles $i$ and $j$. We want to know which of $d(\boldsymbol{p}_t^{(i)})$ or $d(\boldsymbol{p}_t^{(j)})$ **grows faster**. To do this, we take this limit

$$
\lim_{t \rightarrow \infty} \frac{d(\boldsymbol{p}_t^{(i)})}{d(\boldsymbol{p}_t^{(j)})}
$$

Let's expand this limit a little bit

$$
\lim_{t \rightarrow \infty} \frac{d(\boldsymbol{p}_0^{(i)} + \boldsymbol{v}_0^{(i)}t + \tfrac{1}{2} t(t+1) \boldsymbol{a}^{(i)})}{d(\boldsymbol{p}_0^{(j)} + \boldsymbol{v}_0^{(j)}t + \tfrac{1}{2} t(t+1) \boldsymbol{a}^{(j)})}
$$

We notice that $\tfrac{1}{2} t(t+1) \boldsymbol{a}^{(i)}$ and $\tfrac{1}{2} t(t+1) \boldsymbol{a}^{(j)}$ are the dominant terms in this limit. Therefore, this simplifies to

$$
\lim_{t \rightarrow \infty} \frac{d(\tfrac{1}{2} t(t+1) \boldsymbol{a}^{(i)})}{d(\tfrac{1}{2} t(t+1) \boldsymbol{a}^{(j)})} = \lim_{t \rightarrow \infty} \frac{d(\boldsymbol{a}^{(i)})}{d(\boldsymbol{a}^{(j)})}
$$

Therefore, the particle which stays the closest to the origin is the particle with the minimum $d(\boldsymbol{a})$. 

Now, suppose $d(\boldsymbol{a}^{(i)}) = d(\boldsymbol{a}^{(j)})$. Then dominating terms in the limit become

$$
\lim_{t \rightarrow \infty} \frac{d(\boldsymbol{p}_0^{(i)} + \boldsymbol{v}_0^{(i)}t)}{d(\boldsymbol{p}_0^{(j)} + \boldsymbol{v}_0^{(j)}t)} = \lim_{t \rightarrow \infty} \frac{d(\boldsymbol{v}_0^{(i)}t)}{d(\boldsymbol{v}_0^{(j)}t)} = \lim_{t \rightarrow \infty} \frac{d(\boldsymbol{v}_0^{(i)})}{d(\boldsymbol{v}_0^{(j)})} 
$$

Likewise, if also $d(\boldsymbol{v}_0^{(i)}) = d(\boldsymbol{v}_0^{(j)})$, then the comparison becomes

$$
\lim_{t \rightarrow \infty} \frac{d(\boldsymbol{p}_0^{(i)})}{d(\boldsymbol{p}_0^{(j)})}
$$

#### Algorithm

To summarize the above analysis, we have shown that

$$
i^* = \argmin_{i} \ (d(\boldsymbol{a}^{(i)}), \, d(\boldsymbol{v}_0^{(i)}), \, d(\boldsymbol{p}_0^{(i)}))
$$

where the tuples are ordered **lexicographically** (i.e. the way tuples sort in Python).

Intuitively, the distance to the origin is dominated by the acceleration. A larger acceleration will always overcome any initial velocity or position value. However, if acceleration is tied, then we compare initial velocities, as a larger velocity will always overcome any initial position. Finally, if both are tied we check initial position.


## Part 2 

Part 2 is equally as interesting. The crux of the problem is being able to efficiently determine if and when a pair of particles collide.

### Pairwise Particle Collisions

The key to my solution is writing a function which finds the intersections between the trajectories of two particles. This essentially means integer program. In particular linear and quadratic linear programming. I solve each of the 3 spacial dimensions independently and set intersect to get the final intersection. You can see my implementations of the 1D solvers in the functions `integer_linear_programming()` and `integer_quadratic_programming()` in `part_2.py`. It's just standard high-school math.

Once I have all of the possible collisions and their corresponding times, I just have to iterate over the collisions in sequential order and eliminate particles accordingly. Conceptually it is simple, but there are some annoying details. See my implementation in `compute_destroyed_particles()` in `part_2.py`.

### An Alternative Method

I didn't actually code this, but I suspect you could instead do this iteratively and just check the positions of all particles at every time-step. The hard part is determining a stop condition, i.e. some way of knowing none of the particles will intersect again.

Let's note that the trajectories are of each particle is a discrete parabola. So in the general case, the particle starts at one end of the parabola and does a swoop around its apex and then goes off to infinity essentially in a straight-line.

Now, to code this method I think you need 2 functions. 1) a function which determines whether we are in the "straight-line" regime. 2) a function which determines whether two particles are moving towards each other. Then the stop condition is just 
```
(each partical in the straight-line regime) AND (the particles are moving away from each other)
```