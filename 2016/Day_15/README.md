# Day 15: Timing is Everything

[Problem Link](https://adventofcode.com/2016/day/15)

## Part 1

We're searching for the following configuration such as this

```
     (-)
- - O - -
- O - - - - - -
O - - -
- - - - - - O
```

So when the disc (`(-)`) is dropped and falls at one row per time step. Meanwhile, the holes (`O`) move to the right by one each time-step. In this configuration, the disc will perfectly line up with each hole as it falls.

Let $x^{(t)}_k$ denote the position of the $k^{\text{th}}$ disc at time $t$. Let $n_k$ denote the number of disc positions. Then

$$
x^{(t)}_k \equiv x^{(0)}_k + t \mod n_k
$$

Now, we want a configuration such that 

$$
x^{(t+1)}_1 = x^{(t+2)}_2 = \ldots = x^{(t+k)}_k = \ldots = B
$$

for some some $B \in \mathbb{N}$. Writing out in long-form we get

$$
t + x^{(0)}_k + k \equiv B \mod n_k
$$

where $x^{(0)}_k$ and $n_k$ are give by the input for each disc $k$.

Now, we just linearly search $t \in \mathbb{N}$ starting at $t = 0$ until we find a solution. That will be the minimum such $t$.


## Part 2 

Exactly the same as part 1, just with an additional disc.