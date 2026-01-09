# Day 25: Let It Snow

[Problem Link](https://adventofcode.com/2015/day/25)

## Part 1

There are two keys to this problem. The first is translating the manual row and column into the number of iterations. If we imagine the triangle more up-right.
```
1
2 3
4 5 6
7 8 9 10
```

Assuming we are indexing at `1`, then the `height` turns out to be `row + col - 1`. Now, we can calculate the triangle number at a given height, which is the well-known [sum of positive integers formula](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF).

$$
T(n) = \sum_{k=1}^n = \frac{n(n+1)}{2}
$$

This will give us the numbers along the far diagonal of the triangle (1, 3, 6, 10, etc). So now we just have to subtract by the correct amount. So the final formula turns out to be `T(height) - (height - col)`. This is implemented in the function `get_triangle_number_index()`.

Let $N$ be the number that we just computed. Now, the problem boils down to efficiently computing the following expression

$$
a \cdot b^{N-1} \mod m
$$

where $N$ is very large.

This is also a [well-known problem](https://en.wikipedia.org/wiki/Modular_exponentiation), and the simple algorithm is intuitive. Start with $\text{result} \leftarrow a$, and iteratively compute 

$$
\text{result} \leftarrow \text{result} \cdot b \mod m
$$

The trick being computing $\bmod$ in every iteration rather than at the end of the exponentiation. This keeps all of the intermediary numbers small.

There is an even [faster modular exponentiation algorithm](https://courses.cs.washington.edu/courses/cse311/21sp/resources/reference-modular-exponentiation.pdf) which takes advantage of the fact that computers use binary. But I have not implemented this here as it was not necessary.

## Part 2 

