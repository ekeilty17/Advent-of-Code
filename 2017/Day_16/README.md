# Day 16: Permutation Promenade

[Problem Link](https://adventofcode.com/2017/day/16)

## Part 1

Part 1 is just to code the dance algorithm as described by the problem.

## Part 2 

### The Intended Solution

Writing a brute force algorithm is to solve this problem is easy. Take our code from part 1 and just apply it `N` times.

```python
def brute_force(dance_moves: str, programs: List[str], num_dances: int) -> List[int]:
    for _ in range(num_dances):
        programs = execute_moves(programs, dance_moves)
    return programs
```

However, this is far too slow to execute 1 billion times. But, if we do run it we can notice something interesting. The input is cyclical. After 48 iterations, we get back the original program order. Therefore, we don't have to compute all 1 billion iterations, we can compute where the 1 billionth iteration will land in the cycle. This is 

```
1_000_000_000 % 48 --> 16
```

So we just return the 16th iteration.

Note that any finite permutation **must** cycle at some point. So this algorithm would work for any input in general. And I believe this was the intended solution. This is implemented in `part_2.py`.


### An Alternative Solution

I came up with another algorithm (actually this was my first attempt at solving it) that is admittedly more complicated, but I think conceptually more interesting.

The first thing that I noticed is that the `Partner` dance move is fundamentally different than the `Spin` and `Exchange`. The format operates on element names while the latter operate on indices. Going forward, I will call the format **element permutations** and the latter **index permutations**.

Then I noticed that element permutations and index permutations could be executed independently. That is, I can separate out the sequence of element permutations as $\sigma_e$ and the sequence of index permutations as $\sigma_i$. If $\tau$ represents the total permutation as computed by `part_1.py`, then 

$$
\tau = \sigma_e \circ \sigma_i = \sigma_i \circ \sigma_e
$$

Why should this be the case? The index permutation $\sigma_i$ is a true permutation of the indices. The element permutation $\sigma_e$ on the other-hand is just a relabeling. You can convince yourself that it doesn't matter when we relabel. Permuting indices and relabeling are independent of each other.

Part 2 asks us to compute $\tau^n$. Therefore, this can be computed as

$$
\tau^n = \sigma_i^n \circ \sigma_e^n
$$

Now, given some permutation $\sigma$, I need to efficiently compute $\sigma^n$. I'm sure there are numerous ways of doing this. The way I decided to do this is the following.
1. Convert $n$ into its binary digits $[b_0, b_1, \ldots, b_k]$
2. Compute $\sigma^{2^i} = \sigma^{2^{i-1}} \circ \sigma^{2^{i-1}}$ for each $i = 0, \ldots, k$
3. $\sigma^n = \prod_{i=0}^k b_i \sigma^{2^i}$ (where $\prod$ represents composition)

So I've computed each power of $2$ permutation and used the binary representation of $n$ to compose them accordingly.

Using this algorithm, I can compute $\tau^n$ in $O(\lg n)$ time. As opposed to the previous algorithm which depends on the length of the cycle of the input. Either could be more efficient for different inputs. This is implemented in `part_2_alt.py`.